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
        
        # Mapear comandos para handlers (nativos) ou scripts
        command_map = {
            # Scripts (executam no path do workspace)
            'scan': 'context_scanner',
            'demo': 'context_demo',
            
            # Comandos nativos (implementados aqui)
            'new': self._handle_new_command,
            'templates': self._handle_templates_command,
            'info': self._show_workspace_info,
            
            # Comandos compostos
            'component': self._handle_component_command,
            'validate': self._handle_validate_command,
            'daemon': self._handle_daemon_command,
            'remove': self._remove_workspace
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
        
        # Aceitar --help diretamente
        if subcommand in ['-h', '--help']:
            print("Uso: cn validate [subcommando] [opções]")
            print()
            print("Subcomandos:")
            print("  consistency    Valida consistência da documentação")
            print("  (sem args)     Executa validação geral")
            print()
            print("Exemplos:")
            print("  cn validate")
            print("  cn validate consistency")
            print("  cn validate consistency --help")
            return 0
        elif subcommand == 'consistency':
            return self._execute_script(workspace, 'cn_consistency_validator', subcommand_args)
        else:
            print(f"❌ Subcomando não reconhecido: {subcommand}")
            print("💡 Subcomandos disponíveis: consistency")
            print("💡 Use 'cn validate --help' para mais informações")
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
            # Processing engines
            'context_scanner': 'engines/context_scanner.py',
            'context_engine': 'engines/context_engine.py',
            
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
            # Converter path para módulo (ex: scripts/engines/context_scanner.py -> scripts.engines.context_scanner)
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
        print("  new <tipo> <nome>    Cria novo documento")
        print("  templates            Lista templates disponíveis")
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
        print("  cn new decision nome # Cria nova decisão")
        print("  cn scan              # Escaneia projeto")
        print("  cn templates         # Lista templates")
        print("  cn component explore # Explora componentes")
        print("  cn validate          # Valida documentação")
        print()
        print("💡 O Context Navigator detecta workspace pelo registry global")
        print("   Funciona em qualquer subdiretório do workspace registrado")
        
        return 0

    def _handle_new_command(self, workspace: Workspace, args: List[str]) -> int:
        """Criar documentos baseado no workspace do registry"""
        if not args:
            self._show_new_help()
            return 1

        doc_type = args[0]
        doc_name = args[1] if len(args) > 1 else None

        if not doc_name:
            print(f"❌ Nome obrigatório para {doc_type}")
            print(f"💡 Uso: cn new {doc_type} <nome>")
            return 1

        # OPERAÇÃO DETERMINÍSTICA: workspace.root_path vem do workspaces-registry.yml
        return self._create_document(workspace, doc_type, doc_name)

    def _create_document(self, workspace: Workspace, doc_type: str, name: str) -> int:
        """Criar documento usando template no workspace do registry"""
        import shutil
        from datetime import datetime

        # Validações
        valid_types = ['decision', 'process', 'reference', 'architecture', 'analysis', 'planning']
        if doc_type not in valid_types:
            print(f"❌ Tipo inválido: {doc_type}")
            print(f"💡 Tipos válidos: {', '.join(valid_types)}")
            return 1

        # OPERAÇÃO NO PATH DO REGISTRY
        workspace_path = Path(workspace.root_path)  # ← Do workspaces-registry.yml
        
        # Mapear tipos para pastas organizadas
        type_to_folder = {
            "decision": "decisions",
            "process": "processes", 
            "reference": "references",
            "architecture": "architecture",
            "analysis": "analysis",
            "planning": "planning"
        }
        
        # Criar estrutura de diretórios em .cn_model/docs/ (outputs do workspace)
        docs_dir = workspace_path / ".cn_model" / "docs" / type_to_folder.get(doc_type, "misc")
        docs_dir.mkdir(parents=True, exist_ok=True)

        # Determinar nome do arquivo
        filename = f"{name}.md"
        doc_path = docs_dir / filename

        if doc_path.exists():
            print(f"❌ Documento já existe: {doc_path}")
            return 1

        # Gerar conteúdo do template
        template_content = self._generate_template_content(workspace, doc_type, name)
        doc_path.write_text(template_content, encoding='utf-8')

        print(f"✅ Documento criado: {doc_path}")
        print(f"📁 Workspace: {workspace.name}")
        print(f"🎯 Tipo: {doc_type}")
        return 0

    def _handle_templates_command(self, workspace: Workspace, args: List[str]) -> int:
        """Listar templates disponíveis"""

        # Templates do sistema (instalação)
        system_templates = self._get_system_templates_path()

        # Templates do workspace (customizados)
        workspace_templates = Path(workspace.root_path) / ".cn_model" / "templates"

        print("📋 Templates Disponíveis:")
        print()

        print("🏗️ Sistema:")
        if system_templates.exists():
            for template_file in system_templates.glob("*.md"):
                template_name = template_file.stem
                print(f"  {template_name}")
        else:
            print("  (nenhum template de sistema encontrado)")

        if workspace_templates.exists():
            print()
            print("🎯 Workspace:")
            for template_file in workspace_templates.glob("*.md"):
                template_name = template_file.stem
                print(f"  {template_name} (customizado)")

        return 0

    def _get_system_templates_path(self) -> Path:
        """Buscar templates do sistema"""
        # Para desenvolvimento, usar templates locais
        current_script_path = Path(__file__).parent.parent
        return current_script_path / "templates"

    def _get_template_path(self, workspace: Workspace, doc_type: str) -> Optional[Path]:
        """Buscar template (workspace primeiro, depois sistema)"""

        # Mapear tipos para templates (português)
        type_to_template = {
            "decision": "decisao",
            "process": "processo",
            "reference": "referencia",
            "architecture": "arquitetura",
            "analysis": "analise",
            "planning": "planejamento"
        }

        template_name = type_to_template.get(doc_type, doc_type)

        # 1. Template customizado no workspace
        workspace_template = Path(workspace.root_path) / ".cn_model" / "templates" / f"{template_name}.md"
        if workspace_template.exists():
            return workspace_template

        # 2. Template do sistema
        system_template = self._get_system_templates_path() / f"{template_name}.md"
        if system_template.exists():
            return system_template

        # 3. Template padrão não encontrado
        return None

    def _generate_template_content(self, workspace: Workspace, doc_type: str, name: str) -> str:
        """Gerar conteúdo do template"""
        from datetime import datetime

        template_path = self._get_template_path(workspace, doc_type)

        if template_path:
            # Carregar template personalizado
            template_content = template_path.read_text(encoding='utf-8')

            # Substituir variáveis básicas
            template_content = template_content.replace("{name}", name)
            template_content = template_content.replace("{date}", datetime.now().strftime("%Y-%m-%d"))
            template_content = template_content.replace("{workspace}", workspace.name)

            return template_content
        else:
            # Template padrão hardcoded
            return self._get_default_template(doc_type, name)

    def _get_default_template(self, doc_type: str, name: str) -> str:
        """Template padrão quando não encontra arquivo de template"""
        from datetime import datetime
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        
        return f"""# {name}

**Tipo**: {doc_type}
**Data**: {date_str}
**Status**: em desenvolvimento

## Resumo

[Descreva brevemente o contexto e objetivo deste {doc_type}]

## Detalhes

[Desenvolva os detalhes específicos]

## Considerações

[Adicione considerações importantes]

## Próximos Passos

- [ ] [Defina ações necessárias]

---
*Documento criado automaticamente pelo Context Navigator*
"""

    def _show_new_help(self) -> None:
        """Ajuda do comando new"""
        print("Uso: cn new <tipo> <nome>")
        print()
        print("Tipos de documento:")
        print("  decision      Decisões arquiteturais (ADRs)")
        print("  process       Processos e runbooks")
        print("  reference     APIs e documentação técnica")
        print("  architecture  Arquitetura e diagramas")
        print("  analysis      Análises e investigações")
        print("  planning      Planejamentos e roadmaps")
        print()
        print("Exemplos:")
        print("  cn new decision 'escolha-banco-dados'")
        print("  cn new process 'deploy-producao'")
        print("  cn new reference 'api-usuarios'")

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