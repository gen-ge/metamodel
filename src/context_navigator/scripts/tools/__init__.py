"""
Context Navigator - Tool Scripts
Ferramentas utilitárias e auxiliares
"""

from .cn_component_explorer import CNComponentExplorer
from .cn_component_parser import CNComponentParser

__all__ = ['CNComponentExplorer', 'CNComponentParser']

# Documentação dos scripts
SCRIPTS = {
    'cn_component_explorer': {
        'description': 'Explorador visual de componentes hierárquicos',
        'class': 'CNComponentExplorer',
        'file': 'cn_component_explorer.py'
    },
    'cn_component_parser': {
        'description': 'Parser para extrair marcações @cn: do código',
        'class': 'CNComponentParser',
        'file': 'cn_component_parser.py'
    },
    'context_demo': {
        'description': 'Demonstração completa das funcionalidades',
        'class': 'ContextDemo',
        'file': 'context_demo.py'
    },
    'cn_global_launcher': {
        'description': 'Launcher global para arquitetura 2.0',
        'class': None,
        'file': 'cn_global_launcher.py'
    }
} 