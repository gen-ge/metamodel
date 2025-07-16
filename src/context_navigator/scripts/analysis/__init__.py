"""
Context Navigator - Analysis Scripts
Scripts de análise avançada e inteligência artificial
"""

from .pattern_detector import PatternDetector
from .conflict_detector import ConflictDetector
from .impact_analyzer import ImpactAnalyzer
from .context_advisor import ContextAdvisor

__all__ = ['PatternDetector', 'ConflictDetector', 'ImpactAnalyzer', 'ContextAdvisor']

# Documentação dos scripts
SCRIPTS = {
    'pattern_detector': {
        'description': 'Detecta padrões e anomalias na documentação',
        'class': 'PatternDetector',
        'file': 'pattern_detector.py'
    },
    'conflict_detector': {
        'description': 'Detecta conflitos e inconsistências complexas',
        'class': 'ConflictDetector',
        'file': 'conflict_detector.py'
    },
    'impact_analyzer': {
        'description': 'Analisa impacto de mudanças em documentos',
        'class': 'ImpactAnalyzer',
        'file': 'impact_analyzer.py'
    },
    'context_advisor': {
        'description': 'Sistema de sugestões inteligente baseado em contexto',
        'class': 'ContextAdvisor',
        'file': 'context_advisor.py'
    }
} 