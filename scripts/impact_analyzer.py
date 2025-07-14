#!/usr/bin/env python3
"""
Context Navigator - Impact Analyzer
Sistema de análise de impacto automática para mudanças em documentos
"""

import json
import yaml
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass
from collections import defaultdict, deque
import argparse
import hashlib

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('impact_analyzer')

@dataclass
class ImpactNode:
    """Nó no grafo de impacto"""
    document_path: str
    document_type: str
    impact_level: str  # 'direct', 'indirect', 'cascade'
    impact_score: float
    impact_reasons: List[str]
    affected_sections: List[str]
    suggested_actions: List[str]
    
@dataclass
class ImpactAnalysis:
    """Resultado da análise de impacto"""
    source_document: str
    change_type: str  # 'create', 'update', 'delete', 'restructure'
    total_affected: int
    impact_tree: List[ImpactNode]
    critical_paths: List[List[str]]
    recommendations: List[str]
    estimated_effort: str
    confidence: float

@dataclass
class ChangeSignature:
    """Assinatura de mudança para rastreamento"""
    document_path: str
    content_hash: str
    metadata_hash: str
    timestamp: str
    change_type: str
    
class ImpactAnalyzer:
    """Analisador de impacto de mudanças em documentos"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        
        self.config = {}
        self.context_maps = {}
        self.document_graph = {}
        self.impact_history = []
        self.change_signatures = {}
        
        self._load_config()
        self._init_paths()
        self._load_context_maps()
        self._build_document_graph()
        self._load_impact_history()
        
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
        self.impact_history_path = self.context_maps_path / "impact_history.json"
            
    def _load_context_maps(self) -> None:
        """Carrega mapas de contexto"""
        map_files = ['index.yml', 'connections.yml', 'architecture.yml']
        
        for map_file in map_files:
            map_path = self.context_maps_path / map_file
            if map_path.exists():
                try:
                    with open(map_path, 'r', encoding='utf-8') as f:
                        key = map_file.replace('.yml', '')
                        self.context_maps[key] = yaml.safe_load(f) or {}
                except Exception as e:
                    logger.error(f"Erro ao carregar {map_file}: {e}")
                    
    def _build_document_graph(self) -> None:
        """Constrói grafo de documentos baseado em conexões"""
        self.document_graph = defaultdict(set)
        
        if not self.context_maps.get('connections'):
            return
            
        connections_graph = self.context_maps['connections'].get('graph', {})
        
        for doc_path, connections in connections_graph.items():
            if not isinstance(connections, dict):
                continue
                
            for connection_type, targets in connections.items():
                if not isinstance(targets, list):
                    continue
                    
                for target in targets:
                    # Adicionar conexão bidirecional com tipo
                    self.document_graph[doc_path].add((target, connection_type))
                    
                    # Conexão reversa com tipo apropriado
                    reverse_type = self._get_reverse_connection_type(connection_type)
                    self.document_graph[target].add((doc_path, reverse_type))
                    
    def _get_reverse_connection_type(self, connection_type: str) -> str:
        """Obtém tipo de conexão reversa"""
        reverse_mapping = {
            'depends_on': 'blocks',
            'blocks': 'depends_on',
            'references': 'referenced_by',
            'referenced_by': 'references',
            'impacts': 'impacted_by',
            'impacted_by': 'impacts',
            'relates_to': 'relates_to'
        }
        return reverse_mapping.get(connection_type, 'relates_to')
        
    def _load_impact_history(self) -> None:
        """Carrega histórico de impactos"""
        if self.impact_history_path.exists():
            try:
                with open(self.impact_history_path, 'r', encoding='utf-8') as f:
                    self.impact_history = json.load(f)
            except Exception as e:
                logger.error(f"Erro ao carregar histórico de impactos: {e}")
                self.impact_history = []
                
    def _save_impact_history(self) -> None:
        """Salva histórico de impactos"""
        try:
            self.impact_history_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.impact_history_path, 'w', encoding='utf-8') as f:
                json.dump(self.impact_history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Erro ao salvar histórico de impactos: {e}")
            
    def _calculate_content_hash(self, content: str) -> str:
        """Calcula hash do conteúdo"""
        return hashlib.md5(content.encode('utf-8')).hexdigest()
        
    def _calculate_metadata_hash(self, metadata: Dict[str, Any]) -> str:
        """Calcula hash dos metadados"""
        metadata_str = json.dumps(metadata, sort_keys=True)
        return hashlib.md5(metadata_str.encode('utf-8')).hexdigest()
        
    def detect_changes(self) -> List[ChangeSignature]:
        """Detecta mudanças em documentos desde última análise"""
        changes = []
        
        if not self.context_maps.get('index'):
            return changes
            
        document_summary = self.context_maps['index'].get('document_summary', {})
        
        for doc_path, doc_info in document_summary.items():
            if not doc_info or not isinstance(doc_info, dict):
                continue
                
            try:
                full_path = self.base_path / doc_path
                if not full_path.exists():
                    # Documento foi deletado
                    if doc_path in self.change_signatures:
                        changes.append(ChangeSignature(
                            document_path=doc_path,
                            content_hash="",
                            metadata_hash="",
                            timestamp=datetime.now().isoformat(),
                            change_type="delete"
                        ))
                    continue
                    
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                content_hash = self._calculate_content_hash(content)
                metadata_hash = self._calculate_metadata_hash(doc_info)
                
                # Verificar se houve mudança
                if doc_path in self.change_signatures:
                    old_sig = self.change_signatures[doc_path]
                    
                    if old_sig.content_hash != content_hash or old_sig.metadata_hash != metadata_hash:
                        change_type = "update"
                        if old_sig.metadata_hash != metadata_hash:
                            change_type = "restructure"
                            
                        changes.append(ChangeSignature(
                            document_path=doc_path,
                            content_hash=content_hash,
                            metadata_hash=metadata_hash,
                            timestamp=datetime.now().isoformat(),
                            change_type=change_type
                        ))
                else:
                    # Documento novo
                    changes.append(ChangeSignature(
                        document_path=doc_path,
                        content_hash=content_hash,
                        metadata_hash=metadata_hash,
                        timestamp=datetime.now().isoformat(),
                        change_type="create"
                    ))
                    
                # Atualizar assinatura
                self.change_signatures[doc_path] = ChangeSignature(
                    document_path=doc_path,
                    content_hash=content_hash,
                    metadata_hash=metadata_hash,
                    timestamp=datetime.now().isoformat(),
                    change_type="current"
                )
                
            except Exception as e:
                logger.error(f"Erro ao processar {doc_path}: {e}")
                
        return changes
        
    def analyze_impact(self, document_path: str, change_type: str = "update") -> ImpactAnalysis:
        """Analisa impacto de mudanças em um documento"""
        impact_tree = []
        critical_paths = []
        
        # BFS para encontrar documentos afetados
        visited = set()
        queue = deque([(document_path, 0, "direct", 1.0, [])])
        
        while queue:
            current_doc, depth, impact_level, score_multiplier, path = queue.popleft()
            
            if current_doc in visited or depth > 3:  # Limitar profundidade
                continue
                
            visited.add(current_doc)
            
            # Obter informações do documento
            doc_info = self._get_document_info(current_doc)
            if not doc_info:
                continue
                
            # Calcular impacto
            impact_score = self._calculate_impact_score(
                current_doc, document_path, change_type, depth, score_multiplier
            )
            
            impact_reasons = self._get_impact_reasons(current_doc, document_path, change_type)
            affected_sections = self._get_affected_sections(current_doc, change_type)
            suggested_actions = self._get_suggested_actions(current_doc, change_type, impact_score)
            
            impact_node = ImpactNode(
                document_path=current_doc,
                document_type=doc_info.get('type', 'unknown'),
                impact_level=impact_level,
                impact_score=impact_score,
                impact_reasons=impact_reasons,
                affected_sections=affected_sections,
                suggested_actions=suggested_actions
            )
            
            impact_tree.append(impact_node)
            
            # Adicionar caminhos críticos
            current_path = path + [current_doc]
            if impact_score > 0.7:
                critical_paths.append(current_path)
                
            # Adicionar documentos conectados à queue
            if current_doc in self.document_graph:
                for connected_doc, connection_type in self.document_graph[current_doc]:
                    if connected_doc not in visited:
                        new_impact_level = "cascade" if depth > 1 else "indirect"
                        new_score_multiplier = score_multiplier * self._get_connection_strength(connection_type)
                        
                        queue.append((
                            connected_doc,
                            depth + 1,
                            new_impact_level,
                            new_score_multiplier,
                            current_path
                        ))
                        
        # Gerar recomendações
        recommendations = self._generate_impact_recommendations(impact_tree, change_type)
        
        # Estimar esforço
        estimated_effort = self._estimate_effort(impact_tree)
        
        # Calcular confiança
        confidence = self._calculate_analysis_confidence(impact_tree)
        
        return ImpactAnalysis(
            source_document=document_path,
            change_type=change_type,
            total_affected=len(impact_tree),
            impact_tree=impact_tree,
            critical_paths=critical_paths,
            recommendations=recommendations,
            estimated_effort=estimated_effort,
            confidence=confidence
        )
        
    def _get_document_info(self, document_path: str) -> Optional[Dict[str, Any]]:
        """Obtém informações do documento"""
        if not self.context_maps.get('index'):
            return None
            
        document_summary = self.context_maps['index'].get('document_summary', {})
        return document_summary.get(document_path)
        
    def _calculate_impact_score(self, current_doc: str, source_doc: str, change_type: str, 
                               depth: int, score_multiplier: float) -> float:
        """Calcula score de impacto"""
        base_score = 1.0
        
        if current_doc == source_doc:
            return base_score
            
        # Reduzir score por profundidade
        depth_penalty = 0.3 * depth
        base_score -= depth_penalty
        
        # Ajustar por tipo de mudança
        change_multipliers = {
            'create': 0.5,
            'update': 0.7,
            'delete': 1.0,
            'restructure': 0.9
        }
        
        change_multiplier = change_multipliers.get(change_type, 0.7)
        base_score *= change_multiplier
        
        # Aplicar multiplicador de conexão
        base_score *= score_multiplier
        
        return max(0.0, min(1.0, base_score))
        
    def _get_connection_strength(self, connection_type: str) -> float:
        """Obtém força da conexão"""
        strength_mapping = {
            'depends_on': 0.9,
            'blocks': 0.9,
            'impacts': 0.8,
            'impacted_by': 0.8,
            'references': 0.6,
            'referenced_by': 0.6,
            'relates_to': 0.4
        }
        return strength_mapping.get(connection_type, 0.5)
        
    def _get_impact_reasons(self, current_doc: str, source_doc: str, change_type: str) -> List[str]:
        """Obtém razões do impacto"""
        reasons = []
        
        if current_doc == source_doc:
            reasons.append(f"Documento fonte da mudança ({change_type})")
            return reasons
            
        # Verificar conexões diretas
        if current_doc in self.document_graph:
            for connected_doc, connection_type in self.document_graph[current_doc]:
                if connected_doc == source_doc:
                    reasons.append(f"Conexão direta via '{connection_type}'")
                    break
                    
        # Verificar mesmo módulo/contexto
        source_info = self._get_document_info(source_doc)
        current_info = self._get_document_info(current_doc)
        
        if source_info and current_info:
            if source_info.get('module') == current_info.get('module'):
                reasons.append("Mesmo módulo")
            if source_info.get('context_type') == current_info.get('context_type'):
                reasons.append("Mesmo contexto")
                
        return reasons
        
    def _get_affected_sections(self, document_path: str, change_type: str) -> List[str]:
        """Obtém seções afetadas"""
        sections = []
        
        if change_type == "delete":
            sections.append("Documento completo (deletado)")
        elif change_type == "restructure":
            sections.extend(["Metadados", "Estrutura", "Conexões"])
        elif change_type == "update":
            sections.extend(["Conteúdo", "Possíveis conexões"])
        elif change_type == "create":
            sections.extend(["Novo documento", "Novas conexões"])
            
        return sections
        
    def _get_suggested_actions(self, document_path: str, change_type: str, impact_score: float) -> List[str]:
        """Obtém ações sugeridas"""
        actions = []
        
        if impact_score > 0.8:
            actions.append("Revisão obrigatória")
            actions.append("Validar conexões")
            actions.append("Atualizar conteúdo se necessário")
        elif impact_score > 0.5:
            actions.append("Revisão recomendada")
            actions.append("Verificar consistência")
        elif impact_score > 0.2:
            actions.append("Revisão opcional")
            actions.append("Monitorar por mudanças")
        else:
            actions.append("Nenhuma ação necessária")
            
        return actions
        
    def _generate_impact_recommendations(self, impact_tree: List[ImpactNode], change_type: str) -> List[str]:
        """Gera recomendações baseadas no impacto"""
        recommendations = []
        
        high_impact_docs = [node for node in impact_tree if node.impact_score > 0.7]
        medium_impact_docs = [node for node in impact_tree if 0.3 < node.impact_score <= 0.7]
        
        if len(high_impact_docs) > 0:
            recommendations.append(f"Revisar imediatamente {len(high_impact_docs)} documento(s) com alto impacto")
            
        if len(medium_impact_docs) > 0:
            recommendations.append(f"Agendar revisão de {len(medium_impact_docs)} documento(s) com médio impacto")
            
        if change_type == "delete":
            recommendations.append("Verificar se conexões para documento deletado foram removidas")
            
        if change_type == "restructure":
            recommendations.append("Executar validação completa após mudanças estruturais")
            
        # Recomendações específicas por tipo de documento
        doc_types = set(node.document_type for node in impact_tree)
        if 'decision' in doc_types:
            recommendations.append("Decisões afetadas podem impactar arquitetura")
        if 'process' in doc_types:
            recommendations.append("Processos afetados podem precisar de atualização")
            
        return recommendations
        
    def _estimate_effort(self, impact_tree: List[ImpactNode]) -> str:
        """Estima esforço necessário"""
        total_score = sum(node.impact_score for node in impact_tree)
        
        if total_score < 1.0:
            return "15-30 minutos"
        elif total_score < 3.0:
            return "30-60 minutos"
        elif total_score < 5.0:
            return "1-2 horas"
        else:
            return "2+ horas"
            
    def _calculate_analysis_confidence(self, impact_tree: List[ImpactNode]) -> float:
        """Calcula confiança da análise"""
        if not impact_tree:
            return 0.0
            
        # Confiança baseada em completude dos dados
        has_connections = len(self.document_graph) > 0
        has_metadata = any(node.impact_reasons for node in impact_tree)
        
        confidence = 0.6  # Base
        
        if has_connections:
            confidence += 0.2
        if has_metadata:
            confidence += 0.2
            
        return min(1.0, confidence)
        
    def batch_analyze_changes(self) -> List[ImpactAnalysis]:
        """Analisa impacto de todas as mudanças detectadas"""
        changes = self.detect_changes()
        analyses = []
        
        for change in changes:
            analysis = self.analyze_impact(change.document_path, change.change_type)
            analyses.append(analysis)
            
            # Salvar no histórico
            self.impact_history.append({
                'timestamp': change.timestamp,
                'source_document': change.document_path,
                'change_type': change.change_type,
                'total_affected': analysis.total_affected,
                'confidence': analysis.confidence,
                'estimated_effort': analysis.estimated_effort
            })
            
        self._save_impact_history()
        return analyses
        
    def get_impact_report(self) -> Dict[str, Any]:
        """Gera relatório consolidado de impactos"""
        analyses = self.batch_analyze_changes()
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_changes': len(analyses),
            'total_affected_documents': sum(a.total_affected for a in analyses),
            'high_impact_changes': len([a for a in analyses if any(n.impact_score > 0.7 for n in a.impact_tree)]),
            'critical_paths': [],
            'recommendations': [],
            'effort_estimate': '0 minutos'
        }
        
        # Consolidar caminhos críticos
        all_critical_paths = []
        for analysis in analyses:
            all_critical_paths.extend(analysis.critical_paths)
        report['critical_paths'] = all_critical_paths
        
        # Consolidar recomendações
        all_recommendations = []
        for analysis in analyses:
            all_recommendations.extend(analysis.recommendations)
        report['recommendations'] = list(set(all_recommendations))
        
        # Estimar esforço total
        total_effort_minutes = 0
        for analysis in analyses:
            if '15-30' in analysis.estimated_effort:
                total_effort_minutes += 22
            elif '30-60' in analysis.estimated_effort:
                total_effort_minutes += 45
            elif '1-2' in analysis.estimated_effort:
                total_effort_minutes += 90
            else:
                total_effort_minutes += 150
                
        if total_effort_minutes < 60:
            report['effort_estimate'] = f"{total_effort_minutes} minutos"
        else:
            hours = total_effort_minutes / 60
            report['effort_estimate'] = f"{hours:.1f} horas"
            
        return report

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(description='Context Navigator Impact Analyzer')
    parser.add_argument('--path', '-p', default='.', help='Caminho base do projeto')
    parser.add_argument('--document', '-d', help='Analisar impacto de documento específico')
    parser.add_argument('--changes', '-c', action='store_true', help='Analisar todas as mudanças')
    parser.add_argument('--report', '-r', action='store_true', help='Gerar relatório consolidado')
    parser.add_argument('--json', action='store_true', help='Saída em formato JSON')
    
    args = parser.parse_args()
    
    analyzer = ImpactAnalyzer(args.path)
    
    if args.document:
        analysis = analyzer.analyze_impact(args.document)
        
        if args.json:
            print(json.dumps({
                'source_document': analysis.source_document,
                'change_type': analysis.change_type,
                'total_affected': analysis.total_affected,
                'confidence': analysis.confidence,
                'estimated_effort': analysis.estimated_effort,
                'impact_tree': [
                    {
                        'document': node.document_path,
                        'type': node.document_type,
                        'impact_level': node.impact_level,
                        'impact_score': node.impact_score,
                        'reasons': node.impact_reasons,
                        'actions': node.suggested_actions
                    }
                    for node in analysis.impact_tree
                ]
            }, indent=2, ensure_ascii=False))
        else:
            print(f"\n=== ANÁLISE DE IMPACTO: {analysis.source_document} ===")
            print(f"Tipo de mudança: {analysis.change_type}")
            print(f"Total de documentos afetados: {analysis.total_affected}")
            print(f"Confiança: {analysis.confidence:.1%}")
            print(f"Esforço estimado: {analysis.estimated_effort}")
            
            print("\nDocumentos afetados:")
            for node in analysis.impact_tree:
                print(f"  📄 {node.document_path}")
                print(f"     Tipo: {node.document_type}")
                print(f"     Impacto: {node.impact_level} (score: {node.impact_score:.2f})")
                print(f"     Razões: {', '.join(node.impact_reasons)}")
                print(f"     Ações: {', '.join(node.suggested_actions)}")
                print()
                
    elif args.changes:
        analyses = analyzer.batch_analyze_changes()
        print(f"\n=== ANÁLISE DE MUDANÇAS ({len(analyses)} mudanças) ===")
        
        for analysis in analyses:
            print(f"\n📄 {analysis.source_document} ({analysis.change_type})")
            print(f"   Documentos afetados: {analysis.total_affected}")
            print(f"   Esforço estimado: {analysis.estimated_effort}")
            
    elif args.report:
        report = analyzer.get_impact_report()
        
        if args.json:
            print(json.dumps(report, indent=2, ensure_ascii=False))
        else:
            print("\n=== RELATÓRIO DE IMPACTOS ===")
            print(f"Total de mudanças: {report['total_changes']}")
            print(f"Total de documentos afetados: {report['total_affected_documents']}")
            print(f"Mudanças de alto impacto: {report['high_impact_changes']}")
            print(f"Esforço estimado total: {report['effort_estimate']}")
            
            if report['recommendations']:
                print("\nRecomendações:")
                for rec in report['recommendations']:
                    print(f"  - {rec}")
    else:
        print("Especifique --document, --changes ou --report")

if __name__ == '__main__':
    main() 