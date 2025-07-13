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
    def __init__(self, target_path: str = "."):
        """
        Inicializa o instalador
        
        Args:
            target_path: Caminho do workspace onde instalar (padrão: diretório atual)
        """
        self.target_path = Path(target_path).resolve()
        self.install_dir = self.target_path / ".context-navigator"
        self.source_dir = Path(__file__).parent.resolve()
        
        # Versão do Context Navigator
        self.version = "1.0.0"
        
        print(f"🎯 Context Navigator Installer v{self.version}")
        print(f"📁 Workspace: {self.target_path}")
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
        
        # Mapeamento de arquivos para copiar
        files_to_copy = {
            # Scripts
            "scripts/": "scripts/",
            # Templates
            "templates/": "templates/",
            # Documentação
            "docs/": "docs/",
            # Exemplos
            "examples/": "examples/",
            # Configuração
            "context.rule": "context.rule",
            ".contextrc": ".contextrc",
            # Documentação principal
            "README.md": "README.md",
            "QUICK_START.md": "QUICK_START.md",
            "GUIA_IMPLEMENTACAO.md": "GUIA_IMPLEMENTACAO.md"
        }
        
        try:
            for source, dest in files_to_copy.items():
                source_path = self.source_dir / source
                dest_path = self.install_dir / dest
                
                if source_path.exists():
                    if source_path.is_dir():
                        if dest_path.exists():
                            shutil.rmtree(dest_path)
                        shutil.copytree(source_path, dest_path)
                        print(f"✅ Copiado: {source}/ -> {dest}/")
                    else:
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
        """Cria diretório .context-map no workspace"""
        try:
            context_map_dir = self.target_path / ".context-map"
            context_map_dir.mkdir(exist_ok=True)
            
            # Criar arquivo inicial vazio
            index_file = context_map_dir / "index.yml"
            if not index_file.exists():
                initial_content = {
                    "version": self.version,
                    "created_at": datetime.now().isoformat(),
                    "documents": {},
                    "connections": {},
                    "last_scan": None
                }
                with open(index_file, 'w', encoding='utf-8') as f:
                    yaml.dump(initial_content, f, default_flow_style=False, allow_unicode=True)
                    
            print(f"✅ Diretório de contexto criado: .context-map/")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar diretório de contexto: {e}")
            return False
            
    def create_launcher_script(self) -> bool:
        """Cria script launcher 'cn'"""
        print(f"\n🔧 Criando launcher 'cn'...")
        
        launcher_content = f'''#!/usr/bin/env python3
"""
Context Navigator - Launcher
Script que executa comandos do Context Navigator de forma simplificada
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def find_context_navigator():
    """Encontra instalação do Context Navigator no workspace atual"""
    current_dir = Path.cwd()
    
    # Procurar .context-navigator/ no diretório atual e pais
    for path in [current_dir] + list(current_dir.parents):
        cn_dir = path / ".context-navigator"
        if cn_dir.exists() and (cn_dir / "scripts").exists():
            return cn_dir
            
    return None

def show_help():
    """Mostra ajuda dos comandos"""
    print("""
🧭 Context Navigator - Comandos Disponíveis

📊 PRINCIPAIS:
  cn scan                    Escanear documentos
  cn demo                    Demonstração completa
  cn validate                Validar métricas
  cn check                   Verificar sistema
  
📝 DOCUMENTOS:
  cn new decision            Criar nova decisão
  cn new process             Criar novo processo
  cn new reference           Criar nova referência
  cn new architecture        Criar nova arquitetura
  cn new analysis            Criar nova análise
  cn new planning            Criar novo planejamento
  
🔧 AVANÇADO:
  cn patterns                Detectar padrões
  cn conflicts               Detectar conflitos
  cn impact                  Analisar impacto
  cn templates               Validar templates
  
ℹ️  INFORMAÇÕES:
  cn version                 Mostrar versão
  cn help                    Esta ajuda
  cn status                  Status da instalação
  
💡 EXEMPLOS:
  cn scan                    # Escanear tudo
  cn demo --full             # Demo completa
  cn new decision auth       # Nova decisão sobre auth
  cn validate --detailed     # Validação detalhada
""")

def run_script(script_name, args=None):
    """Executa script do Context Navigator"""
    cn_dir = find_context_navigator()
    
    if not cn_dir:
        print("❌ Context Navigator não encontrado neste workspace")
        print("💡 Execute 'python3 install.py' para instalar")
        return 1
        
    script_path = cn_dir / "scripts" / f"{{script_name}}.py"
    
    if not script_path.exists():
        print(f"❌ Script não encontrado: {{script_name}}")
        return 1
        
    # Executar script
    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)
        
    try:
        return subprocess.run(cmd, cwd=Path.cwd()).returncode
    except Exception as e:
        print(f"❌ Erro ao executar script: {{e}}")
        return 1

 def create_document(doc_type, name=None):
     """Cria novo documento baseado em template"""
     cn_dir = find_context_navigator()
     
     if not cn_dir:
         print("❌ Context Navigator não encontrado")
         return 1
         
     # Mapeamento de tipos em inglês para português
     type_mapping = {{
         "decision": "decisao",
         "process": "processo",
         "reference": "referencia",
         "architecture": "arquitetura",
         "analysis": "analise",
         "planning": "planejamento"
     }}
     
     # Usar mapeamento ou o tipo original
     template_name = type_mapping.get(doc_type, doc_type)
     template_path = cn_dir / "templates" / f"{{template_name}}.md"
    
    if not template_path.exists():
        print(f"❌ Template não encontrado: {{doc_type}}")
        return 1
        
    # Determinar nome do arquivo
    if name:
        filename = f"{{name}}.md"
    else:
        filename = f"{{doc_type}}_{{datetime.now().strftime('%Y%m%d_%H%M%S')}}.md"
        
    # Copiar template
    try:
        import shutil
        from datetime import datetime
        
        shutil.copy2(template_path, filename)
        print(f"✅ Documento criado: {{filename}}")
        print(f"📝 Edite o arquivo e preencha os metadados obrigatórios")
        print(f"🔍 Depois execute: cn scan")
        return 0
    except Exception as e:
        print(f"❌ Erro ao criar documento: {{e}}")
        return 1

def show_status():
    """Mostra status da instalação"""
    cn_dir = find_context_navigator()
    
    if not cn_dir:
        print("❌ Context Navigator não instalado neste workspace")
        return 1
        
    # Carregar informações de versão
    version_file = cn_dir / "VERSION"
    if version_file.exists():
        with open(version_file, 'r') as f:
            version_info = json.load(f)
            
        print(f"✅ Context Navigator v{{version_info['version']}}")
        print(f"📁 Instalado em: {{cn_dir}}")
        print(f"📅 Instalado em: {{version_info['installed_at']}}")
        print(f"🐍 Python: {{version_info['python_version']}}")
    else:
        print("⚠️  Informações de versão não encontradas")
        
    return 0

def main():
    """Função principal do launcher"""
    if len(sys.argv) < 2:
        show_help()
        return 0
        
    command = sys.argv[1]
    args = sys.argv[2:] if len(sys.argv) > 2 else []
    
    # Comandos principais
    if command == "scan":
        return run_script("context_scanner", args)
    elif command == "demo":
        return run_script("context_demo", ["--full"] + args)
    elif command == "validate":
        return run_script("metrics_validator", args)
    elif command == "check":
        return run_script("context_scanner", ["--verbose"])
    elif command == "patterns":
        return run_script("pattern_detector", args)
    elif command == "conflicts":
        return run_script("conflict_detector", args)
    elif command == "impact":
        return run_script("impact_analyzer", args)
    elif command == "templates":
        return run_script("template_validator", args)
    elif command == "engine":
        return run_script("context_engine", args)
    elif command == "advisor":
        return run_script("context_advisor", args)
        
    # Comandos de criação
    elif command == "new":
        if len(args) < 1:
            print("❌ Especifique o tipo de documento")
            print("💡 Tipos: decision, process, reference, architecture, analysis, planning")
            return 1
        doc_type = args[0]
        doc_name = args[1] if len(args) > 1 else None
        return create_document(doc_type, doc_name)
        
    # Comandos de informação
    elif command == "help":
        show_help()
        return 0
    elif command == "version":
        return show_status()
    elif command == "status":
        return show_status()
    else:
        print(f"❌ Comando não reconhecido: {{command}}")
        print("💡 Execute 'cn help' para ver comandos disponíveis")
        return 1

if __name__ == "__main__":
    sys.exit(main())
'''
        
        try:
            launcher_path = self.target_path / "cn"
            with open(launcher_path, 'w', encoding='utf-8') as f:
                f.write(launcher_content)
                
            # Tornar executável
            os.chmod(launcher_path, 0o755)
            
            print(f"✅ Launcher criado: cn")
            print(f"💡 Execute 'cn help' para ver comandos disponíveis")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar launcher: {e}")
            return False
            
    def test_installation(self) -> bool:
        """Testa se a instalação está funcionando"""
        print(f"\n🧪 Testando instalação...")
        
        try:
            # Testar launcher
            launcher_path = self.target_path / "cn"
            if not launcher_path.exists():
                print("❌ Launcher não encontrado")
                return False
                
            # Testar comando básico
            result = subprocess.run([
                sys.executable, str(launcher_path), "status"
            ], cwd=self.target_path, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Launcher funcionando")
                return True
            else:
                print(f"❌ Erro no launcher: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Erro no teste: {e}")
            return False
            
    def show_completion_message(self) -> None:
        """Mostra mensagem de conclusão"""
        print(f"\n" + "="*60)
        print(f"🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
        print(f"="*60)
        print(f"")
        print(f"📁 Workspace: {self.target_path}")
        print(f"📦 Instalação: {self.install_dir}")
        print(f"🔧 Launcher: {self.target_path}/cn")
        print(f"")
        print(f"🚀 PRÓXIMOS PASSOS:")
        print(f"")
        print(f"1. 📋 Ver comandos disponíveis:")
        print(f"   ./cn help")
        print(f"")
        print(f"2. 🧪 Testar o sistema:")
        print(f"   ./cn demo")
        print(f"")
        print(f"3. 📝 Criar seu primeiro documento:")
        print(f"   ./cn new decision minha_primeira_decisao")
        print(f"")
        print(f"4. 🔍 Escanear documentos:")
        print(f"   ./cn scan")
        print(f"")
        print(f"5. 📊 Validar métricas:")
        print(f"   ./cn validate")
        print(f"")
        print(f"💡 DICAS:")
        print(f"• Execute './cn status' para ver informações da instalação")
        print(f"• Leia {self.install_dir}/README.md para documentação completa")
        print(f"• Use './cn check' para verificar a saúde do sistema")
        print(f"")
        print(f"🎯 Transforme sua documentação em navegação inteligente!")
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
    
    args = parser.parse_args()
    
    installer = ContextNavigatorInstaller(args.target)
    
    if installer.install():
        print("\n✅ Instalação concluída com sucesso!")
        return 0
    else:
        print("\n❌ Falha na instalação")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 