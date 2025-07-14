"""
Context Navigator - Template Utils
Utilitários para gerenciar templates do Context Navigator
"""

from pathlib import Path
from typing import Dict, Optional
from .path_utils import get_templates_path


def get_template_mapping() -> Dict[str, str]:
    """
    Retorna o mapeamento de tipos de documento para templates
    
    Returns:
        Dicionário com mapeamento tipo -> template
    """
    return {
        'decision': 'decisao.md',
        'process': 'processo.md',
        'reference': 'referencia.md',
        'architecture': 'arquitetura.md',
        'analysis': 'analise.md',
        'planning': 'planejamento.md'
    }


def get_type_mapping() -> Dict[str, str]:
    """
    Retorna o mapeamento de tipos inglês para português
    
    Returns:
        Dicionário com mapeamento inglês -> português
    """
    return {
        'decision': 'decisions',
        'process': 'processes',
        'reference': 'references',
        'architecture': 'architecture',
        'analysis': 'analysis',
        'planning': 'planning'
    }


def get_template_path(template_name: str) -> Path:
    """
    Retorna o caminho para um template específico
    
    Args:
        template_name: Nome do template (ex: 'decisao.md')
        
    Returns:
        Path para o template
    """
    templates_path = get_templates_path()
    return templates_path / template_name


def load_template(template_name: str) -> str:
    """
    Carrega o conteúdo de um template
    
    Args:
        template_name: Nome do template (ex: 'decisao.md')
        
    Returns:
        Conteúdo do template como string
        
    Raises:
        FileNotFoundError: Se o template não existir
    """
    template_path = get_template_path(template_name)
    
    if not template_path.exists():
        raise FileNotFoundError(f"Template não encontrado: {template_path}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def get_template_by_type(doc_type: str) -> str:
    """
    Carrega template baseado no tipo de documento
    
    Args:
        doc_type: Tipo do documento (decision, process, etc.)
        
    Returns:
        Conteúdo do template
        
    Raises:
        ValueError: Se o tipo não for reconhecido
        FileNotFoundError: Se o template não existir
    """
    template_mapping = get_template_mapping()
    
    if doc_type not in template_mapping:
        available_types = ', '.join(template_mapping.keys())
        raise ValueError(f"Tipo '{doc_type}' não reconhecido. Tipos disponíveis: {available_types}")
    
    template_name = template_mapping[doc_type]
    return load_template(template_name)


def list_available_templates() -> Dict[str, Path]:
    """
    Lista todos os templates disponíveis
    
    Returns:
        Dicionário com nome -> Path dos templates
    """
    templates_path = get_templates_path()
    templates = {}
    
    if templates_path.exists():
        for template_file in templates_path.glob('*.md'):
            templates[template_file.name] = template_file
    
    return templates


def validate_template_structure() -> bool:
    """
    Valida se todos os templates necessários existem
    
    Returns:
        True se todos os templates existem
    """
    template_mapping = get_template_mapping()
    
    for template_name in template_mapping.values():
        template_path = get_template_path(template_name)
        if not template_path.exists():
            print(f"❌ Template ausente: {template_name}")
            return False
    
    return True 