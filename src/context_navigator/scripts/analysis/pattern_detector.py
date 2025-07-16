#!/usr/bin/env python3
"""
Context Navigator - Pattern Detector
Sistema de detecção de padrões e anomalias em documentação
"""

import json
import yaml
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass
from collections import defaultdict, Counter
import re
import argparse
import statistics

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('pattern_detector')

@dataclass
class Pattern:
    """Padrão detectado na documentação"""
    pattern_id: str
    pattern_type: str  # 'usage', 'structure', 'content', 'temporal', 'quality'
    name: str
    description: str
    examples: List[str]
    frequency: int
    confidence: float
    impact_level: str  # 'low', 'medium', 'high'
    
@dataclass
class Anomaly:
    """Anomalia detectada"""
    anomaly_id: str
    anomaly_type: str  # 'outlier', 'inconsistency', 'gap', 'duplication'
    name: str
    description: str
    affected_documents: List[str]
    severity: str  # 'low', 'medium', 'high', 'critical'
    confidence: float
    suggested_actions: List[str]
    
@dataclass
class OptimizationSuggestion:
    """Sugestão de otimização baseada em padrões"""
    suggestion_id: str
    title: str
    description: str
    rationale: str
    implementation_steps: List[str]
    expected_benefits: List[str]
    estimated_effort: str
    confidence: float
    
