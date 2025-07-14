#!/usr/bin/env python3
"""
Context Navigator - CLI Principal
COMPORTAMENTO BURRO: Entry point simples, sem tentativas de "ser inteligente"
"""

import sys
import argparse
import subprocess
from pathlib import Path
from typing import List, Optional


def find_context_navigator_simple() -> Optional[Path]:
    """
    Encontra .context-navigator/ com busca inteligente em diretórios pais
    """
    current_dir = Path.cwd()
    
    # Buscar no diretório atual e em diretórios pais
    search_dir = current_dir
    while search_dir != search_dir.parent:  # Evitar loop infinito na raiz
        cn_dir = search_dir / ".context-navigator"
        
        if cn_dir.exists() and cn_dir.is_dir():
            return search_dir
        
        search_dir = search_dir.parent
    
    return None


def run_script_simple(script_name: str, args: Optional[List[str]] = None) -> int:
    """
    Executa script de forma BURRA - sempre no mesmo lugar
    
    Args:
        script_name: Nome do script (sem .py)
        args: Argumentos para o script
        
    Returns:
        Código de retorno do script
    """
    if args is None:
        args = []
        
    # COMPORTAMENTO BURRO: sempre procura em .context-navigator/scripts/
    root_path = find_context_navigator_simple()
    if not root_path:
        print("❌ Context Navigator não encontrado no diretório atual")
        print("💡 Execute o comando do diretório onde há .context-navigator/")
        return 1
    
    # Verificar se o script existe
    script_path = root_path / ".context-navigator" / "scripts" / f"{script_name}.py"
    
    if not script_path.exists():
        print(f"❌ Script não encontrado: {script_name}")
        return 1
    
    # Executar script
    cmd = [sys.executable, str(script_path)]
    cmd.extend(args)
    
    try:
        return subprocess.run(cmd, cwd=Path.cwd()).returncode
    except Exception as e:
        print(f"❌ Erro ao executar script: {e}")
        return 1


def create_document_simple(doc_type: str, name: Optional[str] = None) -> int:
    """
    Cria documento de forma BURRA - sempre em .context-navigator/docs/
    
    Args:
        doc_type: Tipo do documento
        name: Nome do documento (opcional)
        
    Returns:
        Código de retorno
    """
    import shutil
    from datetime import datetime
    
    print(f"🎯 Criando documento tipo: {doc_type}")
    
    # COMPORTAMENTO BURRO: só olha diretório atual
    root_path = find_context_navigator_simple()
    if not root_path:
        print("❌ Context Navigator não encontrado no diretório atual")
        print("💡 Execute do diretório onde há .context-navigator/")
        return 1
    
    cn_dir = root_path / ".context-navigator"
    
    # Mapeamento de tipos para pastas organizadas
    TYPE_TO_FOLDER = {
        "decision": "decisions",
        "process": "processes", 
        "reference": "references",
        "architecture": "architecture",
        "analysis": "analysis",
        "planning": "planning"
    }
    
    # Mapeamento de tipos para templates (português)
    TYPE_TO_TEMPLATE = {
        "decision": "decisao",
        "process": "processo",
        "reference": "referencia",
        "architecture": "arquitetura",
        "analysis": "analise",
        "planning": "planejamento"
    }
    
    try:
        # SEMPRE criar em .context-navigator/docs/ (comportamento burro)
        docs_dir = cn_dir / "docs"
        
        # Criar subpasta por tipo
        type_folder = docs_dir / TYPE_TO_FOLDER.get(doc_type, "misc")
        type_folder.mkdir(parents=True, exist_ok=True)
        
        # Determinar nome do arquivo
        if name:
            filename = f"{name}.md"
        else:
            filename = f"{doc_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        # Copiar template
        template_name = TYPE_TO_TEMPLATE.get(doc_type, doc_type)
        template_path = cn_dir / "templates" / f"{template_name}.md"
        
        if not template_path.exists():
            print(f"❌ Template não encontrado: {template_path}")
            return 1
        
        target_file = type_folder / filename
        shutil.copy2(template_path, target_file)
        
        print(f"✅ Documento criado: {target_file}")
        print(f"📁 Pasta: {type_folder}")
        print(f"🎯 SEMPRE cria em: .context-navigator/docs/{TYPE_TO_FOLDER.get(doc_type, 'misc')}/")
        print("📝 Edite o arquivo e preencha os metadados obrigatórios")
        print("🔍 Depois execute: python3 -m context_navigator.cn_cli scan")
        
        return 0
        
    except Exception as e:
        print(f"❌ Erro ao criar documento: {e}")
        return 1


