#!/usr/bin/env python3

# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component context-engine
# @cn:doc context-engine.md
# @cn:context-level c3_component
# @cn:context-type core
# @cn:parent-module cli-interface
# @cn:purpose "Motor principal de processamento contextual - automatiza decisões sobre templates e contextos"
# @cn:memory-aid "Coração do sistema - analisa conteúdo, recomenda templates, sugere conexões e melhorias"
# @cn:depends-on context.rule, CONVENTIONS.md, template-definitions
# @cn:impacts template-validation, document-processing, user-guidance
# @cn:provides content-analysis, template-recommendation, context-suggestion, improvement-suggestions
# @cn:component-type functional
# @cn:responsibility context-processing
# @cn:single-purpose true
# @cn:complexity critical
# @cn:owner Context Navigator Team
# @cn:last-updated 2025-01-13
# ============================================

"""
Context Navigator - Context Engine
Engine metodológica inteligente que automatiza decisões sobre templates, 
contextos e sugere melhorias baseado na análise de documentos.
"""

import os
import sys
import yaml
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('context_engine')

# @cn:class business-entity
# @cn:responsibility data-structure
# @cn:purpose "Estrutura de dados para resultado de análise de conteúdo"
@dataclass
class ContentAnalysis:
    """Resultado da análise de conteúdo"""
    keywords: List[str]
    entities: List[str]
    complexity_score: float
    purpose: str
    domain: str
    confidence: float

# @cn:class business-entity
# @cn:responsibility data-structure
# @cn:purpose "Estrutura de dados para recomendação de template"
@dataclass
class TemplateRecommendation:
    """Recomendação de template"""
    template_type: str
    confidence: float
    reasoning: str
    alternative_templates: List[str]

# @cn:class business-entity
# @cn:responsibility data-structure
# @cn:purpose "Estrutura de dados para recomendação de contexto"
@dataclass
class ContextRecommendation:
    """Recomendação de contexto"""
    context_level: str
    context_type: str
    confidence: float
    reasoning: str
    suggested_module: str

@dataclass
class ConnectionSuggestion:
    """Sugestão de conexão"""
    target_document: str
    connection_type: str
    confidence: float
    reasoning: str

@dataclass
class ImprovementSuggestion:
    """Sugestão de melhoria"""
    type: str
    description: str
    priority: str
    action: str

