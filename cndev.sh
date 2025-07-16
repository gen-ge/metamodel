#!/bin/bash
# 🛠️ Context Navigator - Development Mode  
# Roda diretamente do código fonte (sem build/install)

# Detectar diretório do projeto automaticamente
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$SCRIPT_DIR/src"

echo "🛠️ Context Navigator Development Mode"
echo "📁 Project: $SCRIPT_DIR"
echo "🐍 PYTHONPATH: $PYTHONPATH"
echo ""

exec python3 -m context_navigator.cn_cli_legacy "$@" 