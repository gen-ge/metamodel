#!/usr/bin/env python3

# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component cn-component-explorer
# @cn:doc cn-component-explorer.md
# @cn:context-level c3_component
# @cn:context-type interface
# @cn:parent-module cli-interface
# @cn:purpose "Explorador de componentes que exibe hierarquia visual do sistema"
# @cn:memory-aid "Explorador visual - mostra árvore de sistema → módulo → componente"
# @cn:depends-on component-map.yml, cn-component-parser
# @cn:impacts user-navigation, system-understanding, component-discovery
# @cn:provides hierarchy-visualization, component-exploration, tree-display
# @cn:component-type interface
# @cn:responsibility visualization
# @cn:single-purpose true
# ============================================

"""
CN Component Explorer - Explorador de Componentes
Exibe hierarquia visual de componentes do Context Navigator
"""

import yaml
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('cn_explorer')

class CNComponentExplorer:
    """Explorador visual de componentes"""
    
    # @cn:class service
    # @cn:responsibility visualization
    # @cn:single-purpose true
    
    def __init__(self, base_path: str = "."):
        # @cn:function core
        # @cn:process initialization
        self.base_path = Path(base_path)
        self.component_map = None
        
        # NOVO: Usar WorkspaceManager para detectar workspace
        self._init_with_workspace_manager()
            
        self._load_component_map()
        
    def _init_with_workspace_manager(self):
        """Inicializa usando WorkspaceManager para detectar workspace"""
        # Importar WorkspaceManager
        try:
            from ..core.workspace_manager import WorkspaceManager, Workspace
        except ImportError:
            # Fallback para desenvolvimento
            import sys
            sys.path.insert(0, str(Path(__file__).parent.parent))
            from core.workspace_manager import WorkspaceManager, Workspace
        
        # Detectar workspace atual
        workspace_manager = WorkspaceManager()
        current_workspace = workspace_manager.detect_current_workspace()
        
        if not current_workspace:
            logger.error("❌ Context Navigator workspace não encontrado")
            logger.error("💡 Execute 'cn init' para configurar este diretório")
            sys.exit(1)
        
        # Configurar paths baseado no workspace
        self.workspace = current_workspace
        self.base_path = current_workspace.root_path
        self.output_dir = current_workspace.root_path / ".cn_model" / "maps"
        
        logger.info(f"🌐 Workspace: {current_workspace.name} ({current_workspace.root_path})")
        
    # @cn:function integration
    # @cn:process data-loading
    # @cn:file-dependency component-map.yml
    def _load_component_map(self) -> None:
        """Carrega component-map.yml"""
        
        # Arquitetura workspace: buscar em .cn_model/maps/
        possible_paths = [
            self.output_dir / "component-map.yml",
            self.output_dir / "component-map-final.yml"
        ]
        help_msg = "💡 Execute: cn component parse para gerar component map"
        
        for path in possible_paths:
            if path.exists():
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        self.component_map = yaml.safe_load(f)
                    logger.info(f"Component map carregado: {path}")
                    return
                except Exception as e:
                    logger.warning(f"Erro ao carregar {path}: {e}")
                    
        logger.error("❌ Nenhum component-map.yml encontrado!")
        logger.info(help_msg)
    
    # @cn:function critical
    # @cn:process hierarchy-visualization
    # @cn:step 1
    def explore_system(self, system_name: Optional[str] = None) -> str:
        """
        Explora e exibe hierarquia de componentes
        
        Args:
            system_name: Nome do sistema (None = todos)
            
        Returns:
            String com árvore hierárquica
        """
        if not self.component_map:
            return "❌ Component map não carregado"
            
        output = []
        output.append("# 🧩 Context Navigator - Exploração de Componentes\n")
        
        # Estatísticas gerais
        total = self.component_map.get('total_components', 0)
        systems = self.component_map.get('systems', {})
        modules = self.component_map.get('modules', {})
        components = self.component_map.get('components', {})
        
        output.append(f"**Total:** {total} componentes")
        output.append(f"- 🏛️  Sistemas: {len(systems)}")
        output.append(f"- 📦 Módulos: {len(modules)}")
        output.append(f"- ⚙️  Componentes: {len(components)}\n")
        
        # Exibir hierarquia
        if system_name:
            # Sistema específico
            if system_name in systems:
                output.append(self._render_system_tree(system_name, systems[system_name], modules, components))
            else:
                output.append(f"❌ Sistema '{system_name}' não encontrado")
        else:
            # Todos os sistemas
            for sys_name, sys_data in systems.items():
                output.append(self._render_system_tree(sys_name, sys_data, modules, components))
                output.append("")
        
        return "\n".join(output)
    
    # @cn:function core
    # @cn:process tree-rendering
    # @cn:step 2
    def _render_system_tree(self, sys_name: str, sys_data: Dict, 
                           modules: Dict, components: Dict) -> str:
        """Renderiza árvore de um sistema específico"""
        
        tree = []
        tree.append(f"## 🏛️  {sys_name.upper()}")
        tree.append(f"📁 **Arquivo:** `{sys_data.get('file', 'N/A')}`")
        tree.append(f"📋 **Doc:** `{sys_data.get('doc', 'N/A')}`")
        tree.append(f"🎯 **Propósito:** {sys_data.get('purpose', 'N/A')}")
        tree.append("")
        
        # Encontrar módulos deste sistema
        system_modules = self._find_modules_for_system(sys_name, modules)
        
        if not system_modules:
            tree.append("└── ℹ️  Nenhum módulo encontrado")
            return "\n".join(tree)
        
        for i, (mod_name, mod_data) in enumerate(system_modules.items()):
            is_last_module = (i == len(system_modules) - 1)
            module_prefix = "└──" if is_last_module else "├──"
            
            tree.append(f"{module_prefix} 📦 **{mod_name}**")
            tree.append(f"{'    ' if is_last_module else '│   '}   📁 `{mod_data.get('file', 'N/A')}`")
            tree.append(f"{'    ' if is_last_module else '│   '}   📋 `{mod_data.get('doc', 'N/A')}`")
            
            # Encontrar componentes deste módulo
            module_components = self._find_components_for_module(mod_name, components)
            
            if module_components:
                for j, (comp_name, comp_data) in enumerate(module_components.items()):
                    is_last_component = (j == len(module_components) - 1)
                    comp_prefix = "└──" if is_last_component else "├──"
                    indent = "    " if is_last_module else "│   "
                    
                    tree.append(f"{indent}   {comp_prefix} ⚙️  **{comp_name}**")
                    tree.append(f"{indent}   {'    ' if is_last_component else '│   '}   📁 `{comp_data.get('file', 'N/A')}`")
                    tree.append(f"{indent}   {'    ' if is_last_component else '│   '}   📋 `{comp_data.get('doc', 'N/A')}`")
                    tree.append(f"{indent}   {'    ' if is_last_component else '│   '}   🏷️  `{comp_data.get('context_type', 'N/A')}`")
            else:
                tree.append(f"{'    ' if is_last_module else '│   '}   └── ℹ️  Nenhum componente")
        
        return "\n".join(tree)
    
    # @cn:function integration
    # @cn:process data-filtering
    def _find_modules_for_system(self, system_name: str, modules: Dict) -> Dict:
        """Encontra módulos que pertencem ao sistema"""
        result = {}
        for mod_name, mod_data in modules.items():
            # Verificar se módulo tem parent-system ou se está relacionado
            if mod_data.get('parent_system') == system_name:
                result[mod_name] = mod_data
            elif system_name in mod_data.get('file', ''):
                result[mod_name] = mod_data
        return result
    
    # @cn:function integration  
    # @cn:process data-filtering
    def _find_components_for_module(self, module_name: str, components: Dict) -> Dict:
        """Encontra componentes que pertencem ao módulo"""
        result = {}
        for comp_name, comp_data in components.items():
            # Verificar se componente tem parent-module ou está no mesmo diretório
            if comp_data.get('parent_module') == module_name:
                result[comp_name] = comp_data
            elif module_name in comp_data.get('file', ''):
                result[comp_name] = comp_data
            # Para Context Navigator, todos os componentes em scripts/ pertencem ao cli-interface
            elif module_name == 'cli-interface' and 'scripts/' in comp_data.get('file', ''):
                result[comp_name] = comp_data
        return result
    
    # @cn:function integration
    # @cn:process list-display
    def list_components(self, filter_type: Optional[str] = None) -> str:
        """Lista componentes em formato simples"""
        
        if not self.component_map:
            return "❌ Component map não carregado"
            
        output = []
        output.append("# 📋 Lista de Componentes\n")
        
        sections = [
            ("🏛️  Sistemas", self.component_map.get('systems', {})),
            ("📦 Módulos", self.component_map.get('modules', {})),
            ("⚙️  Componentes", self.component_map.get('components', {}))
        ]
        
        for section_name, items in sections:
            if filter_type and section_name.lower().find(filter_type.lower()) == -1:
                continue
                
            if items:
                output.append(f"## {section_name}")
                for name, data in items.items():
                    output.append(f"- **{name}** (`{data.get('context_type', 'N/A')}`) - {data.get('purpose', 'N/A')}")
                output.append("")
        
        return "\n".join(output)

# @cn:function entry-point
# @cn:process cli-interface
def main():
    """Função principal para uso via linha de comando"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Explorador de componentes Context Navigator')
    parser.add_argument('system', nargs='?', help='Nome do sistema para explorar (opcional)')
    parser.add_argument('--list', action='store_true', help='Listar componentes em formato simples')
    parser.add_argument('--filter', help='Filtrar por tipo (systems, modules, components)')
    parser.add_argument('--path', default='.', help='Caminho do projeto')
    
    args = parser.parse_args()
    
    explorer = CNComponentExplorer(args.path)
    
    if args.list:
        result = explorer.list_components(args.filter)
    else:
        result = explorer.explore_system(args.system)
    
    print(result)

if __name__ == '__main__':
    main() 