#!/usr/bin/env python3
"""
Context Navigator - Conflict Detector
Detector especializado em conflitos que identifica inconsistências
complexas entre documentos da metodologia Context Navigator.
"""

import os
import sys
import yaml
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import logging
from collections import defaultdict, Counter
import difflib
import hashlib

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('conflict_detector')

class ConflictType(Enum):
    """Tipos de conflitos detectáveis"""
    NOMENCLATURE = "nomenclature"
    DEPENDENCY = "dependency"
    VERSIONING = "versioning"
    CONTEXT = "context"
    RESPONSIBILITY = "responsibility"
    DATA = "data"
    TEMPORAL = "temporal"
    SCHEMA = "schema"

class ConflictSeverity(Enum):
    """Severidade dos conflitos"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"

@dataclass
class ConflictEvidence:
    """Evidência de um conflito"""
    source_file: str
    line_number: Optional[int]
    content: str
    context: str

@dataclass
class ConflictResolution:
    """Sugestão de resolução para um conflito"""
    description: str
    action_required: str
    priority: int
    automated: bool
    steps: List[str]

@dataclass
class Conflict:
    """Representação de um conflito detectado"""
    id: str
    type: ConflictType
    severity: ConflictSeverity
    title: str
    description: str
    evidence: List[ConflictEvidence]
    affected_files: List[str]
    resolution: ConflictResolution
    detected_at: datetime = field(default_factory=datetime.now)
    confidence: float = 1.0

@dataclass
class ConflictReport:
    """Relatório completo de conflitos"""
    total_conflicts: int
    conflicts_by_type: Dict[ConflictType, int]
    conflicts_by_severity: Dict[ConflictSeverity, int]
    conflicts: List[Conflict]
    analysis_summary: Dict[str, Any]
    resolution_plan: List[str]

class ConflictDetector:
    """Detector especializado em conflitos metodológicos"""
    
    def __init__(self, base_path: str = "."):
        """
        Inicializa o detector
        
        Args:
            base_path: Caminho base do projeto
        """
        self.base_path = Path(base_path)
        self.config = {}
        self.documents = {}
        self.context_maps = {}
        self.conflicts = []
        
        # Carregar dados necessários
        self._load_config()
        self._load_context_maps()
        
        # Inicializar padrões de detecção
        self._init_detection_patterns()
        
    def _load_config(self) -> None:
        """Carrega configuração do .contextrc"""
        config_file = self.base_path / ".contextrc"
        
        if not config_file.exists():
            logger.error(f"Arquivo .contextrc não encontrado em {config_file}")
            return
            
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
            logger.info("Configuração carregada com sucesso")
        except Exception as e:
            logger.error(f"Erro ao carregar configuração: {e}")
            
    def _load_context_maps(self) -> None:
        """Carrega mapas de contexto existentes"""
        context_maps_path = self.base_path / ".context-map"
        
        if not context_maps_path.exists():
            logger.warning("Mapas de contexto não encontrados")
            return
            
        # Carregar mapas principais
        map_files = ['index.yml', 'architecture.yml', 'connections.yml', 'conflicts.yml']
        
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
                    
    def _init_detection_patterns(self) -> None:
        """Inicializa padrões para detecção de conflitos"""
        
        # Padrões de nomenclatura para detecção de inconsistências
        self.nomenclature_patterns = {
            'api_endpoints': [
                r'/api/v\d+/\w+',
                r'GET|POST|PUT|DELETE|PATCH',
                r'endpoint\s+\w+',
                r'route\s+\w+'
            ],
            'database_entities': [
                r'table\s+\w+',
                r'model\s+\w+',
                r'entity\s+\w+',
                r'collection\s+\w+'
            ],
            'services': [
                r'service\s+\w+',
                r'class\s+\w+Service',
                r'interface\s+\w+',
                r'component\s+\w+'
            ],
            'modules': [
                r'module\s+\w+',
                r'package\s+\w+',
                r'namespace\s+\w+',
                r'library\s+\w+'
            ]
        }
        
        # Padrões de dependência
        self.dependency_patterns = {
            'depends_on': [
                r'depends\s+on\s+\w+',
                r'requires\s+\w+',
                r'needs\s+\w+',
                r'prerequisite\s+\w+'
            ],
            'blocks': [
                r'blocks\s+\w+',
                r'prevents\s+\w+',
                r'stops\s+\w+',
                r'inhibits\s+\w+'
            ],
            'references': [
                r'references\s+\w+',
                r'uses\s+\w+',
                r'calls\s+\w+',
                r'invokes\s+\w+'
            ]
        }
        
        # Padrões de versioning
        self.versioning_patterns = {
            'version_numbers': [
                r'v\d+\.\d+\.\d+',
                r'version\s+\d+\.\d+',
                r'api\s+v\d+',
                r'schema\s+v\d+'
            ],
            'compatibility': [
                r'compatible\s+with',
                r'requires\s+version',
                r'minimum\s+version',
                r'deprecated\s+in'
            ]
        }
        
    def _extract_entities(self, content: str, patterns: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """
        Extrai entidades específicas do conteúdo usando padrões
        
        Args:
            content: Conteúdo a ser analisado
            patterns: Padrões de extração
            
        Returns:
            Dicionário com entidades extraídas por categoria
        """
        entities = {}
        
        for category, pattern_list in patterns.items():
            entities[category] = []
            
            for pattern in pattern_list:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    entities[category].extend(matches)
                    
        return entities
        
    def _detect_nomenclature_conflicts(self) -> List[Conflict]:
        """
        Detecta conflitos de nomenclatura entre documentos
        
        Returns:
            Lista de conflitos encontrados
        """
        conflicts = []
        
        if not self.context_maps.get('index'):
            return conflicts
            
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        # Coletar todas as entidades mencionadas
        all_entities = defaultdict(list)
        
        for doc_path, doc_info in document_summary.items():
            doc_content = doc_info.get('content', '')
            
            # Extrair entidades usando padrões
            entities = self._extract_entities(doc_content, self.nomenclature_patterns)
            
            for category, entity_list in entities.items():
                for entity in entity_list:
                    all_entities[category].append({
                        'entity': entity.lower().strip(),
                        'original': entity,
                        'file': doc_path,
                        'context': doc_info.get('context_type', 'unknown')
                    })
                    
        # Detectar inconsistências por categoria
        for category, entities in all_entities.items():
            entity_variations = defaultdict(list)
            
            # Agrupar variações similares
            for entity_info in entities:
                base_entity = entity_info['entity']
                entity_variations[base_entity].append(entity_info)
                
            # Detectar variações do mesmo conceito
            for base_entity, variations in entity_variations.items():
                if len(variations) > 1:
                    # Verificar se são realmente variações (similaridade)
                    originals = [v['original'] for v in variations]
                    unique_originals = set(originals)
                    
                    if len(unique_originals) > 1:
                        # Calcular similaridade
                        similarity_threshold = 0.8
                        similar_groups = []
                        
                        for i, orig1 in enumerate(unique_originals):
                            for j, orig2 in enumerate(unique_originals):
                                if i < j:
                                    similarity = difflib.SequenceMatcher(None, orig1, orig2).ratio()
                                    if similarity > similarity_threshold:
                                        similar_groups.append((orig1, orig2, similarity))
                                        
                        if similar_groups:
                            # Criar conflito de nomenclatura
                            conflict_id = hashlib.md5(f"nomenclature_{category}_{base_entity}".encode()).hexdigest()[:8]
                            
                            evidence = []
                            affected_files = []
                            
                            for variation in variations:
                                evidence.append(ConflictEvidence(
                                    source_file=variation['file'],
                                    line_number=None,
                                    content=variation['original'],
                                    context=f"Categoria: {category}, Contexto: {variation['context']}"
                                ))
                                if variation['file'] not in affected_files:
                                    affected_files.append(variation['file'])
                                    
                            resolution = ConflictResolution(
                                description=f"Padronizar nomenclatura para {category}",
                                action_required="Escolher uma nomenclatura padrão e aplicar consistentemente",
                                priority=2,
                                automated=False,
                                steps=[
                                    f"Revisar todas as variações: {', '.join(unique_originals)}",
                                    "Escolher nomenclatura padrão",
                                    "Atualizar todos os documentos afetados",
                                    "Validar consistência"
                                ]
                            )
                            
                            conflicts.append(Conflict(
                                id=conflict_id,
                                type=ConflictType.NOMENCLATURE,
                                severity=ConflictSeverity.MEDIUM,
                                title=f"Nomenclatura inconsistente: {category}",
                                description=f"Entidade '{base_entity}' referenciada de {len(unique_originals)} formas diferentes",
                                evidence=evidence,
                                affected_files=affected_files,
                                resolution=resolution,
                                confidence=max(s[2] for s in similar_groups)
                            ))
                            
        return conflicts
        
    def _detect_dependency_conflicts(self) -> List[Conflict]:
        """
        Detecta conflitos de dependência entre documentos
        
        Returns:
            Lista de conflitos encontrados
        """
        conflicts = []
        
        if not self.context_maps.get('connections'):
            return conflicts
            
        connections_data = self.context_maps['connections']
        
        # Detectar dependências circulares
        dependencies = connections_data.get('dependency_graph', {})
        circular_paths = self._find_circular_dependencies(dependencies)
        
        for path in circular_paths:
            conflict_id = hashlib.md5(f"circular_dep_{'_'.join(path)}".encode()).hexdigest()[:8]
            
            evidence = []
            for i, doc in enumerate(path):
                next_doc = path[(i + 1) % len(path)]
                evidence.append(ConflictEvidence(
                    source_file=doc,
                    line_number=None,
                    content=f"Depende de: {next_doc}",
                    context="Dependência circular detectada"
                ))
                
            resolution = ConflictResolution(
                description="Resolver dependência circular",
                action_required="Refatorar dependências para eliminar ciclo",
                priority=1,
                automated=False,
                steps=[
                    "Analisar necessidade real de cada dependência",
                    "Identificar dependência que pode ser removida ou invertida",
                    "Refatorar documentos afetados",
                    "Validar que o ciclo foi eliminado"
                ]
            )
            
            conflicts.append(Conflict(
                id=conflict_id,
                type=ConflictType.DEPENDENCY,
                severity=ConflictSeverity.HIGH,
                title="Dependência circular detectada",
                description=f"Ciclo de dependência: {' → '.join(path)} → {path[0]}",
                evidence=evidence,
                affected_files=path,
                resolution=resolution
            ))
            
        # Detectar dependências órfãs (referências quebradas)
        document_summary = self.context_maps.get('index', {}).get('document_summary', {})
        existing_docs = set(document_summary.keys())
        
        for doc_path, doc_info in document_summary.items():
            connections = doc_info.get('connections', {})
            
            for connection_type, referenced_docs in connections.items():
                if isinstance(referenced_docs, list):
                    for ref_doc in referenced_docs:
                        if ref_doc not in existing_docs:
                            conflict_id = hashlib.md5(f"broken_ref_{doc_path}_{ref_doc}".encode()).hexdigest()[:8]
                            
                            evidence = [ConflictEvidence(
                                source_file=doc_path,
                                line_number=None,
                                content=f"{connection_type}: {ref_doc}",
                                context="Referência quebrada"
                            )]
                            
                            resolution = ConflictResolution(
                                description="Corrigir referência quebrada",
                                action_required="Atualizar ou remover referência",
                                priority=3,
                                automated=True,
                                steps=[
                                    "Verificar se documento foi movido ou renomeado",
                                    "Atualizar referência ou remover se não existe",
                                    "Executar scanner para validar"
                                ]
                            )
                            
                            conflicts.append(Conflict(
                                id=conflict_id,
                                type=ConflictType.DEPENDENCY,
                                severity=ConflictSeverity.MEDIUM,
                                title="Referência quebrada",
                                description=f"Documento '{doc_path}' referencia '{ref_doc}' que não existe",
                                evidence=evidence,
                                affected_files=[doc_path],
                                resolution=resolution
                            ))
                            
        return conflicts
        
    def _find_circular_dependencies(self, dependencies: Dict[str, List[str]]) -> List[List[str]]:
        """
        Encontra dependências circulares usando DFS
        
        Args:
            dependencies: Grafo de dependências
            
        Returns:
            Lista de caminhos circulares
        """
        visited = set()
        rec_stack = set()
        cycles = []
        
        def dfs(node: str, path: List[str]) -> None:
            if node in rec_stack:
                # Encontrou ciclo
                cycle_start = path.index(node)
                cycle = path[cycle_start:]
                cycles.append(cycle)
                return
                
            if node in visited:
                return
                
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in dependencies.get(node, []):
                dfs(neighbor, path + [neighbor])
                
            rec_stack.remove(node)
            
        for node in dependencies:
            if node not in visited:
                dfs(node, [node])
                
        return cycles
        
    def _detect_context_conflicts(self) -> List[Conflict]:
        """
        Detecta conflitos de contexto entre documentos
        
        Returns:
            Lista de conflitos encontrados
        """
        conflicts = []
        
        if not self.context_maps.get('index'):
            return conflicts
            
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        # Detectar contextos inconsistentes
        context_groups = defaultdict(list)
        
        for doc_path, doc_info in document_summary.items():
            context_level = doc_info.get('context_level', 'unknown')
            context_type = doc_info.get('context_type', 'unknown')
            module = doc_info.get('module', 'unknown')
            
            key = (context_level, context_type, module)
            context_groups[key].append(doc_path)
            
        # Detectar conflitos dentro do mesmo contexto
        for (context_level, context_type, module), docs in context_groups.items():
            if len(docs) > 1:
                # Verificar se documentos têm responsabilidades sobrepostas
                overlapping_docs = []
                
                for doc_path in docs:
                    doc_info = document_summary[doc_path]
                    if not doc_info or not isinstance(doc_info, dict):
                        continue
                    doc_title = (doc_info.get('title') or '').lower()
                    
                    # Verificar padrões de sobreposição
                    overlap_patterns = [
                        'authentication', 'authorization', 'login', 'user',
                        'database', 'storage', 'persistence', 'data',
                        'api', 'endpoint', 'service', 'interface'
                    ]
                    
                    for pattern in overlap_patterns:
                        if pattern in doc_title:
                            overlapping_docs.append((doc_path, pattern))
                            
                # Se há sobreposição, criar conflito
                if len(overlapping_docs) > 1:
                    pattern_groups = defaultdict(list)
                    for doc_path, pattern in overlapping_docs:
                        pattern_groups[pattern].append(doc_path)
                        
                    for pattern, pattern_docs in pattern_groups.items():
                        if len(pattern_docs) > 1:
                            conflict_id = hashlib.md5(f"context_overlap_{pattern}_{module}".encode()).hexdigest()[:8]
                            
                            evidence = []
                            for doc_path in pattern_docs:
                                doc_info = document_summary[doc_path]
                                evidence.append(ConflictEvidence(
                                    source_file=doc_path,
                                    line_number=None,
                                    content=f"Título: {doc_info.get('title', 'N/A')}",
                                    context=f"Contexto: {context_level}/{context_type}/{module}"
                                ))
                                
                            resolution = ConflictResolution(
                                description=f"Resolver sobreposição de responsabilidade em {pattern}",
                                action_required="Clarificar responsabilidades ou consolidar documentos",
                                priority=2,
                                automated=False,
                                steps=[
                                    "Analisar escopo de cada documento",
                                    "Definir responsabilidades específicas",
                                    "Consolidar ou separar conforme necessário",
                                    "Atualizar metadados de contexto"
                                ]
                            )
                            
                            conflicts.append(Conflict(
                                id=conflict_id,
                                type=ConflictType.RESPONSIBILITY,
                                severity=ConflictSeverity.MEDIUM,
                                title=f"Responsabilidade sobreposta: {pattern}",
                                description=f"Múltiplos documentos tratam de {pattern} no mesmo contexto",
                                evidence=evidence,
                                affected_files=pattern_docs,
                                resolution=resolution
                            ))
                            
        return conflicts
        
    def _detect_versioning_conflicts(self) -> List[Conflict]:
        """
        Detecta conflitos de versionamento
        
        Returns:
            Lista de conflitos encontrados
        """
        conflicts = []
        
        if not self.context_maps.get('index'):
            return conflicts
            
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        # Coletar informações de versão
        version_info = {}
        
        for doc_path, doc_info in document_summary.items():
            content = doc_info.get('content', '')
            
            # Extrair versões mencionadas
            versions = self._extract_entities(content, self.versioning_patterns)
            
            if versions.get('version_numbers'):
                version_info[doc_path] = {
                    'versions': versions['version_numbers'],
                    'compatibility': versions.get('compatibility', []),
                    'doc_info': doc_info
                }
                
        # Detectar versões incompatíveis
        for doc_path, info in version_info.items():
            versions = info['versions']
            
            # Verificar se há versões conflitantes no mesmo documento
            unique_versions = set(versions)
            if len(unique_versions) > 1:
                # Verificar se são versões incompatíveis
                version_numbers = []
                for version in unique_versions:
                    match = re.search(r'(\d+)\.(\d+)(?:\.(\d+))?', version)
                    if match:
                        major = int(match.group(1))
                        minor = int(match.group(2))
                        patch = int(match.group(3)) if match.group(3) else 0
                        version_numbers.append((major, minor, patch, version))
                        
                if len(version_numbers) > 1:
                    version_numbers.sort()
                    
                    # Verificar se há quebra de compatibilidade (major version)
                    major_versions = set(v[0] for v in version_numbers)
                    if len(major_versions) > 1:
                        conflict_id = hashlib.md5(f"version_conflict_{doc_path}".encode()).hexdigest()[:8]
                        
                        evidence = [ConflictEvidence(
                            source_file=doc_path,
                            line_number=None,
                            content=f"Versões encontradas: {', '.join(unique_versions)}",
                            context="Versões incompatíveis no mesmo documento"
                        )]
                        
                        resolution = ConflictResolution(
                            description="Resolver conflito de versões",
                            action_required="Escolher versão target e atualizar referências",
                            priority=2,
                            automated=False,
                            steps=[
                                "Identificar versão target do sistema",
                                "Atualizar todas as referências para versão consistente",
                                "Documentar estratégia de migração se necessário",
                                "Validar compatibilidade"
                            ]
                        )
                        
                        conflicts.append(Conflict(
                            id=conflict_id,
                            type=ConflictType.VERSIONING,
                            severity=ConflictSeverity.HIGH,
                            title="Versões incompatíveis",
                            description=f"Documento referencia versões major incompatíveis: {', '.join(unique_versions)}",
                            evidence=evidence,
                            affected_files=[doc_path],
                            resolution=resolution
                        ))
                        
        return conflicts
        
    def _detect_temporal_conflicts(self) -> List[Conflict]:
        """
        Detecta conflitos temporais (cronológicos)
        
        Returns:
            Lista de conflitos encontrados
        """
        conflicts = []
        
        if not self.context_maps.get('index'):
            return conflicts
            
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        # Coletar informações temporais
        temporal_info = {}
        
        for doc_path, doc_info in document_summary.items():
            created_date = doc_info.get('created_date')
            last_updated = doc_info.get('last_updated')
            
            if created_date or last_updated:
                try:
                    created = datetime.fromisoformat(created_date) if created_date else None
                    updated = datetime.fromisoformat(last_updated) if last_updated else None
                    
                    temporal_info[doc_path] = {
                        'created': created,
                        'updated': updated,
                        'doc_info': doc_info
                    }
                except ValueError:
                    # Data inválida, ignorar
                    continue
                    
        # Detectar inconsistências temporais
        for doc_path, info in temporal_info.items():
            created = info['created']
            updated = info['updated']
            
            # Verificar se data de atualização é anterior à criação
            if created and updated and updated < created:
                conflict_id = hashlib.md5(f"temporal_{doc_path}".encode()).hexdigest()[:8]
                
                evidence = [ConflictEvidence(
                    source_file=doc_path,
                    line_number=None,
                    content=f"Criado: {created.date()}, Atualizado: {updated.date()}",
                    context="Data de atualização anterior à criação"
                )]
                
                resolution = ConflictResolution(
                    description="Corrigir datas inconsistentes",
                    action_required="Atualizar metadados com datas corretas",
                    priority=3,
                    automated=True,
                    steps=[
                        "Verificar datas reais no sistema de arquivos",
                        "Corrigir metadados com datas consistentes",
                        "Executar validação de metadados"
                    ]
                )
                
                conflicts.append(Conflict(
                    id=conflict_id,
                    type=ConflictType.TEMPORAL,
                    severity=ConflictSeverity.LOW,
                    title="Inconsistência temporal",
                    description=f"Data de atualização ({updated.date()}) anterior à criação ({created.date()})",
                    evidence=evidence,
                    affected_files=[doc_path],
                    resolution=resolution
                ))
                
        return conflicts
        
    def _detect_data_conflicts(self) -> List[Conflict]:
        """
        Detecta conflitos de dados (informações contraditórias)
        
        Returns:
            Lista de conflitos encontrados
        """
        conflicts = []
        
        if not self.context_maps.get('index'):
            return conflicts
            
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        # Coletar informações factuais
        factual_data = defaultdict(list)
        
        for doc_path, doc_info in document_summary.items():
            content = doc_info.get('content', '')
            
            # Extrair dados factuais (métricas, configurações, etc.)
            metrics = re.findall(r'(\w+)[:=]\s*(\d+(?:\.\d+)?)\s*(%|ms|MB|GB|req/s)?', content)
            configs = re.findall(r'(\w+)[:=]\s*(["\']?)([^"\'\\n]+)\2', content)
            
            for metric, value, unit in metrics:
                factual_data[metric.lower()].append({
                    'value': float(value),
                    'unit': unit,
                    'file': doc_path,
                    'type': 'metric'
                })
                
            for config, _, value in configs:
                factual_data[config.lower()].append({
                    'value': value.strip(),
                    'unit': None,
                    'file': doc_path,
                    'type': 'config'
                })
                
        # Detectar valores contraditórios
        for key, values in factual_data.items():
            if len(values) > 1:
                # Verificar se há valores diferentes para a mesma chave
                unique_values = set()
                for v in values:
                    if v['type'] == 'metric':
                        unique_values.add((v['value'], v['unit']))
                    else:
                        unique_values.add(v['value'])
                        
                if len(unique_values) > 1:
                    conflict_id = hashlib.md5(f"data_conflict_{key}".encode()).hexdigest()[:8]
                    
                    evidence = []
                    affected_files = []
                    
                    for v in values:
                        if v['type'] == 'metric':
                            content = f"{key}: {v['value']}{v['unit'] or ''}"
                        else:
                            content = f"{key}: {v['value']}"
                            
                        evidence.append(ConflictEvidence(
                            source_file=v['file'],
                            line_number=None,
                            content=content,
                            context=f"Tipo: {v['type']}"
                        ))
                        
                        if v['file'] not in affected_files:
                            affected_files.append(v['file'])
                            
                    resolution = ConflictResolution(
                        description=f"Resolver valor contraditório para {key}",
                        action_required="Verificar e padronizar valor correto",
                        priority=2,
                        automated=False,
                        steps=[
                            "Verificar fonte autorizada para o valor",
                            "Atualizar documentos com valor correto",
                            "Adicionar referência à fonte quando relevante",
                            "Validar consistência"
                        ]
                    )
                    
                    conflicts.append(Conflict(
                        id=conflict_id,
                        type=ConflictType.DATA,
                        severity=ConflictSeverity.MEDIUM,
                        title=f"Dados contraditórios: {key}",
                        description=f"Valores diferentes para '{key}': {', '.join(str(v) for v in unique_values)}",
                        evidence=evidence,
                        affected_files=affected_files,
                        resolution=resolution
                    ))
                    
        return conflicts
        
    def detect_all_conflicts(self) -> List[Conflict]:
        """
        Executa todas as detecções de conflito
        
        Returns:
            Lista completa de conflitos encontrados
        """
        all_conflicts = []
        
        logger.info("Iniciando detecção de conflitos...")
        
        # Executar todas as detecções
        detection_methods = [
            ("Nomenclatura", self._detect_nomenclature_conflicts),
            ("Dependências", self._detect_dependency_conflicts),
            ("Contexto", self._detect_context_conflicts),
            ("Versionamento", self._detect_versioning_conflicts),
            ("Temporal", self._detect_temporal_conflicts),
            ("Dados", self._detect_data_conflicts)
        ]
        
        for method_name, method in detection_methods:
            try:
                logger.info(f"Detectando conflitos de {method_name}...")
                conflicts = method()
                all_conflicts.extend(conflicts)
                logger.info(f"Encontrados {len(conflicts)} conflitos de {method_name}")
            except Exception as e:
                logger.error(f"Erro ao detectar conflitos de {method_name}: {e}")
                
        # Ordenar por severidade e prioridade
        severity_order = {
            ConflictSeverity.CRITICAL: 0,
            ConflictSeverity.HIGH: 1,
            ConflictSeverity.MEDIUM: 2,
            ConflictSeverity.LOW: 3,
            ConflictSeverity.INFO: 4
        }
        
        all_conflicts.sort(key=lambda c: (severity_order[c.severity], -c.resolution.priority))
        
        self.conflicts = all_conflicts
        logger.info(f"Detecção concluída. Total: {len(all_conflicts)} conflitos")
        
        return all_conflicts
        
    def generate_report(self) -> ConflictReport:
        """
        Gera relatório completo de conflitos
        
        Returns:
            Relatório estruturado
        """
        conflicts = self.conflicts if self.conflicts else self.detect_all_conflicts()
        
        # Estatísticas por tipo
        conflicts_by_type = {}
        for conflict_type in ConflictType:
            conflicts_by_type[conflict_type] = len([c for c in conflicts if c.type == conflict_type])
            
        # Estatísticas por severidade
        conflicts_by_severity = {}
        for severity in ConflictSeverity:
            conflicts_by_severity[severity] = len([c for c in conflicts if c.severity == severity])
            
        # Análise resumida
        analysis_summary = {
            'total_files_affected': len(set(file for c in conflicts for file in c.affected_files)),
            'automated_resolutions': len([c for c in conflicts if c.resolution.automated]),
            'manual_resolutions': len([c for c in conflicts if not c.resolution.automated]),
            'high_priority_conflicts': len([c for c in conflicts if c.resolution.priority == 1]),
            'average_confidence': sum(c.confidence for c in conflicts) / len(conflicts) if conflicts else 0
        }
        
        # Plano de resolução
        resolution_plan = []
        critical_conflicts = [c for c in conflicts if c.severity == ConflictSeverity.CRITICAL]
        high_conflicts = [c for c in conflicts if c.severity == ConflictSeverity.HIGH]
        
        if critical_conflicts:
            resolution_plan.append(f"🔴 CRÍTICO: Resolver {len(critical_conflicts)} conflitos críticos imediatamente")
        if high_conflicts:
            resolution_plan.append(f"🟡 ALTO: Resolver {len(high_conflicts)} conflitos de alta prioridade")
            
        automated_conflicts = [c for c in conflicts if c.resolution.automated]
        if automated_conflicts:
            resolution_plan.append(f"🤖 AUTOMÁTICO: {len(automated_conflicts)} conflitos podem ser resolvidos automaticamente")
            
        return ConflictReport(
            total_conflicts=len(conflicts),
            conflicts_by_type=conflicts_by_type,
            conflicts_by_severity=conflicts_by_severity,
            conflicts=conflicts,
            analysis_summary=analysis_summary,
            resolution_plan=resolution_plan
        )
        
    def print_report(self, report: ConflictReport) -> None:
        """Imprime relatório de conflitos formatado"""
        
        print(f"\n{'='*70}")
        print(f"CONFLICT DETECTOR - RELATÓRIO DE CONFLITOS")
        print(f"{'='*70}")
        
        print(f"\n📊 RESUMO GERAL:")
        print(f"   Total de conflitos: {report.total_conflicts}")
        print(f"   Arquivos afetados: {report.analysis_summary['total_files_affected']}")
        print(f"   Resoluções automáticas: {report.analysis_summary['automated_resolutions']}")
        print(f"   Resoluções manuais: {report.analysis_summary['manual_resolutions']}")
        print(f"   Confiança média: {report.analysis_summary['average_confidence']:.2f}")
        
        # Estatísticas por severidade
        print(f"\n🎯 POR SEVERIDADE:")
        for severity, count in report.conflicts_by_severity.items():
            if count > 0:
                icon = {"critical": "🔴", "high": "🟡", "medium": "🟠", "low": "🟢", "info": "🔵"}
                print(f"   {icon.get(severity.value, '•')} {severity.value.upper()}: {count}")
                
        # Estatísticas por tipo
        print(f"\n📋 POR TIPO:")
        for conflict_type, count in report.conflicts_by_type.items():
            if count > 0:
                print(f"   • {conflict_type.value.upper()}: {count}")
                
        # Plano de resolução
        if report.resolution_plan:
            print(f"\n🎯 PLANO DE RESOLUÇÃO:")
            for step in report.resolution_plan:
                print(f"   {step}")
                
        # Mostrar conflitos mais críticos
        critical_conflicts = [c for c in report.conflicts if c.severity in [ConflictSeverity.CRITICAL, ConflictSeverity.HIGH]]
        
        if critical_conflicts:
            print(f"\n🚨 CONFLITOS PRIORITÁRIOS:")
            for conflict in critical_conflicts[:5]:  # Top 5
                print(f"\n   ID: {conflict.id}")
                print(f"   Tipo: {conflict.type.value.upper()}")
                print(f"   Severidade: {conflict.severity.value.upper()}")
                print(f"   Título: {conflict.title}")
                print(f"   Descrição: {conflict.description}")
                print(f"   Arquivos afetados: {len(conflict.affected_files)}")
                print(f"   Resolução: {conflict.resolution.description}")
                
        print(f"\n{'='*70}")

def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Context Navigator Conflict Detector')
    parser.add_argument('--path', '-p', default='.', 
                       help='Caminho base do projeto')
    parser.add_argument('--type', '-t', choices=['nomenclature', 'dependency', 'context', 'versioning', 'temporal', 'data', 'all'],
                       default='all', help='Tipo de conflito a detectar')
    parser.add_argument('--severity', '-s', choices=['critical', 'high', 'medium', 'low', 'info'],
                       help='Filtrar por severidade mínima')
    parser.add_argument('--json', action='store_true',
                       help='Saída em formato JSON')
    parser.add_argument('--resolve', '-r', 
                       help='Tentar resolver conflito por ID')
    
    args = parser.parse_args()
    
    detector = ConflictDetector(args.path)
    
    if args.resolve:
        print(f"Resolução automática não implementada para ID: {args.resolve}")
        return
        
    # Detectar conflitos
    conflicts = detector.detect_all_conflicts()
    
    # Filtrar por tipo se especificado
    if args.type != 'all':
        type_filter = ConflictType(args.type)
        conflicts = [c for c in conflicts if c.type == type_filter]
        
    # Filtrar por severidade se especificado
    if args.severity:
        severity_filter = ConflictSeverity(args.severity)
        severity_order = {
            ConflictSeverity.CRITICAL: 0,
            ConflictSeverity.HIGH: 1,
            ConflictSeverity.MEDIUM: 2,
            ConflictSeverity.LOW: 3,
            ConflictSeverity.INFO: 4
        }
        min_severity = severity_order[severity_filter]
        conflicts = [c for c in conflicts if severity_order[c.severity] <= min_severity]
        
    # Atualizar lista filtrada
    detector.conflicts = conflicts
    
    # Gerar relatório
    report = detector.generate_report()
    
    if args.json:
        # Converter para formato JSON serializável
        report_dict = {
            'total_conflicts': report.total_conflicts,
            'conflicts_by_type': {k.value: v for k, v in report.conflicts_by_type.items()},
            'conflicts_by_severity': {k.value: v for k, v in report.conflicts_by_severity.items()},
            'analysis_summary': report.analysis_summary,
            'resolution_plan': report.resolution_plan,
            'conflicts': [
                {
                    'id': c.id,
                    'type': c.type.value,
                    'severity': c.severity.value,
                    'title': c.title,
                    'description': c.description,
                    'affected_files': c.affected_files,
                    'confidence': c.confidence,
                    'resolution': {
                        'description': c.resolution.description,
                        'action_required': c.resolution.action_required,
                        'priority': c.resolution.priority,
                        'automated': c.resolution.automated,
                        'steps': c.resolution.steps
                    }
                }
                for c in report.conflicts
            ]
        }
        print(json.dumps(report_dict, indent=2, ensure_ascii=False))
    else:
        detector.print_report(report)

if __name__ == '__main__':
    main() 