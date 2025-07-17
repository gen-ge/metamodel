#!/usr/bin/env python3

# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component workspace-manager
# @cn:doc workspace-manager.md
# @cn:context-level c3_component
# @cn:context-type core
# @cn:parent-module global-core
# @cn:purpose "Gerenciador de workspaces globais - detecta e configura .cn_model/"
# @cn:memory-aid "Substitui .context-navigator/ por .cn_model/ + instalação global"
# @cn:depends-on pathlib, yaml
# @cn:provides workspace-detection, workspace-initialization, global-registry
# @cn:component-type functional
# @cn:responsibility workspace-management
# ============================================

"""
Context Navigator - Workspace Manager
COMPORTAMENTO: Detecta workspaces (.cn_model/) como git detecta (.git/)
"""

import os
import sys
import yaml
import time
from pathlib import Path
from typing import Optional, Dict, List
from dataclasses import dataclass


@dataclass
class Workspace:
    """Representa um workspace do Context Navigator"""
    id: str
    name: str
    root_path: Path
    config_path: Path
    created_at: str
    configuration: Dict


class WorkspaceRegistry:
    """Registry global que mantém lista de todos os workspaces criados"""
    
    def __init__(self):
        self.registry_file = self._get_global_installation_path() / "workspaces-registry.yml"
        self._ensure_registry_exists()
    
    def _get_global_installation_path(self) -> Path:
        """Detecta onde está a instalação global do Context Navigator"""
        
        # MODO DE DESENVOLVIMENTO: Se rodando do src/, usar fallback sempre
        current_path = Path(__file__).resolve()
        if "src/context_navigator" in str(current_path):
            print("🛠️ Modo de desenvolvimento detectado - usando registry local")
            return current_path.parent.parent

        # MODO PRODUÇÃO: Verificar localizações possíveis de instalação
        possible_locations = [
            # 1. Diretório da instalação atual (onde está o arquivo)
            current_path.parent.parent,  # /path/to/install/core -> /path/to/install
            
            # 2. Locais padrão do sistema
            Path("/opt/context-navigator"),
            Path.home() / ".local" / "share" / "context-navigator",
        ]
        
        for location in possible_locations:
            if location.exists() and (location / "core").exists():
                print(f"🎯 Instalação detectada: {location}")
                return location
        
        # Fallback: usar current script path (desenvolvimento)
        print(f"🔄 Fallback para desenvolvimento: {current_path.parent.parent}")
        return current_path.parent.parent
    
    def _ensure_registry_exists(self):
        """Garante que o arquivo de registry existe"""
        if not self.registry_file.exists():
            self._create_empty_registry()
    
    def _create_empty_registry(self):
        """Cria arquivo de registry vazio"""
        registry_data = {
            'version': '2.0.0',
            'created_at': time.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'workspaces': {}
        }
        
        # Criar diretório se não existir
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.registry_file, 'w', encoding='utf-8') as f:
            yaml.dump(registry_data, f, default_flow_style=False, allow_unicode=True)
    
    def _load_registry(self) -> Dict:
        """Carrega registry do arquivo"""
        try:
            with open(self.registry_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"⚠️ Erro ao carregar registry: {e}")
            return {'workspaces': {}}
    
    def _save_registry(self, registry_data: Dict):
        """Salva registry no arquivo"""
        try:
            with open(self.registry_file, 'w', encoding='utf-8') as f:
                yaml.dump(registry_data, f, default_flow_style=False, allow_unicode=True)
        except Exception as e:
            print(f"❌ Erro ao salvar registry: {e}")
    
    def register_workspace(self, workspace: Workspace) -> bool:
        """Registra um workspace no registry global"""
        registry_data = self._load_registry()
        
        if 'workspaces' not in registry_data:
            registry_data['workspaces'] = {}
        
        # Registrar workspace
        registry_data['workspaces'][workspace.id] = {
            'name': workspace.name,
            'path': str(workspace.root_path.absolute()),
            'created_at': workspace.created_at,
            'last_accessed': time.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'status': 'active'
        }
        
        self._save_registry(registry_data)
        return True
    
    def unregister_workspace(self, workspace_id: str) -> bool:
        """Remove workspace do registry global"""
        registry_data = self._load_registry()
        
        if 'workspaces' in registry_data and workspace_id in registry_data['workspaces']:
            del registry_data['workspaces'][workspace_id]
            self._save_registry(registry_data)
            return True
        
        return False
    
    def list_workspaces(self) -> List[Dict]:
        """Lista todos os workspaces registrados"""
        registry_data = self._load_registry()
        workspaces = registry_data.get('workspaces', {})
        
        # Converter para lista e verificar se paths ainda existem
        workspace_list = []
        for workspace_id, workspace_info in workspaces.items():
            workspace_path = Path(workspace_info['path'])
            workspace_info['id'] = workspace_id
            workspace_info['exists'] = (workspace_path / ".cn_model" / ".cn_workspace").exists()
            workspace_list.append(workspace_info)
        
        return workspace_list
    
    def update_last_accessed(self, workspace_id: str):
        """Atualiza timestamp de último acesso"""
        registry_data = self._load_registry()
        
        if 'workspaces' in registry_data and workspace_id in registry_data['workspaces']:
            registry_data['workspaces'][workspace_id]['last_accessed'] = time.strftime('%Y-%m-%dT%H:%M:%SZ')
            self._save_registry(registry_data)
    
    def cleanup_orphaned_workspaces(self) -> int:
        """Remove workspaces órfãos (que não existem mais) do registry"""
        registry_data = self._load_registry()
        workspaces = registry_data.get('workspaces', {})
        
        orphaned_count = 0
        to_remove = []
        
        for workspace_id, workspace_info in workspaces.items():
            workspace_path = Path(workspace_info['path'])
            if not (workspace_path / ".cn_model" / ".cn_workspace").exists():
                to_remove.append(workspace_id)
                orphaned_count += 1
        
        # Remover órfãos
        for workspace_id in to_remove:
            del registry_data['workspaces'][workspace_id]
        
        if orphaned_count > 0:
            self._save_registry(registry_data)
        
        return orphaned_count


