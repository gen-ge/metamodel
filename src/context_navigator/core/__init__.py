# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:module global-core
# @cn:doc global-core.md
# @cn:context-level c2_module
# @cn:context-type core
# @cn:parent-system context-navigator
# @cn:purpose "Módulo core da arquitetura global - entry points e gerenciadores principais"
# @cn:memory-aid "Coração da arquitetura global - workspace, daemon, migração e router"
# @cn:provides workspace-management, daemon-system, migration-tools, global-routing
# ============================================

"""
Context Navigator - Global Core Module
Componentes centrais da arquitetura global
"""

from .workspace_manager import WorkspaceManager, Workspace
from .cn_global import GlobalCommandRouter
from .daemon_manager import DaemonManager, DaemonMaster, WorkspaceWorker
from .migration_manager import MigrationManager

__version__ = "2.0.0"

__all__ = [
    'WorkspaceManager',
    'Workspace', 
    'GlobalCommandRouter',
    'DaemonManager',
    'DaemonMaster',
    'WorkspaceWorker',
    'MigrationManager'
] 