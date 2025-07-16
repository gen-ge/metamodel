#!/usr/bin/env python3

# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component cn-consistency-validator
# @cn:doc cn-consistency-validator.md
# @cn:context-level c3_component
# @cn:context-type validation
# @cn:parent-module cli-interface
# @cn:purpose "Validador de consistência entre documentação e código através de marcações @cn:"
# @cn:memory-aid "Guardião da sincronização - verifica se docs e código estão alinhados"
# @cn:depends-on cn-component-parser, component-map.yml
# @cn:impacts code-quality, documentation-sync, user-confidence
# @cn:provides consistency-validation, sync-verification, gap-detection
# @cn:component-type validation
# @cn:responsibility consistency-checking
# @cn:single-purpose true
# ============================================

"""
CN Consistency Validator - Validador de Consistência
Verifica consistência entre documentação e código através das marcações @cn:
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import logging
from enum import Enum

# Imports básicos - dependências serão carregadas dinamicamente
import sys
import re

# Import necessário para tipos
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "tools"))
from cn_component_parser import CNComponentParser, ComponentHeader

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('cn_validator')

class ValidationLevel(Enum):
    """Níveis de validação"""
    # @cn:class business-entity
    # @cn:responsibility enumeration
    ERROR = "error"      # Problemas críticos
    WARNING = "warning"  # Problemas não críticos
    INFO = "info"        # Informações

@dataclass
class ValidationIssue:
    """Representa um problema de consistência"""
    # @cn:class business-entity
    # @cn:responsibility data-structure
    level: ValidationLevel
    category: str           # Categoria do problema
    component: str          # Nome do componente
    file_path: str         # Arquivo com problema
    description: str       # Descrição do problema
    suggestion: str        # Sugestão de correção

@dataclass
class ValidationReport:
    """Relatório completo de validação"""
    # @cn:class business-entity
    # @cn:responsibility data-structure
    total_components: int
    total_issues: int
    errors: List[ValidationIssue]
    warnings: List[ValidationIssue]
    infos: List[ValidationIssue]
    summary: Dict[str, int]

class CNConsistencyValidator:
    """Validador principal de consistência"""
    
    # @cn:class service
    # @cn:responsibility consistency-validation
    # @cn:single-purpose true
    
    def __init__(self, base_path: str = "."):
        # @cn:function core
        # @cn:process initialization
        self.base_path = Path(base_path)
        self.parser = CNComponentParser()
        self.issues: List[ValidationIssue] = []
        
        # NOVO: Usar WorkspaceManager para detectar workspace
        self._init_with_workspace_manager()
        
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
        
        # Diretórios na nova arquitetura
        self.docs_dirs = [
            self.output_dir / "docs",
            self.base_path / "docs"  # Docs do usuário se existir
        ]
        
        logger.info(f"🌐 Workspace: {current_workspace.name} ({current_workspace.root_path})")
        
    # @cn:function critical
    # @cn:process full-validation
    # @cn:step 1
    def validate_project(self, project_path: Optional[str] = None) -> ValidationReport:
        """
        Valida consistência de todo o projeto
        
        Args:
            project_path: Caminho do projeto (usa base_path se None)
            
        Returns:
            Relatório completo de validação
        """
        if project_path:
            self.base_path = Path(project_path)
            
        logger.info(f"Iniciando validação de consistência em {self.base_path}")
        
        # Limpar issues anteriores
        self.issues = []
        
        # Analisar todos os componentes
        components = self.parser.parse_directory(str(self.base_path), ['.py'])
        
        if not components:
            self.issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                category="no-components",
                component="project",
                file_path=str(self.base_path),
                description="Nenhum componente Context Navigator encontrado no projeto",
                suggestion="Adicione marcações @cn: aos arquivos principais"
            ))
            
        # Validar cada componente
        for file_path, header in components.items():
            self._validate_component(header)
            
        # Validar estrutura geral
        self._validate_project_structure()
        
        # Gerar relatório
        return self._generate_report(len(components))
    
    # @cn:function core
    # @cn:process component-validation
    # @cn:step 2
    def _validate_component(self, header: ComponentHeader) -> None:
        """Valida um componente específico"""
        
        # 1. Validar cabeçalho obrigatório
        header_errors = self.parser.validate_header(header)
        for error in header_errors:
            self.issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="header-validation",
                component=header.component_name,
                file_path=header.file_path,
                description=error,
                suggestion="Corrija o cabeçalho Context Bridge conforme protocolo"
            ))
        
        # 2. Validar existência de documentação
        self._validate_documentation_exists(header)
        
        # 3. Validar hierarquia e dependências
        self._validate_hierarchy(header)
        
        # 4. Validar nomeação
        self._validate_naming_conventions(header)
        
    # @cn:function integration
    # @cn:process documentation-validation
    # @cn:step 3
    def _validate_documentation_exists(self, header: ComponentHeader) -> None:
        """Valida se documentação referenciada existe"""
        
        doc_file = header.doc_file
        if not doc_file:
            return
            
        # Procurar arquivo de documentação
        doc_found = False
        searched_paths = []
        
        # Procurar em diretórios padrão
        for docs_dir in self.docs_dirs:
            if docs_dir.exists():
                # Procurar diretamente
                doc_path = docs_dir / doc_file
                searched_paths.append(str(doc_path))
                if doc_path.exists():
                    doc_found = True
                    break
                    
                # Procurar recursivamente
                for found_file in docs_dir.rglob(doc_file):
                    doc_found = True
                    break
                    
        if not doc_found:
            self.issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                category="missing-documentation",
                component=header.component_name,
                file_path=header.file_path,
                description=f"Arquivo de documentação não encontrado: {doc_file}",
                suggestion=f"Crie o arquivo {doc_file} ou corrija a referência @cn:doc"
            ))
            
        # Informar onde foi procurado
        if not doc_found and searched_paths:
            self.issues.append(ValidationIssue(
                level=ValidationLevel.INFO,
                category="search-info",
                component=header.component_name,
                file_path=header.file_path,
                description=f"Procurado em: {', '.join(searched_paths[:3])}...",
                suggestion="Verifique se o arquivo está no local correto"
            ))
    
    # @cn:function validation
    # @cn:process hierarchy-validation
    def _validate_hierarchy(self, header: ComponentHeader) -> None:
        """Valida hierarquia de componentes"""
        
        # Verificar parent-module para componentes
        if header.component_type == 'component':
            parent_module = None
            for annotation in header.annotations:
                if annotation.field == 'parent-module':
                    parent_module = annotation.value
                    break
                    
            if not parent_module:
                self.issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    category="missing-parent",
                    component=header.component_name,
                    file_path=header.file_path,
                    description="Componente c3_component sem @cn:parent-module definido",
                    suggestion="Adicione @cn:parent-module para indicar módulo pai"
                ))
                
        # Verificar parent-system para módulos
        if header.component_type == 'module':
            parent_system = None
            for annotation in header.annotations:
                if annotation.field == 'parent-system':
                    parent_system = annotation.value
                    break
                    
            if not parent_system:
                self.issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    category="missing-parent",
                    component=header.component_name,
                    file_path=header.file_path,
                    description="Módulo c2_module sem @cn:parent-system definido",
                    suggestion="Adicione @cn:parent-system para indicar sistema pai"
                ))
    
    # @cn:function validation
    # @cn:process naming-validation
    def _validate_naming_conventions(self, header: ComponentHeader) -> None:
        """Valida convenções de nomeação"""
        
        # Verificar kebab-case
        if '_' in header.component_name:
            self.issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                category="naming-convention",
                component=header.component_name,
                file_path=header.file_path,
                description=f"Nome deve usar kebab-case: {header.component_name}",
                suggestion=f"Mude para: {header.component_name.replace('_', '-')}"
            ))
            
        # Verificar arquivo .md
        if header.doc_file and not header.doc_file.endswith('.md'):
            self.issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                category="doc-extension",
                component=header.component_name,
                file_path=header.file_path,
                description=f"Documentação deve ter extensão .md: {header.doc_file}",
                suggestion="Use arquivo .md para documentação"
            ))
    
    # @cn:function validation
    # @cn:process structure-validation
    def _validate_project_structure(self) -> None:
        """Valida estrutura geral do projeto"""
        
        # Verificar se existe pasta docs
        docs_path = self.base_path / "docs"
        if not docs_path.exists():
            self.issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                category="missing-structure",
                component="project",
                file_path=str(self.base_path),
                description="Pasta 'docs' não encontrada",
                suggestion="Crie estrutura: docs/c1-systems/, docs/c2-modules/, docs/c3-components/"
            ))
            
        # Verificar component-map.yml
        component_map_path = self.base_path / ".context-navigator" / "component-map.yml"
        if not component_map_path.exists():
            self.issues.append(ValidationIssue(
                level=ValidationLevel.INFO,
                category="missing-component-map",
                component="project",
                file_path=str(self.base_path),
                description="component-map.yml não encontrado",
                suggestion="Execute: cn generate component-map"
            ))
    
    # @cn:function integration
    # @cn:process report-generation
    def _generate_report(self, total_components: int) -> ValidationReport:
        """Gera relatório final de validação"""
        
        errors = [issue for issue in self.issues if issue.level == ValidationLevel.ERROR]
        warnings = [issue for issue in self.issues if issue.level == ValidationLevel.WARNING]
        infos = [issue for issue in self.issues if issue.level == ValidationLevel.INFO]
        
        summary = {
            'total_components': total_components,
            'total_issues': len(self.issues),
            'errors': len(errors),
            'warnings': len(warnings),
            'infos': len(infos)
        }
        
        return ValidationReport(
            total_components=total_components,
            total_issues=len(self.issues),
            errors=errors,
            warnings=warnings,
            infos=infos,
            summary=summary
        )
    
    # @cn:function integration
    # @cn:process report-formatting
    def format_report(self, report: ValidationReport, format_type: str = "text") -> str:
        """Formata relatório para exibição"""
        
        if format_type == "text":
            return self._format_text_report(report)
        elif format_type == "yaml":
            return self._format_yaml_report(report)
        else:
            return self._format_text_report(report)
    
    # @cn:function integration
    # @cn:process text-formatting
    def _format_text_report(self, report: ValidationReport) -> str:
        """Formata relatório em texto"""
        
        lines = []
        lines.append("# 🔍 Relatório de Consistência Context Navigator\n")
        
        # Resumo
        lines.append(f"**Total de Componentes:** {report.total_components}")
        lines.append(f"**Total de Issues:** {report.total_issues}")
        lines.append(f"- ❌ Erros: {len(report.errors)}")
        lines.append(f"- ⚠️  Avisos: {len(report.warnings)}")
        lines.append(f"- ℹ️  Informações: {len(report.infos)}\n")
        
        # Status geral
        if len(report.errors) == 0:
            lines.append("✅ **Status:** Nenhum erro crítico encontrado!")
        else:
            lines.append("❌ **Status:** Erros críticos encontrados - correção necessária")
            
        lines.append("")
        
        # Listar issues por categoria
        for level, issues, emoji in [
            ("Erros Críticos", report.errors, "❌"),
            ("Avisos", report.warnings, "⚠️"),
            ("Informações", report.infos, "ℹ️")
        ]:
            if issues:
                lines.append(f"## {emoji} {level}\n")
                for issue in issues:
                    lines.append(f"### {issue.component}")
                    lines.append(f"- **Arquivo:** `{issue.file_path}`")
                    lines.append(f"- **Categoria:** {issue.category}")
                    lines.append(f"- **Problema:** {issue.description}")
                    lines.append(f"- **Sugestão:** {issue.suggestion}\n")
        
        return "\n".join(lines)
    
    # @cn:function integration
    # @cn:process yaml-formatting
    def _format_yaml_report(self, report: ValidationReport) -> str:
        """Formata relatório em YAML"""
        
        data = {
            'validation_report': {
                'summary': report.summary,
                'issues': {
                    'errors': [self._issue_to_dict(issue) for issue in report.errors],
                    'warnings': [self._issue_to_dict(issue) for issue in report.warnings],
                    'infos': [self._issue_to_dict(issue) for issue in report.infos]
                }
            }
        }
        
        return yaml.dump(data, default_flow_style=False, sort_keys=False)
    
    # @cn:function integration
    # @cn:process data-conversion
    def _issue_to_dict(self, issue: ValidationIssue) -> Dict[str, str]:
        """Converte ValidationIssue para dicionário"""
        return {
            'level': issue.level.value,
            'category': issue.category,
            'component': issue.component,
            'file_path': issue.file_path,
            'description': issue.description,
            'suggestion': issue.suggestion
        }

# @cn:function entry-point
# @cn:process cli-interface
def main():
    """Função principal para uso via linha de comando"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validador de consistência Context Navigator')
    parser.add_argument('path', nargs='?', default='.', 
                       help='Caminho do projeto para validar')
    parser.add_argument('--format', choices=['text', 'yaml'], default='text',
                       help='Formato do relatório')
    parser.add_argument('--output', help='Arquivo de saída (opcional)')
    parser.add_argument('--strict', action='store_true',
                       help='Falhar com exit code 1 se houver erros')
    
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
    
    # Executar validação
    validator = CNConsistencyValidator()
    report = validator.validate_project()
    
    # Formatar saída
    output = validator.format_report(report, args.format)
    
    # Salvar ou imprimir
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"📄 Relatório salvo em {args.output}")
    else:
        print(output)
    
    # Exit code baseado em erros
    if args.strict and len(report.errors) > 0:
        exit(1)
    else:
        exit(0)

if __name__ == '__main__':
    main() 