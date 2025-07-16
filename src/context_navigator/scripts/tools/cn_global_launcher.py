#!/usr/bin/env python3
"""
🧭 Context Navigator 2.0.0 - Launcher Global
Launcher global que usa a nova arquitetura workspace-aware
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """
    Launcher global para Context Navigator 2.0.0
    Executa o cn_global.py com detecção automática de workspace
    """
    # Encontrar instalação global do Context Navigator
    possible_locations = [
        Path("/opt/context-navigator"),
        Path.home() / ".local" / "share" / "context-navigator",
    ]
    
    cn_installation = None
    for location in possible_locations:
        if location.exists() and (location / "core" / "cn_global.py").exists():
            cn_installation = location
            break
    
    if not cn_installation:
        print("❌ Context Navigator não encontrado. Execute a instalação primeiro.")
        return 1
    
    # Preparar ambiente para execução como módulo
    env = os.environ.copy()
    env['PYTHONPATH'] = str(cn_installation)
    
    # Executar como módulo Python (evita problemas de import relativo)
    cmd = [sys.executable, "-m", "core.cn_global"] + sys.argv[1:]
    
    try:
        # Manter o diretório de trabalho atual do usuário
        result = subprocess.run(cmd, env=env)
        return result.returncode
    except Exception as e:
        print(f"❌ Erro ao executar Context Navigator: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
