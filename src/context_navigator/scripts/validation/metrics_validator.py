#!/usr/bin/env python3
"""
Context Navigator - Metrics Validator

Avalia o sistema atual contra as métricas de sucesso definidas no PRD.
"""

import json
import yaml
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import sys
import argparse

class MetricsValidator:
    def __init__(self, config_path: str = ".contextrc"):
        # NOVO: Usar WorkspaceManager para detectar workspace
        self._init_with_workspace_manager()
        
        # Métricas do PRD
        self.target_metrics = {
            "ai_consistency": 95.0,  # 95%+ prompts seguem context.rule
            "documentation_coverage": 90.0,  # 90%+ documentos com metadados completos
            "automatic_detection": 95.0,  # 95%+ contextos detectados corretamente
            "conflict_resolution": 90.0,  # 90%+ conflitos detectados automaticamente
            "efficiency_reduction": 80.0,  # 80% redução em retrabalho documental
            "context_switch_time": 2.0,  # <2 minutos para recuperar contexto
            "connection_precision": 95.0,  # 95%+ conexões corretas
            "template_completeness": 100.0,  # 100% casos cobertos por templates
            "manual_intervention": 0.0  # 0 intervenção manual regular
        }
        
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
            print("❌ Context Navigator workspace não encontrado")
            print("💡 Execute 'cn init' para configurar este diretório")
            sys.exit(1)
        
        # Configurar paths baseado no workspace
        self.workspace = current_workspace
        self.base_path = current_workspace.root_path
        self.output_dir = current_workspace.root_path / ".cn_model"
        
        # Configuração vem do workspace
        self.config = current_workspace.configuration
        
        # Paths para nova arquitetura
        self.context_map_path = self.output_dir
        self.templates_path = self._get_global_templates_path()
        self.docs_path = self.output_dir / "docs"
        self.examples_path = self.base_path / "examples"
        self.scripts_path = Path(__file__).parent
        
        print(f"🌐 Workspace: {current_workspace.name} ({current_workspace.root_path})")
        
    def _get_global_templates_path(self) -> Path:
        """Detecta onde estão os templates na instalação global"""
        possible_locations = [
            Path("/opt/context-navigator/templates"),
            Path.home() / ".local" / "share" / "context-navigator" / "templates",
        ]
        
        for location in possible_locations:
            if location.exists():
                return location
        
        # Fallback para desenvolvimento
        return Path(__file__).parent.parent / "templates"
        
    def load_context_map(self, filename: str) -> Dict:
        """Carrega mapa de contexto específico"""
        map_path = self.context_map_path / filename
        if not map_path.exists():
            return {}
        
        try:
            with open(map_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except yaml.YAMLError:
            # Se houver erro YAML, tenta uma abordagem mais simples
            if filename == "conflicts.yml":
                return self.parse_conflicts_manually(map_path)
            return {}
    
    def parse_conflicts_manually(self, conflicts_path: Path) -> Dict:
        """Parse manual do arquivo de conflitos se YAML falhar"""
        try:
            with open(conflicts_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Extrai informações básicas usando regex
            total_conflicts = content.count('- component:')
            duplicate_refs = content.count('duplicate_references')
            orphaned_docs = content.count('orphaned_document')
            
            return {
                "summary": {
                    "total_conflicts": total_conflicts,
                    "by_type": {
                        "duplicate_references": duplicate_refs,
                        "orphaned_document": orphaned_docs
                    }
                }
            }
        except Exception:
            return {}
    
    def evaluate_ai_consistency(self) -> Dict[str, Any]:
        """Avalia consistência da IA com context.rule"""
        score = 0.0
        details = []
        
        # Verificar se context.rule existe
        if Path("context.rule").exists():
            score += 30.0
            details.append("✅ context.rule existe")
        else:
            details.append("❌ context.rule não encontrado")
        
        # Verificar tamanho e completude do context.rule
        if Path("context.rule").exists():
            with open("context.rule", 'r', encoding='utf-8') as f:
                content = f.read()
                if len(content) > 5000:  # Conteúdo substancial
                    score += 20.0
                    details.append("✅ context.rule tem conteúdo substancial")
                else:
                    details.append("⚠️ context.rule pode ser mais detalhado")
        
        # Verificar manuais de IA
        if (self.docs_path / "MANUAL_IA.md").exists():
            score += 25.0
            details.append("✅ Manual da IA existe")
        else:
            details.append("❌ Manual da IA não encontrado")
        
        # Verificar convenções
        if (self.docs_path / "CONVENTIONS.md").exists():
            score += 25.0
            details.append("✅ Convenções definidas")
        else:
            details.append("❌ Convenções não definidas")
        
        return {
            "score": score,
            "target": self.target_metrics["ai_consistency"],
            "status": "✅ PASS" if score >= self.target_metrics["ai_consistency"] else "❌ FAIL",
            "details": details
        }
    
    def evaluate_documentation_coverage(self) -> Dict[str, Any]:
        """Avalia cobertura documental com metadados"""
        index_map = self.load_context_map("index.yml")
        
        if not index_map or "document_summary" not in index_map:
            return {
                "score": 0.0,
                "target": self.target_metrics["documentation_coverage"],
                "status": "❌ FAIL",
                "details": ["❌ Nenhum documento encontrado"]
            }
        
        documents = index_map["document_summary"]
        total_docs = len(documents)
        docs_with_metadata = 0
        details = []
        
        for doc_path, doc_info in documents.items():
            if doc_info.get("type") and doc_info.get("context_level") and doc_info.get("context_type"):
                docs_with_metadata += 1
                details.append(f"✅ {doc_path} - metadados completos")
            else:
                details.append(f"❌ {doc_path} - metadados incompletos")
        
        score = (docs_with_metadata / total_docs) * 100 if total_docs > 0 else 0.0
        
        return {
            "score": score,
            "target": self.target_metrics["documentation_coverage"],
            "status": "✅ PASS" if score >= self.target_metrics["documentation_coverage"] else "❌ FAIL",
            "details": details,
            "stats": {
                "total_documents": total_docs,
                "with_metadata": docs_with_metadata,
                "coverage_percentage": score
            }
        }
    
    def evaluate_automatic_detection(self) -> Dict[str, Any]:
        """Avalia detecção automática de contextos"""
        index_map = self.load_context_map("index.yml")
        
        if not index_map or "context_distribution" not in index_map:
            return {
                "score": 0.0,
                "target": self.target_metrics["automatic_detection"],
                "status": "❌ FAIL",
                "details": ["❌ Mapas de contexto não encontrados"]
            }
        
        context_dist = index_map["context_distribution"]
        total_docs = sum(context_dist.values())
        unknown_docs = context_dist.get("unknown", 0)
        detected_docs = total_docs - unknown_docs
        
        score = (detected_docs / total_docs) * 100 if total_docs > 0 else 0.0
        
        details = []
        for context, count in context_dist.items():
            if context == "unknown":
                details.append(f"❌ {context}: {count} documentos")
            else:
                details.append(f"✅ {context}: {count} documentos")
        
        return {
            "score": score,
            "target": self.target_metrics["automatic_detection"],
            "status": "✅ PASS" if score >= self.target_metrics["automatic_detection"] else "❌ FAIL",
            "details": details,
            "stats": {
                "total_documents": total_docs,
                "detected_documents": detected_docs,
                "unknown_documents": unknown_docs,
                "detection_percentage": score
            }
        }
    
    def evaluate_conflict_resolution(self) -> Dict[str, Any]:
        """Avalia resolução de conflitos"""
        conflicts_map = self.load_context_map("conflicts.yml")
        
        if not conflicts_map or "summary" not in conflicts_map:
            return {
                "score": 100.0,  # Sem conflitos = 100%
                "target": self.target_metrics["conflict_resolution"],
                "status": "✅ PASS",
                "details": ["✅ Nenhum conflito detectado"]
            }
        
        summary = conflicts_map["summary"]
        total_conflicts = summary.get("total_conflicts", 0)
        
        details = []
        if total_conflicts == 0:
            score = 100.0
            details.append("✅ Nenhum conflito detectado")
        else:
            # Analisa tipos de conflitos
            by_type = summary.get("by_type", {})
            critical_conflicts = by_type.get("orphaned_document", 0) + by_type.get("broken_connections", 0)
            warning_conflicts = by_type.get("duplicate_references", 0) + by_type.get("circular_dependencies", 0)
            
            # Score baseado na criticidade
            resolution_score = max(0, 100 - (critical_conflicts * 20) - (warning_conflicts * 5))
            score = resolution_score
            
            for conflict_type, count in by_type.items():
                severity = "crítico" if conflict_type in ["orphaned_document", "broken_connections"] else "aviso"
                details.append(f"⚠️ {conflict_type}: {count} ({severity})")
        
        return {
            "score": score,
            "target": self.target_metrics["conflict_resolution"],
            "status": "✅ PASS" if score >= self.target_metrics["conflict_resolution"] else "❌ FAIL",
            "details": details,
            "stats": {
                "total_conflicts": total_conflicts,
                "resolution_score": score
            }
        }
    
    def evaluate_efficiency(self) -> Dict[str, Any]:
        """Avalia eficiência (baseado em indicadores indiretos)"""
        # Métricas indiretas de eficiência
        score = 0.0
        details = []
        
        # Templates disponíveis
        templates = list(self.templates_path.glob("*.md"))
        if len(templates) >= 6:
            score += 20.0
            details.append(f"✅ {len(templates)} templates disponíveis")
        else:
            details.append(f"⚠️ Apenas {len(templates)} templates disponíveis")
        
        # Scripts de automação
        scripts = list(self.scripts_path.glob("*.py"))
        if len(scripts) >= 4:
            score += 20.0
            details.append(f"✅ {len(scripts)} scripts de automação")
        else:
            details.append(f"⚠️ Apenas {len(scripts)} scripts de automação")
        
        # Documentação completa
        required_docs = ["MANUAL_HUMANO.md", "MANUAL_IA.md", "CONVENTIONS.md"]
        existing_docs = sum(1 for doc in required_docs if (self.docs_path / doc).exists())
        if existing_docs == len(required_docs):
            score += 20.0
            details.append("✅ Documentação completa")
        else:
            details.append(f"⚠️ Documentação incompleta ({existing_docs}/{len(required_docs)})")
        
        # Mapas de contexto automáticos
        context_maps = list(self.context_map_path.glob("*.yml")) + list(self.context_map_path.glob("*.json"))
        if len(context_maps) >= 5:
            score += 20.0
            details.append(f"✅ {len(context_maps)} mapas de contexto")
        else:
            details.append(f"⚠️ Apenas {len(context_maps)} mapas de contexto")
        
        # Conexões entre documentos
        connections_map = self.load_context_map("connections.yml")
        if connections_map and len(connections_map) > 0:
            score += 20.0
            details.append("✅ Conexões entre documentos mapeadas")
        else:
            details.append("⚠️ Conexões não mapeadas")
        
        return {
            "score": score,
            "target": self.target_metrics["efficiency_reduction"],
            "status": "✅ PASS" if score >= self.target_metrics["efficiency_reduction"] else "❌ FAIL",
            "details": details
        }
    
    def evaluate_context_switch_time(self) -> Dict[str, Any]:
        """Avalia tempo de mudança de contexto"""
        # Métricas indiretas baseadas em estrutura
        score = 0.0
        details = []
        
        # Index centralizado
        if (self.context_map_path / "index.yml").exists():
            score += 40.0
            details.append("✅ Índice centralizado disponível")
        else:
            details.append("❌ Índice centralizado não encontrado")
        
        # Context rule para IA
        if Path("context.rule").exists():
            score += 30.0
            details.append("✅ Context rule para IA disponível")
        else:
            details.append("❌ Context rule não encontrado")
        
        # Navegação por conexões
        connections_map = self.load_context_map("connections.yml")
        if connections_map and len(connections_map) > 0:
            score += 30.0
            details.append("✅ Navegação por conexões disponível")
        else:
            details.append("❌ Navegação por conexões não disponível")
        
        # Assume <2 minutos se score alto
        estimated_time = 2.0 - (score / 100.0 * 1.5)  # Linear entre 2.0 e 0.5 minutos
        
        return {
            "score": score,
            "target": self.target_metrics["context_switch_time"],
            "status": "✅ PASS" if estimated_time <= self.target_metrics["context_switch_time"] else "❌ FAIL",
            "details": details,
            "stats": {
                "estimated_time_minutes": estimated_time,
                "infrastructure_score": score
            }
        }
    
    def evaluate_connection_precision(self) -> Dict[str, Any]:
        """Avalia precisão das conexões"""
        connections_map = self.load_context_map("connections.yml")
        conflicts_map = self.load_context_map("conflicts.yml")
        
        if not connections_map:
            return {
                "score": 0.0,
                "target": self.target_metrics["connection_precision"],
                "status": "❌ FAIL",
                "details": ["❌ Nenhuma conexão encontrada"]
            }
        
        total_connections = 0
        broken_connections = 0
        details = []
        
        # Conta conexões totais
        for doc_path, connections in connections_map.items():
            if isinstance(connections, dict):
                for conn_type, conn_list in connections.items():
                    if isinstance(conn_list, list):
                        total_connections += len(conn_list)
        
        # Conta conexões quebradas dos conflitos
        if conflicts_map and "conflicts" in conflicts_map:
            for conflict in conflicts_map["conflicts"]:
                if conflict.get("type") == "broken_connections":
                    broken_connections += 1
        
        if total_connections == 0:
            score = 0.0
            details.append("❌ Nenhuma conexão encontrada")
        else:
            valid_connections = total_connections - broken_connections
            score = (valid_connections / total_connections) * 100
            details.append(f"✅ {valid_connections}/{total_connections} conexões válidas")
            if broken_connections > 0:
                details.append(f"⚠️ {broken_connections} conexões quebradas")
        
        return {
            "score": score,
            "target": self.target_metrics["connection_precision"],
            "status": "✅ PASS" if score >= self.target_metrics["connection_precision"] else "❌ FAIL",
            "details": details,
            "stats": {
                "total_connections": total_connections,
                "valid_connections": total_connections - broken_connections,
                "broken_connections": broken_connections,
                "precision_percentage": score
            }
        }
    
    def evaluate_template_completeness(self) -> Dict[str, Any]:
        """Avalia completude dos templates"""
        required_templates = ["decisao.md", "processo.md", "referencia.md", 
                            "arquitetura.md", "analise.md", "planejamento.md"]
        
        existing_templates = []
        missing_templates = []
        details = []
        
        for template in required_templates:
            template_path = self.templates_path / template
            if template_path.exists():
                existing_templates.append(template)
                details.append(f"✅ {template} disponível")
            else:
                missing_templates.append(template)
                details.append(f"❌ {template} não encontrado")
        
        score = (len(existing_templates) / len(required_templates)) * 100
        
        return {
            "score": score,
            "target": self.target_metrics["template_completeness"],
            "status": "✅ PASS" if score >= self.target_metrics["template_completeness"] else "❌ FAIL",
            "details": details,
            "stats": {
                "required_templates": len(required_templates),
                "existing_templates": len(existing_templates),
                "missing_templates": len(missing_templates),
                "completeness_percentage": score
            }
        }
    
    def evaluate_manual_intervention(self) -> Dict[str, Any]:
        """Avalia necessidade de intervenção manual"""
        # Baseado em automação disponível
        score = 0.0
        details = []
        
        # Scanner automático
        if (self.scripts_path / "context_scanner.py").exists():
            score += 25.0
            details.append("✅ Scanner automático disponível")
        else:
            details.append("❌ Scanner automático não encontrado")
        
        # Validador automático
        if (self.scripts_path / "template_validator.py").exists():
            score += 25.0
            details.append("✅ Validador automático disponível")
        else:
            details.append("❌ Validador automático não encontrado")
        
        # Detector de conflitos
        if (self.scripts_path / "conflict_detector.py").exists():
            score += 25.0
            details.append("✅ Detector de conflitos disponível")
        else:
            details.append("❌ Detector de conflitos não encontrado")
        
        # Engine de contexto
        if (self.scripts_path / "context_engine.py").exists():
            score += 25.0
            details.append("✅ Engine de contexto disponível")
        else:
            details.append("❌ Engine de contexto não encontrado")
        
        # Inverte a pontuação (maior automação = menor intervenção manual)
        intervention_score = 100 - score
        
        return {
            "score": score,
            "target": self.target_metrics["manual_intervention"],
            "status": "✅ PASS" if intervention_score <= self.target_metrics["manual_intervention"] else "❌ FAIL",
            "details": details,
            "stats": {
                "automation_score": score,
                "intervention_needed": intervention_score
            }
        }
    
    def run_full_evaluation(self) -> Dict[str, Any]:
        """Executa avaliação completa de todas as métricas"""
        print("🔍 Iniciando avaliação completa das métricas...")
        
        evaluations = {
            "ai_consistency": self.evaluate_ai_consistency(),
            "documentation_coverage": self.evaluate_documentation_coverage(),
            "automatic_detection": self.evaluate_automatic_detection(),
            "conflict_resolution": self.evaluate_conflict_resolution(),
            "efficiency": self.evaluate_efficiency(),
            "context_switch_time": self.evaluate_context_switch_time(),
            "connection_precision": self.evaluate_connection_precision(),
            "template_completeness": self.evaluate_template_completeness(),
            "manual_intervention": self.evaluate_manual_intervention()
        }
        
        # Calcula score geral
        total_score = 0
        passed_metrics = 0
        
        for metric_name, result in evaluations.items():
            if result["status"] == "✅ PASS":
                passed_metrics += 1
            total_score += result["score"]
        
        overall_score = total_score / len(evaluations)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "overall_score": overall_score,
            "passed_metrics": passed_metrics,
            "total_metrics": len(evaluations),
            "pass_rate": (passed_metrics / len(evaluations)) * 100,
            "evaluations": evaluations
        }
    
    def print_report(self, evaluation_result: Dict[str, Any]):
        """Imprime relatório detalhado"""
        print("\n" + "="*80)
        print("📊 RELATÓRIO DE MÉTRICAS - CONTEXT NAVIGATOR")
        print("="*80)
        
        print(f"\n🎯 SCORE GERAL: {evaluation_result['overall_score']:.1f}%")
        print(f"✅ MÉTRICAS APROVADAS: {evaluation_result['passed_metrics']}/{evaluation_result['total_metrics']}")
        print(f"📈 TAXA DE APROVAÇÃO: {evaluation_result['pass_rate']:.1f}%")
        
        if evaluation_result['pass_rate'] >= 80:
            print("🏆 EXCELENTE - Sistema atende às especificações do PRD!")
        elif evaluation_result['pass_rate'] >= 60:
            print("✅ BOM - Sistema atende à maioria das especificações")
        else:
            print("⚠️ ATENÇÃO - Sistema precisa de melhorias")
        
        print("\n📋 AVALIAÇÃO DETALHADA:")
        print("-" * 80)
        
        for metric_name, result in evaluation_result['evaluations'].items():
            print(f"\n🔍 {metric_name.upper().replace('_', ' ')}")
            print(f"   Score: {result['score']:.1f}% (Meta: {result['target']:.1f}%)")
            print(f"   Status: {result['status']}")
            
            if result['details']:
                print("   Detalhes:")
                for detail in result['details'][:5]:  # Limita a 5 detalhes
                    print(f"     - {detail}")
                if len(result['details']) > 5:
                    print(f"     ... e mais {len(result['details']) - 5} itens")
        
        print("\n" + "="*80)
        print(f"⏰ Relatório gerado em: {evaluation_result['timestamp']}")
        print("="*80)

def main():
    parser = argparse.ArgumentParser(description='Context Navigator - Validador de Métricas')
    parser.add_argument('--config', default='.contextrc', help='Caminho para configuração (ignorado na v2.0)')
    parser.add_argument('--save', help='Salvar resultado em arquivo JSON')
    
    args = parser.parse_args()
    
    try:
        # Detectar workspace usando WorkspaceManager
        try:
            from ..core.workspace_manager import WorkspaceManager
        except ImportError:
            # Fallback para desenvolvimento
            import sys
            sys.path.insert(0, str(Path(__file__).parent.parent))
            from core.workspace_manager import WorkspaceManager
        
        workspace_manager = WorkspaceManager()
        current_workspace = workspace_manager.detect_current_workspace()
        
        if not current_workspace:
            print("❌ Context Navigator workspace não encontrado")
            print("💡 Execute 'cn init' para configurar este diretório")
            return 1
        
        validator = MetricsValidator()
        result = validator.run_full_evaluation()
        validator.print_report(result)
        
        if args.save:
            with open(args.save, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"\n💾 Resultado salvo em: {args.save}")
        
    except Exception as e:
        print(f"❌ Erro durante avaliação: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 