#!/usr/bin/env python3
"""
🚀 Context Navigator - Instalador
Instala o Context Navigator em qualquer workspace de forma isolada
"""

import os
import sys
import shutil
import subprocess
import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

class ContextNavigatorInstaller:
    def __init__(self, target_path: str = ".", global_install: bool = False):
        """
        Inicializa o instalador
        
        Args:
            target_path: Caminho do workspace onde instalar (padrão: diretório atual)
            global_install: Se True, instala globalmente no sistema
        """
        self.global_install = global_install
        self.target_path = Path(target_path).resolve()
        
        if global_install:
            # Instalação global
            self.install_dir = Path.home() / ".local" / "share" / "context-navigator"
            self.bin_dir = Path.home() / ".local" / "bin"
        else:
            # Instalação local
            self.install_dir = self.target_path / ".context-navigator"
            self.bin_dir = self.target_path
            
        # Detectar se estamos em um pacote extraído ou em desenvolvimento
        installer_path = Path(__file__).parent.resolve()
        
        # Se install.py está na raiz de um pacote extraído, source_dir é o diretório do pacote
        if (installer_path.parent / "source").exists():
            self.source_dir = installer_path.parent
        else:
            # Estamos em desenvolvimento, usar estrutura src/
            self.source_dir = installer_path
        
        # Versão do Context Navigator
        self.version = "1.0.0"
        
        print(f"🎯 Context Navigator Installer v{self.version}")
        if global_install:
            print(f"🌐 Instalação Global")
            print(f"📦 Instalando em: {self.install_dir}")
            print(f"🔧 Launcher em: {self.bin_dir}")
        else:
            print(f"📁 Instalação Local - Workspace: {self.target_path}")
            print(f"📦 Instalando em: {self.install_dir}")
        
    def check_prerequisites(self) -> bool:
        """Verifica pré-requisitos do sistema"""
        print("\n🔍 Verificando pré-requisitos...")
        
        # Verificar Python
        if sys.version_info < (3, 7):
            print("❌ Python 3.7+ necessário")
            return False
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
        
        # Verificar se é um workspace válido
        if not self.target_path.exists():
            print(f"❌ Workspace não encontrado: {self.target_path}")
            return False
        print(f"✅ Workspace válido: {self.target_path}")
        
        # Verificar se source dir existe
        if not self.source_dir.exists():
            print(f"❌ Diretório fonte não encontrado: {self.source_dir}")
            return False
        print(f"✅ Arquivos fonte encontrados: {self.source_dir}")
        
        return True
        
    def backup_existing_installation(self) -> bool:
        """Faz backup de instalação existente"""
        if self.install_dir.exists():
            print(f"\n🔄 Instalação existente encontrada...")
            backup_dir = self.target_path / f".context-navigator-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
            
            try:
                shutil.move(str(self.install_dir), str(backup_dir))
                print(f"✅ Backup criado: {backup_dir}")
                return True
            except Exception as e:
                print(f"❌ Erro ao criar backup: {e}")
                return False
                
        return True
        
    def create_installation_directory(self) -> bool:
        """Cria estrutura de diretórios da instalação"""
        print(f"\n📁 Criando estrutura de diretórios...")
        
        try:
            self.install_dir.mkdir(exist_ok=True)
            
            # Criar subdiretórios
            subdirs = ["scripts", "templates", "docs", "examples"]
            for subdir in subdirs:
                (self.install_dir / subdir).mkdir(exist_ok=True)
                print(f"✅ Criado: {subdir}/")
                
            return True
        except Exception as e:
            print(f"❌ Erro ao criar diretórios: {e}")
            return False
            
    def copy_files(self) -> bool:
        """Copia arquivos necessários para a instalação"""
        print(f"\n📋 Copiando arquivos...")
        
        # Detectar se estamos em pacote extraído ou desenvolvimento
        if (self.source_dir / "source").exists():
            # Pacote extraído - usar pasta source/
            source_dir = self.source_dir / "source"
        else:
            # Desenvolvimento - usar estrutura src/
            source_dir = self.source_dir.parent
            
        # Verificar se pasta source/ existe
        if not source_dir.exists():
            print(f"❌ Pasta source/ não encontrada em: {source_dir}")
            return False
            
        # Mapeamento de arquivos para copiar (de source/ para instalação)
        files_to_copy = {
            # Scripts
            "scripts/": "scripts/",
            # Templates
            "templates/": "templates/",
            # Core (não vai para instalação final)
            # "core/": "core/",
            # Configuração
            "context.rule": "context.rule",
            ".contextrc": ".contextrc",
            # CLI
            "cn_cli.py": "cn_cli.py"
        }
        
        # Arquivos de documentação (do root do pacote)
        docs_files = {
            "docs/": "docs/",
            "examples/": "examples/",
            "README.md": "README.md",
            "QUICK_START.md": "QUICK_START.md",
            "INSTALL.md": "INSTALL.md"
        }
        
        try:
            # Copiar arquivos da pasta source/
            for source, dest in files_to_copy.items():
                source_path = source_dir / source
                dest_path = self.install_dir / dest
                
                if source_path.exists():
                    if source_path.is_dir():
                        if dest_path.exists():
                            shutil.rmtree(dest_path)
                        shutil.copytree(source_path, dest_path)
                        print(f"✅ Copiado: source/{source} -> {dest}")
                    else:
                        dest_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(source_path, dest_path)
                        print(f"✅ Copiado: source/{source} -> {dest}")
                else:
                    print(f"⚠️  Arquivo não encontrado: source/{source}")
            
            # Copiar arquivos de documentação (do root do pacote)
            for source, dest in docs_files.items():
                source_path = self.source_dir / source
                dest_path = self.install_dir / dest
                
                if source_path.exists():
                    if source_path.is_dir():
                        if dest_path.exists():
                            shutil.rmtree(dest_path)
                        shutil.copytree(source_path, dest_path)
                        print(f"✅ Copiado: {source} -> {dest}")
                    else:
                        dest_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(source_path, dest_path)
                        print(f"✅ Copiado: {source} -> {dest}")
                else:
                    print(f"⚠️  Arquivo não encontrado: {source}")
                    
            return True
        except Exception as e:
            print(f"❌ Erro ao copiar arquivos: {e}")
            return False
            
    def create_version_file(self) -> bool:
        """Cria arquivo de versão"""
        try:
            version_info = {
                "version": self.version,
                "installed_at": datetime.now().isoformat(),
                "workspace": str(self.target_path),
                "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
            }
            
            version_file = self.install_dir / "VERSION"
            with open(version_file, 'w', encoding='utf-8') as f:
                json.dump(version_info, f, indent=2, ensure_ascii=False)
                
            print(f"✅ Arquivo de versão criado: VERSION")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar arquivo de versão: {e}")
            return False
            
    def create_context_map_directory(self) -> bool:
        """Cria diretório de contexto interno (não cria pasta externa)"""
        try:
            # O diretório .context-navigator/context-map/ é criado automaticamente pelo scanner
            # A pasta externa .context-map/ era lixo de versões anteriores
            print(f"✅ Diretório de contexto será criado automaticamente pelo scanner")
            return True
        except Exception as e:
            print(f"❌ Erro: {e}")
            return False
            
    def create_launcher_script(self) -> bool:
        """Cria launcher e documentação - Local ou Global"""
        print(f"\n📋 Criando launcher e documentação...")
        
        if self.global_install:
            return self.create_global_launcher()
        else:
            return self.create_local_launcher()
    
    def create_global_launcher(self) -> bool:
        """Cria launcher global no PATH"""
        try:
            # Criar diretório bin se não existir
            self.bin_dir.mkdir(parents=True, exist_ok=True)
            
            # Copiar launcher global
            source_launcher = self.source_dir / "source" / "scripts" / "cn_global_launcher.py"
            target_launcher = self.bin_dir / "cn"
            
            if source_launcher.exists():
                import shutil
                shutil.copy2(source_launcher, target_launcher)
                # Tornar executável
                import os
                os.chmod(target_launcher, 0o755)
                print(f"✅ Launcher global criado: {target_launcher}")
            else:
                print(f"⚠️  Launcher global não encontrado: {source_launcher}")
                return False
            
            # Criar documentação global
            docs_content = f'''# Context Navigator - Instalação Global

## 🌐 INSTALAÇÃO GLOBAL ATIVA

O Context Navigator foi instalado globalmente em seu sistema.

### 📋 USAR DE QUALQUER DIRETÓRIO:

```bash
cn scan                    # Escanear documentos
cn demo                    # Demonstração completa
cn help                    # Ver todos os comandos
```

### 🎯 BUSCA AUTOMÁTICA:

O launcher global busca automaticamente por:
1. .context-navigator/ no diretório atual
2. .context-navigator/ em diretórios pais
3. Instalação global do sistema

### 💡 CONFIGURAÇÃO DO PATH:

Para usar o comando 'cn' globalmente, adicione ao seu ~/.bashrc:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### 📁 ESTRUTURA INSTALADA:
- ~/.local/share/context-navigator/  - Sistema instalado
- ~/.local/bin/cn                    - Launcher global
- [workspace]/.context-navigator/    - Instalações locais

### 🔧 COMANDOS DISPONÍVEIS:
- cn scan            - Escanear documentos
- cn demo            - Demonstração completa
- cn validate        - Validar métricas
- cn new TYPE nome   - Criar novo documento
- cn help            - Ajuda completa
'''
            
            # Criar arquivo de documentação
            docs_file = self.install_dir / "HOW_TO_USE.md"
            with open(docs_file, 'w', encoding='utf-8') as f:
                f.write(docs_content)
            print(f"✅ Documentação global criada: HOW_TO_USE.md")
            
            return True
        except Exception as e:
            print(f"❌ Erro ao criar launcher global: {e}")
            return False
    
    def create_local_launcher(self) -> bool:
        """Cria launcher local - comportamento original"""
        # Criar arquivo de documentação local
        docs_content = f'''# Context Navigator - Como Usar (BUSCA INTELIGENTE)

## 🎯 BUSCA AUTOMÁTICA ATIVADA

O Context Navigator agora busca automaticamente por .context-navigator/ no diretório atual e em diretórios pais.

### 📋 COMANDOS BÁSICOS:

Para usar o Context Navigator, execute sempre:

```bash
python3 -m context_navigator.cn_cli COMANDO
```

### 🎯 COMANDOS DISPONÍVEIS:

📊 PRINCIPAIS:
- python3 -m context_navigator.cn_cli scan
- python3 -m context_navigator.cn_cli demo  
- python3 -m context_navigator.cn_cli help

📝 CRIAR DOCUMENTOS:
- python3 -m context_navigator.cn_cli new decision nome
- python3 -m context_navigator.cn_cli new process nome
- python3 -m context_navigator.cn_cli new reference nome

### 💡 ALIAS OPCIONAL (configure você mesmo):

Se quiser usar apenas "cn", adicione ao seu ~/.bashrc:

```bash
alias cn="python3 -m context_navigator.cn_cli"
```

### 🌐 USAR GLOBALMENTE:

Para usar de qualquer diretório, copie o launcher global para o PATH:

```bash
cp {self.install_dir}/scripts/cn_global_launcher.py ~/.local/bin/cn
chmod +x ~/.local/bin/cn
```

### 🎯 BUSCA INTELIGENTE:
- Busca .context-navigator/ no diretório atual
- Busca .context-navigator/ em diretórios pais
- Permite usar de subdiretórios do projeto

### 📁 ESTRUTURA CRIADA:
- .context-navigator/docs/     - Documentos organizados
- .context-navigator/scripts/  - Scripts do sistema
- .context-navigator/templates/ - Templates disponíveis
'''
        
        try:
            # Criar arquivo de documentação
            docs_file = self.install_dir / "HOW_TO_USE.md"
            with open(docs_file, 'w', encoding='utf-8') as f:
                f.write(docs_content)
            print(f"✅ Documentação criada: HOW_TO_USE.md")
            
            return True
        except Exception as e:
            print(f"❌ Erro ao criar documentação: {e}")
            return False
            
    def test_installation(self) -> bool:
        """Testa se a instalação está funcionando - COMPORTAMENTO BURRO"""
        print(f"\n🧪 Testando instalação...")
        
        try:
            # Verificar se arquivos essenciais foram copiados
            essential_files = [
                "scripts/context_scanner.py",
                "templates/decisao.md",
                ".contextrc",
                "context.rule",
                "HOW_TO_USE.md"
            ]
            
            for file_path in essential_files:
                full_path = self.install_dir / file_path
                if not full_path.exists():
                    print(f"❌ Arquivo essencial não encontrado: {file_path}")
                    return False
            
            print("✅ Arquivos essenciais verificados")
            
            # Verificar se a estrutura de diretórios foi criada
            essential_dirs = [
                "scripts",
                "templates", 
                "docs",
                "examples"
            ]
            
            for dir_path in essential_dirs:
                full_path = self.install_dir / dir_path
                if not full_path.exists() or not full_path.is_dir():
                    print(f"❌ Diretório essencial não encontrado: {dir_path}")
                    return False
            
            print("✅ Estrutura de diretórios verificada")
            return True
                
        except Exception as e:
            print(f"❌ Erro no teste: {e}")
            return False
            
    def show_completion_message(self) -> None:
        """Mostra mensagem de conclusão - COMPORTAMENTO BURRO"""
        print(f"\n" + "="*60)
        print(f"🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
        print(f"="*60)
        print(f"")
        print(f"📁 Workspace: {self.target_path}")
        print(f"📦 Instalação: {self.install_dir}")
        print(f"📋 Documentação: {self.install_dir}/HOW_TO_USE.md")
        print(f"")
        print(f"🤖 COMPORTAMENTO BURRO:")
        print(f"")
        print(f"1. 📋 Ver comandos disponíveis:")
        print(f"   python3 -m context_navigator.cn_cli help")
        print(f"")
        print(f"2. 🧪 Testar o sistema:")
        print(f"   python3 -m context_navigator.cn_cli demo")
        print(f"")
        print(f"3. 📝 Criar seu primeiro documento:")
        print(f"   python3 -m context_navigator.cn_cli new decision minha_decisao")
        print(f"")
        print(f"4. 🔍 Escanear documentos:")
        print(f"   python3 -m context_navigator.cn_cli scan")
        print(f"")
        print(f"5. 📊 Validar métricas:")
        print(f"   python3 -m context_navigator.cn_cli validate")
        print(f"")
        print(f"💡 CONFIGURAÇÃO OPCIONAL:")
        print(f"• Para usar apenas 'cn', adicione ao ~/.bashrc:")
        print(f"  alias cn='python3 -m context_navigator.cn_cli'")
        print(f"• Leia {self.install_dir}/HOW_TO_USE.md para detalhes")
        print(f"")
        print(f"🎯 Software que funciona sempre igual - BURRO INTELIGENTE!")
        print(f"")
        
    def install(self) -> bool:
        """Executa processo completo de instalação"""
        print(f"\n🚀 Iniciando instalação do Context Navigator...")
        
        steps = [
            ("Verificar pré-requisitos", self.check_prerequisites),
            ("Fazer backup", self.backup_existing_installation),
            ("Criar diretórios", self.create_installation_directory),
            ("Copiar arquivos", self.copy_files),
            ("Criar versão", self.create_version_file),
            ("Criar context-map", self.create_context_map_directory),
            ("Criar launcher", self.create_launcher_script),
            ("Testar instalação", self.test_installation)
        ]
        
        for step_name, step_func in steps:
            print(f"\n📋 {step_name}...")
            if not step_func():
                print(f"❌ Falha na etapa: {step_name}")
                return False
                
        self.show_completion_message()
        return True

def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Context Navigator Installer')
    parser.add_argument('--target', '-t', default='.',
                       help='Diretório onde instalar (padrão: atual)')
    parser.add_argument('--force', '-f', action='store_true',
                       help='Forçar instalação mesmo se já existir')
    parser.add_argument('--global', '-g', action='store_true',
                       help='Instalar globalmente no sistema (~/.local/)')
    
    args = parser.parse_args()
    
    global_install = getattr(args, 'global', False)
    installer = ContextNavigatorInstaller(args.target, global_install)
    
    if installer.install():
        print("\n✅ Instalação concluída com sucesso!")
        
        if global_install:
            print("\n🌐 INSTALAÇÃO GLOBAL ATIVA!")
            print("💡 Para usar globalmente, adicione ao ~/.bashrc:")
            print("   export PATH=\"$HOME/.local/bin:$PATH\"")
            print("🎯 Depois execute: cn help")
        else:
            print("\n📁 INSTALAÇÃO LOCAL ATIVA!")
            print("💡 Para usar globalmente, copie o launcher:")
            print(f"   cp {installer.install_dir}/scripts/cn_global_launcher.py ~/.local/bin/cn")
            print("   chmod +x ~/.local/bin/cn")
        
        return 0
    else:
        print("\n❌ Falha na instalação")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 