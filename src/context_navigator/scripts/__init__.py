"""
Context Navigator - Scripts
Sistema de scripts organizados por responsabilidade na arquitetura 2.0

Estrutura:
- core/       : Scripts essenciais de processamento
- validation/ : Scripts de validação de qualidade  
- analysis/   : Scripts de análise avançada e IA
- tools/      : Ferramentas utilitárias e auxiliares
"""

# Imports por categoria
from . import engines
from . import validation
from . import analysis
from . import tools

__all__ = ['engines', 'validation', 'analysis', 'tools']

# Mapa completo de scripts
SCRIPT_CATEGORIES = {
    'engines': {
        'description': 'Engines essenciais de processamento principal',
        'scripts': engines.ENGINES
    },
    'validation': {
        'description': 'Scripts especializados em validação de qualidade',
        'scripts': validation.SCRIPTS
    },
    'analysis': {
        'description': 'Scripts de análise avançada e inteligência artificial',
        'scripts': analysis.SCRIPTS
    },
    'tools': {
        'description': 'Ferramentas utilitárias e auxiliares',
        'scripts': tools.SCRIPTS
    }
}

def get_script_info():
    """Retorna informações sobre todos os scripts organizados"""
    return SCRIPT_CATEGORIES

def list_scripts():
    """Lista todos os scripts disponíveis"""
    for category, info in SCRIPT_CATEGORIES.items():
        print(f"\n📁 {category.upper()}: {info['description']}")
        for script_name, script_info in info['scripts'].items():
            print(f"   • {script_name}: {script_info['description']}") 