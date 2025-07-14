"""
Context Navigator - Core Module
Módulo principal com funções comuns do Context Navigator
"""

try:
    from .path_utils import (
        find_context_navigator_root,
        get_context_navigator_paths,
        ensure_context_navigator_structure
    )
    
    from .template_utils import (
        get_template_path,
        load_template,
        get_template_mapping
    )
    
    from .config_utils import (
        load_contextrc,
        get_config_value,
        update_config
    )
    
    __all__ = [
        'find_context_navigator_root',
        'get_context_navigator_paths',
        'ensure_context_navigator_structure',
        'get_template_path',
        'load_template',
        'get_template_mapping',
        'load_contextrc',
        'get_config_value',
        'update_config'
    ]
    
except ImportError:
    # Se imports falharem, definir lista vazia para evitar erros
    __all__ = []
