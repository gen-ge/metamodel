#!/usr/bin/env python3
"""
🏗️ Context Navigator - Build Script
Gera pacotes instaláveis do Context Navigator

🚀 COMO USAR:

# 1. Build básico (usa versão padrão)
python3 build.py

# 2. Build com versão específica  
python3 build.py --version 2.0.0

# 3. Build com diretório fonte específico
python3 build.py --source /caminho/para/metamodelo

# 4. Apenas limpar diretórios (sem build)
python3 build.py --clean-only

# 5. Build completo com versão customizada
python3 build.py --version 2.0.0-RELEASE --source .

📦 ARQUIVOS GERADOS (em dist/):
- context-navigator-{version}.tar.gz       # Pacote principal
- context-navigator-latest.tar.gz          # Alias para latest
- context-navigator-{version}.zip          # Pacote em formato zip
- install-context-navigator-{version}.txt  # Instalador standalone Python
- install-context-navigator-latest.txt     # Instalador standalone latest
- install-context-navigator-latest.sh      # Script shell de instalação

🎯 FLUXO TÍPICO:
1. python3 build.py --version 2.0.0
2. cd dist/
3. # Enviar arquivos para GitHub releases
4. # Testar: tar -xzf context-navigator-2.0.0.tar.gz && cd context-navigator-2.0.0 && python3 install.py

⚙️ OPÇÕES:
--version, -v    : Versão do build (padrão: 2.0.0)
--source, -s     : Diretório fonte (padrão: .)
--clean-only     : Apenas limpar diretórios de build
--help, -h       : Mostrar ajuda
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
        self.src_dir = self.source_dir / "src" / "context_navigator"
        self.version = version or "2.0.0"
        self.build_dir = self.source_dir / "build"
        self.dist_dir = self.source_dir / "dist"
        
        print(f"🏗️  Context Navigator Builder")
        print(f"📁 Fonte: {self.source_dir}")
        print(f"📦 Pacote: {self.src_dir}")
        print(f"🏷️  Versão: {self.version}")
        print(f"📦 Build: {self.build_dir}")
        print(f"📤 Distribuição: {self.dist_dir}")
        
        # Verificar se estrutura src/ existe
        if not self.src_dir.exists():
            print(f"❌ Estrutura src/ não encontrada em: {self.src_dir}")
            raise FileNotFoundError(f"Estrutura src/ não encontrada: {self.src_dir}")
        
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
        
        # CORREÇÃO: Criar estrutura mínima sem duplicação
        # Pacote deve conter apenas:
        # - install.py (raiz)
        # - source/ (pasta com arquivos a serem instalados)
        # - docs/ (documentação do projeto)
        # - README.md, etc. (arquivos informativos)
        
        try:
            # 1. Copiar install.py para a raiz do pacote
            install_source = self.src_dir / "installer" / "install.py"
            install_dest = self.package_dir / "install.py"
            
            if install_source.exists():
                shutil.copy2(install_source, install_dest)
                print(f"✅ Copiado: installer/install.py -> install.py")
            else:
                print(f"⚠️  install.py não encontrado em: {install_source}")
                return False
            
            # 2. Criar pasta source/ com arquivos a serem instalados
            source_dest = self.package_dir / "source"
            source_dest.mkdir(exist_ok=True)
            
            # Arquivos e diretórios para incluir em source/ (de src/context_navigator/)
            src_files_to_include = [
                "core/",              # ✅ NOVO - Módulo global (workspace_manager, daemon_manager, etc.)
                "scripts/",           # ✅ Scripts globais (todos os .py)
                "templates/",         # ✅ Templates para usuários
                "installer/",         # ✅ Sistema de instalação global
                "context.rule",       # ✅ Regras de contexto
                ".contextrc",         # ✅ Configuração (se existir)
                "__init__.py",        # ✅ Módulo principal
                "cn_cli_legacy.py"    # ✅ CLI legado (nome correto)
            ]
            
            for item in src_files_to_include:
                source_path = self.src_dir / item
                dest_path = source_dest / item
                
                if not source_path.exists():
                    print(f"⚠️  Arquivo não encontrado: src/context_navigator/{item}")
                    continue
                    
                if source_path.is_dir():
                    shutil.copytree(source_path, dest_path)
                    print(f"✅ Copiado: src/context_navigator/{item} -> source/{item}")
                else:
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source_path, dest_path)
                    print(f"✅ Copiado: src/context_navigator/{item} -> source/{item}")
            
            # 3. Copiar arquivos informativos do root do projeto para a raiz do pacote
            root_files_to_include = [
                "docs/",
                "examples/", 
                "README.md",               
                "LICENSE"
            ]
            
            for item in root_files_to_include:
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

### 📁 Instalação Local (Padrão)
```bash
# 1. Extrair o pacote
tar -xzf context-navigator-{self.version}.tar.gz
cd context-navigator-{self.version}

# 2. Instalar localmente
python3 install.py

# 3. Testar
python3 -m context_navigator.cn_cli demo
```

### 🌐 Instalação Global (Recomendada)
```bash
# 1. Extrair o pacote
tar -xzf context-navigator-{self.version}.tar.gz
cd context-navigator-{self.version}

# 2. Instalar globalmente
python3 install.py --global

# 3. Configurar PATH (adicione ao ~/.bashrc)
export PATH="$HOME/.local/bin:$PATH"

# 4. Testar de qualquer diretório
cn demo
```

## 📋 Comandos Principais

### 🌐 Instalação Global
```bash
cn scan                      # Escanear documentos
cn demo                      # Demonstração completa
cn validate                  # Validar métricas
cn new decision nome         # Criar nova decisão
cn help                      # Ver todos os comandos
```

### 📁 Instalação Local
```bash
python3 -m context_navigator.cn_cli scan
python3 -m context_navigator.cn_cli demo
python3 -m context_navigator.cn_cli validate
python3 -m context_navigator.cn_cli new decision nome
python3 -m context_navigator.cn_cli help
```

## 🎯 Opções de Instalação

### 🌐 Global (Recomendada)
- **Comando**: `python3 install.py --global`
- **Localização**: `~/.local/share/context-navigator/`
- **Launcher**: `~/.local/bin/cn`
- **Uso**: `cn comando` de qualquer diretório

### 📁 Local
- **Comando**: `python3 install.py`
- **Localização**: `.context-navigator/`
- **Uso**: `python3 -m context_navigator.cn_cli comando`

## 🔍 Busca Inteligente

O Context Navigator agora busca automaticamente por `.context-navigator/`:
- No diretório atual
- Em diretórios pais
- Permite usar de subdiretórios do projeto

## 🎯 Sistema Instalado

- **`.context-navigator/`** - Sistema completo isolado
- **`.context-map/`** - Dados gerados pelo sistema
- **`cn`** - Launcher global (instalação global)

## 📚 Documentação

- `README.md` - Documentação completa
- `QUICK_START.md` - Guia de 15 minutos
- `INSTALL.md` - Guia de instalação
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

set -e  # Sair em caso de erro

echo "🚀 Context Navigator - Instalador v{self.version}"
echo "📥 Baixando e instalando..."

# Verificar dependências
check_dependencies() {{
    echo "🔍 Verificando dependências..."
    
    # Verificar Python 3
    if ! command -v python3 &> /dev/null; then
        echo "❌ Python 3 não encontrado. Instale Python 3.7+ para continuar."
        exit 1
    fi
    
    # Verificar versão do Python
    python_version=$(python3 -c "import sys; print(f'{{sys.version_info.major}}.{{sys.version_info.minor}}')")
    if ! python3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 7) else 1)"; then
        echo "❌ Python 3.7+ requerido. Versão atual: $python_version"
        exit 1
    fi
    
    # Verificar ferramenta de download
    if command -v wget &> /dev/null; then
        DOWNLOAD_CMD="wget -q"
    elif command -v curl &> /dev/null; then
        DOWNLOAD_CMD="curl -sL -o"
    else
        echo "❌ Nem wget nem curl encontrados. Instale uma dessas ferramentas."
        exit 1
    fi
    
    # Verificar tar
    if ! command -v tar &> /dev/null; then
        echo "❌ tar não encontrado. Instale tar para continuar."
        exit 1
    fi
    
    echo "✅ Dependências verificadas"
}}

# Função de limpeza
cleanup() {{
    if [ -n "$temp_dir" ] && [ -d "$temp_dir" ]; then
        echo "🧹 Limpando diretório temporário..."
        rm -rf "$temp_dir"
    fi
}}

# Configurar trap para limpeza em caso de interrupção
trap cleanup EXIT INT TERM

# Verificar dependências
check_dependencies

# Verificar permissões no diretório atual
if [ ! -w "." ]; then
    echo "❌ Sem permissão de escrita no diretório atual"
    exit 1
fi

# Salvar workspace original
original_dir=$(pwd)

# Criar diretório temporário
temp_dir=$(mktemp -d)
echo "📁 Diretório temporário: $temp_dir"
cd "$temp_dir"

# URL do pacote
PACKAGE_URL="https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz"
PACKAGE_FILE="context-navigator-latest.tar.gz"

# Baixar pacote
echo "📥 Baixando pacote..."
if command -v wget &> /dev/null; then
    wget -q "$PACKAGE_URL" -O "$PACKAGE_FILE"
else
    curl -sL "$PACKAGE_URL" -o "$PACKAGE_FILE"
fi

if [ $? -ne 0 ]; then
    echo "❌ Erro ao baixar pacote. Verifique sua conexão com a internet."
    exit 1
fi

# Verificar se o arquivo foi baixado
if [ ! -f "$PACKAGE_FILE" ]; then
    echo "❌ Arquivo não foi baixado corretamente"
    exit 1
fi

# Extrair pacote
echo "📦 Extraindo pacote..."
tar -xzf "$PACKAGE_FILE"

if [ $? -ne 0 ]; then
    echo "❌ Erro ao extrair pacote"
    exit 1
fi

# Encontrar diretório extraído
extracted_dir=$(find . -name "context-navigator-*" -type d | head -1)

if [ -z "$extracted_dir" ]; then
    echo "❌ Diretório extraído não encontrado"
    exit 1
fi

# Verificar se install.py existe
if [ ! -f "$extracted_dir/install.py" ]; then
    echo "❌ Script de instalação não encontrado no pacote"
    exit 1
fi

# Executar instalação global
echo "⚙️  Instalando..."
cd "$extracted_dir"
python3 install.py --global

if [ $? -eq 0 ]; then
    echo "✅ Instalação global concluída!"
    echo "💡 Execute 'cn help' para começar (sem ./)"
    
    # Verificar se o launcher global foi criado
    if [ -f "$HOME/.local/bin/cn" ]; then
        echo "🎯 Launcher global criado em: $HOME/.local/bin/cn"
        echo "💡 Adicione $HOME/.local/bin ao seu PATH se necessário"
        echo "💡 Para usar: cn help"
    else
        echo "⚠️  Launcher global não encontrado. Verifique a instalação."
        echo "💡 Verifique se ~/.local/bin/ existe e tem permissões corretas"
    fi
else
    echo "❌ Falha na instalação"
    exit 1
fi

# A limpeza será feita automaticamente pelo trap
echo "🧹 Limpando arquivos temporários..."
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
            # Verificar arquivos essenciais na raiz do pacote
            root_files = [
                "install.py",
                "README.md"
            ]
            
            for file in root_files:
                file_path = self.package_dir / file
                if not file_path.exists():
                    print(f"❌ Arquivo essencial não encontrado: {file}")
                    return False
                print(f"✅ Validado: {file}")
            
            # Verificar pasta source/ existe
            source_dir = self.package_dir / "source"
            if not source_dir.exists():
                print(f"❌ Pasta source/ não encontrada")
                return False
            print(f"✅ Validado: source/")
            
            # Verificar arquivos essenciais em source/
            source_files = [
                "scripts/core/context_scanner.py",
                "templates/decisao.md",
                "context.rule",
                ".contextrc",
                "cn_cli_legacy.py"
            ]
            
            for file in source_files:
                file_path = source_dir / file
                if not file_path.exists():
                    print(f"❌ Arquivo essencial não encontrado: source/{file}")
                    return False
                print(f"✅ Validado: source/{file}")
                
            # Verificar estrutura de diretórios em source/
            source_dirs = ["scripts", "templates"]
            
            for dir_name in source_dirs:
                dir_path = source_dir / dir_name
                if not dir_path.is_dir():
                    print(f"❌ Diretório essencial não encontrado: source/{dir_name}")
                    return False
                print(f"✅ Validado: source/{dir_name}/")
                
            # Verificar estrutura de diretórios na raiz
            root_dirs = ["docs", "examples"]
            
            for dir_name in root_dirs:
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