def show_help() -> None:
    """Mostra ajuda dos comandos - COMPORTAMENTO BURRO"""
    print("""
🧭 Context Navigator - COMPORTAMENTO BURRO

🤖 SEMPRE execute do diretório onde há .context-navigator/

📊 PRINCIPAIS:
  python3 -m context_navigator.cn_cli scan
  python3 -m context_navigator.cn_cli demo
  python3 -m context_navigator.cn_cli validate
  
📝 DOCUMENTOS:
  python3 -m context_navigator.cn_cli new decision <nome>
  python3 -m context_navigator.cn_cli new process <nome>
  python3 -m context_navigator.cn_cli new reference <nome>
  python3 -m context_navigator.cn_cli new architecture <nome>
  python3 -m context_navigator.cn_cli new analysis <nome>
  python3 -m context_navigator.cn_cli new planning <nome>
  
🔧 AVANÇADO:
  python3 -m context_navigator.cn_cli patterns
  python3 -m context_navigator.cn_cli conflicts
  python3 -m context_navigator.cn_cli impact
  python3 -m context_navigator.cn_cli templates
  
ℹ️  INFORMAÇÕES:
  python3 -m context_navigator.cn_cli version
  python3 -m context_navigator.cn_cli help
  python3 -m context_navigator.cn_cli status
  
💡 ALIAS OPCIONAL:
  alias cn='python3 -m context_navigator.cn_cli'
  
🎯 COMPORTAMENTO BURRO:
• Sempre funciona igual
• Não procura instalações
• Não tenta "adivinhar" nada
• Execute do diretório correto
""")


def main() -> int:
    """Função principal do CLI - COMPORTAMENTO BURRO"""
    parser = argparse.ArgumentParser(
        description='Context Navigator - COMPORTAMENTO BURRO',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis')
    
    # Comando scan - aceita argumentos adicionais
    scan_parser = subparsers.add_parser('scan', help='Escanear documentos')
    scan_parser.add_argument('extra_args', nargs='*', help=argparse.SUPPRESS)
    
    # Comando demo - aceita argumentos adicionais
    demo_parser = subparsers.add_parser('demo', help='Demonstração completa')
    demo_parser.add_argument('extra_args', nargs='*', help=argparse.SUPPRESS)
    
    # Comando validate - aceita argumentos adicionais
    validate_parser = subparsers.add_parser('validate', help='Validar métricas')
    validate_parser.add_argument('extra_args', nargs='*', help=argparse.SUPPRESS)
    
    # Comando new
    new_parser = subparsers.add_parser('new', help='Criar novo documento')
    new_parser.add_argument('type', choices=['decision', 'process', 'reference', 'architecture', 'analysis', 'planning'])
    new_parser.add_argument('name', nargs='?', help='Nome do documento')
    
    # Comando version
    subparsers.add_parser('version', help='Mostrar versão')
    
    # Comando help
    subparsers.add_parser('help', help='Mostrar ajuda')
    
    # Comando status
    subparsers.add_parser('status', help='Status da instalação')
    
    # Scripts avançados - aceita argumentos adicionais
    patterns_parser = subparsers.add_parser('patterns', help='Detectar padrões')
    patterns_parser.add_argument('extra_args', nargs='*', help=argparse.SUPPRESS)
    
    conflicts_parser = subparsers.add_parser('conflicts', help='Detectar conflitos')
    conflicts_parser.add_argument('extra_args', nargs='*', help=argparse.SUPPRESS)
    
    impact_parser = subparsers.add_parser('impact', help='Analisar impacto')
    impact_parser.add_argument('extra_args', nargs='*', help=argparse.SUPPRESS)
    
    templates_parser = subparsers.add_parser('templates', help='Validar templates')
    templates_parser.add_argument('extra_args', nargs='*', help=argparse.SUPPRESS)
    
    args = parser.parse_args()
    
    if not args.command or args.command == 'help':
        show_help()
        return 0
    
    # Comandos especiais
    if args.command == 'new':
        return create_document_simple(args.type, args.name)
    
    if args.command == 'version':
        print("Context Navigator v1.0.19-CLEAN (COMPORTAMENTO BURRO)")
        return 0
    
    if args.command == 'status':
        root_path = find_context_navigator_simple()
        if root_path:
            print(f"✅ Context Navigator encontrado em: {root_path}/.context-navigator")
            return 0
        else:
            print("❌ Context Navigator não encontrado no diretório atual")
            print("💡 Execute do diretório onde há .context-navigator/")
            return 1
    
    # Mapeamento de comandos para scripts - COMPORTAMENTO BURRO
    script_mapping = {
        'scan': 'context_scanner',
        'demo': 'context_demo',
        'validate': 'metrics_validator',
        'patterns': 'pattern_detector',
        'conflicts': 'conflict_detector',
        'impact': 'impact_analyzer',
        'templates': 'template_validator'
    }
    
    script_name = script_mapping.get(args.command)
    if script_name:
        # Usar extra_args se disponível, senão usar método antigo
        if hasattr(args, 'extra_args') and args.extra_args:
            script_args = args.extra_args
        else:
            # Método antigo - construir argumentos para o script
            script_args = []
            command_found = False
            for arg in sys.argv[1:]:
                if command_found:
                    script_args.append(arg)
                elif arg == args.command:
                    command_found = True
        return run_script_simple(script_name, script_args)
    
    print(f"❌ Comando não reconhecido: {args.command}")
    return 1


if __name__ == '__main__':
    sys.exit(main()) 