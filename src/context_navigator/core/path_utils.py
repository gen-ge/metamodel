"""
Context Navigator - Path Utils
Utilitários para gerenciar caminhos do Context Navigator
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any


def find_context_navigator_root(start_path: str = ".") -> Optional[Path]:
    """
    Encontra o diretório root do Context Navigator procurando por .context-navigator/
    
    Args:
        start_path: Diretório inicial para busca
        
    Returns:
        Path para o diretório root ou None se não encontrado
    """
    current_path = Path(start_path).resolve()
    
    while current_path != current_path.parent:
        context_nav_path = current_path / ".context-navigator"
        if context_nav_path.exists() and context_nav_path.is_dir():
            return current_path
        current_path = current_path.parent
    
    return None


def get_context_navigator_paths(root_path: Optional[Path] = None) -> Dict[str, Path]:
    """
    Retorna os caminhos principais do Context Navigator
    
    Args:
        root_path: Diretório root (se não fornecido, busca automaticamente)
        
    Returns:
        Dicionário com os caminhos principais
    """
    if root_path is None:
        root_path = find_context_navigator_root()
        if root_path is None:
            raise FileNotFoundError("Context Navigator root não encontrado")
    
    paths = {
        'root': root_path,
        'context_navigator': root_path / '.context-navigator',
        'docs': root_path / '.context-navigator' / 'docs',
        'context_map': root_path / '.context-navigator' / 'context-map',
        'config': root_path / '.context-navigator' / '.contextrc',
        'rule': root_path / '.context-navigator' / 'context.rule',
        'decisions': root_path / '.context-navigator' / 'docs' / 'decisions',
        'processes': root_path / '.context-navigator' / 'docs' / 'processes',
        'references': root_path / '.context-navigator' / 'docs' / 'references',
        'architecture': root_path / '.context-navigator' / 'docs' / 'architecture',
        'analysis': root_path / '.context-navigator' / 'docs' / 'analysis',
        'planning': root_path / '.context-navigator' / 'docs' / 'planning'
    }
    
    return paths


def ensure_context_navigator_structure(root_path: Optional[Path] = None) -> bool:
    """
    Garante que a estrutura do Context Navigator existe
    
    Args:
        root_path: Diretório root (se não fornecido, busca automaticamente)
        
    Returns:
        True se a estrutura foi criada/verificada com sucesso
    """
    try:
        paths = get_context_navigator_paths(root_path)
        
        # Criar diretórios necessários
        dirs_to_create = [
            paths['context_navigator'],
            paths['docs'],
            paths['context_map'],
            paths['decisions'],
            paths['processes'],
            paths['references'],
            paths['architecture'],
            paths['analysis'],
            paths['planning']
        ]
        
        for dir_path in dirs_to_create:
            dir_path.mkdir(parents=True, exist_ok=True)
            
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar estrutura: {e}")
        return False


def get_package_path() -> Path:
    """
    Retorna o caminho para o pacote context_navigator
    
    Returns:
        Path para o diretório do pacote
    """
    return Path(__file__).parent.parent


def get_templates_path() -> Path:
    """
    Retorna o caminho para os templates
    
    Returns:
        Path para o diretório de templates
    """
    return get_package_path() / 'templates'


def get_scripts_path() -> Path:
    """
    Retorna o caminho para os scripts
    
    Returns:
        Path para o diretório de scripts
    """
    return get_package_path() / 'scripts' 