#!/usr/bin/env python3

# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component daemon-manager
# @cn:doc daemon-manager.md
# @cn:context-level c3_component
# @cn:context-type core
# @cn:parent-module global-core
# @cn:purpose "Sistema de daemon Master/Worker para workspaces - balanceado e não fanático"
# @cn:memory-aid "Gerencia daemons por workspace com TTL 30min - cleanup inteligente"
# @cn:depends-on workspace-manager, threading, time
# @cn:provides daemon-management, file-watching, auto-scan
# @cn:component-type functional
# @cn:responsibility daemon-management
# ============================================

"""
Context Navigator - Daemon Manager
COMPORTAMENTO: Master/Worker balanceado - não fanático com TTL aceitável
"""

import os
import sys
import time
import json
import signal
import threading
import subprocess
from pathlib import Path
from typing import Dict, Optional, List, Callable
from dataclasses import dataclass

from .workspace_manager import WorkspaceManager, Workspace


@dataclass
class WorkerInfo:
    """Informações sobre um worker de workspace"""
    worker: 'WorkspaceWorker'
    last_used: float
    start_time: float
    workspace_id: str


class DaemonMaster:
    """Daemon central que gerencia workers por workspace"""
    
    def __init__(self):
        self.workers: Dict[str, WorkerInfo] = {}
        self.worker_ttl = 1800  # 30 minutos (aceitável, não fanático)
        self.cleanup_interval = 300  # 5 minutos
        self.running = False
        self.cleanup_thread: Optional[threading.Thread] = None
        self.workspace_manager = WorkspaceManager()
    
    def start(self):
        """Inicia daemon master"""
        if self.running:
            return
        
        self.running = True
        
        # Iniciar thread de cleanup
        self.cleanup_thread = threading.Thread(target=self._cleanup_loop, daemon=True)
        self.cleanup_thread.start()
        
        print(f"🚀 Daemon Master iniciado (TTL: {self.worker_ttl}s)")
    
    def stop(self):
        """Para daemon master e todos os workers"""
        self.running = False
        
        # Parar todos os workers
        for worker_info in list(self.workers.values()):
            worker_info.worker.stop()
        
        self.workers.clear()
        print("⏹️  Daemon Master parado")
    
    def get_or_spawn_worker(self, workspace_id: str) -> Optional['WorkspaceWorker']:
        """Spawn worker sob demanda"""
        current_time = time.time()
        
        if workspace_id not in self.workers:
            # Criar novo worker
            workspace = self._load_workspace_by_id(workspace_id)
            if not workspace:
                print(f"❌ Workspace não encontrado: {workspace_id}")
                return None
            
            worker = WorkspaceWorker(workspace, ttl=self.worker_ttl)
            self.workers[workspace_id] = WorkerInfo(
                worker=worker,
                last_used=current_time,
                start_time=current_time,
                workspace_id=workspace_id
            )
            
            worker.start()
            print(f"🚀 Worker iniciado para workspace: {workspace.name}")
        
        # Atualizar last_used
        self.workers[workspace_id].last_used = current_time
        return self.workers[workspace_id].worker
    
    def _load_workspace_by_id(self, workspace_id: str) -> Optional[Workspace]:
        """Carrega workspace por ID (implementação básica)"""
        # Em uma implementação completa, manteria registry de workspaces
        # Por ora, assumir que workspace_id é o path do workspace
        try:
            workspace_path = Path(workspace_id)
            if workspace_path.exists():
                return self.workspace_manager.load_workspace(workspace_path)
        except:
            pass
        return None
    
    def _cleanup_loop(self):
        """Loop de cleanup de workers inativos"""
        while self.running:
            try:
                time.sleep(self.cleanup_interval)
                if self.running:
                    self._cleanup_inactive_workers()
            except Exception as e:
                print(f"⚠️  Erro no cleanup: {e}")
    
    def _cleanup_inactive_workers(self):
        """Remove workers inativos (não fanático)"""
        current_time = time.time()
        inactive_workers = []
        
        for workspace_id, worker_info in self.workers.items():
            time_since_use = current_time - worker_info.last_used
            if time_since_use > self.worker_ttl:
                inactive_workers.append(workspace_id)
        
        for workspace_id in inactive_workers:
            worker_info = self.workers.pop(workspace_id)
            worker_info.worker.stop()
            
            uptime = current_time - worker_info.start_time
            print(f"⏰ Worker finalizado por inatividade: {workspace_id} (uptime: {uptime:.0f}s)")
    
    def get_status(self) -> Dict:
        """Status do daemon master"""
        return {
            'running': self.running,
            'workers_count': len(self.workers),
            'worker_ttl': self.worker_ttl,
            'cleanup_interval': self.cleanup_interval,
            'workers': [
                {
                    'workspace_id': info.workspace_id,
                    'uptime': time.time() - info.start_time,
                    'last_used': time.time() - info.last_used,
                    'active': info.worker.active
                }
                for info in self.workers.values()
            ]
        }


