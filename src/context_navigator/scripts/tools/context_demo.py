#!/usr/bin/env python3
"""
Context Navigator - Demonstração Completa
Script que demonstra todas as funcionalidades implementadas
"""

import json
import yaml
import logging
from datetime import datetime
from pathlib import Path
import subprocess
import sys
import argparse

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('context_demo')

class ContextDemo:
    """Demonstração completa das funcionalidades do Context Navigator"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.scripts_path = self.base_path / "scripts"
        
    def run_command(self, command: str, description: str) -> dict:
        """Executa um comando e retorna resultado"""
        print(f"\n🔧 {description}")
        print(f"Executando: {command}")
        print("-" * 50)
        
        try:
            result = subprocess.run(
                command.split(),
                capture_output=True,
                text=True,
                cwd=self.base_path
            )
            
            if result.returncode == 0:
                print(result.stdout)
                return {
                    'success': True,
                    'output': result.stdout,
                    'error': None
                }
            else:
                print(f"❌ Erro: {result.stderr}")
                return {
                    'success': False,
                    'output': result.stdout,
                    'error': result.stderr
                }
        except Exception as e:
            print(f"❌ Exceção: {e}")
            return {
                'success': False,
                'output': None,
                'error': str(e)
            }
    
    def demo_phase_1(self) -> dict:
        """Demonstração da Fase 1: Fundação"""
        print("\n" + "="*60)
        print("🎯 FASE 1: FUNDAÇÃO - Context Navigator")
        print("="*60)
        
        results = {}
        
        # 1. Verificar configuração
        print("\n📋 1. Verificando configuração metodológica...")
        
        contextrc_path = self.base_path / ".contextrc"
        if contextrc_path.exists():
            print("✅ .contextrc encontrado")
            with open(contextrc_path, 'r') as f:
                config = yaml.safe_load(f)
                print(f"   - Projeto: {config.get('project', {}).get('name', 'N/A')}")
                print(f"   - Versão: {config.get('project', {}).get('version', 'N/A')}")
                print(f"   - Templates: {len(config.get('document_types', {}))}")
        else:
            print("❌ .contextrc não encontrado")
            
        # 2. Verificar templates
        print("\n📝 2. Verificando templates disponíveis...")
        
        templates_path = self.base_path / "templates"
        if templates_path.exists():
            templates = list(templates_path.glob("*.md"))
            print(f"✅ {len(templates)} templates encontrados:")
            for template in templates:
                print(f"   - {template.name}")
        else:
            print("❌ Pasta templates não encontrada")
            
        # 3. Verificar examples
        print("\n📚 3. Verificando exemplos práticos...")
        
        examples_path = self.base_path / "examples"
        if examples_path.exists():
            examples = list(examples_path.glob("*.md"))
            print(f"✅ {len(examples)} exemplos encontrados:")
            for example in examples:
                print(f"   - {example.name}")
        else:
            print("❌ Pasta examples não encontrada")
            
        # 4. Verificar "lei sagrada"
        print("\n⚖️  4. Verificando 'lei sagrada' para IA...")
        
        context_rule_path = self.base_path / "context.rule"
        if context_rule_path.exists():
            print("✅ context.rule encontrado")
            with open(context_rule_path, 'r') as f:
                content = f.read()
                print(f"   - Tamanho: {len(content)} caracteres")
                print(f"   - Linhas: {len(content.split())}")
        else:
            print("❌ context.rule não encontrado")
            
        results['phase_1'] = {
            'config_exists': contextrc_path.exists(),
            'templates_count': len(list(templates_path.glob("*.md"))) if templates_path.exists() else 0,
            'examples_count': len(list(examples_path.glob("*.md"))) if examples_path.exists() else 0,
            'context_rule_exists': context_rule_path.exists()
        }
        
        return results
    
    def demo_phase_2(self) -> dict:
        """Demonstração da Fase 2: Automação"""
        print("\n" + "="*60)
        print("🤖 FASE 2: AUTOMAÇÃO - Scripts Especializados")
        print("="*60)
        
        results = {}
        
        # 1. Context Scanner
        result = self.run_command(
            "python3 scripts/context_scanner.py",
            "Context Scanner - Análise de documentos"
        )
        results['scanner'] = result
        
        # 2. Template Validator
        result = self.run_command(
            "python3 scripts/template_validator.py --templates",
            "Template Validator - Validação de templates"
        )
        results['validator'] = result
        
        # 3. Context Engine
        result = self.run_command(
            "python3 scripts/context_engine.py --patterns",
            "Context Engine - Detecção de padrões"
        )
        results['engine'] = result
        
        # 4. Conflict Detector
        result = self.run_command(
            "python3 scripts/conflict_detector.py --type all",
            "Conflict Detector - Detecção de conflitos"
        )
        results['conflicts'] = result
        
        return results
    
    def demo_phase_3(self) -> dict:
        """Demonstração da Fase 3: Inteligência"""
        print("\n" + "="*60)
        print("🧠 FASE 3: INTELIGÊNCIA - Funcionalidades Avançadas")
        print("="*60)
        
        results = {}
        
        # 1. Context Advisor
        result = self.run_command(
            "python3 scripts/context_advisor.py --all",
            "Context Advisor - Sugestões inteligentes"
        )
        results['advisor'] = result
        
        # 2. Impact Analyzer
        result = self.run_command(
            "python3 scripts/impact_analyzer.py --report",
            "Impact Analyzer - Análise de impacto"
        )
        results['impact'] = result
        
        # 3. Pattern Detector
        result = self.run_command(
            "python3 scripts/pattern_detector.py --full",
            "Pattern Detector - Detecção de padrões e anomalias"
        )
        results['patterns'] = result
        
        return results
    
    def demo_documentation(self) -> dict:
        """Demonstração da documentação implementada"""
        print("\n" + "="*60)
        print("📚 DOCUMENTAÇÃO IMPLEMENTADA")
        print("="*60)
        
        results = {}
        
        # 1. Manual Humano
        print("\n👨‍💻 1. Manual para Operador Humano...")
        
        manual_humano = self.base_path / "docs" / "MANUAL_HUMANO.md"
        if manual_humano.exists():
            with open(manual_humano, 'r') as f:
                content = f.read()
                print(f"✅ MANUAL_HUMANO.md: {len(content)} caracteres, {len(content.split())} palavras")
        else:
            print("❌ MANUAL_HUMANO.md não encontrado")
            
        # 2. Manual IA
        print("\n🤖 2. Manual para IA...")
        
        manual_ia = self.base_path / "docs" / "MANUAL_IA.md"
        if manual_ia.exists():
            with open(manual_ia, 'r') as f:
                content = f.read()
                print(f"✅ MANUAL_IA.md: {len(content)} caracteres, {len(content.split())} palavras")
        else:
            print("❌ MANUAL_IA.md não encontrado")
            
        # 3. Convenções
        print("\n📋 3. Convenções Imutáveis...")
        
        conventions = self.base_path / "docs" / "CONVENTIONS.md"
        if conventions.exists():
            with open(conventions, 'r') as f:
                content = f.read()
                print(f"✅ CONVENTIONS.md: {len(content)} caracteres, {len(content.split())} palavras")
        else:
            print("❌ CONVENTIONS.md não encontrado")
            
        results['documentation'] = {
            'manual_humano': manual_humano.exists(),
            'manual_ia': manual_ia.exists(),
            'conventions': conventions.exists()
        }
        
        return results
    
    def demo_context_maps(self) -> dict:
        """Demonstração dos mapas de contexto"""
        print("\n" + "="*60)
        print("🗺️  MAPAS DE CONTEXTO GERADOS")
        print("="*60)
        
        results = {}
        
        context_maps_path = self.base_path / ".context-map"
        if context_maps_path.exists():
            map_files = list(context_maps_path.glob("*"))
            print(f"✅ {len(map_files)} mapas de contexto gerados:")
            
            for map_file in map_files:
                size = map_file.stat().st_size
                print(f"   - {map_file.name}: {size} bytes")
                
                if map_file.suffix == '.yml':
                    try:
                        with open(map_file, 'r') as f:
                            data = yaml.safe_load(f)
                            if isinstance(data, dict):
                                print(f"     → {len(data)} seções principais")
                    except:
                        pass
                        
            results['context_maps'] = {
                'exists': True,
                'files_count': len(map_files),
                'files': [f.name for f in map_files]
            }
        else:
            print("❌ Pasta .context-map não encontrada")
            results['context_maps'] = {'exists': False}
            
        return results
    
    def generate_summary_report(self, all_results: dict) -> None:
        """Gera relatório resumo da demonstração"""
        print("\n" + "="*60)
        print("📊 RELATÓRIO RESUMO - CONTEXT NAVIGATOR")
        print("="*60)
        
        # Contadores
        total_scripts = 0
        working_scripts = 0
        total_docs = 0
        total_features = 0
        
        # Fase 1
        phase1 = all_results.get('phase_1', {})
        phase1_score = sum([
            phase1.get('config_exists', False),
            phase1.get('templates_count', 0) > 0,
            phase1.get('examples_count', 0) > 0,
            phase1.get('context_rule_exists', False)
        ])
        
        print(f"\n🎯 FASE 1 - FUNDAÇÃO: {phase1_score}/4 componentes")
        print(f"   - Configuração: {'✅' if phase1.get('config_exists') else '❌'}")
        print(f"   - Templates: {phase1.get('templates_count', 0)} disponíveis")
        print(f"   - Exemplos: {phase1.get('examples_count', 0)} disponíveis")
        print(f"   - Lei Sagrada: {'✅' if phase1.get('context_rule_exists') else '❌'}")
        
        # Fase 2
        phase2 = all_results.get('phase_2', {})
        phase2_working = sum([
            phase2.get('scanner', {}).get('success', False),
            phase2.get('validator', {}).get('success', False),
            phase2.get('engine', {}).get('success', False),
            phase2.get('conflicts', {}).get('success', False)
        ])
        
        print(f"\n🤖 FASE 2 - AUTOMAÇÃO: {phase2_working}/4 scripts funcionais")
        print(f"   - Context Scanner: {'✅' if phase2.get('scanner', {}).get('success') else '❌'}")
        print(f"   - Template Validator: {'✅' if phase2.get('validator', {}).get('success') else '❌'}")
        print(f"   - Context Engine: {'✅' if phase2.get('engine', {}).get('success') else '❌'}")
        print(f"   - Conflict Detector: {'✅' if phase2.get('conflicts', {}).get('success') else '❌'}")
        
        # Fase 3
        phase3 = all_results.get('phase_3', {})
        phase3_working = sum([
            phase3.get('advisor', {}).get('success', False),
            phase3.get('impact', {}).get('success', False),
            phase3.get('patterns', {}).get('success', False)
        ])
        
        print(f"\n🧠 FASE 3 - INTELIGÊNCIA: {phase3_working}/3 funcionalidades avançadas")
        print(f"   - Context Advisor: {'✅' if phase3.get('advisor', {}).get('success') else '❌'}")
        print(f"   - Impact Analyzer: {'✅' if phase3.get('impact', {}).get('success') else '❌'}")
        print(f"   - Pattern Detector: {'✅' if phase3.get('patterns', {}).get('success') else '❌'}")
        
        # Documentação
        docs = all_results.get('documentation', {})
        docs_count = sum([
            docs.get('manual_humano', False),
            docs.get('manual_ia', False),
            docs.get('conventions', False)
        ])
        
        print(f"\n📚 DOCUMENTAÇÃO: {docs_count}/3 manuais")
        print(f"   - Manual Humano: {'✅' if docs.get('manual_humano') else '❌'}")
        print(f"   - Manual IA: {'✅' if docs.get('manual_ia') else '❌'}")
        print(f"   - Convenções: {'✅' if docs.get('conventions') else '❌'}")
        
        # Context Maps
        maps = all_results.get('context_maps', {})
        print(f"\n🗺️  MAPAS DE CONTEXTO: {'✅' if maps.get('exists') else '❌'}")
        if maps.get('exists'):
            print(f"   - Arquivos gerados: {maps.get('files_count', 0)}")
            
        # Score final
        total_possible = 4 + 4 + 3 + 3 + 1  # 15 componentes
        total_working = phase1_score + phase2_working + phase3_working + docs_count + (1 if maps.get('exists') else 0)
        
        final_score = (total_working / total_possible) * 100
        
        print(f"\n🎯 SCORE FINAL: {final_score:.1f}% ({total_working}/{total_possible} componentes)")
        
        if final_score >= 90:
            print("🏆 EXCELENTE - Context Navigator totalmente funcional!")
        elif final_score >= 70:
            print("✅ BOM - Context Navigator funcionando bem!")
        elif final_score >= 50:
            print("⚠️  MÉDIO - Context Navigator parcialmente funcional")
        else:
            print("❌ BAIXO - Context Navigator precisa de ajustes")
            
        print(f"\n⏰ Demonstração concluída em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    def run_full_demo(self) -> dict:
        """Executa demonstração completa"""
        print("🚀 INICIANDO DEMONSTRAÇÃO COMPLETA - CONTEXT NAVIGATOR")
        print(f"📅 Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        all_results = {}
        
        # Executar todas as fases
        all_results.update(self.demo_phase_1())
        all_results['phase_2'] = self.demo_phase_2()
        all_results['phase_3'] = self.demo_phase_3()
        all_results.update(self.demo_documentation())
        all_results.update(self.demo_context_maps())
        
        # Gerar relatório final
        self.generate_summary_report(all_results)
        
        return all_results

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(description='Context Navigator - Demonstração Completa')
    parser.add_argument('--path', '-p', default='.', help='Caminho base do projeto')
    parser.add_argument('--phase', choices=['1', '2', '3'], help='Executar fase específica')
    parser.add_argument('--full', action='store_true', help='Demonstração completa')
    parser.add_argument('--docs', action='store_true', help='Mostrar documentação')
    parser.add_argument('--maps', action='store_true', help='Mostrar mapas de contexto')
    
    args = parser.parse_args()
    
    demo = ContextDemo(args.path)
    
    if args.phase == '1':
        demo.demo_phase_1()
    elif args.phase == '2':
        demo.demo_phase_2()
    elif args.phase == '3':
        demo.demo_phase_3()
    elif args.docs:
        demo.demo_documentation()
    elif args.maps:
        demo.demo_context_maps()
    elif args.full:
        demo.run_full_demo()
    else:
        print("Especifique --full, --phase [1|2|3], --docs ou --maps")

if __name__ == '__main__':
    main() 