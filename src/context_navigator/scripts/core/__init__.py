"""
Context Navigator - Core Scripts
Scripts essenciais de processamento principal
"""

from .context_scanner import ContextScanner
from .context_engine import ContextEngine

# Import WorkspaceManager from the correct location for scripts that need it
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from core.workspace_manager import WorkspaceManager

__all__ = ['ContextScanner', 'ContextEngine', 'WorkspaceManager']

# Documentação dos scripts
SCRIPTS = {
    'context_scanner': {
        'description': 'Escaneia documentos e gera mapas de contexto',
        'class': 'ContextScanner',
        'file': 'context_scanner.py'
    },
    'context_engine': {
        'description': 'Motor principal de processamento contextual',
        'class': 'ContextEngine', 
        'file': 'context_engine.py'
    }
} 