class WorkspaceWorker:
    """Worker específico de um workspace"""
    
    def __init__(self, workspace: Workspace, ttl: int):
        self.workspace = workspace
        self.ttl = ttl
        self.active = False
        self.file_watcher: Optional['FileWatcher'] = None
        self.last_scan_time = 0
        self.scan_debounce = 5  # 5 segundos debounce
    
    def start(self):
        """Inicia monitoramento do workspace"""
        if self.active:
            return
        
        self.active = True
        
        # Iniciar file watcher (implementação básica)
        self.file_watcher = FileWatcher(self.workspace.root_path)
        self.file_watcher.on_change = self.handle_file_change
        self.file_watcher.start()
        
        print(f"📁 Worker ativo para: {self.workspace.name}")
    
    def stop(self):
        """Para worker"""
        self.active = False
        
        if self.file_watcher:
            self.file_watcher.stop()
            self.file_watcher = None
    
    def handle_file_change(self, file_path: Path):
        """Reage a mudanças de arquivo (inteligente, não fanático)"""
        if not self.active:
            return
        
        # Filtrar apenas arquivos relevantes
        if not self._is_relevant_file(file_path):
            return
        
        # Debounce: evitar spam de mudanças
        if self._should_trigger_scan():
            self._trigger_auto_scan()
    
    def _is_relevant_file(self, file_path: Path) -> bool:
        """Verifica se arquivo é relevante para CN"""
        relevant_extensions = {'.py', '.js', '.ts', '.md', '.yml', '.yaml'}
        
        # Verificações básicas
        if file_path.suffix not in relevant_extensions:
            return False
        
        # Ignorar .cn_model/
        if '.cn_model' in str(file_path):
            return False
        
        # Verificar se tem marcações @cn: (implementação básica)
        return self._has_cn_markers(file_path)
    
    def _has_cn_markers(self, file_path: Path) -> bool:
        """Verifica se arquivo tem marcações @cn:"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(1024)  # Ler só o início
                return '@cn:' in content
        except:
            return False
    
    def _should_trigger_scan(self) -> bool:
        """Verifica se deve disparar scan (debounce)"""
        current_time = time.time()
        if current_time - self.last_scan_time > self.scan_debounce:
            self.last_scan_time = current_time
            return True
        return False
    
    def _trigger_auto_scan(self):
        """Executa scan automático"""
        print(f"🔄 Auto-scan disparado: {self.workspace.name}")
        
        # Executar context_scanner real
        self._execute_context_scanner()
    
    def _execute_context_scanner(self):
        """Executa context_scanner no contexto do workspace"""
        try:
            import subprocess
            
            # Preparar ambiente para execução workspace-aware
            env = {
                **os.environ,
                'CN_WORKSPACE_ROOT': str(self.workspace.root_path),
                'CN_WORKSPACE_CONFIG': str(self.workspace.config_path),
                'CN_OUTPUT_DIR': str(self.workspace.root_path / self.workspace.configuration.get('output_dir', '.cn_model')),
                'PYTHONPATH': str(self.workspace.root_path / 'src')
            }
            
            # Localizar script do scanner
            scanner_script = self.workspace.root_path / 'src' / 'context_navigator' / 'scripts' / 'context_scanner.py'
            
            if not scanner_script.exists():
                print(f"⚠️  Scanner script não encontrado: {scanner_script}")
                return
            
            # Executar scanner em background (não bloquear daemon)
            cmd = [sys.executable, str(scanner_script), '--quiet']
            
            process = subprocess.Popen(
                cmd,
                env=env,
                cwd=self.workspace.root_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Não aguardar finalização (async)
            print(f"📡 Scanner executado em background (PID: {process.pid})")
            
        except Exception as e:
            print(f"❌ Erro ao executar auto-scan: {e}")


class FileWatcher:
    """File watcher básico (implementação simplificada)"""
    
    def __init__(self, path: Path):
        self.path = path
        self.on_change: Optional[Callable[[Path], None]] = None
        self.running = False
        self.watch_thread: Optional[threading.Thread] = None
        self.file_times: Dict[str, float] = {}
    
    def start(self):
        """Inicia watching"""
        if self.running:
            return
        
        self.running = True
        self.watch_thread = threading.Thread(target=self._watch_loop, daemon=True)
        self.watch_thread.start()
    
    def stop(self):
        """Para watching"""
        self.running = False
    
    def _watch_loop(self):
        """Loop de monitoramento (implementação básica)"""
        while self.running:
            try:
                self._check_changes()
                time.sleep(2)  # Check a cada 2 segundos
            except Exception as e:
                # Ignorar erros silenciosamente (não fanático)
                pass
    
    def _check_changes(self):
        """Verifica mudanças nos arquivos"""
        try:
            # Padrões otimizados para Context Navigator
            relevant_patterns = ['**/*.py', '**/*.js', '**/*.ts', '**/*.md', '**/*.yml']
            ignore_patterns = ['.cn_model', '.git', 'node_modules', '__pycache__', '.venv']
            
            for pattern in relevant_patterns:
                for file_path in self.path.glob(pattern):
                    if file_path.is_file():
                        # Filtrar diretórios ignorados
                        if any(ignore in str(file_path) for ignore in ignore_patterns):
                            continue
                        
                        try:
                            current_mtime = file_path.stat().st_mtime
                            file_key = str(file_path)
                            
                            if file_key in self.file_times:
                                if current_mtime > self.file_times[file_key]:
                                    self.file_times[file_key] = current_mtime
                                    if self.on_change and self._has_cn_markers(file_path):
                                        self.on_change(file_path)
                            else:
                                self.file_times[file_key] = current_mtime
                        except (OSError, PermissionError):
                            # Ignorar arquivos inacessíveis
                            continue
        except (OSError, PermissionError):
            # Ignorar erros de diretório
            pass
    
    def _has_cn_markers(self, file_path: Path) -> bool:
        """Verifica se arquivo tem marcações @cn: (otimizado)"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Ler apenas primeiras linhas para performance
                for i, line in enumerate(f):
                    if i > 50:  # Verificar apenas primeiras 50 linhas
                        break
                    if '@cn:' in line:
                        return True
                return False
        except:
            return False


