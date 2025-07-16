"""
Context Navigator - Core Scripts
Scripts essenciais de processamento principal
"""

from .context_scanner import ContextScanner
from .context_engine import ContextEngine

__all__ = ['ContextScanner', 'ContextEngine']

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