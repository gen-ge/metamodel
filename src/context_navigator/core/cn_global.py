#!/usr/bin/env python3

# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component global-command-router
# @cn:doc global-command-router.md
# @cn:context-level c3_component
# @cn:context-type interface
# @cn:parent-module global-core
# @cn:purpose "Entry point global - detecta workspace e roteia comandos para engines apropriados"
# @cn:memory-aid "Substitui cn_cli.py local - funciona de qualquer lugar como git"
# @cn:depends-on workspace-manager, context-engine, argparse
# @cn:provides global-cli, command-routing, workspace-awareness
# @cn:component-type interface
# @cn:responsibility command-routing
# ============================================

"""
Context Navigator - Global Command Router
COMPORTAMENTO: Entry point global que detecta workspace e executa comandos
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import List, Optional

try:
    from .workspace_manager import WorkspaceManager, Workspace
    from .daemon_manager import DaemonManager
except ImportError:
    # Fallback para execução direta
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from core.workspace_manager import WorkspaceManager, Workspace
    from core.daemon_manager import DaemonManager


class GlobalCommandRouter:
    """Roteador global de comandos do Context Navigator"""
    
    def __init__(self):
        self.workspace_manager = WorkspaceManager()
        self.daemon_manager = DaemonManager()
        self.global_installation_path = self._detect_global_installation()
    
    def _detect_global_installation(self) -> Path:
        """Detecta onde está instalado o Context Navigator globalmente"""
        # Por enquanto, usar o path atual do script
        # Em produção seria /opt/context-navigator/ ou similar
        current_script = Path(__file__).resolve()
        return current_script.parent.parent  # src/context_navigator/
    
    def route_command(self, args: List[str]) -> int:
        """Roteia comando baseado no workspace atual e argumentos"""
        if not args:
            return self._show_help()
        
        command = args[0]
        command_args = args[1:] if len(args) > 1 else []
        
        # Comandos que não precisam de workspace
        if command in ['init', 'migrate', 'list', 'help', '--help', '-h', '--version']:
            return self._handle_global_command(command, command_args)
        
        # Comandos que precisam de workspace
        current_workspace = self.workspace_manager.detect_current_workspace()
        if not current_workspace:
            print("❌ Context Navigator workspace não encontrado")
            print("💡 Execute 'cn init' para configurar este diretório")
            print("💡 Ou navegue para um diretório com workspace configurado")
            return 1
        
        return self._handle_workspace_command(current_workspace, command, command_args)
    
    def _handle_global_command(self, command: str, args: List[str]) -> int:
        """Manuseia comandos globais que não precisam de workspace"""
        if command == 'init':
            return self._init_workspace(args)
        elif command == 'migrate':
            return self._handle_migrate_command(args)
        elif command == 'list':
            return self._list_workspaces(args)
        elif command in ['help', '--help', '-h']:
            return self._show_help()
        elif command == '--version':
            return self._show_version()
        else:
            print(f"❌ Comando global não reconhecido: {command}")
            return 1
    
    def _handle_workspace_command(self, workspace: Workspace, command: str, args: List[str]) -> int:
        """Manuseia comandos que operam dentro de um workspace"""
        print(f"📁 Workspace: {workspace.name} ({workspace.root_path})")
        
        # Mapear comandos para scripts
        command_map = {
            'scan': 'context_scanner',
            'component': self._handle_component_command,
            'validate': self._handle_validate_command,
            'demo': 'context_demo',
            'daemon': self._handle_daemon_command,
            'remove': self._remove_workspace,
            'info': self._show_workspace_info
        }
        
        if command not in command_map:
            print(f"❌ Comando não reconhecido: {command}")
            print("💡 Execute 'cn help' para ver comandos disponíveis")
            return 1
        
        handler = command_map[command]
        
        if callable(handler):
            result = handler(workspace, args)
            return result if isinstance(result, int) else 0
        else:
            # É um script - executar diretamente
            return self._execute_script(workspace, handler, args)
    
    def _init_workspace(self, args: List[str]) -> int:
        """Inicializa workspace no diretório atual"""
        current_path = Path.cwd()
        
        if args and args[0] in ['-h', '--help']:
            print("Uso: cn init")
            print("Inicializa Context Navigator workspace no diretório atual")
            print("Cria .cn_model/ com configuração necessária")
            return 0
        
        return self.workspace_manager.init_workspace(current_path)
    
    def _handle_migrate_command(self, args: List[str]) -> int:
        """Manuseia comando de migração"""
        # Importar migration manager
        try:
            from .migration_manager import MigrationManager
        except ImportError:
            import sys
            sys.path.insert(0, str(Path(__file__).parent))
            from migration_manager import MigrationManager
        
        migration_manager = MigrationManager()
        
        if args and args[0] == 'check':
            return migration_manager.show_migration_status()
        elif not args or args[0] == 'migrate':
            return migration_manager.migrate_all_local_installations()
        else:
            print("❌ Subcomando inválido para 'migrate'")
            print("💡 Uso: cn migrate [check]")
            return 1
    
    def _handle_component_command(self, workspace: Workspace, args: List[str]) -> int:
        """Manuseia subcomandos de component"""
        if not args:
            print("❌ Subcomando necessário para 'component'")
            print("💡 Uso: cn component [explore|parse|validate]")
            return 1
        
        subcommand = args[0]
        subcommand_args = args[1:]
        
        if subcommand == 'explore':
            return self._execute_script(workspace, 'cn_component_explorer', subcommand_args)
        elif subcommand == 'parse':
            return self._execute_script(workspace, 'cn_component_parser', subcommand_args)
        else:
            print(f"❌ Subcomando não reconhecido: {subcommand}")
            print("💡 Subcomandos disponíveis: explore, parse")
            return 1
    
    def _handle_validate_command(self, workspace: Workspace, args: List[str]) -> int:
        """Manuseia subcomandos de validate"""
        if not args:
            # Validação geral
            return self._execute_script(workspace, 'cn_consistency_validator', [])
        
        subcommand = args[0]
        subcommand_args = args[1:]
        
        if subcommand == 'consistency':
            return self._execute_script(workspace, 'cn_consistency_validator', subcommand_args)
        else:
            print(f"❌ Subcomando não reconhecido: {subcommand}")
            print("💡 Subcomandos disponíveis: consistency")
            return 1
    
    def _handle_daemon_command(self, workspace: Workspace, args: List[str]) -> int:
        """Manuseia comandos daemon"""
        return self.daemon_manager.handle_daemon_command(workspace, args)
    
    def _remove_workspace(self, workspace: Workspace, args: List[str]) -> int:
        """Remove workspace atual"""
        if args and args[0] in ['-h', '--help']:
            print("Uso: cn remove")
            print("Remove workspace Context Navigator do diretório atual")
            print("Cria backup antes de remover")
            return 0
        
        return self.workspace_manager.remove_workspace(workspace)
    
    def _show_workspace_info(self, workspace: Workspace, args: List[str]) -> int:
        """Mostra informações do workspace atual"""
        print(f"📁 Workspace: {workspace.name}")
        print(f"📍 Localização: {workspace.root_path}")
        print(f"🆔 ID: {workspace.id}")
        print(f"📅 Criado em: {workspace.created_at}")
        print(f"⚙️  Configuração: {workspace.config_path}")
        
        config = workspace.configuration
        print(f"\n🔧 Configuração:")
        print(f"   📂 Diretório de saída: {config.get('output_dir', 'N/A')}")
        print(f"   🔍 Padrões de código: {config.get('source_patterns', [])}")
        print(f"   🚫 Padrões ignorados: {config.get('ignore_patterns', [])}")
        print(f"   🤖 Auto-scan: {config.get('auto_scan', False)}")
        
        return 0
    
    def _list_workspaces(self, args: List[str]) -> int:
        """Lista todos os workspaces registrados"""
        if args and args[0] in ['-h', '--help']:
            print("Uso: cn list")
            print("Lista todos os workspaces Context Navigator registrados")
            print("Mostra ID, nome, localização e status de cada workspace")
            return 0
        
        # Obter lista de workspaces
        workspaces = self.workspace_manager.registry.list_workspaces()
        
        if not workspaces:
            print("📂 Nenhum workspace registrado")
            print("💡 Execute 'cn init' em um diretório para criar um workspace")
            return 0
        
        print(f"📋 Workspaces registrados ({len(workspaces)}):\n")
        
        for workspace in workspaces:
            status_icon = "✅" if workspace['exists'] else "❌"
            status_text = "ativo" if workspace['exists'] else "órfão"
            
            print(f"{status_icon} {workspace['name']}")
            print(f"   📍 Localização: {workspace['path']}")
            print(f"   🆔 ID: {workspace['id']}")
            print(f"   📅 Criado: {workspace['created_at']}")
            print(f"   🕒 Último acesso: {workspace['last_accessed']}")
            print(f"   📊 Status: {status_text}")
            print()
        
        # Verificar se há workspaces órfãos
        orphaned = [w for w in workspaces if not w['exists']]
        if orphaned:
            print(f"⚠️  {len(orphaned)} workspace(s) órfão(s) detectado(s)")
            print("💡 Execute 'cn migrate check' para limpeza automática")
        
        return 0
    
    def _execute_script(self, workspace: Workspace, script_name: str, args: List[str]) -> int:
        """Executa script no contexto do workspace"""
        # Mapeamento de scripts para seus diretórios na organização 2.0
        script_locations = {
            # Core scripts
            'context_scanner': 'core/context_scanner.py',
            'context_engine': 'core/context_engine.py',
            
            # Validation scripts  
            'template_validator': 'validation/template_validator.py',
            'cn_consistency_validator': 'validation/cn_consistency_validator.py',
            'metrics_validator': 'validation/metrics_validator.py',
            
            # Analysis scripts
            'pattern_detector': 'analysis/pattern_detector.py', 
            'conflict_detector': 'analysis/conflict_detector.py',
            'impact_analyzer': 'analysis/impact_analyzer.py',
            'context_advisor': 'analysis/context_advisor.py',
            
            # Tools scripts
            'cn_component_explorer': 'tools/cn_component_explorer.py',
            'cn_component_parser': 'tools/cn_component_parser.py',
            'context_demo': 'tools/context_demo.py',
            'cn_global_launcher': 'tools/cn_global_launcher.py'
        }
        
        # Localizar script na instalação global
        scripts_dir = self.global_installation_path / "scripts"
        
        if script_name in script_locations:
            script_path = scripts_dir / script_locations[script_name]
        else:
            # Fallback: procurar diretamente em scripts/ (compatibilidade)
            script_path = scripts_dir / f"{script_name}.py"
        
        if not script_path.exists():
            print(f"❌ Script não encontrado: {script_name}")
            print(f"🔍 Procurado em: {script_path}")
            if script_name in script_locations:
                print(f"💡 Path esperado (organização 2.0): {script_locations[script_name]}")
            return 1
        
        # Preparar ambiente
        env = {
            'CN_WORKSPACE_ROOT': str(workspace.root_path),
            'CN_WORKSPACE_CONFIG': str(workspace.config_path),
            'CN_OUTPUT_DIR': str(workspace.root_path / workspace.configuration.get('output_dir', '.cn_model')),
            'PYTHONPATH': str(self.global_installation_path)
        }
        
        # Executar script como módulo Python para resolver imports
        if script_name in script_locations:
            # Converter path para módulo (ex: scripts/core/context_scanner.py -> scripts.core.context_scanner)
            module_path = script_locations[script_name].replace('/', '.').replace('.py', '')
            cmd = [sys.executable, "-m", f"scripts.{module_path}"] + args
        else:
            # Fallback: executar diretamente
            cmd = [sys.executable, str(script_path)] + args
        
        try:
            result = subprocess.run(
                cmd,
                env={**os.environ, **env},
                cwd=workspace.root_path
            )
            return result.returncode
        except Exception as e:
            print(f"❌ Erro ao executar script: {e}")
            return 1
    
    def _show_help(self) -> int:
        """Mostra ajuda do Context Navigator"""
        print("🧭 Context Navigator - Sistema de Documentação Context-Aware")
        print()
        print("Uso: cn <comando> [opções]")
        print()
        print("Comandos Globais:")
        print("  init                 Inicializa workspace no diretório atual")
        print("  migrate              Migra instalações locais para arquitetura global")
        print("  migrate check        Verifica instalações locais existentes")
        print("  help                 Mostra esta ajuda")
        print("  --version           Mostra versão")
        print()
        print("Comandos de Workspace:")
        print("  scan                 Escaneia código e atualiza documentação")
        print("  component explore    Explora componentes do workspace")
        print("  component parse      Analisa componentes específicos")
        print("  validate consistency Valida consistência da documentação")
        print("  demo                 Demonstração do sistema")
        print("  daemon status        Status do daemon do workspace")
        print("  daemon start         Inicia daemon do workspace")
        print("  daemon stop          Para daemon")
        print("  daemon restart       Reinicia daemon")
        print("  info                 Informações do workspace atual")
        print("  remove               Remove workspace atual")
        print()
        print("Exemplos:")
        print("  cn init              # Configura workspace")
        print("  cn scan              # Escaneia projeto")
        print("  cn component explore # Explora componentes")
        print("  cn validate          # Valida documentação")
        print()
        print("💡 O Context Navigator funciona como git - detecta workspace automaticamente")
        print("   subindo na hierarquia de diretórios procurando por .cn_model/")
        
        return 0
    
    def _show_version(self) -> int:
        """Mostra versão do Context Navigator"""
        print("Context Navigator 2.0.0 - Global Edition")
        return 0


def main():
    """Entry point principal do Context Navigator global"""
    import os
    
    router = GlobalCommandRouter()
    
    # Se chamado sem argumentos, mostrar ajuda
    if len(sys.argv) == 1:
        return router._show_help()
    
    # Processar argumentos
    return router.route_command(sys.argv[1:])


if __name__ == "__main__":
    sys.exit(main()) 