class DaemonManager:
    """Interface para gerenciar daemon system"""
    
    def __init__(self):
        self.master: Optional[DaemonMaster] = None
    
    def ensure_master_running(self):
        """Garante que daemon master está rodando"""
        if not self.master or not self.master.running:
            self.master = DaemonMaster()
            self.master.start()
    
    def handle_daemon_command(self, workspace: Optional[Workspace], args: List[str]) -> int:
        """Manuseia comandos daemon"""
        if not args:
            return self._show_daemon_status(workspace)
        
        command = args[0]
        
        if command == 'status':
            return self._show_daemon_status(workspace)
        elif command == 'start':
            return self._start_daemon(workspace)
        elif command == 'stop':
            return self._stop_daemon()
        elif command == 'restart':
            return self._restart_daemon(workspace)
        else:
            print(f"❌ Comando daemon não reconhecido: {command}")
            print("💡 Comandos disponíveis: status, start, stop, restart")
            return 1
    
    def _show_daemon_status(self, workspace: Optional[Workspace]) -> int:
        """Mostra status do daemon"""
        if not self.master or not self.master.running:
            print("⏹️  Daemon Master: Parado")
            return 0
        
        status = self.master.get_status()
        print(f"🚀 Daemon Master: Ativo")
        print(f"📊 Workers ativos: {status['workers_count']}")
        print(f"⏰ TTL: {status['worker_ttl']}s")
        
        if workspace:
            workspace_id = str(workspace.root_path)
            worker_found = False
            for worker_status in status['workers']:
                if worker_status['workspace_id'] == workspace_id:
                    print(f"\n📁 Worker deste workspace:")
                    print(f"   ⏰ Uptime: {worker_status['uptime']:.0f}s")
                    print(f"   📅 Último uso: {worker_status['last_used']:.0f}s atrás")
                    print(f"   ✅ Status: {'Ativo' if worker_status['active'] else 'Inativo'}")
                    worker_found = True
                    break
            
            if not worker_found:
                print(f"\n📁 Nenhum worker ativo para este workspace")
        
        return 0
    
    def _start_daemon(self, workspace: Optional[Workspace]) -> int:
        """Inicia daemon"""
        self.ensure_master_running()
        
        if workspace and self.master:
            workspace_id = str(workspace.root_path)
            worker = self.master.get_or_spawn_worker(workspace_id)
            if worker:
                print(f"✅ Worker iniciado para workspace: {workspace.name}")
            else:
                print(f"❌ Falha ao iniciar worker")
                return 1
        
        return 0
    
    def _stop_daemon(self) -> int:
        """Para daemon"""
        if self.master:
            self.master.stop()
            self.master = None
            print("⏹️  Daemon parado")
        else:
            print("⏹️  Daemon já estava parado")
        return 0
    
    def _restart_daemon(self, workspace: Optional[Workspace]) -> int:
        """Reinicia daemon"""
        self._stop_daemon()
        return self._start_daemon(workspace)


def main():
    """Função para testes do Daemon Manager"""
    manager = DaemonManager()
    
    # Teste básico
    print("🧪 Testando Daemon Manager...")
    manager.ensure_master_running()
    
    # Simular status
    status = manager.master.get_status() if manager.master else {}
    print(f"Status: {status}")


if __name__ == "__main__":
    main() 