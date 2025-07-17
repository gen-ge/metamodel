"""
Context Navigator - Processing Engines
Engines essenciais de processamento (scanner, context engine)
"""

from .context_scanner import ContextScanner
from .context_engine import ContextEngine

# Clean import - WorkspaceManager available when needed via context

__all__ = ['ContextScanner', 'ContextEngine']

# Documentação dos engines
ENGINES = {
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