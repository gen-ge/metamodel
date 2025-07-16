#!/usr/bin/env python3

# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component cn-component-parser
# @cn:doc cn-component-parser.md
# @cn:context-level c3_component
# @cn:context-type core
# @cn:parent-module cli-interface
# @cn:purpose "Parser para extrair e validar marcações @cn: em arquivos de código"
# @cn:memory-aid "Extrator de marcações - lê código e identifica todas as anotações @cn:"
# @cn:depends-on PROTOCOLO_MARCACAO_CN.md
# @cn:impacts component-map-generation, validation-process
# @cn:provides annotation-extraction, metadata-parsing, validation-support
# @cn:component-type functional
# @cn:responsibility annotation-processing
# @cn:single-purpose true
# ============================================

"""
CN Component Parser - Extrator de Marcações @cn:
Analisa arquivos de código e extrai todas as marcações @cn: para mapeamento de componentes
"""

import re
import os
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('cn_parser')

@dataclass
class CNAnnotation:
    """Representação de uma marcação @cn:"""
    # @cn:class business-entity
    # @cn:responsibility data-structure
    field: str          # Campo da marcação (ex: 'component', 'doc', 'purpose')
    value: str          # Valor da marcação
    line_number: int    # Linha onde foi encontrada
    raw_line: str       # Linha completa original

@dataclass
class ComponentHeader:
    """Cabeçalho Context Bridge extraído"""
    # @cn:class business-entity  
    # @cn:responsibility data-structure
    component_type: str      # system, module ou component
    component_name: str      # Nome do componente
    doc_file: str           # Arquivo de documentação
    context_level: str      # c1_root, c2_module, c3_component
    context_type: str       # core, api, data, ui, etc.
    purpose: str            # Propósito do componente
    memory_aid: str         # Auxiliar de memória
    annotations: List[CNAnnotation]  # Todas as marcações encontradas
    file_path: str          # Arquivo onde foi encontrado
    start_line: int         # Linha inicial do cabeçalho
    end_line: int           # Linha final do cabeçalho

