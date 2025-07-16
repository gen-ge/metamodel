#!/usr/bin/env python3
"""
Context Navigator - Context Advisor
Sistema de sugestões inteligente baseado em contexto
"""

import json
import yaml
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from collections import defaultdict
import re
import argparse

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('context_advisor')

@dataclass
class ContextualSuggestion:
    """Sugestão contextual avançada"""
    type: str  # 'template', 'connection', 'improvement', 'workflow', 'pattern'
    category: str  # 'urgent', 'recommended', 'optional', 'maintenance'
    title: str
    description: str
    rationale: str
    actions: List[str]
    confidence: float
    priority: int  # 1-5 (1 = mais prioritário)
    estimated_time: str
    related_documents: List[str]
    context_factors: List[str]

@dataclass
class WorkflowSuggestion:
    """Sugestão de fluxo de trabalho"""
    current_stage: str
    next_actions: List[str]
    prerequisites: List[str]
    expected_outcomes: List[str]
    timeline: str
    confidence: float

@dataclass
class PatternAnalysis:
    """Análise de padrões no projeto"""
    pattern_type: str
    description: str
    examples: List[str]
    implications: List[str]
    suggestions: List[str]
    confidence: float

class ContextAdvisor:
    """Sistema inteligente de sugestões baseado em contexto"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        
        self.document_cache = {}
        self.pattern_cache = {}
        
        # NOVO: Usar WorkspaceManager para detectar workspace
        self._init_with_workspace_manager()
        
        # Carregar dados necessários
        self._load_context_maps()
        self._load_document_cache()
        self._initialize_pattern_analysis()
        
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
            logger.error("❌ Context Navigator workspace não encontrado")
            logger.error("💡 Execute 'cn init' para configurar este diretório")
            sys.exit(1)
        
        # Configurar paths baseado no workspace
        self.workspace = current_workspace
        self.base_path = current_workspace.root_path
        self.output_dir = current_workspace.root_path / ".cn_model"
        
        # Configuração vem do workspace
        self.config = current_workspace.configuration
        self.context_maps = {}
        
        logger.info(f"🌐 Workspace: {current_workspace.name} ({current_workspace.root_path})")
        
    def _load_context_maps(self) -> None:
        """Carrega mapas de contexto gerados pelo scanner"""
        map_files = ['index.yml', 'architecture.yml', 'connections.yml', 'conflicts.yml']
        
        for map_file in map_files:
            map_path = self.output_dir / map_file
            if map_path.exists():
                try:
                    with open(map_path, 'r', encoding='utf-8') as f:
                        key = map_file.replace('.yml', '')
                        self.context_maps[key] = yaml.safe_load(f) or {}
                except Exception as e:
                    logger.error(f"Erro ao carregar {map_file}: {e}")
                    
    def _load_document_cache(self) -> None:
        """Carrega cache de documentos processados"""
        if not self.context_maps.get('index'):
            return
            
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        for doc_path, doc_info in document_summary.items():
            if not doc_info or not isinstance(doc_info, dict):
                continue
                
            try:
                full_path = self.base_path / doc_path
                if full_path.exists():
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    self.document_cache[doc_path] = {
                        'info': doc_info,
                        'content': content,
                        'size': len(content),
                        'word_count': len(content.split()),
                        'last_analyzed': datetime.now().isoformat()
                    }
            except Exception as e:
                logger.warning(f"Erro ao carregar documento {doc_path}: {e}")
                
    def _initialize_pattern_analysis(self) -> None:
        """Inicializa análise de padrões"""
        self.pattern_cache = {
            'workflow_patterns': self._analyze_workflow_patterns(),
            'quality_patterns': self._analyze_quality_patterns(),
            'usage_patterns': self._analyze_usage_patterns(),
            'connection_patterns': self._analyze_connection_patterns()
        }
        
    def _analyze_workflow_patterns(self) -> Dict[str, Any]:
        """Analisa padrões de fluxo de trabalho"""
        patterns = {
            'common_sequences': [],
            'bottlenecks': [],
            'optimization_opportunities': []
        }
        
        if not self.context_maps.get('index'):
            return patterns
            
        # Analisar sequências comuns baseado em tipos de documento
        doc_types = self.context_maps['index'].get('type_distribution', {})
        
        # Detectar padrões de desenvolvimento
        if doc_types.get('decision', 0) > 0 and doc_types.get('architecture', 0) == 0:
            patterns['optimization_opportunities'].append({
                'type': 'missing_architecture',
                'description': 'Muitas decisões sem documentação arquitetural',
                'suggestion': 'Considerar criar documentos de arquitetura'
            })
            
        if doc_types.get('process', 0) > 0 and doc_types.get('reference', 0) == 0:
            patterns['optimization_opportunities'].append({
                'type': 'missing_reference',
                'description': 'Processos definidos sem documentação de referência',
                'suggestion': 'Criar documentação de referência para APIs/componentes'
            })
            
        return patterns
        
    def _analyze_quality_patterns(self) -> Dict[str, Any]:
        """Analisa padrões de qualidade"""
        patterns = {
            'quality_trends': [],
            'improvement_areas': [],
            'best_practices': []
        }
        
        if not self.context_maps.get('index'):
            return patterns
            
        # Analisar taxa de erros por tipo de documento
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        error_by_type = defaultdict(list)
        for doc_path, doc_info in document_summary.items():
            if not doc_info or not isinstance(doc_info, dict):
                continue
                
            if doc_info.get('has_errors', False):
                doc_type = doc_info.get('type', 'unknown')
                error_by_type[doc_type].append(doc_path)
                
        for doc_type, error_docs in error_by_type.items():
            if len(error_docs) > 1:
                patterns['improvement_areas'].append({
                    'type': f'recurring_errors_{doc_type}',
                    'description': f'Erros recorrentes em documentos {doc_type}',
                    'affected_documents': error_docs,
                    'suggestion': f'Revisar template {doc_type} ou processo de criação'
                })
                
        return patterns
        
    def _analyze_usage_patterns(self) -> Dict[str, Any]:
        """Analisa padrões de uso"""
        patterns = {
            'underutilized_templates': [],
            'overutilized_templates': [],
            'context_distribution': {}
        }
        
        if not self.context_maps.get('index'):
            return patterns
            
        # Analisar distribuição de tipos
        type_distribution = self.context_maps['index'].get('type_distribution', {})
        total_docs = sum(type_distribution.values())
        
        if total_docs > 0:
            expected_distribution = {
                'decision': 0.4,  # 40% esperado
                'process': 0.2,   # 20% esperado
                'reference': 0.15, # 15% esperado
                'architecture': 0.1, # 10% esperado
                'analysis': 0.1,   # 10% esperado
                'planning': 0.05   # 5% esperado
            }
            
            for doc_type, expected_ratio in expected_distribution.items():
                actual_count = type_distribution.get(doc_type, 0)
                actual_ratio = actual_count / total_docs
                
                if actual_ratio < expected_ratio * 0.5:  # Menos que 50% do esperado
                    patterns['underutilized_templates'].append({
                        'type': doc_type,
                        'expected_ratio': expected_ratio,
                        'actual_ratio': actual_ratio,
                        'suggestion': f'Considerar criar mais documentos {doc_type}'
                    })
                elif actual_ratio > expected_ratio * 2:  # Mais que 200% do esperado
                    patterns['overutilized_templates'].append({
                        'type': doc_type,
                        'expected_ratio': expected_ratio,
                        'actual_ratio': actual_ratio,
                        'suggestion': f'Avaliar se alguns documentos {doc_type} podem ser simplificados'
                    })
                    
        return patterns
        
    def _analyze_connection_patterns(self) -> Dict[str, Any]:
        """Analisa padrões de conexão"""
        patterns = {
            'isolated_clusters': [],
            'over_connected': [],
            'weak_connections': []
        }
        
        if not self.context_maps.get('connections'):
            return patterns
            
        connections_data = self.context_maps['connections']
        
        # Documentos isolados
        isolated = connections_data.get('isolated_components', [])
        if len(isolated) > 0:
            patterns['isolated_clusters'] = [{
                'documents': isolated,
                'count': len(isolated),
                'suggestion': 'Revisar e mapear conexões com outros documentos'
            }]
            
        # Documentos super conectados
        strong_coupling = connections_data.get('strong_coupling', [])
        if len(strong_coupling) > 0:
            patterns['over_connected'] = [{
                'documents': [doc['document'] for doc in strong_coupling],
                'suggestion': 'Avaliar se algumas conexões podem ser simplificadas'
            }]
            
        return patterns
        
    def generate_contextual_suggestions(self) -> List[ContextualSuggestion]:
        """Gera sugestões contextuais baseadas em análise completa"""
        suggestions = []
        
        # Sugestões baseadas em padrões de workflow
        suggestions.extend(self._generate_workflow_suggestions())
        
        # Sugestões baseadas em qualidade
        suggestions.extend(self._generate_quality_suggestions())
        
        # Sugestões baseadas em uso
        suggestions.extend(self._generate_usage_suggestions())
        
        # Sugestões baseadas em conexões
        suggestions.extend(self._generate_connection_suggestions())
        
        # Sugestões baseadas em contexto atual
        suggestions.extend(self._generate_context_suggestions())
        
        # Ordenar por prioridade e confiança
        suggestions.sort(key=lambda x: (x.priority, -x.confidence))
        
        return suggestions
        
    def _generate_workflow_suggestions(self) -> List[ContextualSuggestion]:
        """Gera sugestões de fluxo de trabalho"""
        suggestions = []
        workflow_patterns = self.pattern_cache['workflow_patterns']
        
        for opportunity in workflow_patterns.get('optimization_opportunities', []):
            if opportunity['type'] == 'missing_architecture':
                suggestions.append(ContextualSuggestion(
                    type='workflow',
                    category='recommended',
                    title='Documentação Arquitetural Faltando',
                    description='Projeto tem decisões técnicas mas carece de documentação arquitetural',
                    rationale='Decisões técnicas são mais efetivas quando suportadas por documentação arquitetural clara',
                    actions=[
                        'Criar documento de arquitetura usando template ARQUITETURA',
                        'Mapear componentes e suas interações',
                        'Conectar com decisões técnicas existentes'
                    ],
                    confidence=0.8,
                    priority=2,
                    estimated_time='2-4 horas',
                    related_documents=[],
                    context_factors=['missing_architecture_docs', 'existing_decisions']
                ))
                
        return suggestions
        
    def _generate_quality_suggestions(self) -> List[ContextualSuggestion]:
        """Gera sugestões de qualidade"""
        suggestions = []
        quality_patterns = self.pattern_cache['quality_patterns']
        
        for improvement in quality_patterns.get('improvement_areas', []):
            if improvement['type'].startswith('recurring_errors_'):
                doc_type = improvement['type'].replace('recurring_errors_', '')
                suggestions.append(ContextualSuggestion(
                    type='improvement',
                    category='urgent',
                    title=f'Erros Recorrentes em {doc_type.upper()}',
                    description=f'Múltiplos documentos {doc_type} têm erros de validação',
                    rationale='Erros recorrentes indicam problemas sistemáticos no processo',
                    actions=[
                        f'Revisar template {doc_type}',
                        'Validar documentos existentes',
                        'Atualizar processo de criação'
                    ],
                    confidence=0.9,
                    priority=1,
                    estimated_time='1-2 horas',
                    related_documents=improvement['affected_documents'],
                    context_factors=['recurring_errors', 'quality_issues']
                ))
                
        return suggestions
        
    def _generate_usage_suggestions(self) -> List[ContextualSuggestion]:
        """Gera sugestões de uso"""
        suggestions = []
        usage_patterns = self.pattern_cache['usage_patterns']
        
        for underutilized in usage_patterns.get('underutilized_templates', []):
            suggestions.append(ContextualSuggestion(
                type='template',
                category='optional',
                title=f'Template {underutilized["type"].upper()} Subutilizado',
                description=f'Template {underutilized["type"]} está sendo usado abaixo do esperado',
                rationale=f'Uso balanceado de templates melhora cobertura documental',
                actions=[
                    f'Identificar oportunidades para documentos {underutilized["type"]}',
                    'Revisar se outros tipos podem ser convertidos',
                    'Considerar necessidade real deste tipo'
                ],
                confidence=0.6,
                priority=4,
                estimated_time='30 minutos',
                related_documents=[],
                context_factors=['underutilized_template', 'usage_patterns']
            ))
            
        return suggestions
        
    def _generate_connection_suggestions(self) -> List[ContextualSuggestion]:
        """Gera sugestões de conexão"""
        suggestions = []
        connection_patterns = self.pattern_cache['connection_patterns']
        
        for cluster in connection_patterns.get('isolated_clusters', []):
            if cluster['count'] > 2:
                suggestions.append(ContextualSuggestion(
                    type='connection',
                    category='recommended',
                    title='Documentos Isolados Detectados',
                    description=f'{cluster["count"]} documentos não têm conexões mapeadas',
                    rationale='Documentos isolados reduzem navegabilidade e contexto',
                    actions=[
                        'Revisar documentos isolados',
                        'Mapear relacionamentos existentes',
                        'Conectar com documentos relacionados'
                    ],
                    confidence=0.7,
                    priority=3,
                    estimated_time='1 hora',
                    related_documents=cluster['documents'],
                    context_factors=['isolated_documents', 'connection_gaps']
                ))
                
        return suggestions
        
    def _generate_context_suggestions(self) -> List[ContextualSuggestion]:
        """Gera sugestões baseadas em contexto atual"""
        suggestions = []
        
        if not self.context_maps.get('index'):
            return suggestions
            
        # Analisar contexto atual do projeto
        scan_info = self.context_maps['index'].get('scan_info', {})
        total_docs = scan_info.get('total_documents', 0)
        
        if total_docs < 5:
            suggestions.append(ContextualSuggestion(
                type='workflow',
                category='recommended',
                title='Projeto Precisa de Mais Documentação',
                description='Projeto tem pouca documentação estruturada',
                rationale='Documentação adequada melhora manutenibilidade e colaboração',
                actions=[
                    'Identificar áreas não documentadas',
                    'Criar documentos fundamentais (ADRs, processos)',
                    'Estabelecer rotina de documentação'
                ],
                confidence=0.8,
                priority=2,
                estimated_time='2-3 horas',
                related_documents=[],
                context_factors=['low_doc_count', 'project_setup']
            ))
            
        return suggestions
        
    def suggest_next_actions(self) -> WorkflowSuggestion:
        """Sugere próximas ações baseadas no estado atual"""
        if not self.context_maps.get('index'):
            return WorkflowSuggestion(
                current_stage='setup',
                next_actions=['Executar context scanner', 'Criar documentos iniciais'],
                prerequisites=['Configurar .contextrc'],
                expected_outcomes=['Mapas de contexto gerados'],
                timeline='30 minutos',
                confidence=0.9
            )
            
        scan_info = self.context_maps['index'].get('scan_info', {})
        total_docs = scan_info.get('total_documents', 0)
        validation_errors = scan_info.get('validation_errors', 0)
        
        if validation_errors > 0:
            return WorkflowSuggestion(
                current_stage='validation',
                next_actions=[
                    'Corrigir erros de validação',
                    'Executar template validator',
                    'Atualizar documentos não conformes'
                ],
                prerequisites=['Identificar documentos com erros'],
                expected_outcomes=['Documentos válidos', 'Qualidade melhorada'],
                timeline='1-2 horas',
                confidence=0.8
            )
            
        if total_docs < 10:
            return WorkflowSuggestion(
                current_stage='expansion',
                next_actions=[
                    'Criar documentos fundamentais',
                    'Mapear conexões entre documentos',
                    'Estabelecer rotina de documentação'
                ],
                prerequisites=['Templates disponíveis'],
                expected_outcomes=['Cobertura documental adequada'],
                timeline='2-4 horas',
                confidence=0.7
            )
            
        return WorkflowSuggestion(
            current_stage='maintenance',
            next_actions=[
                'Revisar documentos desatualizados',
                'Otimizar conexões',
                'Monitorar qualidade'
            ],
            prerequisites=['Documentação estabelecida'],
            expected_outcomes=['Documentação atualizada e consistente'],
            timeline='1 hora/semana',
            confidence=0.9
        )
        
    def analyze_project_health(self) -> Dict[str, Any]:
        """Analisa saúde geral do projeto"""
        health = {
            'score': 0.0,
            'areas': {
                'documentation_coverage': 0.0,
                'quality_consistency': 0.0,
                'connection_completeness': 0.0,
                'maintenance_status': 0.0
            },
            'recommendations': [],
            'critical_issues': []
        }
        
        if not self.context_maps.get('index'):
            health['critical_issues'].append('Context maps não encontrados - execute scanner')
            return health
            
        scan_info = self.context_maps['index'].get('scan_info', {})
        total_docs = scan_info.get('total_documents', 0)
        validation_errors = scan_info.get('validation_errors', 0)
        
        # Cobertura documental
        if total_docs >= 10:
            health['areas']['documentation_coverage'] = 1.0
        elif total_docs >= 5:
            health['areas']['documentation_coverage'] = 0.7
        else:
            health['areas']['documentation_coverage'] = total_docs / 10.0
            
        # Consistência de qualidade
        if validation_errors == 0:
            health['areas']['quality_consistency'] = 1.0
        else:
            error_rate = validation_errors / total_docs if total_docs > 0 else 1.0
            health['areas']['quality_consistency'] = max(0.0, 1.0 - error_rate)
            
        # Completude de conexões
        if self.context_maps.get('connections'):
            isolated_count = len(self.context_maps['connections'].get('isolated_components', []))
            if isolated_count == 0:
                health['areas']['connection_completeness'] = 1.0
            else:
                isolated_rate = isolated_count / total_docs if total_docs > 0 else 1.0
                health['areas']['connection_completeness'] = max(0.0, 1.0 - isolated_rate)
                
        # Status de manutenção (baseado em datas de atualização)
        health['areas']['maintenance_status'] = 0.8  # Valor padrão
        
        # Score geral
        health['score'] = sum(health['areas'].values()) / len(health['areas'])
        
        # Recomendações baseadas em score
        if health['score'] < 0.5:
            health['recommendations'].append('Projeto precisa de atenção urgente na documentação')
        elif health['score'] < 0.8:
            health['recommendations'].append('Projeto está no caminho certo, mas pode melhorar')
        else:
            health['recommendations'].append('Projeto tem documentação saudável')
            
        return health

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(description='Context Navigator Advisor')
    parser.add_argument('--path', '-p', default='.', help='Caminho base do projeto')
    parser.add_argument('--suggestions', '-s', action='store_true', help='Mostrar sugestões contextuais')
    parser.add_argument('--workflow', '-w', action='store_true', help='Mostrar sugestões de workflow')
    parser.add_argument('--health', action='store_true', help='Analisar saúde do projeto')
    parser.add_argument('--all', '-a', action='store_true', help='Mostrar todas as análises')
    
    args = parser.parse_args()
    
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
    
    advisor = ContextAdvisor()
    
    if args.suggestions or args.all:
        print("\n=== SUGESTÕES CONTEXTUAIS ===")
        suggestions = advisor.generate_contextual_suggestions()
        
        if not suggestions:
            print("Nenhuma sugestão específica no momento.")
        else:
            for i, suggestion in enumerate(suggestions[:10], 1):  # Top 10
                print(f"\n{i}. {suggestion.title}")
                print(f"   Categoria: {suggestion.category}")
                print(f"   Tipo: {suggestion.type}")
                print(f"   Descrição: {suggestion.description}")
                print(f"   Confiança: {suggestion.confidence:.1%}")
                print(f"   Prioridade: {suggestion.priority}/5")
                print(f"   Tempo estimado: {suggestion.estimated_time}")
                print(f"   Ações:")
                for action in suggestion.actions:
                    print(f"     - {action}")
                    
    if args.workflow or args.all:
        print("\n=== SUGESTÕES DE WORKFLOW ===")
        workflow = advisor.suggest_next_actions()
        print(f"Estágio atual: {workflow.current_stage}")
        print(f"Próximas ações:")
        for action in workflow.next_actions:
            print(f"  - {action}")
        print(f"Pré-requisitos: {', '.join(workflow.prerequisites)}")
        print(f"Resultados esperados: {', '.join(workflow.expected_outcomes)}")
        print(f"Timeline: {workflow.timeline}")
        print(f"Confiança: {workflow.confidence:.1%}")
        
    if args.health or args.all:
        print("\n=== ANÁLISE DE SAÚDE DO PROJETO ===")
        health = advisor.analyze_project_health()
        print(f"Score geral: {health['score']:.1%}")
        
        print("\nÁreas avaliadas:")
        for area, score in health['areas'].items():
            print(f"  {area}: {score:.1%}")
            
        if health['recommendations']:
            print("\nRecomendações:")
            for rec in health['recommendations']:
                print(f"  - {rec}")
                
        if health['critical_issues']:
            print("\nProblemas críticos:")
            for issue in health['critical_issues']:
                print(f"  ❌ {issue}")

if __name__ == '__main__':
    main() 