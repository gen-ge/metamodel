#!/usr/bin/env python3

# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component migration-manager
# @cn:doc migration-manager.md
# @cn:context-level c3_component
# @cn:context-type integration
# @cn:parent-module global-core
# @cn:purpose "Migração de instalações locais (.context-navigator/) para workspaces globais (.cn_model/)"
# @cn:memory-aid "Cuida dos usuários existentes - migração suave e com backup"
# @cn:depends-on workspace-manager, shutil, pathlib
# @cn:provides migration-script, backup-system, compatibility
# @cn:component-type functional
# @cn:responsibility migration-management
# ============================================

"""
Context Navigator - Migration Manager
COMPORTAMENTO: Migração suave de instalações locais para globais com backup
"""

import os
import sys
import shutil
import time
from pathlib import Path
from typing import List, Dict, Optional

try:
    from .workspace_manager import WorkspaceManager
except ImportError:
    # Execução direta - adicionar path
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from workspace_manager import WorkspaceManager


class MigrationManager:
    """Gerencia migração de instalações locais para globais"""
    
    def __init__(self):
        self.workspace_manager = WorkspaceManager()
        self.backup_suffix = f".backup.{int(time.time())}"
    
    def migrate_all_local_installations(self) -> int:
        """Migra todas as instalações locais encontradas"""
        print("🔄 Context Navigator - Migração para Arquitetura Global")
        print("=" * 60)
        
        # 1. Detectar instalações locais
        local_installations = self.find_local_installations()
        
        if not local_installations:
            print("✅ Nenhuma instalação local encontrada")
            print("💡 Sistema já está na versão global ou não há instalações antigas")
            return 0
        
        print(f"📦 Encontradas {len(local_installations)} instalações locais:")
        for install in local_installations:
            print(f"   📁 {install}")
        
        # 2. Confirmar migração
        if not self._confirm_migration():
            print("❌ Migração cancelada pelo usuário")
            return 1
        
        # 3. Migrar cada instalação
        migrated_count = 0
        failed_count = 0
        
        for install_path in local_installations:
            try:
                result = self.migrate_single_installation(install_path)
                if result == 0:
                    migrated_count += 1
                else:
                    failed_count += 1
            except Exception as e:
                print(f"❌ Erro ao migrar {install_path}: {e}")
                failed_count += 1
        
        # 4. Relatório final
        print("\n" + "=" * 60)
        print(f"🎉 Migração concluída!")
        print(f"✅ Migradas com sucesso: {migrated_count}")
        if failed_count > 0:
            print(f"❌ Falhas: {failed_count}")
        
        print(f"\n💡 Agora use 'cn' de qualquer diretório")
        print(f"💡 Execute 'cn --version' para verificar a nova versão")
        
        return 0 if failed_count == 0 else 1
    
    def migrate_single_installation(self, install_path: Path) -> int:
        """Migra uma instalação local específica"""
        print(f"\n🔄 Migrando: {install_path}")
        
        try:
            # 1. Validar instalação local
            if not self._validate_local_installation(install_path):
                print(f"   ❌ Instalação local inválida")
                return 1
            
            # 2. Determinar workspace root
            workspace_root = install_path.parent
            print(f"   📁 Workspace root: {workspace_root}")
            
            # 3. Backup da instalação local
            backup_path = self._backup_local_installation(install_path)
            print(f"   📦 Backup criado: {backup_path}")
            
            # 4. Migrar documentos para novo formato
            docs_migrated = self._migrate_documents(install_path, workspace_root)
            print(f"   📄 Documentos migrados: {docs_migrated}")
            
            # 5. Criar novo workspace global
            init_result = self.workspace_manager.init_workspace(workspace_root)
            if init_result != 0:
                print(f"   ❌ Falha ao criar workspace global")
                return 1
            
            # 6. Limpar instalação local antiga
            self._cleanup_local_installation(install_path)
            print(f"   🧹 Instalação local removida")
            
            print(f"   ✅ Migração completa: {workspace_root}")
            return 0
            
        except Exception as e:
            print(f"   ❌ Erro durante migração: {e}")
            return 1
    
    def find_local_installations(self) -> List[Path]:
        """Encontra todas as instalações locais do Context Navigator"""
        installations = []
        
        # Diretórios comuns onde procurar
        search_paths = [
            Path.home(),
            Path.cwd(),
            Path.home() / "projetos",
            Path.home() / "workspace", 
            Path.home() / "Documents",
            Path.home() / "dev"
        ]
        
        print("🔍 Procurando instalações locais...")
        
        for search_path in search_paths:
            if search_path.exists():
                try:
                    # Buscar .context-navigator/ recursivamente
                    for cn_dir in search_path.rglob(".context-navigator"):
                        if self._validate_local_installation(cn_dir):
                            installations.append(cn_dir)
                            print(f"   📍 Encontrada: {cn_dir}")
                except (PermissionError, OSError):
                    # Ignorar diretórios sem permissão
                    continue
        
        return installations
    
    def _validate_local_installation(self, cn_dir: Path) -> bool:
        """Valida se é uma instalação local válida"""
        if not cn_dir.exists() or not cn_dir.is_dir():
            return False
        
        # Verificar se tem estrutura esperada
        required_items = [
            cn_dir / "scripts",
            cn_dir / "docs"
        ]
        
        for item in required_items:
            if not item.exists():
                return False
        
        # Verificar se tem scripts principais
        key_scripts = [
            cn_dir / "scripts" / "context_engine.py",
            cn_dir / "scripts" / "context_scanner.py"
        ]
        
        for script in key_scripts:
            if script.exists():
                return True
        
        return False
    
    def _confirm_migration(self) -> bool:
        """Confirma migração com o usuário"""
        print("\n⚠️  Esta migração irá:")
        print("   • Converter instalações locais em workspaces globais")
        print("   • Fazer backup das instalações antigas")
        print("   • Criar estrutura .cn_model/ em cada projeto")
        print("   • Remover diretórios .context-navigator/ após migração")
        
        while True:
            response = input("\n🤔 Continuar com a migração? (s/N): ").strip().lower()
            if response in ['s', 'sim', 'y', 'yes']:
                return True
            elif response in ['n', 'nao', 'não', 'no', '']:
                return False
            else:
                print("💡 Responda 's' para sim ou 'n' para não")
    
    def _backup_local_installation(self, install_path: Path) -> Path:
        """Cria backup da instalação local antes de migrar"""
        backup_name = f".context-navigator{self.backup_suffix}"
        backup_path = install_path.parent / backup_name
        
        shutil.copytree(install_path, backup_path)
        return backup_path
    
    def _migrate_documents(self, install_path: Path, workspace_root: Path) -> int:
        """Migra documentos da instalação local para novo formato"""
        old_docs_dir = install_path / "docs"
        
        if not old_docs_dir.exists():
            return 0
        
        # Preparar novo diretório de docs
        new_cn_model = workspace_root / ".cn_model"
        new_cn_model.mkdir(exist_ok=True)
        new_docs_dir = new_cn_model / "docs"
        new_docs_dir.mkdir(exist_ok=True)
        
        # Copiar documentos
        docs_count = 0
        try:
            for doc_file in old_docs_dir.glob("*.md"):
                target_file = new_docs_dir / doc_file.name
                shutil.copy2(doc_file, target_file)
                docs_count += 1
                
            # Copiar component-map.yml se existir
            component_map = install_path / "component-map.yml"
            if component_map.exists():
                shutil.copy2(component_map, new_cn_model / "component-map.yml")
                
        except Exception as e:
            print(f"   ⚠️  Aviso ao migrar documentos: {e}")
        
        return docs_count
    
    def _cleanup_local_installation(self, install_path: Path):
        """Remove instalação local após migração bem-sucedida"""
        try:
            shutil.rmtree(install_path)
        except Exception as e:
            print(f"   ⚠️  Aviso ao remover instalação local: {e}")
            print(f"   💡 Você pode remover manualmente: {install_path}")
    
    def check_migration_needed(self) -> bool:
        """Verifica se há necessidade de migração"""
        installations = self.find_local_installations()
        return len(installations) > 0
    
    def show_migration_status(self) -> int:
        """Mostra status de migração"""
        print("🔍 Context Navigator - Status de Migração")
        print("=" * 50)
        
        installations = self.find_local_installations()
        
        if not installations:
            print("✅ Sistema totalmente migrado para arquitetura global")
            print("💡 Nenhuma instalação local encontrada")
            return 0
        
        print(f"📦 Instalações locais encontradas: {len(installations)}")
        for install in installations:
            print(f"   📁 {install}")
        
        print(f"\n💡 Execute 'cn migrate' para converter para arquitetura global")
        return 1


def main():
    """Função principal para execução do migration manager"""
    manager = MigrationManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "check":
            return manager.show_migration_status()
        elif command == "migrate":
            return manager.migrate_all_local_installations()
        else:
            print(f"❌ Comando não reconhecido: {command}")
            print("💡 Comandos disponíveis: check, migrate")
            return 1
    else:
        # Execução interativa
        print("🔄 Context Navigator - Migration Manager")
        print("1. check   - Verificar status de migração")
        print("2. migrate - Executar migração completa")
        
        choice = input("\nEscolha (1/2): ").strip()
        
        if choice == "1":
            return manager.show_migration_status()
        elif choice == "2":
            return manager.migrate_all_local_installations()
        else:
            print("❌ Opção inválida")
            return 1


if __name__ == "__main__":
    sys.exit(main()) 