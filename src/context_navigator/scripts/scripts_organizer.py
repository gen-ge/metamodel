#!/usr/bin/env python3
"""
Context Navigator - Scripts Organizer
Organizador e mapa da nova estrutura de scripts 2.0
"""

import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Any

class ScriptsOrganizer:
    """Organizador dos scripts do Context Navigator"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent
        
        # Mapa da nova estrutura
        self.script_map = {
            'engines': {
                'description': 'Engines essenciais de processamento principal',
                'scripts': {
                    'context_scanner': {
                        'file': 'engines/context_scanner.py',
                        'description': 'Escaneia documentos e gera mapas de contexto',
                        'main_class': 'ContextScanner'
                    },
                    'context_engine': {
                        'file': 'engines/context_engine.py', 
                        'description': 'Motor principal de processamento contextual',
                        'main_class': 'ContextEngine'
                    }
                }
            },
            'validation': {
                'description': 'Scripts especializados em validação de qualidade',
                'scripts': {
                    'template_validator': {
                        'file': 'validation/template_validator.py',
                        'description': 'Validação especializada de templates metodológicos',
                        'main_class': 'TemplateValidator'
                    },
                    'cn_consistency_validator': {
                        'file': 'validation/cn_consistency_validator.py',
                        'description': 'Validação de consistência entre código e documentação',
                        'main_class': 'CNConsistencyValidator'
                    },
                    'metrics_validator': {
                        'file': 'validation/metrics_validator.py',
                        'description': 'Validação contra métricas de sucesso do PRD',
                        'main_class': 'MetricsValidator'
                    }
                }
            },
            'analysis': {
                'description': 'Scripts de análise avançada e inteligência artificial',
                'scripts': {
                    'pattern_detector': {
                        'file': 'analysis/pattern_detector.py',
                        'description': 'Detecta padrões e anomalias na documentação',
                        'main_class': 'PatternDetector'
                    },
                    'conflict_detector': {
                        'file': 'analysis/conflict_detector.py',
                        'description': 'Detecta conflitos e inconsistências complexas',
                        'main_class': 'ConflictDetector'
                    },
                    'impact_analyzer': {
                        'file': 'analysis/impact_analyzer.py',
                        'description': 'Analisa impacto de mudanças em documentos',
                        'main_class': 'ImpactAnalyzer'
                    },
                    'context_advisor': {
                        'file': 'analysis/context_advisor.py',
                        'description': 'Sistema de sugestões inteligente baseado em contexto',
                        'main_class': 'ContextAdvisor'
                    }
                }
            },
            'tools': {
                'description': 'Ferramentas utilitárias e auxiliares',
                'scripts': {
                    'cn_component_explorer': {
                        'file': 'tools/cn_component_explorer.py',
                        'description': 'Explorador visual de componentes hierárquicos',
                        'main_class': 'CNComponentExplorer'
                    },
                    'cn_component_parser': {
                        'file': 'tools/cn_component_parser.py',
                        'description': 'Parser para extrair marcações @cn: do código',
                        'main_class': 'CNComponentParser'
                    },
                    'context_demo': {
                        'file': 'tools/context_demo.py',
                        'description': 'Demonstração completa das funcionalidades',
                        'main_class': 'ContextDemo'
                    },
                    'cn_global_launcher': {
                        'file': 'tools/cn_global_launcher.py',
                        'description': 'Launcher global para arquitetura 2.0',
                        'main_class': None
                    }
                }
            }
        }
    
    def list_all_scripts(self):
        """Lista todos os scripts organizados"""
        print("🧭 Context Navigator - Scripts Organizados (Arquitetura 2.0)")
        print("=" * 70)
        
        total_scripts = 0
        for category, info in self.script_map.items():
            print(f"\n📁 {category.upper()}: {info['description']}")
            print("-" * 50)
            
            for script_name, script_info in info['scripts'].items():
                print(f"   • {script_name}")
                print(f"     Arquivo: {script_info['file']}")
                print(f"     Descrição: {script_info['description']}")
                if script_info['main_class']:
                    print(f"     Classe: {script_info['main_class']}")
                print()
                total_scripts += 1
        
        print(f"📊 Total: {total_scripts} scripts organizados em 4 categorias")
        
    def verify_scripts_exist(self):
        """Verifica se todos os scripts existem"""
        print("🔍 Verificando existência dos scripts...")
        print("=" * 50)
        
        missing_scripts = []
        existing_scripts = []
        
        for category, info in self.script_map.items():
            for script_name, script_info in info['scripts'].items():
                script_path = self.base_path / script_info['file']
                
                if script_path.exists():
                    print(f"✅ {script_info['file']}")
                    existing_scripts.append(script_name)
                else:
                    print(f"❌ {script_info['file']} - NÃO ENCONTRADO")
                    missing_scripts.append(script_name)
        
        print(f"\n📊 Resumo:")
        print(f"   ✅ Existentes: {len(existing_scripts)}")
        print(f"   ❌ Faltando: {len(missing_scripts)}")
        
        if missing_scripts:
            print(f"\n⚠️  Scripts não encontrados: {', '.join(missing_scripts)}")
            
        return len(missing_scripts) == 0
    
    def test_script_execution(self, script_name: str):
        """Testa execução de um script específico"""
        # Encontrar script
        script_info = None
        for category_info in self.script_map.values():
            if script_name in category_info['scripts']:
                script_info = category_info['scripts'][script_name]
                break
        
        if not script_info:
            print(f"❌ Script '{script_name}' não encontrado")
            return False
            
        script_path = self.base_path / script_info['file']
        
        if not script_path.exists():
            print(f"❌ Arquivo não encontrado: {script_path}")
            return False
            
        print(f"🧪 Testando {script_name}...")
        print(f"   Arquivo: {script_info['file']}")
        print(f"   Descrição: {script_info['description']}")
        
        try:
            # Testar execução com --help
            result = subprocess.run(
                [sys.executable, str(script_path), '--help'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                print(f"✅ Script executável - help funciona")
                return True
            else:
                print(f"⚠️  Script com problemas: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏰ Timeout na execução")
            return False
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
            return False
    
    def generate_documentation(self):
        """Gera documentação da estrutura"""
        doc = []
        doc.append("# 📋 Context Navigator - Scripts Organizados")
        doc.append("")
        doc.append("Estrutura reorganizada da arquitetura 2.0:")
        doc.append("")
        
        for category, info in self.script_map.items():
            doc.append(f"## 📁 {category.upper()}")
            doc.append(f"{info['description']}")
            doc.append("")
            
            for script_name, script_info in info['scripts'].items():
                doc.append(f"### {script_name}")
                doc.append(f"- **Arquivo:** `{script_info['file']}`")
                doc.append(f"- **Descrição:** {script_info['description']}")
                if script_info['main_class']:
                    doc.append(f"- **Classe:** `{script_info['main_class']}`")
                doc.append("")
        
        return "\n".join(doc)

def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Context Navigator Scripts Organizer')
    parser.add_argument('--list', action='store_true', help='Listar todos os scripts')
    parser.add_argument('--verify', action='store_true', help='Verificar existência dos scripts')
    parser.add_argument('--test', help='Testar execução de script específico')
    parser.add_argument('--docs', action='store_true', help='Gerar documentação')
    
    args = parser.parse_args()
    
    organizer = ScriptsOrganizer()
    
    if args.list:
        organizer.list_all_scripts()
    elif args.verify:
        organizer.verify_scripts_exist()
    elif args.test:
        organizer.test_script_execution(args.test)
    elif args.docs:
        print(organizer.generate_documentation())
    else:
        print("Use --help para ver opções disponíveis")

if __name__ == '__main__':
    main() 