class CNComponentParser:
    """Parser principal para marcações @cn:"""
    
    # @cn:class service
    # @cn:responsibility annotation-parsing
    # @cn:single-purpose true
    
    def __init__(self):
        # @cn:function core
        # @cn:process initialization
        self.pattern_cn = re.compile(r'#\s*@cn:(\S+)\s+(.*)')
        self.header_start = re.compile(r'#\s*=+\s*CONTEXT NAVIGATOR CODE BRIDGE\s*=+')
        self.header_end = re.compile(r'#\s*=+')
        
        # NOVO: Suporte à arquitetura global
        if self._is_global_workspace():
            self._init_global_workspace()
        else:
            self._init_legacy_local()
            
    def _is_global_workspace(self) -> bool:
        """Verifica se está rodando na nova arquitetura global"""
        return (
            'CN_WORKSPACE_ROOT' in os.environ and 
            'CN_OUTPUT_DIR' in os.environ
        )
        
    def _init_global_workspace(self):
        """Inicializa para arquitetura global workspace"""
        self.workspace_root = Path(os.environ['CN_WORKSPACE_ROOT'])
        self.output_dir = Path(os.environ['CN_OUTPUT_DIR'])
        logger.info(f"🌐 Modo Global - Workspace: {self.workspace_root}")
        
    def _init_legacy_local(self):
        """Inicializa para arquitetura local legada"""
        logger.info(f"📁 Modo Legado")
        
    # @cn:function critical
    # @cn:process file-parsing
    # @cn:step 1
    def parse_file(self, file_path: str) -> Optional[ComponentHeader]:
        """
        Analisa arquivo e extrai cabeçalho Context Bridge
        
        Args:
            file_path: Caminho do arquivo para analisar
            
        Returns:
            ComponentHeader ou None se não encontrado
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            return self._extract_header(lines, file_path)
            
        except Exception as e:
            logger.error(f"Erro ao analisar {file_path}: {e}")
            return None
    
    # @cn:function core
    # @cn:process header-extraction
    # @cn:step 2
    def _extract_header(self, lines: List[str], file_path: str) -> Optional[ComponentHeader]:
        """Extrai cabeçalho Context Bridge das linhas do arquivo"""
        
        # Encontrar início e fim do cabeçalho
        header_start_line = None
        header_end_line = None
        
        for i, line in enumerate(lines):
            if self.header_start.match(line):
                header_start_line = i
            elif header_start_line is not None and self.header_end.match(line) and i > header_start_line:
                header_end_line = i
                break
        
        if header_start_line is None:
            logger.debug(f"Cabeçalho Context Bridge não encontrado em {file_path}")
            return None
            
        if header_end_line is None:
            header_end_line = len(lines)
        
        # Extrair marcações do cabeçalho
        header_lines = lines[header_start_line:header_end_line + 1]
        annotations = self._parse_annotations(header_lines, header_start_line)
        
        if not annotations:
            logger.warning(f"Nenhuma marcação @cn: encontrada no cabeçalho de {file_path}")
            return None
            
        # Construir ComponentHeader
        return self._build_component_header(annotations, file_path, header_start_line, header_end_line)
    
    # @cn:function core
    # @cn:process annotation-parsing
    # @cn:step 3
    def _parse_annotations(self, lines: List[str], start_line: int) -> List[CNAnnotation]:
        """Extrai todas as marcações @cn: das linhas"""
        annotations = []
        
        for i, line in enumerate(lines):
            match = self.pattern_cn.match(line.strip())
            if match:
                field = match.group(1)
                value = match.group(2).strip('"')  # Remove aspas se existirem
                
                annotation = CNAnnotation(
                    field=field,
                    value=value,
                    line_number=start_line + i + 1,
                    raw_line=line.strip()
                )
                annotations.append(annotation)
                
        return annotations
    
    # @cn:function core  
    # @cn:process header-building
    # @cn:step 4
    def _build_component_header(self, annotations: List[CNAnnotation], file_path: str, 
                              start_line: int, end_line: int) -> ComponentHeader:
        """Constrói ComponentHeader a partir das marcações"""
        
        # Extrair campos obrigatórios
        component_info = self._extract_component_info(annotations)
        
        return ComponentHeader(
            component_type=component_info.get('type', 'unknown'),
            component_name=component_info.get('name', 'unnamed'),
            doc_file=component_info.get('doc', ''),
            context_level=component_info.get('context-level', ''),
            context_type=component_info.get('context-type', ''),
            purpose=component_info.get('purpose', ''),
            memory_aid=component_info.get('memory-aid', ''),
            annotations=annotations,
            file_path=file_path,
            start_line=start_line + 1,
            end_line=end_line + 1
        )
    
    # @cn:function integration
    # @cn:process field-extraction
    def _extract_component_info(self, annotations: List[CNAnnotation]) -> Dict[str, str]:
        """Extrai informações principais das marcações"""
        info = {}
        
        for annotation in annotations:
            field = annotation.field
            value = annotation.value
            
            # Identificar tipo de componente
            if field in ['system', 'module', 'component']:
                info['type'] = field
                info['name'] = value
            else:
                info[field] = value
                
        return info
    
    # @cn:function critical
    # @cn:process directory-scanning
    def parse_directory(self, directory: str, extensions: Optional[List[str]] = None) -> Dict[str, ComponentHeader]:
        """
        Analisa todos os arquivos de um diretório
        
        Args:
            directory: Diretório para analisar
            extensions: Extensões de arquivo para incluir (padrão: ['.py'])
            
        Returns:
            Dicionário {file_path: ComponentHeader}
        """
        if extensions is None:
            extensions = ['.py']
            
        components = {}
        directory_path = Path(directory)
        
        if not directory_path.exists():
            logger.error(f"Diretório não encontrado: {directory}")
            return components
        
        # @cn:process recursive-search
        for file_path in directory_path.rglob('*'):
            if file_path.suffix in extensions and file_path.is_file():
                header = self.parse_file(str(file_path))
                if header:
                    components[str(file_path)] = header
                    logger.info(f"Componente encontrado: {header.component_name} em {file_path}")
        
        return components
    
    # @cn:function validation
    # @cn:process header-validation
    def validate_header(self, header: ComponentHeader) -> List[str]:
        """
        Valida cabeçalho Context Bridge
        
        Returns:
            Lista de erros encontrados (vazia se válido)
        """
        errors = []
        
        # Campos obrigatórios
        required_fields = {
            'component_name': 'Nome do componente',
            'doc_file': 'Arquivo de documentação (@cn:doc)',
            'context_level': 'Nível de contexto (@cn:context-level)',
            'context_type': 'Tipo de contexto (@cn:context-type)',
            'purpose': 'Propósito (@cn:purpose)',
            'memory_aid': 'Auxiliar de memória (@cn:memory-aid)'
        }
        
        for field, description in required_fields.items():
            value = getattr(header, field, '').strip()
            if not value:
                errors.append(f"Campo obrigatório ausente: {description}")
        
        # Validar valores específicos
        if header.context_level not in ['c1_root', 'c2_module', 'c3_component']:
            errors.append(f"context-level inválido: {header.context_level}")
            
        valid_context_types = ['core', 'api', 'data', 'ui', 'interface', 'validation', 'integration']
        if header.context_type not in valid_context_types:
            errors.append(f"context-type inválido: {header.context_type}")
        
        # Validar hierarquia
        if header.component_type == 'component' and header.context_level != 'c3_component':
            errors.append("@cn:component deve ter context-level c3_component")
            
        if header.component_type == 'module' and header.context_level != 'c2_module':
            errors.append("@cn:module deve ter context-level c2_module")
            
        if header.component_type == 'system' and header.context_level != 'c1_root':
            errors.append("@cn:system deve ter context-level c1_root")
        
        return errors
    
    # @cn:function integration
    # @cn:process component-map-generation
    def generate_component_map(self, components: Dict[str, ComponentHeader]) -> Dict[str, Any]:
        """
        Gera mapa de componentes em formato YAML
        
        Args:
            components: Dicionário de componentes analisados
            
        Returns:
            Estrutura do component-map.yml
        """
        component_map = {
            'generated_by': 'cn-component-parser',
            'generated_at': '',
            'total_components': len(components),
            'systems': {},
            'modules': {},
            'components': {}
        }
        
        # Organizar por tipo
        for file_path, header in components.items():
            component_data = {
                'name': header.component_name,
                'doc': header.doc_file,
                'context_level': header.context_level,
                'context_type': header.context_type,
                'purpose': header.purpose,
                'file': file_path,
                'lines': f"{header.start_line}-{header.end_line}"
            }
            
            if header.component_type == 'system':
                component_map['systems'][header.component_name] = component_data
            elif header.component_type == 'module':
                component_map['modules'][header.component_name] = component_data
            elif header.component_type == 'component':
                component_map['components'][header.component_name] = component_data
        
        return component_map
    
    # @cn:function integration
    # @cn:process report-generation
    def generate_report(self, components: Dict[str, ComponentHeader]) -> str:
        """Gera relatório textual dos componentes encontrados"""
        
        report = []
        report.append("# 📊 Relatório de Componentes Context Navigator\n")
        
        # Estatísticas gerais
        total = len(components)
        systems = sum(1 for h in components.values() if h.component_type == 'system')
        modules = sum(1 for h in components.values() if h.component_type == 'module')
        components_count = sum(1 for h in components.values() if h.component_type == 'component')
        
        report.append(f"**Total de Componentes:** {total}")
        report.append(f"- Sistemas (c1_root): {systems}")
        report.append(f"- Módulos (c2_module): {modules}")
        report.append(f"- Componentes (c3_component): {components_count}\n")
        
        # Listar componentes por tipo
        for component_type in ['system', 'module', 'component']:
            filtered = {k: v for k, v in components.items() if v.component_type == component_type}
            if filtered:
                report.append(f"## 🏗️ {component_type.title()}s\n")
                for file_path, header in filtered.items():
                    report.append(f"### {header.component_name}")
                    report.append(f"- **Arquivo:** `{file_path}`")
                    report.append(f"- **Documentação:** `{header.doc_file}`")
                    report.append(f"- **Contexto:** {header.context_level} / {header.context_type}")
                    report.append(f"- **Propósito:** {header.purpose}")
                    report.append(f"- **Linhas:** {header.start_line}-{header.end_line}\n")
        
        return "\n".join(report)

# @cn:function entry-point
# @cn:process cli-interface
def main():
    """Função principal para uso via linha de comando"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Parser de marcações @cn:')
    parser.add_argument('path', nargs='?', default='.', help='Arquivo ou diretório para analisar (padrão: .)')
    parser.add_argument('--format', choices=['yaml', 'json', 'report'], default='yaml',
                       help='Formato de saída (padrão: yaml)')
    parser.add_argument('--validate', action='store_true', 
                       help='Validar cabeçalhos encontrados')
    parser.add_argument('--output', help='Arquivo de saída (opcional, padrão: .cn_model/maps/component-map.yml)')
    
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
    
    # Determinar path de saída baseado no workspace
    if not args.output:
        maps_dir = current_workspace.root_path / ".cn_model" / "maps"
        maps_dir.mkdir(parents=True, exist_ok=True)
        if args.format == 'yaml':
            args.output = maps_dir / "component-map.yml"
        elif args.format == 'json':
            args.output = maps_dir / "component-map.json"
        else:
            args.output = maps_dir / "component-report.txt"
    
    cn_parser = CNComponentParser()
    
    # Analisar baseado no workspace root (ignora .cn_model)
    search_path = current_workspace.root_path / args.path if not Path(args.path).is_absolute() else Path(args.path)
    
    if search_path.is_file():
        header = cn_parser.parse_file(str(search_path))
        if header:
            components = {str(search_path): header}
        else:
            components = {}
    else:
        # Filtrar .cn_model das buscas
        components = {}
        for root, dirs, files in os.walk(search_path):
            # Ignorar .cn_model
            if '.cn_model' in dirs:
                dirs.remove('.cn_model')
            
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.md')):
                    file_path = os.path.join(root, file)
                    header = cn_parser.parse_file(file_path)
                    if header:
                        components[file_path] = header
    
    if not components:
        print(f"❌ Nenhum componente Context Navigator encontrado em {search_path}")
        return 0
    
    # Validar se solicitado
    if args.validate:
        print("🔍 Validando componentes...\n")
        for file_path, header in components.items():
            errors = cn_parser.validate_header(header)
            if errors:
                print(f"❌ {header.component_name} ({file_path}):")
                for error in errors:
                    print(f"   - {error}")
            else:
                print(f"✅ {header.component_name} ({file_path})")
        print()
    
    # Gerar saída
    if args.format == 'yaml':
        component_map = cn_parser.generate_component_map(components)
        import datetime
        component_map['generated_at'] = datetime.datetime.now().isoformat()
        output = yaml.dump(component_map, default_flow_style=False, sort_keys=False)
    elif args.format == 'json':
        component_map = cn_parser.generate_component_map(components)
        import json
        output = json.dumps(component_map, indent=2)
    else:  # report
        output = cn_parser.generate_report(components)
    
    # Salvar ou imprimir
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"📄 Resultado salvo em {args.output}")
    else:
        print(output)

if __name__ == '__main__':
    main() 