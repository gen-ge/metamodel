#!/usr/bin/env python3
"""
Context Navigator - Scanner Básico
Lê documentos da pasta metodológica, valida metadados e gera context maps
"""

import os
import sys
import yaml
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('context_scanner')

class ContextScanner:
    """Scanner que processa documentos da metodologia Context Navigator"""
    
    def __init__(self, base_path: str = "."):
        """
        Inicializa o scanner
        
        Args:
            base_path: Caminho base do projeto
        """
        self.base_path = Path(base_path)
        self.config = {}
        self.documents = {}
        self.context_maps = {}
        self.validation_errors = []
        self.conflicts = []
        
        # Carregar configuração
        self._load_config()
        
        # Configurar caminhos usando configuração do .contextrc
        scanner_config = self.config.get('scanner', {}).get('directories', {})
        
        # Usar configuração do .contextrc ou valores padrão
        self.docs_path = self.base_path / scanner_config.get('docs_path', 'docs')
        self.templates_path = self.base_path / scanner_config.get('templates_path', 'templates')
        self.context_maps_path = self.base_path / scanner_config.get('context_maps_path', '.context-map')
        self.examples_path = self.base_path / scanner_config.get('examples_path', 'examples')
        
        # Criar diretórios se necessário
        self.context_maps_path.mkdir(exist_ok=True)
        self.docs_path.mkdir(exist_ok=True)
        self.templates_path.mkdir(exist_ok=True)
        self.examples_path.mkdir(exist_ok=True)
        
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
            sys.exit(1)
            
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
            logger.info(f"Configuração carregada com sucesso de {config_file}")
        except Exception as e:
            logger.error(f"Erro ao carregar configuração: {e}")
            sys.exit(1)
            
    def _extract_front_matter(self, content: str) -> Tuple[Dict[str, Any], str]:
        """
        Extrai front matter YAML do conteúdo
        
        Args:
            content: Conteúdo do arquivo
            
        Returns:
            Tupla com (metadados, conteúdo_sem_front_matter)
        """
        if not content.startswith('---'):
            return {}, content
            
        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}, content
            
        try:
            metadata = yaml.safe_load(parts[1])
            content_without_fm = parts[2].strip()
            return metadata or {}, content_without_fm
        except yaml.YAMLError as e:
            logger.warning(f"Erro ao parsear front matter: {e}")
            return {}, content
            
    def _extract_inline_metadata(self, content: str) -> Dict[str, Any]:
        """
        Extrai metadados inline do formato <!-- CONTEXT_META ... -->
        
        Args:
            content: Conteúdo do arquivo
            
        Returns:
            Dicionário com metadados inline
        """
        pattern = r'<!-- CONTEXT_META\s*(.*?)\s*-->'
        matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
        
        inline_metadata = {}
        for match in matches:
            try:
                # Parse como YAML
                metadata = yaml.safe_load(match)
                if metadata:
                    inline_metadata.update(metadata)
            except yaml.YAMLError:
                # Se não for YAML válido, tenta parsear linha por linha
                lines = match.strip().split('\n')
                for line in lines:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        inline_metadata[key.strip()] = value.strip().strip('"\'')
                        
        return inline_metadata
        
    def _validate_required_fields(self, metadata: Dict[str, Any], file_path: str) -> List[str]:
        """
        Valida campos obrigatórios nos metadados
        
        Args:
            metadata: Metadados extraídos
            file_path: Caminho do arquivo
            
        Returns:
            Lista de erros de validação
        """
        errors = []
        required_fields = self.config.get('metadata', {}).get('required_fields', {})
        
        for field, field_config in required_fields.items():
            if field not in metadata:
                errors.append(f"{file_path}: Campo obrigatório '{field}' não encontrado")
                continue
                
            value = metadata[field]
            field_type = field_config.get('type', 'string')
            
            # Validar tipo
            if field_type == 'string' and not isinstance(value, str):
                errors.append(f"{file_path}: Campo '{field}' deve ser string")
            elif field_type == 'array' and not isinstance(value, list):
                errors.append(f"{file_path}: Campo '{field}' deve ser array")
            elif field_type == 'object' and not isinstance(value, dict):
                errors.append(f"{file_path}: Campo '{field}' deve ser object")
                
            # Validar valores permitidos
            allowed_values = field_config.get('values', [])
            if allowed_values and value not in allowed_values:
                errors.append(f"{file_path}: Campo '{field}' deve ser um de {allowed_values}")
                
        return errors
        
    def _validate_connections(self, metadata: Dict[str, Any], file_path: str) -> List[str]:
        """
        Valida conexões entre documentos
        
        Args:
            metadata: Metadados extraídos
            file_path: Caminho do arquivo
            
        Returns:
            Lista de erros de validação
        """
        errors = []
        connections = metadata.get('connections', {})
        
        if not isinstance(connections, dict):
            errors.append(f"{file_path}: 'connections' deve ser um objeto")
            return errors
            
        # Validar tipos de conexão conhecidos
        connection_types = self.config.get('connection_types', {})
        for conn_type, targets in connections.items():
            if conn_type not in connection_types:
                errors.append(f"{file_path}: Tipo de conexão '{conn_type}' não reconhecido")
                continue
                
            if not isinstance(targets, list):
                errors.append(f"{file_path}: Conexão '{conn_type}' deve ser uma lista")
                
        return errors
        
    def _validate_document_type(self, metadata: Dict[str, Any], file_path: str) -> List[str]:
        """
        Valida se o tipo de documento é válido
        
        Args:
            metadata: Metadados extraídos
            file_path: Caminho do arquivo
            
        Returns:
            Lista de erros de validação
        """
        errors = []
        doc_type = metadata.get('doc_type')
        
        if not doc_type:
            return errors  # Já validado em required_fields
            
        document_types = self.config.get('document_types', {})
        if doc_type not in document_types:
            errors.append(f"{file_path}: Tipo de documento '{doc_type}' não reconhecido")
            
        return errors
        
    def _validate_context(self, metadata: Dict[str, Any], file_path: str) -> List[str]:
        """
        Valida contexto hierárquico e especializado
        
        Args:
            metadata: Metadados extraídos
            file_path: Caminho do arquivo
            
        Returns:
            Lista de erros de validação
        """
        errors = []
        
        context_level = metadata.get('context_level')
        context_type = metadata.get('context_type')
        
        # Validar context_level
        if context_level:
            hierarchical_contexts = self.config.get('contexts', {}).get('hierarchical', {})
            if context_level not in hierarchical_contexts:
                errors.append(f"{file_path}: context_level '{context_level}' não reconhecido")
                
        # Validar context_type
        if context_type:
            specialized_contexts = self.config.get('contexts', {}).get('specialized', {})
            if context_type not in specialized_contexts:
                errors.append(f"{file_path}: context_type '{context_type}' não reconhecido")
                
        return errors
        
    def _detect_conflicts(self) -> List[Dict[str, Any]]:
        """
        Detecta conflitos entre documentos
        
        Returns:
            Lista de conflitos detectados
        """
        conflicts = []
        
        # Detectar referências duplicadas
        component_refs = {}
        for file_path, doc_data in self.documents.items():
            connections = doc_data['metadata'].get('connections', {})
            for conn_type, targets in connections.items():
                for target in targets:
                    if target not in component_refs:
                        component_refs[target] = []
                    component_refs[target].append((file_path, conn_type))
                    
        for component, refs in component_refs.items():
            if len(refs) > 1:
                ref_types = set(ref[1] for ref in refs)
                if len(ref_types) > 1:
                    conflicts.append({
                        'type': 'duplicate_references',
                        'component': component,
                        'references': refs,
                        'severity': 'warning'
                    })
                    
        # Detectar dependências circulares
        def has_circular_dependency(doc_path: str, target: str, visited: set) -> bool:
            if target in visited:
                return True
            if target not in self.documents:
                return False
                
            visited.add(target)
            target_doc = self.documents[target]
            depends_on = target_doc['metadata'].get('connections', {}).get('depends_on', [])
            
            for dep in depends_on:
                if has_circular_dependency(doc_path, dep, visited.copy()):
                    return True
            return False
            
        for file_path, doc_data in self.documents.items():
            depends_on = doc_data['metadata'].get('connections', {}).get('depends_on', [])
            for dep in depends_on:
                if has_circular_dependency(file_path, dep, set()):
                    conflicts.append({
                        'type': 'circular_dependency',
                        'source': file_path,
                        'target': dep,
                        'severity': 'error'
                    })
                    
        # Detectar documentos órfãos
        referenced_docs = set()
        for doc_data in self.documents.values():
            connections = doc_data['metadata'].get('connections', {})
            for targets in connections.values():
                referenced_docs.update(targets)
                
        for file_path in self.documents:
            has_outbound = any(
                targets for targets in 
                self.documents[file_path]['metadata'].get('connections', {}).values()
            )
            has_inbound = file_path in referenced_docs
            
            if not has_outbound and not has_inbound:
                conflicts.append({
                    'type': 'orphaned_document',
                    'document': file_path,
                    'severity': 'info'
                })
                
        return conflicts
        
    def scan_documents(self) -> None:
        """Escaneia todos os documentos nas pastas configuradas"""
        logger.info("Iniciando escaneamento de documentos...")
        
        # Pastas para escanear
        scan_paths = [
            self.docs_path,
            self.templates_path,
            self.examples_path
        ]
        
        for scan_path in scan_paths:
            self._scan_directory(scan_path)
            
        logger.info(f"Escaneamento concluído. {len(self.documents)} documentos processados")
        
    def _scan_directory(self, directory: Path) -> None:
        """
        Escaneia uma pasta específica
        
        Args:
            directory: Pasta para escanear
        """
        for file_path in directory.rglob("*.md"):
            if file_path.name.startswith('.'):
                continue  # Pular arquivos ocultos
                
            try:
                self._process_document(file_path)
            except Exception as e:
                logger.error(f"Erro ao processar {file_path}: {e}")
                
    def _process_document(self, file_path: Path) -> None:
        """
        Processa um documento individual
        
        Args:
            file_path: Caminho do arquivo
        """
        relative_path = file_path.relative_to(self.base_path)
        logger.debug(f"Processando: {relative_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            logger.error(f"Erro ao ler {relative_path}: {e}")
            return
            
        # Extrair metadados
        front_matter, content_without_fm = self._extract_front_matter(content)
        inline_metadata = self._extract_inline_metadata(content)
        
        # Combinar metadados (front matter tem prioridade)
        metadata = {**inline_metadata, **front_matter}
        
        # Validar documento
        errors = []
        errors.extend(self._validate_required_fields(metadata, str(relative_path)))
        errors.extend(self._validate_connections(metadata, str(relative_path)))
        errors.extend(self._validate_document_type(metadata, str(relative_path)))
        errors.extend(self._validate_context(metadata, str(relative_path)))
        
        self.validation_errors.extend(errors)
        
        # Armazenar documento processado
        self.documents[str(relative_path)] = {
            'path': str(relative_path),
            'absolute_path': str(file_path),
            'metadata': metadata,
            'content': content_without_fm,
            'size': file_path.stat().st_size,
            'modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
            'validation_errors': errors
        }
        
    def generate_context_maps(self) -> None:
        """Gera os mapas de contexto"""
        logger.info("Gerando mapas de contexto...")
        
        # Detectar conflitos
        self.conflicts = self._detect_conflicts()
        
        # Gerar index.yml
        self._generate_index_map()
        
        # Gerar architecture.yml
        self._generate_architecture_map()
        
        # Gerar connections.yml
        self._generate_connections_map()
        
        # Gerar conflicts.yml
        self._generate_conflicts_map()
        
        # Gerar relatório de validação
        self._generate_validation_report()
        
        logger.info("Mapas de contexto gerados com sucesso")
        
    def _generate_index_map(self) -> None:
        """Gera o mapa índice geral"""
        index_data = {
            'project': self.config.get('project', {}),
            'methodology': self.config.get('methodology', {}),
            'scan_info': {
                'timestamp': datetime.now().isoformat(),
                'total_documents': len(self.documents),
                'validation_errors': len(self.validation_errors),
                'conflicts': len(self.conflicts)
            },
            'document_summary': {},
            'context_distribution': {},
            'type_distribution': {}
        }
        
        # Resumo por tipo de documento
        for doc_data in self.documents.values():
            doc_type = doc_data['metadata'].get('doc_type', 'unknown')
            if doc_type not in index_data['type_distribution']:
                index_data['type_distribution'][doc_type] = 0
            index_data['type_distribution'][doc_type] += 1
            
        # Distribuição por contexto
        for doc_data in self.documents.values():
            context_level = doc_data['metadata'].get('context_level', 'unknown')
            if context_level not in index_data['context_distribution']:
                index_data['context_distribution'][context_level] = 0
            index_data['context_distribution'][context_level] += 1
            
        # Resumo de documentos
        for path, doc_data in self.documents.items():
            index_data['document_summary'][path] = {
                'type': doc_data['metadata'].get('doc_type'),
                'title': doc_data['metadata'].get('title'),
                'context_level': doc_data['metadata'].get('context_level'),
                'context_type': doc_data['metadata'].get('context_type'),
                'module': doc_data['metadata'].get('module'),
                'status': doc_data['metadata'].get('status'),
                'last_updated': doc_data['metadata'].get('last_updated'),
                'has_errors': len(doc_data['validation_errors']) > 0
            }
            
        self._save_context_map('index.yml', index_data)
        
    def _generate_architecture_map(self) -> None:
        """Gera o mapa arquitetural"""
        architecture_data = {
            'contexts': {
                'hierarchical': {},
                'specialized': {}
            },
            'modules': {},
            'components': {},
            'patterns': {}
        }
        
        # Agrupar por contexto hierárquico
        for doc_data in self.documents.values():
            context_level = doc_data['metadata'].get('context_level')
            if context_level:
                if context_level not in architecture_data['contexts']['hierarchical']:
                    architecture_data['contexts']['hierarchical'][context_level] = []
                architecture_data['contexts']['hierarchical'][context_level].append({
                    'path': doc_data['path'],
                    'title': doc_data['metadata'].get('title'),
                    'type': doc_data['metadata'].get('doc_type'),
                    'module': doc_data['metadata'].get('module')
                })
                
        # Agrupar por contexto especializado
        for doc_data in self.documents.values():
            context_type = doc_data['metadata'].get('context_type')
            if context_type:
                if context_type not in architecture_data['contexts']['specialized']:
                    architecture_data['contexts']['specialized'][context_type] = []
                architecture_data['contexts']['specialized'][context_type].append({
                    'path': doc_data['path'],
                    'title': doc_data['metadata'].get('title'),
                    'type': doc_data['metadata'].get('doc_type'),
                    'module': doc_data['metadata'].get('module')
                })
                
        # Agrupar por módulos
        for doc_data in self.documents.values():
            module = doc_data['metadata'].get('module')
            if module:
                if module not in architecture_data['modules']:
                    architecture_data['modules'][module] = []
                architecture_data['modules'][module].append({
                    'path': doc_data['path'],
                    'title': doc_data['metadata'].get('title'),
                    'type': doc_data['metadata'].get('doc_type'),
                    'context_level': doc_data['metadata'].get('context_level'),
                    'context_type': doc_data['metadata'].get('context_type')
                })
                
        self._save_context_map('architecture.yml', architecture_data)
        
    def _generate_connections_map(self) -> None:
        """Gera o mapa de conexões"""
        connections_data = {
            'graph': {},
            'connection_types': {},
            'strong_coupling': [],
            'weak_coupling': [],
            'isolated_components': []
        }
        
        # Construir grafo de conexões
        for doc_path, doc_data in self.documents.items():
            connections = doc_data['metadata'].get('connections', {})
            connections_data['graph'][doc_path] = connections
            
            # Contar por tipo de conexão
            for conn_type, targets in connections.items():
                if conn_type not in connections_data['connection_types']:
                    connections_data['connection_types'][conn_type] = 0
                connections_data['connection_types'][conn_type] += len(targets)
                
        # Analisar acoplamento
        for doc_path, doc_data in self.documents.items():
            connections = doc_data['metadata'].get('connections', {})
            total_connections = sum(len(targets) for targets in connections.values())
            
            if total_connections >= 3:
                connections_data['strong_coupling'].append({
                    'document': doc_path,
                    'connection_count': total_connections
                })
            elif total_connections >= 1:
                connections_data['weak_coupling'].append({
                    'document': doc_path,
                    'connection_count': total_connections
                })
            else:
                connections_data['isolated_components'].append(doc_path)
                
        self._save_context_map('connections.yml', connections_data)
        
    def _generate_conflicts_map(self) -> None:
        """Gera o mapa de conflitos"""
        conflicts_data = {
            'summary': {
                'total_conflicts': len(self.conflicts),
                'by_severity': {},
                'by_type': {}
            },
            'conflicts': self.conflicts
        }
        
        # Estatísticas por severidade
        for conflict in self.conflicts:
            severity = conflict.get('severity', 'unknown')
            if severity not in conflicts_data['summary']['by_severity']:
                conflicts_data['summary']['by_severity'][severity] = 0
            conflicts_data['summary']['by_severity'][severity] += 1
            
        # Estatísticas por tipo
        for conflict in self.conflicts:
            conflict_type = conflict.get('type', 'unknown')
            if conflict_type not in conflicts_data['summary']['by_type']:
                conflicts_data['summary']['by_type'][conflict_type] = 0
            conflicts_data['summary']['by_type'][conflict_type] += 1
            
        self._save_context_map('conflicts.yml', conflicts_data)
        
    def _generate_validation_report(self) -> None:
        """Gera relatório de validação"""
        validation_data = {
            'summary': {
                'total_documents': len(self.documents),
                'documents_with_errors': len([d for d in self.documents.values() if d['validation_errors']]),
                'total_errors': len(self.validation_errors)
            },
            'errors_by_type': {},
            'errors_by_document': {},
            'validation_details': []
        }
        
        # Agrupar erros por tipo
        for error in self.validation_errors:
            error_type = error.split(':')[1].strip().split()[0] if ':' in error else 'unknown'
            if error_type not in validation_data['errors_by_type']:
                validation_data['errors_by_type'][error_type] = 0
            validation_data['errors_by_type'][error_type] += 1
            
        # Agrupar erros por documento
        for doc_path, doc_data in self.documents.items():
            if doc_data['validation_errors']:
                validation_data['errors_by_document'][doc_path] = doc_data['validation_errors']
                
        # Detalhes de validação
        for doc_path, doc_data in self.documents.items():
            validation_data['validation_details'].append({
                'document': doc_path,
                'valid': len(doc_data['validation_errors']) == 0,
                'error_count': len(doc_data['validation_errors']),
                'errors': doc_data['validation_errors']
            })
            
        self._save_context_map('validation.json', validation_data, format='json')
        
    def _save_context_map(self, filename: str, data: Dict[str, Any], format: str = 'yaml') -> None:
        """
        Salva um mapa de contexto
        
        Args:
            filename: Nome do arquivo
            data: Dados para salvar
            format: Formato do arquivo (yaml ou json)
        """
        file_path = self.context_maps_path / filename
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                if format == 'json':
                    json.dump(data, f, indent=2, ensure_ascii=False)
                else:
                    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
            logger.debug(f"Salvo: {file_path}")
        except Exception as e:
            logger.error(f"Erro ao salvar {file_path}: {e}")
            
    def print_summary(self) -> None:
        """Imprime resumo do escaneamento"""
        print("\n" + "="*60)
        print("CONTEXT NAVIGATOR - RESUMO DO ESCANEAMENTO")
        print("="*60)
        
        print(f"\n📄 DOCUMENTOS PROCESSADOS: {len(self.documents)}")
        
        # Distribuição por tipo
        type_dist = {}
        for doc_data in self.documents.values():
            doc_type = doc_data['metadata'].get('doc_type', 'unknown')
            type_dist[doc_type] = type_dist.get(doc_type, 0) + 1
            
        print("\n📊 DISTRIBUIÇÃO POR TIPO:")
        for doc_type, count in sorted(type_dist.items()):
            print(f"   {doc_type}: {count}")
            
        # Validação
        print(f"\n✅ VALIDAÇÃO:")
        docs_with_errors = len([d for d in self.documents.values() if d['validation_errors']])
        print(f"   Documentos válidos: {len(self.documents) - docs_with_errors}")
        print(f"   Documentos com erros: {docs_with_errors}")
        print(f"   Total de erros: {len(self.validation_errors)}")
        
        # Conflitos
        print(f"\n⚠️  CONFLITOS:")
        print(f"   Total de conflitos: {len(self.conflicts)}")
        if self.conflicts:
            conflict_types = {}
            for conflict in self.conflicts:
                conflict_type = conflict.get('type', 'unknown')
                conflict_types[conflict_type] = conflict_types.get(conflict_type, 0) + 1
            for conflict_type, count in sorted(conflict_types.items()):
                print(f"   {conflict_type}: {count}")
                
        # Mapas gerados
        print(f"\n📁 MAPAS DE CONTEXTO:")
        map_files = list(self.context_maps_path.glob('*'))
        for map_file in sorted(map_files):
            print(f"   {map_file.name}")
            
        print("\n" + "="*60)
        
        # Mostrar erros se houver
        if self.validation_errors:
            print("\n❌ ERROS DE VALIDAÇÃO:")
            for error in self.validation_errors[:10]:  # Mostrar apenas os primeiros 10
                print(f"   {error}")
            if len(self.validation_errors) > 10:
                print(f"   ... e mais {len(self.validation_errors) - 10} erros")
                
    def run(self) -> int:
        """
        Executa o scanner completo
        
        Returns:
            Código de saída (0 para sucesso, 1 para erro)
        """
        try:
            self.scan_documents()
            self.generate_context_maps()
            self.print_summary()
            
            # Retornar código de erro se houver problemas críticos
            critical_errors = [e for e in self.validation_errors if 'obrigatório' in e]
            critical_conflicts = [c for c in self.conflicts if c.get('severity') == 'error']
            
            if critical_errors or critical_conflicts:
                logger.warning("Scanner concluído com problemas críticos")
                return 1
            else:
                logger.info("Scanner concluído com sucesso")
                return 0
                
        except Exception as e:
            logger.error(f"Erro durante escaneamento: {e}")
            return 1

def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Context Navigator Scanner')
    parser.add_argument('--path', '-p', default='.', 
                       help='Caminho base do projeto (padrão: diretório atual)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Modo verboso')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        
    scanner = ContextScanner(args.path)
    return scanner.run()

if __name__ == '__main__':
    sys.exit(main()) 