class WorkspaceManager:
    """Gerenciador de workspaces globais"""
    
    def __init__(self):
        self.workspace_dir = ".cn_model"
        self.workspace_config_file = ".cn_workspace"
        self.registry = WorkspaceRegistry()
    
    def detect_current_workspace(self) -> Optional[Workspace]:
        """Detectar workspace APENAS via registry (não busca hierárquica)"""

        current_path = Path.cwd().resolve()

        # Buscar no registry por path exato ou pai
        for workspace_info in self.registry.list_workspaces():
            workspace_path = Path(workspace_info['path']).resolve()

            # Workspace exato ou subdiretório
            if current_path == workspace_path or current_path.is_relative_to(workspace_path):
                # Atualizar last_accessed
                self.registry.update_last_accessed(workspace_info['id'])
                
                # Carregar workspace completo
                return Workspace(
                    id=workspace_info['id'],
                    name=workspace_info['name'],
                    root_path=workspace_path,
                    config_path=Path(workspace_info.get('config_path', '')),
                    created_at=workspace_info['created_at'],
                    configuration={}
                )

        return None
    
    def _find_workspace_root(self, start_path: Path) -> Optional[Path]:
        """
        Busca .cn_model/.cn_workspace subindo na hierarquia
        Similar ao git que busca .git/
        """
        search_path = start_path
        
        while search_path != search_path.parent:  # Não chegou na raiz do sistema
            cn_model_dir = search_path / self.workspace_dir
            workspace_file = cn_model_dir / self.workspace_config_file
            
            if workspace_file.exists():
                return search_path  # Este é o root do workspace
            
            search_path = search_path.parent
        
        return None
    
    def load_workspace(self, workspace_root: Path) -> Workspace:
        """Carrega configuração do workspace"""
        config_path = workspace_root / self.workspace_dir / self.workspace_config_file
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            workspace_info = config.get('workspace', {})
            return Workspace(
                id=workspace_info.get('id', ''),
                name=workspace_info.get('name', workspace_root.name),
                root_path=workspace_root,
                config_path=config_path,
                created_at=workspace_info.get('created_at', ''),
                configuration=config.get('configuration', {})
            )
        except Exception as e:
            raise Exception(f"Erro ao carregar workspace config: {e}")
    
    def init_workspace(self, path: Path) -> int:
        """
        Inicializa novo workspace no diretório especificado
        Cria .cn_model/ com .cn_workspace config
        """
        # 1. Verificar se já existe workspace
        existing_workspace = self._find_workspace_root(path)
        if existing_workspace:
            print(f"❌ Workspace já existe em: {existing_workspace}")
            print(f"💡 Para reconfigurar escopo, execute 'cn init' no diretório pai")
            print(f"💡 Para remover workspace: 'cn remove' em {existing_workspace}")
            return 1
        
        # 2. Criar estrutura .cn_model/
        cn_model_dir = path / self.workspace_dir
        cn_model_dir.mkdir(exist_ok=True)
        
        # 3. Criar subdiretórios
        (cn_model_dir / "docs").mkdir(exist_ok=True)
        
        # 4. Gerar configuração do workspace
        workspace_config = self._generate_workspace_config(path)
        
        # 5. Salvar .cn_workspace
        workspace_file = cn_model_dir / self.workspace_config_file
        with open(workspace_file, 'w', encoding='utf-8') as f:
            yaml.dump(workspace_config, f, default_flow_style=False, allow_unicode=True)
        
        # 6. Sugerir atualização do .gitignore
        self._suggest_gitignore_update(path)
        
        # 7. Criar workspace object e registrar no registry global
        workspace = Workspace(
            id=workspace_config['workspace']['id'],
            name=workspace_config['workspace']['name'],
            root_path=path,
            config_path=workspace_file,
            created_at=workspace_config['workspace']['created_at'],
            configuration=workspace_config['configuration']
        )
        
        # 8. Registrar no registry global
        self.registry.register_workspace(workspace)
        
        print(f"✅ Workspace inicializado: {path}")
        print(f"📁 Estrutura criada em: {cn_model_dir}")
        print(f"🗂️ Registrado no registry global")
        print(f"💡 Sugestão: adicione '{self.workspace_dir}/' ao .gitignore")
        
        return 0
    
    def _generate_workspace_config(self, path: Path) -> Dict:
        """Gera configuração inicial do workspace"""
        workspace_id = self._generate_workspace_id(path)
        
        return {
            'workspace': {
                'id': workspace_id,
                'name': path.name,  # Nome da pasta = nome do workspace
                'root_path': '.',   # Relativo para portabilidade
                'created_at': time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                'version': '2.0.0'
            },
            'configuration': {
                'output_dir': self.workspace_dir,
                'source_patterns': ['**/*.py', '**/*.js', '**/*.ts', '**/*.md'],
                'ignore_patterns': [self.workspace_dir, '.git', 'node_modules', '__pycache__'],
                'auto_scan': True,
                'templates_enabled': True
            },
            'daemon': {
                'enabled': True,
                'auto_start': True,
                'port': None,  # Será determinado automaticamente
                'log_level': 'INFO'
            }
        }
    
    def _generate_workspace_id(self, path: Path) -> str:
        """Gera ID único para o workspace"""
        import hashlib
        base_name = path.name
        path_hash = hashlib.md5(str(path.absolute()).encode()).hexdigest()[:8]
        return f"{base_name}-{path_hash}"
    
    def _suggest_gitignore_update(self, path: Path):
        """Sugere atualizar .gitignore mas não força"""
        gitignore_path = path / ".gitignore"
        
        if gitignore_path.exists():
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if self.workspace_dir not in content:
                print(f"💡 Considere adicionar '{self.workspace_dir}/' ao seu .gitignore")
        else:
            print(f"💡 Considere criar .gitignore com '{self.workspace_dir}/'")
    
    def find_workspace_in_hierarchy(self, path: Path) -> Optional[Path]:
        """
        Encontra qualquer workspace na hierarquia (pai ou filho)
        Usado para detectar conflitos de workspaces aninhados
        """
        # Verificar pais
        parent_workspace = self._find_workspace_root(path)
        if parent_workspace:
            return parent_workspace
        
        # Verificar filhos (busca básica)
        child_workspaces = self._find_child_workspaces(path)
        if child_workspaces:
            return child_workspaces[0]  # Primeiro encontrado
        
        return None
    
    def _find_child_workspaces(self, path: Path) -> List[Path]:
        """Busca workspaces filhos (implementação básica)"""
        child_workspaces = []
        
        try:
            for item in path.rglob(f"{self.workspace_dir}/{self.workspace_config_file}"):
                if item.is_file():
                    workspace_root = item.parent.parent
                    if workspace_root != path:  # Não contar o próprio path
                        child_workspaces.append(workspace_root)
        except (PermissionError, OSError):
            # Ignorar erros de permissão
            pass
        
        return child_workspaces
    
    def get_workspace_name(self, path: Path) -> str:
        """Nome do workspace = nome da pasta (simples e direto)"""
        return path.name
    
    def remove_workspace(self, workspace: Workspace) -> int:
        """Remove workspace atual"""
        try:
            import shutil
            cn_model_path = workspace.root_path / self.workspace_dir
            
            if cn_model_path.exists():
                # Backup antes de remover
                backup_name = f"{self.workspace_dir}.backup.{int(time.time())}"
                backup_path = workspace.root_path / backup_name
                shutil.move(cn_model_path, backup_path)
                
                # Desregistrar do registry global
                self.registry.unregister_workspace(workspace.id)
                
                print(f"✅ Workspace removido: {workspace.root_path}")
                print(f"📦 Backup criado: {backup_path}")
                print(f"🗂️ Removido do registry global")
                return 0
            else:
                print(f"❌ Workspace não encontrado: {cn_model_path}")
                return 1
                
        except Exception as e:
            print(f"❌ Erro ao remover workspace: {e}")
            return 1


def main():
    """Função para testes do WorkspaceManager"""
    manager = WorkspaceManager()
    
    # Teste: detectar workspace atual
    current = manager.detect_current_workspace()
    if current:
        print(f"📁 Workspace atual: {current.name} ({current.root_path})")
    else:
        print("❌ Nenhum workspace encontrado")


if __name__ == "__main__":
    main() 