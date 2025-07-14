"""
Context Navigator - Config Utils
Utilitários para gerenciar configurações do Context Navigator
"""

import os
from pathlib import Path
from typing import Any, Dict, Optional
from .path_utils import get_context_navigator_paths


def load_contextrc(config_path: Optional[Path] = None) -> Dict[str, Any]:
    """
    Carrega configurações do .contextrc
    
    Args:
        config_path: Caminho para o arquivo .contextrc (opcional)
        
    Returns:
        Dicionário com configurações
    """
    if config_path is None:
        try:
            paths = get_context_navigator_paths()
            config_path = paths['config']
        except FileNotFoundError:
            return {}
    
    config = {}
    
    if config_path and config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if '=' in line:
                            key, value = line.split('=', 1)
                            config[key.strip()] = value.strip().strip('"\'')
        except Exception as e:
            print(f"⚠️  Erro ao carregar .contextrc: {e}")
    
    return config


def get_config_value(key: str, default: Any = None, config_path: Optional[Path] = None) -> Any:
    """
    Obtém valor de configuração específico
    
    Args:
        key: Chave da configuração
        default: Valor padrão se não encontrado
        config_path: Caminho para o arquivo .contextrc (opcional)
        
    Returns:
        Valor da configuração ou default
    """
    config = load_contextrc(config_path)
    return config.get(key, default)


def update_config(updates: Dict[str, Any], config_path: Optional[Path] = None) -> bool:
    """
    Atualiza configurações no .contextrc
    
    Args:
        updates: Dicionário com atualizações
        config_path: Caminho para o arquivo .contextrc (opcional)
        
    Returns:
        True se atualizado com sucesso
    """
    if config_path is None:
        try:
            paths = get_context_navigator_paths()
            config_path = paths['config']
        except FileNotFoundError:
            print("❌ Context Navigator não encontrado")
            return False
    
    if not config_path:
        print("❌ Caminho de configuração inválido")
        return False
    
    try:
        # Carregar configurações existentes
        existing_config = load_contextrc(config_path)
        
        # Aplicar atualizações
        existing_config.update(updates)
        
        # Salvar configurações atualizadas
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write("# Context Navigator Configuration\n")
            f.write("# Generated automatically\n\n")
            
            for key, value in existing_config.items():
                f.write(f"{key}={value}\n")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao atualizar configuração: {e}")
        return False


def get_default_config() -> Dict[str, Any]:
    """
    Retorna configuração padrão do Context Navigator
    
    Returns:
        Dicionário com configuração padrão
    """
    return {
        'CONTEXT_NAVIGATOR_VERSION': '1.0.0',
        'CONTEXT_DOCS_PATH': '.context-navigator/docs',
        'CONTEXT_MAP_PATH': '.context-navigator/context-map',
        'DEFAULT_EDITOR': 'nano',
        'AUTO_SCAN': 'true',
        'DEBUG_MODE': 'false',
        'TEMPLATE_LANGUAGE': 'pt-BR'
    }


def init_default_config(config_path: Optional[Path] = None) -> bool:
    """
    Inicializa arquivo .contextrc com configurações padrão
    
    Args:
        config_path: Caminho para o arquivo .contextrc (opcional)
        
    Returns:
        True se inicializado com sucesso
    """
    default_config = get_default_config()
    return update_config(default_config, config_path)


def validate_config(config_path: Optional[Path] = None) -> bool:
    """
    Valida configurações do Context Navigator
    
    Args:
        config_path: Caminho para o arquivo .contextrc (opcional)
        
    Returns:
        True se configuração é válida
    """
    try:
        config = load_contextrc(config_path)
        
        # Verificar se configurações essenciais existem
        required_keys = ['CONTEXT_DOCS_PATH', 'CONTEXT_MAP_PATH']
        
        for key in required_keys:
            if key not in config:
                print(f"❌ Configuração obrigatória ausente: {key}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na validação da configuração: {e}")
        return False 