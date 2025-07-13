#!/usr/bin/env python3
"""
🏗️ Context Navigator - Build Script
Gera pacotes instaláveis do Context Navigator
"""

import os
import sys
import shutil
import tarfile
import zipfile
import json
from pathlib import Path
from datetime import datetime
from typing import Optional
import argparse

class ContextNavigatorBuilder:
    def __init__(self, source_dir: str = ".", version: Optional[str] = None):
        """
        Inicializa o builder
        
        Args:
            source_dir: Diretório fonte do Context Navigator
            version: Versão do build (se não especificada, usa timestamp)
        """
        self.source_dir = Path(source_dir).resolve()
        self.version = version or datetime.now().strftime('%Y%m%d-%H%M%S')
        self.build_dir = self.source_dir / "build"
        self.dist_dir = self.source_dir / "dist"
        
        print(f"🏗️  Context Navigator Builder")
        print(f"📁 Fonte: {self.source_dir}")
        print(f"🏷️  Versão: {self.version}")
        print(f"📦 Build: {self.build_dir}")
        print(f"📤 Distribuição: {self.dist_dir}")
        
    def clean_build_dirs(self) -> bool:
        """Remove diretórios de build e dist anteriores"""
        print(f"\n🧹 Limpando diretórios de build...")
        
        try:
            if self.build_dir.exists():
                shutil.rmtree(self.build_dir)
                print(f"✅ Removido: {self.build_dir}")
                
            if self.dist_dir.exists():
                shutil.rmtree(self.dist_dir)
                print(f"✅ Removido: {self.dist_dir}")
                
            return True
        except Exception as e:
            print(f"❌ Erro ao limpar diretórios: {e}")
            return False
            
    def create_build_structure(self) -> bool:
        """Cria estrutura de diretórios para build"""
        print(f"\n📁 Criando estrutura de build...")
        
        try:
            self.build_dir.mkdir(exist_ok=True)
            self.dist_dir.mkdir(exist_ok=True)
            
            # Criar diretório do pacote
            self.package_dir = self.build_dir / f"context-navigator-{self.version}"
            self.package_dir.mkdir(exist_ok=True)
            
            print(f"✅ Criado: {self.package_dir}")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar estrutura: {e}")
            return False
            
    def copy_source_files(self) -> bool:
        """Copia arquivos fonte para o build"""
        print(f"\n📋 Copiando arquivos fonte...")
        
        # Arquivos e diretórios para incluir no pacote
        files_to_include = [
            "scripts/",
            "templates/",
            "docs/",
            "examples/",
            "context.rule",
            ".contextrc",
            "README.md",
            "QUICK_START.md", 
            "GUIA_IMPLEMENTACAO.md",
            "install.py"
        ]
        
        try:
            for item in files_to_include:
                source_path = self.source_dir / item
                dest_path = self.package_dir / item
                
                if not source_path.exists():
                    print(f"⚠️  Arquivo não encontrado: {item}")
                    continue
                    
                if source_path.is_dir():
                    shutil.copytree(source_path, dest_path)
                    print(f"✅ Copiado: {item}/ -> {dest_path.name}/")
                else:
                    shutil.copy2(source_path, dest_path)
                    print(f"✅ Copiado: {item} -> {dest_path.name}")
                    
            return True
        except Exception as e:
            print(f"❌ Erro ao copiar arquivos: {e}")
            return False
            
    def create_metadata_files(self) -> bool:
        """Cria arquivos de metadados do pacote"""
        print(f"\n📝 Criando metadados do pacote...")
        
        try:
            # Criar arquivo de versão
            version_info = {
                "version": self.version,
                "build_date": datetime.now().isoformat(),
                "python_min_version": "3.7",
                "dependencies": [],
                "description": "Context Navigator - Sistema de Documentação Context-Aware",
                "author": "Context Navigator Team",
                "license": "MIT"
            }
            
            version_file = self.package_dir / "VERSION"
            with open(version_file, 'w', encoding='utf-8') as f:
                json.dump(version_info, f, indent=2, ensure_ascii=False)
            print(f"✅ Criado: VERSION")
            
            # Criar arquivo de instalação
            install_info = {
                "install_command": "python3 install.py",
                "launcher_command": "./cn",
                "test_command": "./cn demo",
                "requirements": [
                    "Python 3.7+",
                    "Nenhuma dependência externa"
                ],
                "structure": {
                    ".context-navigator/": "Sistema instalado",
                    ".context-map/": "Dados gerados", 
                    "cn": "Launcher principal"
                }
            }
            
            install_file = self.package_dir / "INSTALL.json"
            with open(install_file, 'w', encoding='utf-8') as f:
                json.dump(install_info, f, indent=2, ensure_ascii=False)
            print(f"✅ Criado: INSTALL.json")
            
            # Criar README do pacote
            readme_content = f"""# 🧭 Context Navigator v{self.version}

## 🚀 Instalação Rápida

```bash
# 1. Extrair o pacote
tar -xzf context-navigator-{self.version}.tar.gz
cd context-navigator-{self.version}

# 2. Instalar
python3 install.py

# 3. Testar
./cn demo
```

## 📋 Comandos Principais

```bash
./cn scan                    # Escanear documentos
./cn demo                    # Demonstração completa
./cn validate                # Validar métricas
./cn new decision nome       # Criar nova decisão
./cn help                    # Ver todos os comandos
```

## 🎯 Sistema Instalado

- **`.context-navigator/`** - Sistema completo isolado
- **`.context-map/`** - Dados gerados pelo sistema
- **`cn`** - Launcher principal

## 📚 Documentação

- `README.md` - Documentação completa
- `QUICK_START.md` - Guia de 15 minutos
- `GUIA_IMPLEMENTACAO.md` - Guia de implementação
- `docs/` - Documentação técnica detalhada

## 🔧 Requisitos

- Python 3.7+
- Nenhuma dependência externa

## 🎯 Transforme sua documentação em navegação inteligente!
"""
            
            package_readme = self.package_dir / "README_PACKAGE.md"
            with open(package_readme, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            print(f"✅ Criado: README_PACKAGE.md")
            
            return True
        except Exception as e:
            print(f"❌ Erro ao criar metadados: {e}")
            return False
            
    def create_tarball(self) -> bool:
        """Cria arquivo .tar.gz do pacote"""
        print(f"\n📦 Criando arquivo .tar.gz...")
        
        try:
            # Arquivo com versão específica
            tarball_name = f"context-navigator-{self.version}.tar.gz"
            tarball_path = self.dist_dir / tarball_name
            
            with tarfile.open(tarball_path, 'w:gz') as tar:
                tar.add(self.package_dir, arcname=f"context-navigator-{self.version}")
                
            print(f"✅ Criado: {tarball_path}")
            print(f"📊 Tamanho: {tarball_path.stat().st_size / 1024:.1f} KB")
            
            # Criar também versão "latest" para facilitar download
            latest_name = "context-navigator-latest.tar.gz"
            latest_path = self.dist_dir / latest_name
            
            with tarfile.open(latest_path, 'w:gz') as tar:
                tar.add(self.package_dir, arcname=f"context-navigator-{self.version}")
                
            print(f"✅ Criado: {latest_path} (alias para latest)")
            print(f"📊 Tamanho: {latest_path.stat().st_size / 1024:.1f} KB")
            
            return True
        except Exception as e:
            print(f"❌ Erro ao criar tarball: {e}")
            return False
            
    def create_zipfile(self) -> bool:
        """Cria arquivo .zip do pacote"""
        print(f"\n📦 Criando arquivo .zip...")
        
        try:
            zip_name = f"context-navigator-{self.version}.zip"
            zip_path = self.dist_dir / zip_name
            
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(self.package_dir):
                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(self.package_dir.parent)
                        zf.write(file_path, arcname)
                        
            print(f"✅ Criado: {zip_path}")
            print(f"📊 Tamanho: {zip_path.stat().st_size / 1024:.1f} KB")
            
            return True
        except Exception as e:
            print(f"❌ Erro ao criar zip: {e}")
            return False
            
    def create_installer_script(self) -> bool:
        """Cria script de instalação standalone"""
        print(f"\n🔧 Criando instalador standalone...")
        
        installer_script = f"""#!/usr/bin/env python3
'''
🚀 Context Navigator - Instalador Standalone v{self.version}
Download e instalação automática do Context Navigator
'''

import os
import sys
import urllib.request
import tarfile
import tempfile
import shutil
from pathlib import Path

def download_and_install():
    print("🚀 Context Navigator - Instalador Standalone v{self.version}")
    print("📥 Baixando e instalando...")
    
         # URL do pacote (sempre a versão mais recente)
     package_url = "https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz"
    
    try:
        # Criar diretório temporário
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Baixar pacote
            print("📥 Baixando pacote...")
            package_path = temp_path / "context-navigator.tar.gz"
            urllib.request.urlretrieve(package_url, package_path)
            
            # Extrair pacote
            print("📦 Extraindo pacote...")
            with tarfile.open(package_path, 'r:gz') as tar:
                tar.extractall(temp_path)
                
                         # Executar instalação
             print("⚙️  Instalando...")
             # Procurar diretório extraído (pode ter qualquer versão)
             import glob
             extracted_dirs = glob.glob(str(temp_path / "context-navigator-*"))
             if not extracted_dirs:
                 print("❌ Diretório extraído não encontrado")
                 return False
             install_dir = Path(extracted_dirs[0])
             install_script = install_dir / "install.py"
            
            if install_script.exists():
                os.system(f"cd {{install_dir}} && python3 install.py")
                print("✅ Instalação concluída!")
            else:
                print("❌ Script de instalação não encontrado")
                return False
                
    except Exception as e:
        print(f"❌ Erro na instalação: {{e}}")
        return False
        
    return True

if __name__ == "__main__":
    if download_and_install():
        print("🎉 Context Navigator instalado com sucesso!")
        print("💡 Execute './cn help' para começar")
    else:
        print("❌ Falha na instalação")
        sys.exit(1)
"""
        
        try:
            # Criar instalador como .txt (GitHub não bloqueia)
            standalone_path = self.dist_dir / f"install-context-navigator-{self.version}.txt"
            with open(standalone_path, 'w', encoding='utf-8') as f:
                f.write(installer_script)
                
            print(f"✅ Criado: {standalone_path}")
            
            # Criar também versão "latest" para facilitar download
            latest_installer_path = self.dist_dir / "install-context-navigator-latest.txt"
            with open(latest_installer_path, 'w', encoding='utf-8') as f:
                f.write(installer_script)
                
            print(f"✅ Criado: {latest_installer_path} (alias para latest)")
            
            # Criar script shell como alternativa
            shell_script = f'''#!/bin/bash
# Context Navigator - Instalador Shell v{self.version}
# Download e instalação automática do Context Navigator

echo "🚀 Context Navigator - Instalador v{self.version}"
echo "📥 Baixando e instalando..."

# Criar diretório temporário
temp_dir=$(mktemp -d)
cd "$temp_dir"

# Baixar pacote
echo "📥 Baixando pacote..."
wget -q https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz

if [ $? -ne 0 ]; then
    echo "❌ Erro ao baixar pacote"
    exit 1
fi

# Extrair pacote
echo "📦 Extraindo pacote..."
tar -xzf context-navigator-latest.tar.gz

# Encontrar diretório extraído
extracted_dir=$(find . -name "context-navigator-*" -type d | head -1)

if [ -z "$extracted_dir" ]; then
    echo "❌ Diretório extraído não encontrado"
    exit 1
fi

# Executar instalação
echo "⚙️  Instalando..."
cd "$extracted_dir"
python3 install.py

if [ $? -eq 0 ]; then
    echo "✅ Instalação concluída!"
    echo "💡 Execute './cn help' para começar"
else
    echo "❌ Falha na instalação"
    exit 1
fi

# Limpar diretório temporário
cd /
rm -rf "$temp_dir"
'''
            
            # Criar script shell
            shell_path = self.dist_dir / "install-context-navigator-latest.sh"
            with open(shell_path, 'w', encoding='utf-8') as f:
                f.write(shell_script)
                
            # Tornar executável
            os.chmod(shell_path, 0o755)
            
            print(f"✅ Criado: {shell_path} (script shell)")
            
            return True
        except Exception as e:
            print(f"❌ Erro ao criar instalador: {e}")
            return False
            
    def validate_build(self) -> bool:
        """Valida se o build está correto"""
        print(f"\n🔍 Validando build...")
        
        try:
            # Verificar arquivos essenciais
            essential_files = [
                "install.py",
                "scripts/context_scanner.py",
                "templates/decisao.md",
                "context.rule",
                ".contextrc",
                "README.md"
            ]
            
            for file in essential_files:
                file_path = self.package_dir / file
                if not file_path.exists():
                    print(f"❌ Arquivo essencial não encontrado: {file}")
                    return False
                print(f"✅ Validado: {file}")
                
            # Verificar estrutura de diretórios
            essential_dirs = ["scripts", "templates", "docs", "examples"]
            
            for dir_name in essential_dirs:
                dir_path = self.package_dir / dir_name
                if not dir_path.is_dir():
                    print(f"❌ Diretório essencial não encontrado: {dir_name}")
                    return False
                print(f"✅ Validado: {dir_name}/")
                
            print(f"✅ Build validado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro na validação: {e}")
            return False
            
    def show_build_summary(self) -> None:
        """Mostra resumo do build"""
        print(f"\n" + "="*60)
        print(f"🎉 BUILD CONCLUÍDO COM SUCESSO!")
        print(f"="*60)
        print(f"")
        print(f"📦 Versão: {self.version}")
        print(f"📁 Build: {self.package_dir}")
        print(f"📤 Distribuição: {self.dist_dir}")
        print(f"")
        print(f"🎯 ARQUIVOS GERADOS:")
        print(f"")
        
        # Listar arquivos gerados
        if self.dist_dir.exists():
            for file in self.dist_dir.iterdir():
                if file.is_file():
                    size_kb = file.stat().st_size / 1024
                    print(f"  📄 {file.name} ({size_kb:.1f} KB)")
                    
        print(f"")
        print(f"🚀 PARA DISTRIBUIR:")
        print(f"")
        print(f"1. 📤 Envie arquivos para releases do GitHub")
        print(f"2. 📝 Atualize URLs no instalador standalone")
        print(f"3. 🧪 Teste instalação em workspace limpo")
        print(f"")
        print(f"🎯 PARA TESTAR LOCALMENTE:")
        print(f"")
        print(f"  cd {self.dist_dir}")
        print(f"  tar -xzf context-navigator-{self.version}.tar.gz")
        print(f"  cd context-navigator-{self.version}")
        print(f"  python3 install.py")
        print(f"")
        
    def build(self) -> bool:
        """Executa build completo"""
        print(f"\n🏗️  Iniciando build do Context Navigator...")
        
        steps = [
            ("Limpar diretórios", self.clean_build_dirs),
            ("Criar estrutura", self.create_build_structure),
            ("Copiar arquivos", self.copy_source_files),
            ("Criar metadados", self.create_metadata_files),
            ("Validar build", self.validate_build),
            ("Criar tarball", self.create_tarball),
            ("Criar zip", self.create_zipfile),
            ("Criar instalador", self.create_installer_script)
        ]
        
        for step_name, step_func in steps:
            print(f"\n📋 {step_name}...")
            if not step_func():
                print(f"❌ Falha na etapa: {step_name}")
                return False
                
        self.show_build_summary()
        return True

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(description='Context Navigator Build Script')
    parser.add_argument('--version', '-v', 
                       help='Versão do build (padrão: timestamp)')
    parser.add_argument('--source', '-s', default='.',
                       help='Diretório fonte (padrão: atual)')
    parser.add_argument('--clean-only', action='store_true',
                       help='Apenas limpar diretórios de build')
    
    args = parser.parse_args()
    
    if args.clean_only:
        builder = ContextNavigatorBuilder(args.source)
        builder.clean_build_dirs()
        return 0
    
    builder = ContextNavigatorBuilder(args.source, args.version)
    
    if builder.build():
        print("\n✅ Build concluído com sucesso!")
        return 0
    else:
        print("\n❌ Falha no build")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 