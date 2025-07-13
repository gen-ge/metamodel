#!/usr/bin/env python3
"""
Context Navigator - Template Validator
Validador especializado que realiza validações profundas e específicas
para cada tipo de template da metodologia Context Navigator.
"""

import os
import sys
import yaml
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass
from enum import Enum
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('template_validator')

class ValidationSeverity(Enum):
    """Severidade das validações"""
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    SUCCESS = "success"

@dataclass
class ValidationResult:
    """Resultado de uma validação específica"""
    rule_name: str
    severity: ValidationSeverity
    message: str
    line_number: Optional[int] = None
    suggestion: Optional[str] = None
    auto_fixable: bool = False

@dataclass
class TemplateValidationReport:
    """Relatório completo de validação de template"""
    template_type: str
    file_path: str
    overall_score: float
    results: List[ValidationResult]
    metadata_validation: Dict[str, Any]
    structure_validation: Dict[str, Any]
    content_validation: Dict[str, Any]
    completeness_score: float
    quality_score: float

class TemplateValidator:
    """Validador especializado para templates do Context Navigator"""
    
    def __init__(self, base_path: str = "."):
        """
        Inicializa o validador
        
        Args:
            base_path: Caminho base do projeto
        """
        self.base_path = Path(base_path)
        self.config = {}
        
        # Carregar configuração
        self._load_config()
        
        # Inicializar regras de validação por template
        self._init_validation_rules()
        
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
            
    def _init_validation_rules(self) -> None:
        """Inicializa regras de validação específicas por template"""
        
        # Regras para template DECISÃO
        self.decision_rules = {
            'required_sections': [
                'contexto e problema', 'análise detalhada', 'opções consideradas', 
                'decisão final', 'impactos e consequências'
            ],
            'min_options': 2,
            'required_subsections': {
                'contexto e problema': ['situação atual', 'problema identificado', 'motivação'],
                'opções consideradas': ['prós', 'contras', 'esforço', 'risco'],
                'decisão final': ['justificativa', 'fatores decisivos'],
                'impactos e consequências': ['impactos positivos', 'impactos negativos']
            },
            'quality_indicators': ['trade-off', 'alternativa', 'justificativa', 'consequência']
        }
        
        # Regras para template PROCESSO
        self.process_rules = {
            'required_sections': [
                'objetivo', 'pré-requisitos', 'procedimento principal', 
                'validação e testes', 'troubleshooting'
            ],
            'min_steps': 3,
            'required_subsections': {
                'pré-requisitos': ['conhecimentos necessários', 'ferramentas obrigatórias'],
                'procedimento principal': ['passo', 'validação', 'resultado esperado'],
                'troubleshooting': ['problemas comuns', 'sintomas', 'solução']
            },
            'quality_indicators': ['comando', 'verificação', 'teste', 'validação']
        }
        
        # Regras para template REFERÊNCIA
        self.reference_rules = {
            'required_sections': [
                'overview', 'configuração e setup', 'referência detalhada', 
                'exemplos práticos', 'versionamento'
            ],
            'min_examples': 2,
            'required_subsections': {
                'overview': ['propósito', 'escopo', 'audiência alvo'],
                'referência detalhada': ['parâmetros', 'resposta', 'códigos de status'],
                'exemplos práticos': ['código', 'resultado']
            },
            'quality_indicators': ['endpoint', 'parâmetro', 'exemplo', 'response']
        }
        
        # Regras para template ARQUITETURA
        self.architecture_rules = {
            'required_sections': [
                'contexto arquitetural', 'visão arquitetural', 'componentes arquiteturais',
                'fluxos arquiteturais', 'decisões arquiteturais'
            ],
            'min_components': 2,
            'required_subsections': {
                'contexto arquitetural': ['visão geral', 'objetivos', 'restrições'],
                'componentes arquiteturais': ['responsabilidade', 'interfaces', 'tecnologias'],
                'fluxos arquiteturais': ['sequência', 'passos detalhados']
            },
            'quality_indicators': ['componente', 'fluxo', 'padrão', 'arquitetura']
        }
        
        # Regras para template ANÁLISE
        self.analysis_rules = {
            'required_sections': [
                'situação e contexto', 'metodologia e coleta de dados', 
                'dados e evidências', 'análise detalhada', 'descobertas e insights',
                'ações recomendadas'
            ],
            'min_findings': 2,
            'required_subsections': {
                'metodologia e coleta de dados': ['metodologia aplicada', 'fontes de dados'],
                'dados e evidências': ['dados quantitativos', 'dados qualitativos'],
                'análise detalhada': ['root cause', 'correlação'],
                'ações recomendadas': ['ações imediatas', 'prioridade', 'esforço']
            },
            'quality_indicators': ['métrica', 'evidência', 'correlação', 'análise']
        }
        
        # Regras para template PLANEJAMENTO
        self.planning_rules = {
            'required_sections': [
                'objetivos e visão', 'escopo e entregas', 'cronograma e marcos',
                'recursos e equipe', 'riscos e dependências', 'métricas e monitoramento'
            ],
            'min_milestones': 2,
            'required_subsections': {
                'objetivos e visão': ['objetivos smart', 'resultados esperados'],
                'cronograma e marcos': ['marcos principais', 'fases do projeto'],
                'recursos e equipe': ['estrutura da equipe', 'orçamento detalhado'],
                'riscos e dependências': ['análise de riscos', 'dependências críticas']
            },
            'quality_indicators': ['objetivo', 'marco', 'cronograma', 'orçamento']
        }
        
    def _extract_sections(self, content: str) -> Dict[str, Dict[str, Any]]:
        """
        Extrai seções e subseções do documento
        
        Args:
            content: Conteúdo do documento
            
        Returns:
            Dicionário com estrutura das seções
        """
        sections = {}
        current_section = None
        current_subsection = None
        
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # Detectar headers
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                title = line.strip('#').strip().lower()
                
                if level == 2:  # Seção principal
                    current_section = title
                    sections[current_section] = {
                        'line_number': i + 1,
                        'content': [],
                        'subsections': {},
                        'word_count': 0
                    }
                    current_subsection = None
                    
                elif level == 3 and current_section:  # Subseção
                    current_subsection = title
                    sections[current_section]['subsections'][current_subsection] = {
                        'line_number': i + 1,
                        'content': [],
                        'word_count': 0
                    }
                    
            else:
                # Adicionar conteúdo à seção/subseção atual
                if current_section:
                    if current_subsection:
                        sections[current_section]['subsections'][current_subsection]['content'].append(line)
                        sections[current_section]['subsections'][current_subsection]['word_count'] += len(line.split())
                    else:
                        sections[current_section]['content'].append(line)
                        sections[current_section]['word_count'] += len(line.split())
                        
        return sections
        
    def _validate_metadata(self, metadata: Dict[str, Any], template_type: str) -> List[ValidationResult]:
        """
        Valida metadados específicos do template
        
        Args:
            metadata: Metadados do documento
            template_type: Tipo do template
            
        Returns:
            Lista de resultados de validação
        """
        results = []
        
        # Validar campos obrigatórios
        required_fields = self.config.get('metadata', {}).get('required_fields', {})
        
        for field, field_config in required_fields.items():
            if field not in metadata:
                results.append(ValidationResult(
                    rule_name=f"required_field_{field}",
                    severity=ValidationSeverity.ERROR,
                    message=f"Campo obrigatório '{field}' não encontrado",
                    suggestion=f"Adicionar '{field}' aos metadados",
                    auto_fixable=True
                ))
                continue
                
            value = metadata[field]
            
            # Validar tipo de dado
            field_type = field_config.get('type', 'string')
            if field_type == 'string' and not isinstance(value, str):
                results.append(ValidationResult(
                    rule_name=f"field_type_{field}",
                    severity=ValidationSeverity.ERROR,
                    message=f"Campo '{field}' deve ser string, encontrado {type(value).__name__}",
                    suggestion=f"Converter '{field}' para string",
                    auto_fixable=True
                ))
                
            # Validar valores permitidos
            allowed_values = field_config.get('values', [])
            if allowed_values and value not in allowed_values:
                results.append(ValidationResult(
                    rule_name=f"field_value_{field}",
                    severity=ValidationSeverity.ERROR,
                    message=f"Campo '{field}' com valor inválido '{value}'. Permitidos: {allowed_values}",
                    suggestion=f"Usar um dos valores permitidos: {', '.join(allowed_values)}",
                    auto_fixable=True
                ))
                
        # Validar consistência do doc_type
        if metadata.get('doc_type') != template_type:
            results.append(ValidationResult(
                rule_name="doc_type_consistency",
                severity=ValidationSeverity.ERROR,
                message=f"doc_type '{metadata.get('doc_type')}' inconsistente com template {template_type}",
                suggestion=f"Corrigir doc_type para '{template_type}'",
                auto_fixable=True
            ))
            
        # Validar formato de datas
        date_fields = ['created_date', 'last_updated']
        for date_field in date_fields:
            if date_field in metadata:
                try:
                    datetime.fromisoformat(str(metadata[date_field]))
                except ValueError:
                    results.append(ValidationResult(
                        rule_name=f"date_format_{date_field}",
                        severity=ValidationSeverity.ERROR,
                        message=f"Formato de data inválido em '{date_field}': {metadata[date_field]}",
                        suggestion="Usar formato YYYY-MM-DD",
                        auto_fixable=True
                    ))
                    
        return results
        
    def _validate_structure(self, sections: Dict[str, Any], template_type: str) -> List[ValidationResult]:
        """
        Valida estrutura específica do template
        
        Args:
            sections: Seções extraídas do documento
            template_type: Tipo do template
            
        Returns:
            Lista de resultados de validação
        """
        results = []
        rules = getattr(self, f"{template_type}_rules", {})
        
        # Validar seções obrigatórias
        required_sections = rules.get('required_sections', [])
        found_sections = set(sections.keys())
        
        for required_section in required_sections:
            # Busca flexível (partial match)
            section_found = any(required_section in section_name for section_name in found_sections)
            
            if not section_found:
                results.append(ValidationResult(
                    rule_name=f"missing_section_{required_section}",
                    severity=ValidationSeverity.ERROR,
                    message=f"Seção obrigatória não encontrada: '{required_section}'",
                    suggestion=f"Adicionar seção '## {required_section.title()}'",
                    auto_fixable=False
                ))
                
        # Validar subseções obrigatórias
        required_subsections = rules.get('required_subsections', {})
        
        for section_name, subsection_list in required_subsections.items():
            # Encontrar seção correspondente
            matching_section = None
            for section_key in sections.keys():
                if section_name in section_key:
                    matching_section = section_key
                    break
                    
            if matching_section:
                section_subsections = set(sections[matching_section]['subsections'].keys())
                
                for required_subsection in subsection_list:
                    subsection_found = any(required_subsection in sub_name for sub_name in section_subsections)
                    
                    if not subsection_found:
                        results.append(ValidationResult(
                            rule_name=f"missing_subsection_{required_subsection}",
                            severity=ValidationSeverity.WARNING,
                            message=f"Subseção recomendada não encontrada em '{section_name}': '{required_subsection}'",
                            suggestion=f"Adicionar subseção '### {required_subsection.title()}'",
                            line_number=sections[matching_section]['line_number'],
                            auto_fixable=False
                        ))
                        
        # Validações específicas por tipo de template
        if template_type == 'decision':
            self._validate_decision_specific(sections, results)
        elif template_type == 'process':
            self._validate_process_specific(sections, results)
        elif template_type == 'reference':
            self._validate_reference_specific(sections, results)
        elif template_type == 'architecture':
            self._validate_architecture_specific(sections, results)
        elif template_type == 'analysis':
            self._validate_analysis_specific(sections, results)
        elif template_type == 'planning':
            self._validate_planning_specific(sections, results)
            
        return results
        
    def _validate_decision_specific(self, sections: Dict[str, Any], results: List[ValidationResult]) -> None:
        """Validações específicas para template DECISÃO"""
        
        # Verificar número mínimo de opções
        options_section = None
        for section_name in sections.keys():
            if 'opções consideradas' in section_name or 'opções' in section_name:
                options_section = sections[section_name]
                break
                
        if options_section:
            content_text = '\n'.join(options_section['content'])
            option_count = len(re.findall(r'###.*opção \d+', content_text, re.IGNORECASE))
            
            if option_count < self.decision_rules['min_options']:
                results.append(ValidationResult(
                    rule_name="min_options_decision",
                    severity=ValidationSeverity.WARNING,
                    message=f"Encontradas {option_count} opções, recomendado mínimo {self.decision_rules['min_options']}",
                    suggestion="Adicionar mais opções para comparação",
                    line_number=options_section['line_number']
                ))
                
        # Verificar presença de trade-offs
        all_content = ' '.join([
            ' '.join(section['content']) for section in sections.values()
        ])
        
        trade_off_indicators = ['trade-off', 'prós', 'contras', 'vantagem', 'desvantagem']
        trade_offs_found = sum(1 for indicator in trade_off_indicators if indicator in all_content.lower())
        
        if trade_offs_found < 2:
            results.append(ValidationResult(
                rule_name="trade_offs_analysis",
                severity=ValidationSeverity.WARNING,
                message="Análise de trade-offs parece insuficiente",
                suggestion="Detalhar prós/contras e trade-offs das opções"
            ))
            
    def _validate_process_specific(self, sections: Dict[str, Any], results: List[ValidationResult]) -> None:
        """Validações específicas para template PROCESSO"""
        
        # Verificar número de passos
        procedure_section = None
        for section_name in sections.keys():
            if 'procedimento' in section_name or 'passos' in section_name:
                procedure_section = sections[section_name]
                break
                
        if procedure_section:
            content_text = '\n'.join(procedure_section['content'])
            step_count = len(re.findall(r'###.*passo \d+', content_text, re.IGNORECASE))
            
            if step_count < self.process_rules['min_steps']:
                results.append(ValidationResult(
                    rule_name="min_steps_process",
                    severity=ValidationSeverity.WARNING,
                    message=f"Encontrados {step_count} passos, recomendado mínimo {self.process_rules['min_steps']}",
                    suggestion="Detalhar procedimento em mais passos específicos",
                    line_number=procedure_section['line_number']
                ))
                
        # Verificar presença de comandos e validações
        all_content = ' '.join([
            ' '.join(section['content']) for section in sections.values()
        ])
        
        command_count = len(re.findall(r'```[^`]*```', all_content))
        validation_count = all_content.lower().count('validação') + all_content.lower().count('verificar')
        
        if command_count == 0:
            results.append(ValidationResult(
                rule_name="commands_present",
                severity=ValidationSeverity.WARNING,
                message="Nenhum bloco de comando encontrado",
                suggestion="Adicionar comandos específicos usando blocos de código ```"
            ))
            
        if validation_count < 2:
            results.append(ValidationResult(
                rule_name="validation_steps",
                severity=ValidationSeverity.WARNING,
                message="Poucos passos de validação encontrados",
                suggestion="Adicionar critérios de validação para cada passo"
            ))
            
    def _validate_reference_specific(self, sections: Dict[str, Any], results: List[ValidationResult]) -> None:
        """Validações específicas para template REFERÊNCIA"""
        
        # Verificar exemplos práticos
        examples_section = None
        for section_name in sections.keys():
            if 'exemplos' in section_name:
                examples_section = sections[section_name]
                break
                
        if examples_section:
            content_text = '\n'.join(examples_section['content'])
            example_count = len(re.findall(r'###.*exemplo \d+', content_text, re.IGNORECASE))
            
            if example_count < self.reference_rules['min_examples']:
                results.append(ValidationResult(
                    rule_name="min_examples_reference",
                    severity=ValidationSeverity.WARNING,
                    message=f"Encontrados {example_count} exemplos, recomendado mínimo {self.reference_rules['min_examples']}",
                    suggestion="Adicionar mais exemplos práticos de uso",
                    line_number=examples_section['line_number']
                ))
                
        # Verificar endpoints e códigos de resposta
        all_content = ' '.join([
            ' '.join(section['content']) for section in sections.values()
        ])
        
        endpoint_count = len(re.findall(r'(GET|POST|PUT|DELETE|PATCH)\s+/', all_content))
        status_code_count = len(re.findall(r'(200|201|400|401|404|500)', all_content))
        
        if endpoint_count == 0:
            results.append(ValidationResult(
                rule_name="api_endpoints",
                severity=ValidationSeverity.INFO,
                message="Nenhum endpoint de API encontrado",
                suggestion="Se aplicável, documentar endpoints da API"
            ))
            
        if endpoint_count > 0 and status_code_count == 0:
            results.append(ValidationResult(
                rule_name="status_codes",
                severity=ValidationSeverity.WARNING,
                message="Endpoints encontrados mas sem códigos de status",
                suggestion="Documentar códigos de resposta HTTP"
            ))
            
    def _validate_architecture_specific(self, sections: Dict[str, Any], results: List[ValidationResult]) -> None:
        """Validações específicas para template ARQUITETURA"""
        
        # Verificar componentes arquiteturais
        components_section = None
        for section_name in sections.keys():
            if 'componentes' in section_name:
                components_section = sections[section_name]
                break
                
        if components_section:
            content_text = '\n'.join(components_section['content'])
            component_count = len(re.findall(r'###.*componente \d+', content_text, re.IGNORECASE))
            
            if component_count < self.architecture_rules['min_components']:
                results.append(ValidationResult(
                    rule_name="min_components_architecture",
                    severity=ValidationSeverity.WARNING,
                    message=f"Encontrados {component_count} componentes, recomendado mínimo {self.architecture_rules['min_components']}",
                    suggestion="Detalhar mais componentes da arquitetura",
                    line_number=components_section['line_number']
                ))
                
        # Verificar diagramas e fluxos
        all_content = ' '.join([
            ' '.join(section['content']) for section in sections.values()
        ])
        
        diagram_count = all_content.count('```') + all_content.count('┌') + all_content.count('│')
        decision_count = all_content.lower().count('adr') + all_content.lower().count('decisão')
        
        if diagram_count == 0:
            results.append(ValidationResult(
                rule_name="architectural_diagrams",
                severity=ValidationSeverity.WARNING,
                message="Nenhum diagrama ou representação visual encontrada",
                suggestion="Adicionar diagramas ASCII ou referências para diagramas"
            ))
            
    def _validate_analysis_specific(self, sections: Dict[str, Any], results: List[ValidationResult]) -> None:
        """Validações específicas para template ANÁLISE"""
        
        # Verificar descobertas
        findings_section = None
        for section_name in sections.keys():
            if 'descobertas' in section_name or 'insights' in section_name:
                findings_section = sections[section_name]
                break
                
        if findings_section:
            content_text = '\n'.join(findings_section['content'])
            finding_count = len(re.findall(r'###.*descoberta \d+', content_text, re.IGNORECASE))
            
            if finding_count < self.analysis_rules['min_findings']:
                results.append(ValidationResult(
                    rule_name="min_findings_analysis",
                    severity=ValidationSeverity.WARNING,
                    message=f"Encontradas {finding_count} descobertas, recomendado mínimo {self.analysis_rules['min_findings']}",
                    suggestion="Detalhar mais descobertas da análise",
                    line_number=findings_section['line_number']
                ))
                
        # Verificar dados e métricas
        all_content = ' '.join([
            ' '.join(section['content']) for section in sections.values()
        ])
        
        metric_count = len(re.findall(r'\d+(\.\d+)?%', all_content)) + len(re.findall(r'\d+ms', all_content))
        table_count = all_content.count('|')
        
        if metric_count == 0:
            results.append(ValidationResult(
                rule_name="quantitative_data",
                severity=ValidationSeverity.WARNING,
                message="Poucos dados quantitativos encontrados",
                suggestion="Incluir métricas e dados numéricos na análise"
            ))
            
        if table_count < 6:  # Pelo menos uma tabela pequena
            results.append(ValidationResult(
                rule_name="data_tables",
                severity=ValidationSeverity.INFO,
                message="Considerar usar tabelas para organizar dados",
                suggestion="Organizar dados em tabelas para melhor visualização"
            ))
            
    def _validate_planning_specific(self, sections: Dict[str, Any], results: List[ValidationResult]) -> None:
        """Validações específicas para template PLANEJAMENTO"""
        
        # Verificar marcos
        milestones_section = None
        for section_name in sections.keys():
            if 'marcos' in section_name or 'cronograma' in section_name:
                milestones_section = sections[section_name]
                break
                
        if milestones_section:
            content_text = '\n'.join(milestones_section['content'])
            milestone_count = content_text.lower().count('marco') + content_text.lower().count('m1') + content_text.lower().count('m2')
            
            if milestone_count < self.planning_rules['min_milestones']:
                results.append(ValidationResult(
                    rule_name="min_milestones_planning",
                    severity=ValidationSeverity.WARNING,
                    message=f"Encontrados {milestone_count} marcos, recomendado mínimo {self.planning_rules['min_milestones']}",
                    suggestion="Definir marcos específicos para o projeto",
                    line_number=milestones_section['line_number']
                ))
                
        # Verificar objetivos SMART
        objectives_section = None
        for section_name in sections.keys():
            if 'objetivos' in section_name:
                objectives_section = sections[section_name]
                break
                
        if objectives_section:
            content_text = '\n'.join(objectives_section['content'])
            smart_indicators = ['específico', 'mensurável', 'atingível', 'relevante', 'temporal']
            smart_count = sum(1 for indicator in smart_indicators if indicator in content_text.lower())
            
            if smart_count < 3:
                results.append(ValidationResult(
                    rule_name="smart_objectives",
                    severity=ValidationSeverity.WARNING,
                    message="Objetivos podem não seguir critérios SMART",
                    suggestion="Definir objetivos Específicos, Mensuráveis, Atingíveis, Relevantes e Temporais",
                    line_number=objectives_section['line_number']
                ))
                
    def _validate_content_quality(self, content: str, sections: Dict[str, Any], template_type: str) -> List[ValidationResult]:
        """
        Valida qualidade geral do conteúdo
        
        Args:
            content: Conteúdo completo
            sections: Seções extraídas
            template_type: Tipo do template
            
        Returns:
            Lista de resultados de validação
        """
        results = []
        
        # Verificar comprimento adequado
        word_count = len(content.split())
        
        if word_count < 500:
            results.append(ValidationResult(
                rule_name="content_length",
                severity=ValidationSeverity.WARNING,
                message=f"Documento parece muito curto ({word_count} palavras)",
                suggestion="Expandir conteúdo com mais detalhes e exemplos"
            ))
        elif word_count > 5000:
            results.append(ValidationResult(
                rule_name="content_length",
                severity=ValidationSeverity.INFO,
                message=f"Documento é muito longo ({word_count} palavras)",
                suggestion="Considerar dividir em documentos menores"
            ))
            
        # Verificar presença de elementos estruturais
        checklist_count = content.count('- [ ]')
        table_count = content.count('|')
        code_block_count = content.count('```')
        
        if template_type in ['process', 'reference'] and code_block_count == 0:
            results.append(ValidationResult(
                rule_name="code_examples",
                severity=ValidationSeverity.WARNING,
                message="Nenhum exemplo de código encontrado",
                suggestion="Adicionar exemplos práticos com código"
            ))
            
        if template_type in ['decision', 'planning'] and checklist_count == 0:
            results.append(ValidationResult(
                rule_name="checklists",
                severity=ValidationSeverity.INFO,
                message="Considerar adicionar checklists",
                suggestion="Usar checklists para critérios e validações"
            ))
            
        # Verificar links e referências
        external_links = len(re.findall(r'https?://[^\s\]]+', content))
        internal_refs = len(re.findall(r'\[\[.*?\]\]', content))
        
        if external_links == 0 and internal_refs == 0:
            results.append(ValidationResult(
                rule_name="references",
                severity=ValidationSeverity.INFO,
                message="Nenhuma referência externa ou interna encontrada",
                suggestion="Adicionar links para recursos e documentos relacionados"
            ))
            
        # Verificar seções vazias
        empty_sections = []
        for section_name, section_data in sections.items():
            if section_data['word_count'] < 10:
                empty_sections.append(section_name)
                
        if empty_sections:
            results.append(ValidationResult(
                rule_name="empty_sections",
                severity=ValidationSeverity.WARNING,
                message=f"Seções com pouco conteúdo: {', '.join(empty_sections)}",
                suggestion="Expandir seções com conteúdo mais detalhado"
            ))
            
        return results
        
    def _calculate_scores(self, results: List[ValidationResult], sections: Dict[str, Any], template_type: str) -> Tuple[float, float, float]:
        """
        Calcula scores de completude, qualidade e geral
        
        Returns:
            Tupla com (completeness_score, quality_score, overall_score)
        """
        total_results = len(results)
        error_count = len([r for r in results if r.severity == ValidationSeverity.ERROR])
        warning_count = len([r for r in results if r.severity == ValidationSeverity.WARNING])
        
        # Score de completude (baseado em erros estruturais)
        completeness_score = max(0.0, 1.0 - (error_count * 0.2) - (warning_count * 0.1))
        
        # Score de qualidade (baseado em indicadores de qualidade)
        quality_indicators_found = 0
        rules = getattr(self, f"{template_type}_rules", {})
        quality_indicators = rules.get('quality_indicators', [])
        
        all_content = ' '.join([
            ' '.join(section['content']) for section in sections.values()
        ]).lower()
        
        for indicator in quality_indicators:
            if indicator in all_content:
                quality_indicators_found += 1
                
        quality_score = min(1.0, quality_indicators_found / len(quality_indicators)) if quality_indicators else 0.5
        
        # Score geral (média ponderada)
        overall_score = (completeness_score * 0.6) + (quality_score * 0.4)
        
        return completeness_score, quality_score, overall_score
        
    def validate_template(self, file_path: str) -> TemplateValidationReport:
        """
        Valida um template específico
        
        Args:
            file_path: Caminho do arquivo a validar
            
        Returns:
            Relatório completo de validação
        """
        results = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return TemplateValidationReport(
                template_type='unknown',
                file_path=file_path,
                overall_score=0.0,
                results=[ValidationResult(
                    rule_name="file_read_error",
                    severity=ValidationSeverity.ERROR,
                    message=f"Erro ao ler arquivo: {e}",
                    suggestion="Verificar se arquivo existe e tem permissões adequadas"
                )],
                metadata_validation={},
                structure_validation={},
                content_validation={},
                completeness_score=0.0,
                quality_score=0.0
            )
            
        # Extrair metadados
        metadata = {}
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    metadata = yaml.safe_load(parts[1]) or {}
                    content = parts[2]
                except yaml.YAMLError as e:
                    results.append(ValidationResult(
                        rule_name="metadata_parse_error",
                        severity=ValidationSeverity.ERROR,
                        message=f"Erro ao parsear metadados: {e}",
                        suggestion="Verificar sintaxe YAML dos metadados"
                    ))
                    
        template_type = metadata.get('doc_type', 'unknown')
        
        # Extrair seções
        sections = self._extract_sections(content)
        
        # Executar validações
        metadata_results = self._validate_metadata(metadata, template_type)
        structure_results = self._validate_structure(sections, template_type)
        content_results = self._validate_content_quality(content, sections, template_type)
        
        results.extend(metadata_results)
        results.extend(structure_results)
        results.extend(content_results)
        
        # Calcular scores
        completeness_score, quality_score, overall_score = self._calculate_scores(results, sections, template_type)
        
        return TemplateValidationReport(
            template_type=template_type,
            file_path=file_path,
            overall_score=overall_score,
            results=results,
            metadata_validation={
                'total_rules': len(metadata_results),
                'errors': len([r for r in metadata_results if r.severity == ValidationSeverity.ERROR]),
                'warnings': len([r for r in metadata_results if r.severity == ValidationSeverity.WARNING])
            },
            structure_validation={
                'total_rules': len(structure_results),
                'errors': len([r for r in structure_results if r.severity == ValidationSeverity.ERROR]),
                'warnings': len([r for r in structure_results if r.severity == ValidationSeverity.WARNING])
            },
            content_validation={
                'total_rules': len(content_results),
                'errors': len([r for r in content_results if r.severity == ValidationSeverity.ERROR]),
                'warnings': len([r for r in content_results if r.severity == ValidationSeverity.WARNING])
            },
            completeness_score=completeness_score,
            quality_score=quality_score
        )
        
    def print_report(self, report: TemplateValidationReport) -> None:
        """Imprime relatório de validação formatado"""
        
        print(f"\n{'='*60}")
        print(f"TEMPLATE VALIDATOR - RELATÓRIO DE VALIDAÇÃO")
        print(f"{'='*60}")
        
        print(f"\n📄 ARQUIVO: {report.file_path}")
        print(f"📋 TIPO: {report.template_type.upper()}")
        print(f"⭐ SCORE GERAL: {report.overall_score:.2f}")
        print(f"📊 COMPLETUDE: {report.completeness_score:.2f}")
        print(f"🎯 QUALIDADE: {report.quality_score:.2f}")
        
        # Resumo por categoria
        print(f"\n📈 RESUMO POR CATEGORIA:")
        print(f"   Metadados: {report.metadata_validation['errors']} erros, {report.metadata_validation['warnings']} avisos")
        print(f"   Estrutura: {report.structure_validation['errors']} erros, {report.structure_validation['warnings']} avisos")
        print(f"   Conteúdo: {report.content_validation['errors']} erros, {report.content_validation['warnings']} avisos")
        
        # Mostrar resultados por severidade
        errors = [r for r in report.results if r.severity == ValidationSeverity.ERROR]
        warnings = [r for r in report.results if r.severity == ValidationSeverity.WARNING]
        info = [r for r in report.results if r.severity == ValidationSeverity.INFO]
        
        if errors:
            print(f"\n❌ ERROS ({len(errors)}):")
            for error in errors:
                line_info = f" (linha {error.line_number})" if error.line_number else ""
                print(f"   • {error.message}{line_info}")
                if error.suggestion:
                    print(f"     💡 {error.suggestion}")
                    
        if warnings:
            print(f"\n⚠️  AVISOS ({len(warnings)}):")
            for warning in warnings:
                line_info = f" (linha {warning.line_number})" if warning.line_number else ""
                print(f"   • {warning.message}{line_info}")
                if warning.suggestion:
                    print(f"     💡 {warning.suggestion}")
                    
        if info:
            print(f"\n💡 SUGESTÕES ({len(info)}):")
            for suggestion in info[:5]:  # Mostrar só as primeiras 5
                print(f"   • {suggestion.message}")
                
        print(f"\n{'='*60}")