# @cn:class service
# @cn:responsibility context-processing
# @cn:pattern singleton
# @cn:lifecycle singleton
# @cn:purpose "Serviço principal que analisa conteúdo e recomenda templates/contextos"
class ContextEngine:
    """Engine metodológica inteligente do Context Navigator"""
    
    # @cn:function core
    # @cn:process initialization
    # @cn:step 1
    def __init__(self, base_path: str = "."):
        """
        Inicializa a engine
        
        Args:
            base_path: Caminho base do projeto
        """
        self.base_path = Path(base_path)
        self.config = {}
        self.documents = {}
        self.context_maps = {}
        
        # NOVO: Usar WorkspaceManager para detectar workspace
        self._init_with_workspace_manager()
        
        # Carregar dados de contexto
        self._load_context_maps()
        
        # Padrões para análise de conteúdo
        self._init_content_patterns()
        
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
        
        logger.info(f"🌐 Workspace: {current_workspace.name} ({current_workspace.root_path})")
        
    # @cn:function integration
    # @cn:process configuration-loading
    # @cn:step 2
    # @cn:file-dependency .contextrc
    # @cn:error-handling required

            
    # @cn:function integration
    # @cn:process context-maps-loading
    # @cn:step 3
    # @cn:directory-dependency .context-map/
    # @cn:depends-on configuration
    def _load_context_maps(self) -> None:
        """Carrega mapas de contexto existentes"""
        # Usar arquitetura workspace: mapas ficam em .cn_model/
        context_maps_path = self.output_dir
        map_files = ['index.yml', 'component-map.yml', 'context-map/index.yml']
        
        if not context_maps_path.exists():
            logger.warning("Mapas de contexto não encontrados")
            return
            
        # Carregar mapas principais
        for map_file in map_files:
            file_path = context_maps_path / map_file
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        map_name = map_file.replace('.yml', '')
                        self.context_maps[map_name] = yaml.safe_load(f)
                    logger.debug(f"Mapa carregado: {map_file}")
                except Exception as e:
                    logger.warning(f"Erro ao carregar {map_file}: {e}")
                    
    def _init_content_patterns(self) -> None:
        """Inicializa padrões para análise de conteúdo"""
        # Padrões para detecção de tipo de documento
        self.template_patterns = {
            'decision': {
                'keywords': ['decisão', 'escolha', 'opção', 'alternativa', 'pros', 'contras', 'justificativa', 'trade-off'],
                'structures': ['problema', 'análise', 'opções', 'decisão', 'consequências'],
                'entities': ['ADR', 'RFC', 'PRD', 'escolha técnica']
            },
            'process': {
                'keywords': ['processo', 'procedimento', 'passo', 'tutorial', 'guia', 'runbook', 'playbook'],
                'structures': ['objetivo', 'pré-requisitos', 'passos', 'validação', 'troubleshooting'],
                'entities': ['comando', 'execução', 'verificação', 'teste']
            },
            'reference': {
                'keywords': ['referência', 'API', 'documentação', 'especificação', 'endpoint', 'parâmetro'],
                'structures': ['overview', 'referência', 'exemplos', 'recursos'],
                'entities': ['GET', 'POST', 'PUT', 'DELETE', 'HTTP', 'JSON', 'endpoint']
            },
            'architecture': {
                'keywords': ['arquitetura', 'design', 'componente', 'sistema', 'padrão', 'estrutura'],
                'structures': ['contexto', 'componentes', 'fluxos', 'decisões', 'evolução'],
                'entities': ['microservice', 'database', 'cache', 'queue', 'service']
            },
            'analysis': {
                'keywords': ['análise', 'investigação', 'performance', 'bug', 'métrica', 'dados'],
                'structures': ['situação', 'análise', 'descobertas', 'ações', 'acompanhamento'],
                'entities': ['CPU', 'memória', 'latência', 'throughput', 'erro']
            },
            'planning': {
                'keywords': ['planejamento', 'roadmap', 'sprint', 'release', 'cronograma', 'marco'],
                'structures': ['objetivos', 'escopo', 'cronograma', 'riscos', 'métricas'],
                'entities': ['milestone', 'deadline', 'resource', 'budget', 'timeline']
            }
        }
        
        # Padrões para detecção de contexto
        self.context_patterns = {
            'infra': ['deploy', 'infrastructure', 'docker', 'kubernetes', 'aws', 'cloud'],
            'shared': ['utils', 'common', 'library', 'helper', 'shared', 'util'],
            'core': ['business', 'domain', 'logic', 'service', 'entity', 'model'],
            'api': ['endpoint', 'controller', 'route', 'rest', 'graphql', 'api'],
            'data': ['database', 'repository', 'model', 'migration', 'schema', 'query'],
            'ui': ['component', 'view', 'page', 'interface', 'frontend', 'react']
        }
        
    def analyze_content(self, content: str) -> ContentAnalysis:
        """
        Analisa conteúdo de texto para extrair características
        
        Args:
            content: Conteúdo a ser analisado
            
        Returns:
            Análise do conteúdo
        """
        content_lower = content.lower()
        
        # Extrair palavras-chave
        keywords = []
        for template_type, patterns in self.template_patterns.items():
            for keyword in patterns['keywords']:
                if keyword in content_lower:
                    keywords.append(keyword)
                    
        # Extrair entidades técnicas
        entities = []
        for template_type, patterns in self.template_patterns.items():
            for entity in patterns['entities']:
                if entity.lower() in content_lower:
                    entities.append(entity)
                    
        # Calcular score de complexidade baseado em indicadores
        complexity_indicators = [
            len(re.findall(r'```', content)),  # Blocos de código
            len(re.findall(r'\|.*\|', content)),  # Tabelas
            len(re.findall(r'- \[', content)),  # Checklists
            len(re.findall(r'#{1,6}', content)),  # Headers
            content.count('http'),  # URLs
            content.count('@'),  # Referências
        ]
        complexity_score = sum(complexity_indicators) / 100.0
        complexity_score = min(complexity_score, 1.0)
        
        # Determinar propósito principal
        purpose_scores = {}
        for template_type, patterns in self.template_patterns.items():
            score = 0
            for keyword in patterns['keywords']:
                score += content_lower.count(keyword)
            for entity in patterns['entities']:
                score += content_lower.count(entity.lower())
            purpose_scores[template_type] = score
            
        purpose = max(purpose_scores.keys(), key=lambda x: purpose_scores[x]) if purpose_scores else 'unknown'
        confidence = purpose_scores.get(purpose, 0) / 10.0
        confidence = min(confidence, 1.0)
        
        # Determinar domínio
        domain_scores = {}
        for context_type, keywords in self.context_patterns.items():
            score = sum(content_lower.count(keyword) for keyword in keywords)
            domain_scores[context_type] = score
            
        domain = max(domain_scores.keys(), key=lambda x: domain_scores[x]) if domain_scores else 'core'
        
        return ContentAnalysis(
            keywords=keywords[:10],  # Top 10 keywords
            entities=entities[:10],  # Top 10 entities
            complexity_score=complexity_score,
            purpose=purpose,
            domain=domain,
            confidence=confidence
        )
        
    def recommend_template(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> TemplateRecommendation:
        """
        Recomenda template baseado no conteúdo
        
        Args:
            content: Conteúdo do documento
            metadata: Metadados existentes (opcional)
            
        Returns:
            Recomendação de template
        """
        analysis = self.analyze_content(content)
        
        # Se já tem doc_type nos metadados, validar
        if metadata and 'doc_type' in metadata:
            existing_type = metadata['doc_type']
            if existing_type in self.template_patterns:
                return TemplateRecommendation(
                    template_type=existing_type,
                    confidence=0.9,
                    reasoning=f"Tipo já definido nos metadados: {existing_type}",
                    alternative_templates=[]
                )
                
        # Calcular scores para cada template
        template_scores = {}
        
        for template_type, patterns in self.template_patterns.items():
            score = 0
            
            # Score baseado em keywords
            keyword_score = 0
            for keyword in patterns['keywords']:
                keyword_score += content.lower().count(keyword)
            score += keyword_score * 2
            
            # Score baseado em entidades
            entity_score = 0
            for entity in patterns['entities']:
                entity_score += content.lower().count(entity.lower())
            score += entity_score * 3
            
            # Score baseado em estruturas (headers)
            structure_score = 0
            for structure in patterns['structures']:
                if structure in content.lower():
                    structure_score += 1
            score += structure_score * 5
            
            template_scores[template_type] = score
            
        # Ordenar por score
        sorted_templates = sorted(template_scores.items(), key=lambda x: x[1], reverse=True)
        
        if not sorted_templates or sorted_templates[0][1] == 0:
            return TemplateRecommendation(
                template_type='decision',  # Default
                confidence=0.3,
                reasoning="Não foi possível determinar tipo específico, usando padrão DECISÃO",
                alternative_templates=['process', 'reference']
            )
            
        best_template = sorted_templates[0][0]
        best_score = sorted_templates[0][1]
        
        # Calcular confiança baseado no score
        confidence = min(best_score / 10.0, 1.0)
        
        # Templates alternativos
        alternatives = [t[0] for t in sorted_templates[1:3] if t[1] > 0]
        
        # Reasoning
        reasoning = f"Análise de conteúdo indica tipo {best_template.upper()} "
        reasoning += f"(score: {best_score}, keywords: {len(analysis.keywords)}, "
        reasoning += f"entities: {len(analysis.entities)})"
        
        return TemplateRecommendation(
            template_type=best_template,
            confidence=confidence,
            reasoning=reasoning,
            alternative_templates=alternatives
        )
        
    def recommend_context(self, content: str, file_path: str, metadata: Optional[Dict[str, Any]] = None) -> ContextRecommendation:
        """
        Recomenda contexto baseado no conteúdo e localização
        
        Args:
            content: Conteúdo do documento
            file_path: Caminho do arquivo
            metadata: Metadados existentes
            
        Returns:
            Recomendação de contexto
        """
        analysis = self.analyze_content(content)
        
        # Analisar path para determinar context_level
        path_parts = Path(file_path).parts
        
        context_level = 'c2_module'  # Default
        if len(path_parts) <= 2:
            context_level = 'c1_root'
        elif len(path_parts) >= 4:
            context_level = 'c3_component'
            
        # Determinar context_type baseado em análise de conteúdo
        context_type = analysis.domain
        
        # Sugerir módulo baseado no path e conteúdo
        suggested_module = 'unknown'
        if len(path_parts) >= 2:
            suggested_module = path_parts[-2]  # Pasta pai
            
        # Se há metadados, validar consistência
        confidence = 0.7
        reasoning = f"Baseado em análise de conteúdo (domínio: {analysis.domain}) e estrutura de path"
        
        if metadata:
            if 'context_level' in metadata and metadata['context_level'] != context_level:
                confidence -= 0.2
                reasoning += f". ATENÇÃO: Conflito com metadados existentes ({metadata['context_level']})"
                
        return ContextRecommendation(
            context_level=context_level,
            context_type=context_type,
            confidence=confidence,
            reasoning=reasoning,
            suggested_module=suggested_module
        )
        
    def suggest_connections(self, content: str, metadata: Dict[str, Any]) -> List[ConnectionSuggestion]:
        """
        Sugere conexões com outros documentos
        
        Args:
            content: Conteúdo do documento
            metadata: Metadados do documento
            
        Returns:
            Lista de sugestões de conexão
        """
        suggestions = []
        
        if not self.context_maps.get('index'):
            return suggestions
            
        current_module = metadata.get('module', '')
        current_context_type = metadata.get('context_type', '')
        current_doc_type = metadata.get('doc_type', '')
        
        # Buscar documentos relacionados nos context maps
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        for doc_path, doc_info in document_summary.items():
            if doc_path == metadata.get('path', ''):
                continue  # Skip self
                
            # Verificar se doc_info é válido
            if not doc_info or not isinstance(doc_info, dict):
                continue
                
            connection_score = 0
            connection_type = 'relates_to'
            reasoning_parts = []
            
            # Mesmo módulo = conexão mais forte
            if doc_info.get('module') == current_module:
                connection_score += 3
                reasoning_parts.append('mesmo módulo')
                
            # Mesmo context_type = conexão média
            if doc_info.get('context_type') == current_context_type:
                connection_score += 2
                reasoning_parts.append('mesmo contexto')
                
            # Padrões específicos de dependência
            if current_doc_type == 'decision' and doc_info.get('type') == 'architecture':
                connection_score += 3
                connection_type = 'impacts'
                reasoning_parts.append('decisão impacta arquitetura')
                
            if current_doc_type == 'process' and doc_info.get('type') == 'reference':
                connection_score += 2
                connection_type = 'references'
                reasoning_parts.append('processo referencia documentação')
                
            if current_doc_type == 'analysis' and doc_info.get('type') == 'decision':
                connection_score += 3
                connection_type = 'impacts'
                reasoning_parts.append('análise pode gerar decisões')
                
            # Análise de conteúdo para referências implícitas
            doc_title = doc_info.get('title') or ''
            if doc_title:
                title_words = doc_title.lower().split()
                content_lower = content.lower()
                
                for word in title_words:
                    if len(word) > 3 and word in content_lower:
                        connection_score += 1
                        reasoning_parts.append(f"menciona '{word}'")
                        
            # Só sugerir se score >= 2
            if connection_score >= 2:
                confidence = min(connection_score / 5.0, 1.0)
                reasoning = "Sugestão baseada em: " + ", ".join(reasoning_parts)
                
                suggestions.append(ConnectionSuggestion(
                    target_document=doc_path,
                    connection_type=connection_type,
                    confidence=confidence,
                    reasoning=reasoning
                ))
                
        # Ordenar por confiança
        suggestions.sort(key=lambda x: x.confidence, reverse=True)
        
        return suggestions[:5]  # Top 5 sugestões
        
    def suggest_improvements(self, metadata: Dict[str, Any], content: str) -> List[ImprovementSuggestion]:
        """
        Sugere melhorias para o documento
        
        Args:
            metadata: Metadados do documento
            content: Conteúdo do documento
            
        Returns:
            Lista de sugestões de melhoria
        """
        suggestions = []
        
        # Verificar metadados obrigatórios
        required_fields = self.config.get('metadata', {}).get('required_fields', {})
        for field in required_fields:
            if field not in metadata or not metadata[field]:
                suggestions.append(ImprovementSuggestion(
                    type='metadata',
                    description=f"Campo obrigatório '{field}' não preenchido",
                    priority='high',
                    action=f"Adicionar valor para '{field}' nos metadados"
                ))
                
        # Verificar conexões vazias
        connections = metadata.get('connections', {})
        if isinstance(connections, dict):
            empty_connections = [k for k, v in connections.items() if not v]
            if len(empty_connections) == len(connections):
                suggestions.append(ImprovementSuggestion(
                    type='connections',
                    description="Documento não tem conexões mapeadas",
                    priority='medium',
                    action="Revisar e mapear relacionamentos com outros documentos"
                ))
                
        # Verificar qualidade do conteúdo
        analysis = self.analyze_content(content)
        
        if analysis.complexity_score < 0.1:
            suggestions.append(ImprovementSuggestion(
                type='content',
                description="Conteúdo parece muito simples ou incompleto",
                priority='medium',
                action="Adicionar mais detalhes, exemplos ou estrutura"
            ))
            
        if len(analysis.keywords) < 3:
            suggestions.append(ImprovementSuggestion(
                type='content',
                description="Poucos termos técnicos identificados",
                priority='low',
                action="Considerar adicionar mais contexto técnico específico"
            ))
            
        # Verificar data de atualização
        last_updated = metadata.get('last_updated')
        if last_updated:
            try:
                update_date = datetime.fromisoformat(last_updated)
                days_old = (datetime.now() - update_date).days
                if days_old > 90:
                    suggestions.append(ImprovementSuggestion(
                        type='maintenance',
                        description=f"Documento não atualizado há {days_old} dias",
                        priority='medium',
                        action="Revisar e atualizar informações se necessário"
                    ))
            except ValueError:
                suggestions.append(ImprovementSuggestion(
                    type='metadata',
                    description="Formato de data inválido em 'last_updated'",
                    priority='high',
                    action="Corrigir formato da data para YYYY-MM-DD"
                ))
                
        # Verificar se template está sendo usado corretamente
        template_rec = self.recommend_template(content, metadata)
        current_type = metadata.get('doc_type')
        
        if current_type and current_type != template_rec.template_type and template_rec.confidence > 0.7:
            suggestions.append(ImprovementSuggestion(
                type='template',
                description=f"Tipo '{current_type}' pode não ser ideal. Sugestão: '{template_rec.template_type}'",
                priority='medium',
                action=f"Considerar usar template {template_rec.template_type.upper()}"
            ))
            
        return suggestions
        
    def detect_patterns(self) -> Dict[str, Any]:
        """
        Detecta padrões nos documentos existentes
        
        Returns:
            Dicionário com padrões detectados
        """
        patterns = {
            'usage_patterns': {},
            'context_patterns': {},
            'connection_patterns': {},
            'quality_patterns': {}
        }
        
        if not self.context_maps.get('index'):
            return patterns
            
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        # Padrões de uso de templates
        type_distribution = self.context_maps['index'].get('type_distribution', {})
        total_docs = sum(type_distribution.values())
        
        for doc_type, count in type_distribution.items():
            percentage = (count / total_docs) * 100 if total_docs > 0 else 0
            patterns['usage_patterns'][doc_type] = {
                'count': count,
                'percentage': round(percentage, 1),
                'trend': 'normal'  # Poderia calcular tendência temporal
            }
            
        # Padrões de contexto
        context_distribution = self.context_maps['index'].get('context_distribution', {})
        for context_level, count in context_distribution.items():
            percentage = (count / total_docs) * 100 if total_docs > 0 else 0
            patterns['context_patterns'][context_level] = {
                'count': count,
                'percentage': round(percentage, 1)
            }
            
        # Padrões de conexão
        if self.context_maps.get('connections'):
            connections_data = self.context_maps['connections']
            patterns['connection_patterns'] = {
                'strong_coupling_count': len(connections_data.get('strong_coupling', [])),
                'weak_coupling_count': len(connections_data.get('weak_coupling', [])),
                'isolated_count': len(connections_data.get('isolated_components', [])),
                'connection_types': connections_data.get('connection_types', {})
            }
            
        # Padrões de qualidade
        docs_with_errors = sum(1 for doc in document_summary.values() if doc.get('has_errors', False))
        patterns['quality_patterns'] = {
            'error_rate': round((docs_with_errors / total_docs) * 100, 1) if total_docs > 0 else 0,
            'total_documents': total_docs,
            'documents_with_errors': docs_with_errors
        }
        
        return patterns
        
    def analyze_document(self, file_path: str, content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Análise completa de um documento
        
        Args:
            file_path: Caminho do arquivo
            content: Conteúdo do documento
            metadata: Metadados existentes
            
        Returns:
            Análise completa com recomendações
        """
        content_analysis = self.analyze_content(content)
        template_rec = self.recommend_template(content, metadata)
        context_rec = self.recommend_context(content, file_path, metadata)
        connection_suggestions = self.suggest_connections(content, metadata)
        improvement_suggestions = self.suggest_improvements(metadata, content)
        
        return {
            'file_path': file_path,
            'content_analysis': {
                'keywords': content_analysis.keywords,
                'entities': content_analysis.entities,
                'complexity_score': content_analysis.complexity_score,
                'purpose': content_analysis.purpose,
                'domain': content_analysis.domain,
                'confidence': content_analysis.confidence
            },
            'template_recommendation': {
                'recommended_type': template_rec.template_type,
                'confidence': template_rec.confidence,
                'reasoning': template_rec.reasoning,
                'alternatives': template_rec.alternative_templates
            },
            'context_recommendation': {
                'context_level': context_rec.context_level,
                'context_type': context_rec.context_type,
                'suggested_module': context_rec.suggested_module,
                'confidence': context_rec.confidence,
                'reasoning': context_rec.reasoning
            },
            'connection_suggestions': [
                {
                    'target': suggestion.target_document,
                    'type': suggestion.connection_type,
                    'confidence': suggestion.confidence,
                    'reasoning': suggestion.reasoning
                }
                for suggestion in connection_suggestions
            ],
            'improvement_suggestions': [
                {
                    'type': suggestion.type,
                    'description': suggestion.description,
                    'priority': suggestion.priority,
                    'action': suggestion.action
                }
                for suggestion in improvement_suggestions
            ],
            'overall_score': self._calculate_overall_score(
                content_analysis, template_rec, context_rec, improvement_suggestions
            )
        }
        
    def _calculate_overall_score(self, content_analysis: ContentAnalysis, 
                               template_rec: TemplateRecommendation,
                               context_rec: ContextRecommendation,
                               improvements: List[ImprovementSuggestion]) -> float:
        """
        Calcula score geral do documento
        
        Returns:
            Score de 0.0 a 1.0
        """
        score = 0.0
        
        # Score baseado em confiança das recomendações
        score += template_rec.confidence * 0.3
        score += context_rec.confidence * 0.2
        score += content_analysis.confidence * 0.2
        
        # Penalizar por melhorias necessárias
        high_priority_improvements = len([i for i in improvements if i.priority == 'high'])
        medium_priority_improvements = len([i for i in improvements if i.priority == 'medium'])
        
        penalty = (high_priority_improvements * 0.1) + (medium_priority_improvements * 0.05)
        score = max(0.0, score - penalty)
        
        # Bonus por complexidade adequada
        if 0.3 <= content_analysis.complexity_score <= 0.8:
            score += 0.1
            
        return min(score, 1.0)

def main():
    """Função principal para teste da engine"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Context Navigator Engine')
    parser.add_argument('--path', '-p', default='.', 
                       help='Caminho base do projeto')
    parser.add_argument('--analyze', '-a', 
                       help='Analisar arquivo específico')
    parser.add_argument('--patterns', action='store_true',
                       help='Detectar padrões gerais')
    
    args = parser.parse_args()
    
    engine = ContextEngine(args.path)
    
    if args.patterns:
        patterns = engine.detect_patterns()
        print("\n=== PADRÕES DETECTADOS ===")
        print(json.dumps(patterns, indent=2, ensure_ascii=False))
        
    if args.analyze:
        file_path = Path(args.analyze)
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extrair metadados (simplificado)
            metadata = {}
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    try:
                        metadata = yaml.safe_load(parts[1]) or {}
                    except:
                        pass
                        
            analysis = engine.analyze_document(str(file_path), content, metadata)
            print(f"\n=== ANÁLISE DE {file_path} ===")
            print(json.dumps(analysis, indent=2, ensure_ascii=False))
        else:
            print(f"Arquivo não encontrado: {file_path}")

if __name__ == '__main__':
    main() 