#!/usr/bin/env python3
"""
🚀 Context Navigator - Instalador Unificado
SISTEMA SIMPLIFICADO: Um só instalador para todas as situações

FUNCIONALIDADES:
- Detecção automática do melhor local
- Modo dry-run para testar
- Backup de instalação existente
- Instalação global e local
- Verificação de pré-requisitos

USO:
    python3 install.py                    # Instalação automática
    python3 install.py --global          # Forçar instalação global
    python3 install.py --dry-run         # Apenas testar (sem instalar)
    python3 install.py --path /custom    # Local customizado
"""

import os
import sys
import shutil
import subprocess
import yaml
from pathlib import Path
from datetime import datetime
from typing import Optional

class UnifiedInstaller:
    """Instalador unificado - melhor dos dois mundos"""
    
    def __init__(self, install_path: Optional[str] = None, global_install: bool = False, dry_run: bool = False):
        self.dry_run = dry_run
        
        print("🚀 Context Navigator - Instalador Unificado")
        print(f"🎯 Modo: {'DRY-RUN (teste)' if dry_run else 'INSTALAÇÃO REAL'}")
        
        # Detectar local de instalação
        if install_path:
            self.install_path = Path(install_path)
        elif global_install:
            self.install_path = self._get_global_install_path()
        else:
            self.install_path = self._detect_best_install_path()

        self.bin_path = self._detect_best_bin_path()
        
        # Detectar arquivos fonte
        installer_dir = Path(__file__).parent.resolve()
        
        # Se estamos em um pacote extraído (install.py na raiz, source/ ao lado)
        if (installer_dir.parent.parent / "source").exists():
            self.source_dir = installer_dir.parent.parent / "source"
        else:
            # Desenvolvimento - usar estrutura src/
            self.source_dir = installer_dir.parent
            
        self.version = "2.1.0"

    def _get_global_install_path(self) -> Path:
        """Local para instalação global forçada"""
        if os.access("/opt", os.W_OK):
            return Path("/opt/context-navigator")
        else:
            return Path.home() / ".local" / "share" / "context-navigator"

    def _detect_best_install_path(self) -> Path:
        """Detecta automaticamente o melhor local"""
        print("🔍 Detectando melhor local para instalação...")
        
        candidates = [
            Path.home() / ".local" / "share" / "context-navigator",  # XDG padrão
            Path.home() / ".context-navigator",                     # Alternativa
            Path("/opt/context-navigator"),                         # Sistema (se possível)
            Path.cwd() / ".context-navigator-install"               # Fallback local
        ]

        for i, path in enumerate(candidates, 1):
            if self.dry_run:
                print(f"  {i}. Testaria: {path}")
                continue
                
            try:
                print(f"  {i}. Testando: {path}")
                path.mkdir(parents=True, exist_ok=True)
                test_file = path / ".test_write"
                test_file.write_text("test")
                test_file.unlink()
                
                print(f"  ✅ Local escolhido: {path}")
                return path
                
            except (PermissionError, OSError) as e:
                print(f"  ❌ Sem permissão: {e}")
                continue

        # Se dry-run, retornar primeiro candidato
        if self.dry_run:
            return candidates[0]
            
        raise RuntimeError("❌ Não foi possível encontrar local para instalação")

    def _detect_best_bin_path(self) -> Path:
        """Detecta melhor local para executáveis"""
        print("🔍 Detectando melhor local para executáveis...")
        
        candidates = [
            Path.home() / ".local" / "bin",     # XDG padrão 
            Path("/usr/local/bin"),             # Sistema (se possível)
            Path.home() / "bin",                # Alternativa tradicional
            self.install_path / "bin"           # Junto com instalação
        ]

        for i, path in enumerate(candidates, 1):
            if self.dry_run:
                print(f"  {i}. Testaria: {path}")
                continue
                
            try:
                print(f"  {i}. Testando: {path}")
                path.mkdir(parents=True, exist_ok=True)
                test_file = path / ".test_exec"
                test_file.write_text("#!/bin/bash\necho test")
                test_file.chmod(0o755)
                test_file.unlink()
                
                print(f"  ✅ Local escolhido: {path}")
                return path
                
            except (PermissionError, OSError) as e:
                print(f"  ❌ Sem permissão: {e}")
                continue

        # Fallback ou dry-run
        fallback = self.install_path / "bin"
        print(f"  🔄 {'Testaria' if self.dry_run else 'Usando'}: {fallback}")
        return fallback

    def check_prerequisites(self) -> bool:
        """Verifica pré-requisitos"""
        print(f"\n🔍 Verificando pré-requisitos...")
        
        # Python version
        if sys.version_info < (3, 7):
            print("❌ Python 3.7+ necessário")
            return False
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
        
        # Source directory
        if not self.source_dir.exists():
            print(f"❌ Arquivos fonte não encontrados: {self.source_dir}")
            return False
        print(f"✅ Arquivos fonte: {self.source_dir}")
        
        # Essential files
        essential_files = [
            "core/cn_global.py",
            "scripts/engines/context_scanner.py", 
            "templates/decisao.md"
        ]
        
        for file in essential_files:
            if not (self.source_dir / file).exists():
                print(f"❌ Arquivo essencial não encontrado: {file}")
                return False
        print(f"✅ Arquivos essenciais verificados")
        
        return True

    def backup_existing(self) -> bool:
        """Backup de instalação existente"""
        if not self.install_path.exists():
            return True
            
        if self.dry_run:
            print(f"🔄 Faria backup de: {self.install_path}")
            return True
            
        print(f"🔄 Fazendo backup de instalação existente...")
        backup_name = f"context-navigator-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        backup_path = self.install_path.parent / backup_name
        
        try:
            shutil.move(str(self.install_path), str(backup_path))
            print(f"✅ Backup criado: {backup_path}")
            return True
        except Exception as e:
            print(f"❌ Erro no backup: {e}")
            return False

    def copy_files(self) -> bool:
        """Copia arquivos para instalação"""
        if self.dry_run:
            print(f"📋 Copiaria arquivos de {self.source_dir} para {self.install_path}")
            return True
            
        print(f"📋 Copiando arquivos...")
        
        try:
            # Criar diretório de instalação
            self.install_path.mkdir(parents=True, exist_ok=True)
            
            # Copiar tudo da source
            for item in self.source_dir.iterdir():
                if item.name.startswith('.'):
                    continue
                    
                dest = self.install_path / item.name
                if item.is_dir():
                    shutil.copytree(item, dest, dirs_exist_ok=True)
                else:
                    shutil.copy2(item, dest)
                print(f"✅ Copiado: {item.name}")
                
            return True
        except Exception as e:
            print(f"❌ Erro ao copiar arquivos: {e}")
            return False

    def create_launcher(self) -> bool:
        """Cria launcher global 'cn'"""
        if self.dry_run:
            print(f"🚀 Criaria launcher: {self.bin_path / 'cn'}")
            return True
            
        print(f"🚀 Criando launcher global...")
        
        launcher_content = f'''#!/bin/bash
# Context Navigator Global Launcher
# Auto-generated by installer

export CN_INSTALL_PATH="{self.install_path}"
export PYTHONPATH="$CN_INSTALL_PATH:$PYTHONPATH"
exec python3 "$CN_INSTALL_PATH/core/cn_global.py" "$@"
'''
        
        try:
            self.bin_path.mkdir(parents=True, exist_ok=True)
            launcher_path = self.bin_path / "cn"
            
            launcher_path.write_text(launcher_content)
            launcher_path.chmod(0o755)
            
            print(f"✅ Launcher criado: {launcher_path}")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar launcher: {e}")
            return False

    def create_registry(self) -> bool:
        """Cria registry global"""
        if self.dry_run:
            print(f"📋 Criaria registry: {self.install_path / 'workspaces-registry.yml'}")
            return True
            
        print(f"📋 Criando registry global...")
        
        registry_content = {
            'version': '2.0',
            'created_at': datetime.now().isoformat(),
            'workspaces': {}
        }
        
        try:
            registry_path = self.install_path / "workspaces-registry.yml"
            with open(registry_path, 'w') as f:
                yaml.dump(registry_content, f, default_flow_style=False)
            
            print(f"✅ Registry criado: {registry_path}")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar registry: {e}")
            return False

    def install(self) -> bool:
        """Processo completo de instalação"""
        print(f"\n{'='*60}")
        print(f"CONTEXT NAVIGATOR - {'TESTE' if self.dry_run else 'INSTALAÇÃO'}")
        print(f"{'='*60}")
        print(f"📁 Destino: {self.install_path}")
        print(f"🎯 Launcher: {self.bin_path}")
        print(f"📦 Fonte: {self.source_dir}")
        print(f"🏷️  Versão: {self.version}")
        print()
        
        steps = [
            ("Verificar pré-requisitos", self.check_prerequisites),
            ("Backup instalação existente", self.backup_existing),
            ("Copiar arquivos", self.copy_files),
            ("Criar launcher global", self.create_launcher),
            ("Criar registry", self.create_registry)
        ]
        
        for step_name, step_func in steps:
            print(f"🔄 {step_name}...")
            if not step_func():
                print(f"❌ Falha: {step_name}")
                return False
        
        self.show_completion_message()
        return True

    def show_completion_message(self):
        """Mostra mensagem de conclusão"""
        print(f"\n{'='*60}")
        if self.dry_run:
            print(f"🧪 TESTE CONCLUÍDO - INSTALAÇÃO SERIA POSSÍVEL")
        else:
            print(f"🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
        print(f"{'='*60}")
        
        print(f"📁 Local: {self.install_path}")
        print(f"🎯 Launcher: {self.bin_path / 'cn'}")
        
        if not self.dry_run:
            print(f"\n💡 PRÓXIMOS PASSOS:")
            print(f"1. Adicione ao PATH (se necessário):")
            print(f"   echo 'export PATH=\"{self.bin_path}:$PATH\"' >> ~/.bashrc")
            print(f"   source ~/.bashrc")
            print(f"")
            print(f"2. Teste a instalação:")
            print(f"   cn help")
            print(f"   cn init  # Em um projeto")
            print(f"   cn scan  # Para testar")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Context Navigator - Instalador Unificado')
    parser.add_argument('--path', help='Local customizado de instalação')
    parser.add_argument('--global', action='store_true', help='Forçar instalação global')
    parser.add_argument('--dry-run', action='store_true', help='Apenas testar (não instalar)')
    
    args = parser.parse_args()
    
    try:
        installer = UnifiedInstaller(
            install_path=args.path,
            global_install=getattr(args, 'global', False),
            dry_run=args.dry_run
        )
        
        if installer.install():
            return 0
        else:
            print(f"\n❌ Falha na {'simulação' if args.dry_run else 'instalação'}")
            return 1
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 