def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Context Navigator Template Validator')
    parser.add_argument('--path', '-p', default='.', 
                       help='Caminho base do projeto')
    parser.add_argument('--file', '-f',
                       help='Validar arquivo específico')
    parser.add_argument('--templates', '-t', action='store_true',
                       help='Validar todos os templates')
    parser.add_argument('--json', action='store_true',
                       help='Saída em formato JSON')
    
    args = parser.parse_args()
    
    validator = TemplateValidator(args.path)
    
    if args.file:
        file_path = Path(args.file)
        if file_path.exists():
            report = validator.validate_template(str(file_path))
            
            if args.json:
                # Converter para formato JSON serializável
                report_dict = {
                    'template_type': report.template_type,
                    'file_path': report.file_path,
                    'overall_score': report.overall_score,
                    'completeness_score': report.completeness_score,
                    'quality_score': report.quality_score,
                    'metadata_validation': report.metadata_validation,
                    'structure_validation': report.structure_validation,
                    'content_validation': report.content_validation,
                    'results': [
                        {
                            'rule_name': r.rule_name,
                            'severity': r.severity.value,
                            'message': r.message,
                            'line_number': r.line_number,
                            'suggestion': r.suggestion,
                            'auto_fixable': r.auto_fixable
                        }
                        for r in report.results
                    ]
                }
                print(json.dumps(report_dict, indent=2, ensure_ascii=False))
            else:
                validator.print_report(report)
        else:
            print(f"Arquivo não encontrado: {file_path}")
            
    elif args.templates:
        templates_path = Path(args.path) / "templates"
        if templates_path.exists():
            for template_file in templates_path.glob("*.md"):
                print(f"\n🔍 Validando: {template_file.name}")
                report = validator.validate_template(str(template_file))
                
                if args.json:
                    # Só mostrar resumo em JSON para múltiplos arquivos
                    summary = {
                        'file': str(template_file),
                        'template_type': report.template_type,
                        'overall_score': report.overall_score,
                        'errors': len([r for r in report.results if r.severity == ValidationSeverity.ERROR]),
                        'warnings': len([r for r in report.results if r.severity == ValidationSeverity.WARNING])
                    }
                    print(json.dumps(summary, ensure_ascii=False))
                else:
                    validator.print_report(report)
        else:
            print(f"Pasta de templates não encontrada: {templates_path}")
    else:
        print("Uso: python template_validator.py --file <arquivo> ou --templates")

if __name__ == '__main__':
    main() 