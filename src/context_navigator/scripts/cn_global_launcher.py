#!/usr/bin/env python3
"""
🧭 Context Navigator - Launcher Global
Permite usar o Context Navigator de qualquer diretório através do PATH
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Optional

def find_context_navigator_in_path() -> Optional[Path]:
    """
    Busca .context-navigator/ no diretório atual e em diretórios pais
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

def find_global_installation() -> Optional[Path]:
    """
    Busca instalação global do Context Navigator
    """
    # Locais padrão para instalação global
    global_locations = [
        Path.home() / ".local" / "share" / "context-navigator",
        Path("/usr/local/share/context-navigator"),
        Path("/opt/context-navigator")
    ]
    
    for location in global_locations:
        if location.exists() and (location / "cn_cli.py").exists():
            return location
    
    return None

def run_context_navigator(args: list) -> int:
    """
    Executa o Context Navigator com os argumentos fornecidos
    """
    # Primeiro, tentar encontrar instalação local
    local_root = find_context_navigator_in_path()
    if local_root:
        print(f"🎯 Usando instalação local: {local_root}/.context-navigator")
        
        # Adicionar o diretório local ao Python path
        sys.path.insert(0, str(local_root / ".context-navigator"))
        
        # Executar o CLI
        try:
            from cn_cli import main
                # Simular sys.argv para o CLI - precisa ter formato correto
            original_argv = sys.argv
            sys.argv = ["cn"] + args
            result = main()
            sys.argv = original_argv
            return result
        except ImportError:
            print("❌ Erro ao importar cn_cli")
            return 1
        except Exception as e:
            print(f"❌ Erro ao executar Context Navigator: {e}")
            return 1
    
    # Se não encontrar local, tentar instalação global
    global_root = find_global_installation()
    if global_root:
        print(f"🌐 Usando instalação global: {global_root}")
        
        # Executar através do Python
        cmd = [sys.executable, str(global_root / "cn_cli.py")] + args
        try:
            return subprocess.run(cmd, cwd=Path.cwd()).returncode
        except Exception as e:
            print(f"❌ Erro ao executar instalação global: {e}")
            return 1
    
    # Se não encontrar nenhuma instalação
    print("❌ Context Navigator não encontrado")
    print("💡 Opções:")
    print("• Execute de um diretório que contenha .context-navigator/")
    print("• Instale globalmente com: cn install --global")
    print("• Verifique se o Context Navigator está instalado")
    return 1

def show_help():
    """Mostra ajuda específica do launcher global"""
    print("""
🧭 Context Navigator - Launcher Global

🎯 Este launcher permite usar o Context Navigator de qualquer diretório.

📍 BUSCA AUTOMÁTICA:
• Busca .context-navigator/ no diretório atual
• Busca .context-navigator/ em diretórios pais
• Busca instalação global do sistema

💡 MODOS DE USO:
• Local: cn scan (busca .context-navigator/ automaticamente)
• Global: cn --global scan (força uso da instalação global)

📦 INSTALAÇÃO NO PATH:
1. Copie este script para /usr/local/bin/cn
2. Torne executável: chmod +x /usr/local/bin/cn
3. Use de qualquer diretório: cn scan

🔧 COMANDOS DISPONÍVEIS:
""")
    
    # Chamar ajuda do CLI principal
    return run_context_navigator(["help"])

def main():
    """Função principal do launcher global"""
    args = sys.argv[1:]
    
    # Verificar se é pedido de ajuda
    if not args or args[0] in ["help", "--help", "-h"]:
        return show_help()
    
    # Verificar se é comando de instalação global
    if args[0] == "install" and "--global" in args:
        print("🌐 Instalação global ainda não implementada")
        print("💡 Use o instalador normal e depois copie este script para o PATH")
        return 1
    
    # Executar Context Navigator
    return run_context_navigator(args)

if __name__ == "__main__":
    sys.exit(main()) 