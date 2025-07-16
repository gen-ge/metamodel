"""
Context Navigator - Validation Scripts
Scripts especializados em validação de qualidade
"""

from .template_validator import TemplateValidator
from .cn_consistency_validator import CNConsistencyValidator
from .metrics_validator import MetricsValidator

__all__ = ['TemplateValidator', 'CNConsistencyValidator', 'MetricsValidator']

# Documentação dos scripts
SCRIPTS = {
    'template_validator': {
        'description': 'Validação especializada de templates metodológicos',
        'class': 'TemplateValidator',
        'file': 'template_validator.py'
    },
    'cn_consistency_validator': {
        'description': 'Validação de consistência entre código e documentação',
        'class': 'CNConsistencyValidator',
        'file': 'cn_consistency_validator.py'
    },
    'metrics_validator': {
        'description': 'Validação contra métricas de sucesso do PRD',
        'class': 'MetricsValidator',
        'file': 'metrics_validator.py'
    }
} 