class PatternDetector:
    """Detector de padrões e anomalias em documentação"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        
        self.config = {}
        self.context_maps = {}
        self.document_cache = {}
        self.patterns_cache = {}
        
        # Thresholds para detecção
        self.thresholds = {
            'min_pattern_frequency': 3,
            'max_outlier_score': 2.0,
            'min_confidence': 0.6,
            'max_duplication_similarity': 0.8
        }
        
        self._init_with_workspace_manager()
        self._load_context_maps()
        self._load_document_cache()
        self._load_patterns_cache()
        
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
        self.config = current_workspace.configuration
        
        # Definir paths para nova arquitetura
        self.context_maps_path = current_workspace.root_path / ".cn_model"
        cache_dir = current_workspace.root_path / ".cn_model" / "cache"
        cache_dir.mkdir(parents=True, exist_ok=True)
        self.patterns_cache_path = cache_dir / "patterns-cache.json"
        
        logger.info(f"🌐 Workspace: {current_workspace.name} ({current_workspace.root_path})")
        
    def _load_config(self) -> None:
        """Carrega configuração do .contextrc"""
        # Procurar .contextrc em múltiplas localizações
        config_locations = [
            self.base_path / ".contextrc",  # Raiz do workspace
            self.base_path / ".context-navigator" / ".contextrc"  # Pasta de instalação
        ]
        
        config_file = None
        for location in config_locations:
            if location.exists():
                config_file = location
                break
        
        if not config_file:
            logger.error("Arquivo .contextrc não encontrado em nenhuma localização:")
            for location in config_locations:
                logger.error(f"  - {location}")
            self.config = {}
            return
            
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f) or {}
            logger.info(f"Configuração carregada com sucesso de {config_file}")
        except Exception as e:
            logger.error(f"Erro ao carregar configuração: {e}")
            self.config = {}
            
    def _init_paths(self) -> None:
        """Inicializa paths baseado na configuração"""
        scanner_config = self.config.get('scanner', {}).get('directories', {})
        self.context_maps_path = self.base_path / scanner_config.get('context_maps_path', '.context-map')
        self.patterns_cache_path = self.context_maps_path / "patterns_cache.json"
            
    def _load_context_maps(self) -> None:
        """Carrega mapas de contexto"""
        map_files = ['index.yml', 'connections.yml', 'architecture.yml', 'validation.json']
        
        for map_file in map_files:
            map_path = self.context_maps_path / map_file
            if map_path.exists():
                try:
                    with open(map_path, 'r', encoding='utf-8') as f:
                        key = map_file.replace('.yml', '').replace('.json', '')
                        if map_file.endswith('.json'):
                            self.context_maps[key] = json.load(f)
                        else:
                            self.context_maps[key] = yaml.safe_load(f) or {}
                except Exception as e:
                    logger.error(f"Erro ao carregar {map_file}: {e}")
                    
    def _load_document_cache(self) -> None:
        """Carrega cache de documentos"""
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
                    
                    # Extrair métricas básicas
                    lines = content.split('\n')
                    words = content.split()
                    
                    self.document_cache[doc_path] = {
                        'info': doc_info,
                        'content': content,
                        'lines': len(lines),
                        'words': len(words),
                        'chars': len(content),
                        'headers': len([line for line in lines if line.startswith('#')]),
                        'code_blocks': len(re.findall(r'```[\s\S]*?```', content)),
                        'links': len(re.findall(r'\[.*?\]\(.*?\)', content)),
                        'last_analyzed': datetime.now().isoformat()
                    }
            except Exception as e:
                logger.warning(f"Erro ao carregar documento {doc_path}: {e}")
                
    def _load_patterns_cache(self) -> None:
        """Carrega cache de padrões"""
        if self.patterns_cache_path.exists():
            try:
                with open(self.patterns_cache_path, 'r', encoding='utf-8') as f:
                    self.patterns_cache = json.load(f)
            except Exception as e:
                logger.error(f"Erro ao carregar cache de padrões: {e}")
                self.patterns_cache = {}
                
    def _save_patterns_cache(self) -> None:
        """Salva cache de padrões"""
        try:
            self.patterns_cache_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.patterns_cache_path, 'w', encoding='utf-8') as f:
                json.dump(self.patterns_cache, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Erro ao salvar cache de padrões: {e}")
            
    def detect_usage_patterns(self) -> List[Pattern]:
        """Detecta padrões de uso de templates e contextos"""
        patterns = []
        
        if not self.context_maps.get('index'):
            return patterns
            
        # Padrões de tipo de documento
        type_distribution = self.context_maps['index'].get('type_distribution', {})
        total_docs = sum(type_distribution.values())
        
        for doc_type, count in type_distribution.items():
            if count >= self.thresholds['min_pattern_frequency']:
                frequency_ratio = count / total_docs if total_docs > 0 else 0
                
                patterns.append(Pattern(
                    pattern_id=f"usage_type_{doc_type}",
                    pattern_type="usage",
                    name=f"Uso Frequente de {doc_type.upper()}",
                    description=f"Template {doc_type} usado em {count} documentos ({frequency_ratio:.1%})",
                    examples=[doc for doc, info in self.context_maps['index'].get('document_summary', {}).items() 
                             if info and info.get('type') == doc_type][:3],
                    frequency=count,
                    confidence=0.9,
                    impact_level="medium" if frequency_ratio > 0.3 else "low"
                ))
                
        # Padrões de contexto
        context_distribution = self.context_maps['index'].get('context_distribution', {})
        
        for context_level, count in context_distribution.items():
            if count >= self.thresholds['min_pattern_frequency']:
                frequency_ratio = count / total_docs if total_docs > 0 else 0
                
                patterns.append(Pattern(
                    pattern_id=f"usage_context_{context_level}",
                    pattern_type="usage",
                    name=f"Concentração em {context_level.upper()}",
                    description=f"Contexto {context_level} usado em {count} documentos ({frequency_ratio:.1%})",
                    examples=[doc for doc, info in self.context_maps['index'].get('document_summary', {}).items() 
                             if info and info.get('context_level') == context_level][:3],
                    frequency=count,
                    confidence=0.8,
                    impact_level="high" if frequency_ratio > 0.6 else "medium"
                ))
                
        return patterns
        
    def detect_structure_patterns(self) -> List[Pattern]:
        """Detecta padrões estruturais na documentação"""
        patterns = []
        
        if not self.document_cache:
            return patterns
            
        # Análise de tamanho de documentos
        doc_sizes = [doc['words'] for doc in self.document_cache.values()]
        if len(doc_sizes) >= 3:
            mean_size = statistics.mean(doc_sizes)
            std_size = statistics.stdev(doc_sizes) if len(doc_sizes) > 1 else 0
            
            # Padrão de tamanho consistente
            if std_size / mean_size < 0.5:  # Baixa variabilidade
                patterns.append(Pattern(
                    pattern_id="structure_consistent_size",
                    pattern_type="structure",
                    name="Tamanho Consistente de Documentos",
                    description=f"Documentos têm tamanho consistente (média: {mean_size:.0f} palavras, desvio: {std_size:.0f})",
                    examples=[doc_path for doc_path, doc_data in self.document_cache.items()
                             if abs(doc_data['words'] - mean_size) < std_size][:3],
                    frequency=len(doc_sizes),
                    confidence=0.8,
                    impact_level="medium"
                ))
                
        # Padrões de estrutura de cabeçalhos
        header_patterns = defaultdict(int)
        
        for doc_path, doc_data in self.document_cache.items():
            headers_per_word = doc_data['headers'] / max(doc_data['words'], 1)
            
            if headers_per_word > 0.1:  # Muitos cabeçalhos
                header_patterns['high_structure'] += 1
            elif headers_per_word < 0.02:  # Poucos cabeçalhos
                header_patterns['low_structure'] += 1
            else:
                header_patterns['balanced_structure'] += 1
                
        for pattern_type, count in header_patterns.items():
            if count >= self.thresholds['min_pattern_frequency']:
                patterns.append(Pattern(
                    pattern_id=f"structure_{pattern_type}",
                    pattern_type="structure",
                    name=f"Estrutura {pattern_type.replace('_', ' ').title()}",
                    description=f"{count} documentos seguem padrão de {pattern_type.replace('_', ' ')}",
                    examples=[],
                    frequency=count,
                    confidence=0.7,
                    impact_level="medium"
                ))
                
        return patterns
        
    def detect_content_patterns(self) -> List[Pattern]:
        """Detecta padrões de conteúdo"""
        patterns = []
        
        if not self.document_cache:
            return patterns
            
        # Padrões de uso de código
        code_usage = {"high": 0, "medium": 0, "low": 0}
        
        for doc_path, doc_data in self.document_cache.items():
            code_ratio = doc_data['code_blocks'] / max(doc_data['words'], 1) * 100
            
            if code_ratio > 5:
                code_usage["high"] += 1
            elif code_ratio > 1:
                code_usage["medium"] += 1
            else:
                code_usage["low"] += 1
                
        for usage_level, count in code_usage.items():
            if count >= self.thresholds['min_pattern_frequency']:
                patterns.append(Pattern(
                    pattern_id=f"content_code_{usage_level}",
                    pattern_type="content",
                    name=f"Uso {usage_level.title()} de Código",
                    description=f"{count} documentos têm {usage_level} uso de blocos de código",
                    examples=[],
                    frequency=count,
                    confidence=0.6,
                    impact_level="low"
                ))
                
        # Padrões de links
        link_usage = {"high": 0, "medium": 0, "low": 0}
        
        for doc_path, doc_data in self.document_cache.items():
            link_ratio = doc_data['links'] / max(doc_data['words'], 1) * 100
            
            if link_ratio > 2:
                link_usage["high"] += 1
            elif link_ratio > 0.5:
                link_usage["medium"] += 1
            else:
                link_usage["low"] += 1
                
        for usage_level, count in link_usage.items():
            if count >= self.thresholds['min_pattern_frequency']:
                patterns.append(Pattern(
                    pattern_id=f"content_links_{usage_level}",
                    pattern_type="content",
                    name=f"Uso {usage_level.title()} de Links",
                    description=f"{count} documentos têm {usage_level} densidade de links",
                    examples=[],
                    frequency=count,
                    confidence=0.7,
                    impact_level="medium" if usage_level == "high" else "low"
                ))
                
        return patterns
        
    def detect_quality_patterns(self) -> List[Pattern]:
        """Detecta padrões de qualidade"""
        patterns = []
        
        if not self.context_maps.get('validation'):
            return patterns
            
        validation_data = self.context_maps['validation']
        
        # Padrões de erro
        error_patterns = defaultdict(int)
        
        for doc_detail in validation_data.get('validation_details', []):
            if isinstance(doc_detail, dict) and doc_detail.get('errors'):
                for error in doc_detail['errors']:
                    # Extrair tipo de erro
                    error_type = error.split(':')[1].strip().split()[0] if ':' in error else 'unknown'
                    error_patterns[error_type] += 1
                    
        for error_type, count in error_patterns.items():
            if count >= self.thresholds['min_pattern_frequency']:
                patterns.append(Pattern(
                    pattern_id=f"quality_error_{error_type}",
                    pattern_type="quality",
                    name=f"Erro Recorrente: {error_type}",
                    description=f"Tipo de erro '{error_type}' aparece {count} vezes",
                    examples=[],
                    frequency=count,
                    confidence=0.9,
                    impact_level="high"
                ))
                
        return patterns
        
    def detect_anomalies(self) -> List[Anomaly]:
        """Detecta anomalias na documentação"""
        anomalies = []
        
        # Anomalias de tamanho
        anomalies.extend(self._detect_size_anomalies())
        
        # Anomalias de estrutura
        anomalies.extend(self._detect_structure_anomalies())
        
        # Anomalias de qualidade
        anomalies.extend(self._detect_quality_anomalies())
        
        # Anomalias de conexão
        anomalies.extend(self._detect_connection_anomalies())
        
        return anomalies
        
    def _detect_size_anomalies(self) -> List[Anomaly]:
        """Detecta anomalias de tamanho"""
        anomalies = []
        
        if not self.document_cache:
            return anomalies
            
        doc_sizes = [(doc_path, doc_data['words']) for doc_path, doc_data in self.document_cache.items()]
        
        if len(doc_sizes) < 3:
            return anomalies
            
        sizes = [size for _, size in doc_sizes]
        mean_size = statistics.mean(sizes)
        std_size = statistics.stdev(sizes) if len(sizes) > 1 else 0
        
        # Detectar outliers (documentos muito grandes ou pequenos)
        for doc_path, size in doc_sizes:
            z_score = abs(size - mean_size) / std_size if std_size > 0 else 0
            
            if z_score > self.thresholds['max_outlier_score']:
                anomalies.append(Anomaly(
                    anomaly_id=f"size_outlier_{doc_path}",
                    anomaly_type="outlier",
                    name=f"Tamanho Anômalo: {doc_path}",
                    description=f"Documento tem {size} palavras (média: {mean_size:.0f})",
                    affected_documents=[doc_path],
                    severity="medium",
                    confidence=0.8,
                    suggested_actions=[
                        "Revisar se documento está completo/incompleto",
                        "Considerar dividir documento grande",
                        "Expandir conteúdo se muito pequeno"
                    ]
                ))
                
        return anomalies
        
    def _detect_structure_anomalies(self) -> List[Anomaly]:
        """Detecta anomalias estruturais"""
        anomalies = []
        
        if not self.document_cache:
            return anomalies
            
        # Documentos sem cabeçalhos
        no_headers = []
        
        for doc_path, doc_data in self.document_cache.items():
            if doc_data['headers'] == 0 and doc_data['words'] > 50:
                no_headers.append(doc_path)
                
        if len(no_headers) > 0:
            anomalies.append(Anomaly(
                anomaly_id="structure_no_headers",
                anomaly_type="inconsistency",
                name="Documentos Sem Estrutura",
                description=f"{len(no_headers)} documentos não têm cabeçalhos",
                affected_documents=no_headers,
                severity="medium",
                confidence=0.9,
                suggested_actions=[
                    "Adicionar cabeçalhos para melhorar estrutura",
                    "Organizar conteúdo em seções",
                    "Revisar template usado"
                ]
            ))
            
        return anomalies
        
    def _detect_quality_anomalies(self) -> List[Anomaly]:
        """Detecta anomalias de qualidade"""
        anomalies = []
        
        if not self.context_maps.get('validation'):
            return anomalies
            
        validation_data = self.context_maps['validation']
        
        # Documentos com muitos erros
        high_error_docs = []
        
        for doc_detail in validation_data.get('validation_details', []):
            if isinstance(doc_detail, dict):
                error_count = doc_detail.get('error_count', 0)
                if error_count > 5:  # Threshold para "muitos erros"
                    high_error_docs.append(doc_detail.get('document', ''))
                    
        if len(high_error_docs) > 0:
            anomalies.append(Anomaly(
                anomaly_id="quality_high_errors",
                anomaly_type="outlier",
                name="Documentos com Muitos Erros",
                description=f"{len(high_error_docs)} documentos têm mais de 5 erros",
                affected_documents=high_error_docs,
                severity="high",
                confidence=0.9,
                suggested_actions=[
                    "Revisar documentos com muitos erros",
                    "Verificar se template está sendo usado corretamente",
                    "Corrigir problemas de validação"
                ]
            ))
            
        return anomalies
        
    def _detect_connection_anomalies(self) -> List[Anomaly]:
        """Detecta anomalias de conexão"""
        anomalies = []
        
        if not self.context_maps.get('connections'):
            return anomalies
            
        connections_data = self.context_maps['connections']
        
        # Documentos isolados
        isolated_docs = connections_data.get('isolated_components', [])
        
        if len(isolated_docs) > 0:
            anomalies.append(Anomaly(
                anomaly_id="connection_isolated",
                anomaly_type="gap",
                name="Documentos Isolados",
                description=f"{len(isolated_docs)} documentos não têm conexões",
                affected_documents=isolated_docs,
                severity="medium",
                confidence=0.8,
                suggested_actions=[
                    "Mapear conexões com outros documentos",
                    "Revisar se documento está no contexto correto",
                    "Considerar se documento é necessário"
                ]
            ))
            
        # Documentos super conectados
        strong_coupling = connections_data.get('strong_coupling', [])
        over_connected = [doc['document'] for doc in strong_coupling if doc.get('connection_count', 0) > 10]
        
        if len(over_connected) > 0:
            anomalies.append(Anomaly(
                anomaly_id="connection_over_connected",
                anomaly_type="outlier",
                name="Documentos Super Conectados",
                description=f"{len(over_connected)} documentos têm mais de 10 conexões",
                affected_documents=over_connected,
                severity="low",
                confidence=0.7,
                suggested_actions=[
                    "Revisar se todas as conexões são necessárias",
                    "Considerar simplificar relacionamentos",
                    "Verificar se documento não está muito genérico"
                ]
            ))
            
        return anomalies
        
    def generate_optimization_suggestions(self, patterns: List[Pattern], anomalies: List[Anomaly]) -> List[OptimizationSuggestion]:
        """Gera sugestões de otimização baseadas em padrões e anomalias"""
        suggestions = []
        
        # Sugestões baseadas em padrões
        usage_patterns = [p for p in patterns if p.pattern_type == "usage"]
        quality_patterns = [p for p in patterns if p.pattern_type == "quality"]
        
        # Otimização de templates subutilizados
        if usage_patterns:
            type_counts = {}
            for pattern in usage_patterns:
                if pattern.pattern_id.startswith("usage_type_"):
                    doc_type = pattern.pattern_id.replace("usage_type_", "")
                    type_counts[doc_type] = pattern.frequency
                    
            # Identificar templates pouco usados
            total_docs = sum(type_counts.values())
            for doc_type, count in type_counts.items():
                ratio = count / total_docs if total_docs > 0 else 0
                if ratio < 0.05:  # Menos de 5% de uso
                    suggestions.append(OptimizationSuggestion(
                        suggestion_id=f"optimize_underused_{doc_type}",
                        title=f"Otimizar Uso de Template {doc_type.upper()}",
                        description=f"Template {doc_type} está sendo subutilizado ({ratio:.1%})",
                        rationale="Templates subutilizados podem indicar lacunas na documentação",
                        implementation_steps=[
                            f"Identificar oportunidades para documentos {doc_type}",
                            "Revisar se template é necessário",
                            "Treinar equipe no uso do template"
                        ],
                        expected_benefits=[
                            "Melhor cobertura documental",
                            "Documentação mais balanceada"
                        ],
                        estimated_effort="2-3 horas",
                        confidence=0.7
                    ))
                    
        # Sugestões baseadas em anomalias
        size_anomalies = [a for a in anomalies if a.anomaly_type == "outlier" and "size" in a.anomaly_id]
        
        if len(size_anomalies) > 0:
            suggestions.append(OptimizationSuggestion(
                suggestion_id="optimize_document_sizes",
                title="Padronizar Tamanhos de Documentos",
                description="Alguns documentos têm tamanhos anômalos",
                rationale="Tamanhos consistentes melhoram legibilidade e manutenção",
                implementation_steps=[
                    "Revisar documentos muito grandes/pequenos",
                    "Estabelecer diretrizes de tamanho",
                    "Dividir ou expandir conforme necessário"
                ],
                expected_benefits=[
                    "Documentação mais consistente",
                    "Melhor experiência de leitura"
                ],
                estimated_effort="1-2 horas",
                confidence=0.8
            ))
            
        # Sugestões baseadas em qualidade
        if quality_patterns:
            error_patterns = [p for p in quality_patterns if "error" in p.pattern_id]
            if error_patterns:
                suggestions.append(OptimizationSuggestion(
                    suggestion_id="optimize_quality_process",
                    title="Melhorar Processo de Qualidade",
                    description="Erros recorrentes detectados na documentação",
                    rationale="Erros sistemáticos indicam problemas no processo",
                    implementation_steps=[
                        "Identificar causas raiz dos erros",
                        "Melhorar templates problemáticos",
                        "Implementar checklist de qualidade"
                    ],
                    expected_benefits=[
                        "Menos erros de validação",
                        "Melhor qualidade geral"
                    ],
                    estimated_effort="3-4 horas",
                    confidence=0.9
                ))
                
        return suggestions
        
    def run_full_analysis(self) -> Dict[str, Any]:
        """Executa análise completa e retorna resultados"""
        logger.info("Iniciando análise completa de padrões...")
        
        # Detectar padrões
        usage_patterns = self.detect_usage_patterns()
        structure_patterns = self.detect_structure_patterns()
        content_patterns = self.detect_content_patterns()
        quality_patterns = self.detect_quality_patterns()
        
        all_patterns = usage_patterns + structure_patterns + content_patterns + quality_patterns
        
        # Detectar anomalias
        anomalies = self.detect_anomalies()
        
        # Gerar sugestões
        suggestions = self.generate_optimization_suggestions(all_patterns, anomalies)
        
        # Atualizar cache
        self.patterns_cache = {
            'last_analysis': datetime.now().isoformat(),
            'patterns': [
                {
                    'pattern_id': p.pattern_id,
                    'pattern_type': p.pattern_type,
                    'name': p.name,
                    'description': p.description,
                    'frequency': p.frequency,
                    'confidence': p.confidence,
                    'impact_level': p.impact_level
                }
                for p in all_patterns
            ],
            'anomalies': [
                {
                    'anomaly_id': a.anomaly_id,
                    'anomaly_type': a.anomaly_type,
                    'name': a.name,
                    'description': a.description,
                    'severity': a.severity,
                    'confidence': a.confidence,
                    'affected_count': len(a.affected_documents)
                }
                for a in anomalies
            ],
            'suggestions': [
                {
                    'suggestion_id': s.suggestion_id,
                    'title': s.title,
                    'description': s.description,
                    'estimated_effort': s.estimated_effort,
                    'confidence': s.confidence
                }
                for s in suggestions
            ]
        }
        
        self._save_patterns_cache()
        
        return {
            'patterns': all_patterns,
            'anomalies': anomalies,
            'suggestions': suggestions,
            'summary': {
                'total_patterns': len(all_patterns),
                'total_anomalies': len(anomalies),
                'total_suggestions': len(suggestions),
                'analysis_confidence': statistics.mean([p.confidence for p in all_patterns]) if all_patterns else 0.0
            }
        }

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(description='Context Navigator Pattern Detector')
    parser.add_argument('--path', '-p', default='.', help='Caminho base do projeto')
    parser.add_argument('--patterns', action='store_true', help='Detectar padrões')
    parser.add_argument('--anomalies', action='store_true', help='Detectar anomalias')
    parser.add_argument('--suggestions', action='store_true', help='Gerar sugestões')
    parser.add_argument('--full', action='store_true', help='Análise completa')
    parser.add_argument('--json', action='store_true', help='Saída em formato JSON')
    
    args = parser.parse_args()
    
    detector = PatternDetector(args.path)
    
    if args.full:
        results = detector.run_full_analysis()
        
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False, default=str))
        else:
            print(f"\n=== ANÁLISE COMPLETA DE PADRÕES ===")
            print(f"Padrões detectados: {results['summary']['total_patterns']}")
            print(f"Anomalias detectadas: {results['summary']['total_anomalies']}")
            print(f"Sugestões geradas: {results['summary']['total_suggestions']}")
            print(f"Confiança média: {results['summary']['analysis_confidence']:.1%}")
            
            # Mostrar top padrões
            print("\nTop Padrões:")
            for pattern in results['patterns'][:5]:
                print(f"  📊 {pattern.name}")
                print(f"     {pattern.description}")
                print(f"     Frequência: {pattern.frequency}, Confiança: {pattern.confidence:.1%}")
                
            # Mostrar anomalias críticas
            critical_anomalies = [a for a in results['anomalies'] if a.severity == 'high']
            if critical_anomalies:
                print("\nAnomalias Críticas:")
                for anomaly in critical_anomalies:
                    print(f"  ⚠️  {anomaly.name}")
                    print(f"     {anomaly.description}")
                    print(f"     Afetados: {len(anomaly.affected_documents)}")
                    
            # Mostrar sugestões principais
            if results['suggestions']:
                print("\nSugestões Principais:")
                for suggestion in results['suggestions'][:3]:
                    print(f"  💡 {suggestion.title}")
                    print(f"     {suggestion.description}")
                    print(f"     Esforço: {suggestion.estimated_effort}")
                    
    elif args.patterns:
        all_patterns = (detector.detect_usage_patterns() + 
                       detector.detect_structure_patterns() + 
                       detector.detect_content_patterns() + 
                       detector.detect_quality_patterns())
        
        print(f"\n=== PADRÕES DETECTADOS ({len(all_patterns)}) ===")
        for pattern in all_patterns:
            print(f"\n📊 {pattern.name}")
            print(f"   Tipo: {pattern.pattern_type}")
            print(f"   Descrição: {pattern.description}")
            print(f"   Frequência: {pattern.frequency}")
            print(f"   Confiança: {pattern.confidence:.1%}")
            print(f"   Impacto: {pattern.impact_level}")
            
    elif args.anomalies:
        anomalies = detector.detect_anomalies()
        
        print(f"\n=== ANOMALIAS DETECTADAS ({len(anomalies)}) ===")
        for anomaly in anomalies:
            print(f"\n⚠️  {anomaly.name}")
            print(f"   Tipo: {anomaly.anomaly_type}")
            print(f"   Descrição: {anomaly.description}")
            print(f"   Severidade: {anomaly.severity}")
            print(f"   Confiança: {anomaly.confidence:.1%}")
            print(f"   Documentos afetados: {len(anomaly.affected_documents)}")
            
    else:
        print("Especifique --patterns, --anomalies, --suggestions ou --full")

if __name__ == '__main__':
    main() 