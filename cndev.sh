#!/bin/bash
# cndev.sh - Versão Final Unificada

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$SCRIPT_DIR/src"

echo "🛠️ Context Navigator Development Mode"
echo "📁 Project: $SCRIPT_DIR"
echo "🐍 PYTHONPATH: $PYTHONPATH"
echo "🎯 Sistema: cn_global.py (unificado)"
echo "📋 Registry: src/context_navigator/workspaces-registry.yml"
echo ""

# USAR APENAS SISTEMA UNIFICADO
exec python3 -m context_navigator.core.cn_global "$@" 