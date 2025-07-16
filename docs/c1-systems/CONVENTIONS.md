---
doc_type: "reference"
context_level: "c1_root"
context_type: "core"
module: "context-navigator"
priority: "critical"
status: "active"
connections:
  references: ["MANUAL_HUMANO.md", "MANUAL_IA.md"]
  impacts:
    [
      "context_scanner.py",
      "context_engine.py",
      "template_validator.py",
      "templates/",
    ]
  depends_on: ["workspace.yml", "context.rule"]
  relates_to: ["WorkspaceManager"]
created_date: "2024-01-15"
last_updated: "2025-07-12"
owner: "Context Navigator Team"
tags: ["conventions", "immutable-rules", "methodology", "reference", "2.0"]
complexity: "critical"
maintenance_schedule: "never"
stakeholders: ["developers", "ai-systems", "documentation-team"]
architectural_impact: "critical"
version: "2.0"
---

# 📜 Context Navigator 2.0 - Convenções Imutáveis

## ⚡ Regras Fundamentais

### **Lei Sagrada**

1. **NUNCA** responder sem carregar `context.rule`
2. **NUNCA** alterar estrutura de templates
3. **NUNCA** omitir metadados obrigatórios
4. **NUNCA** criar conexões inválidas
5. **NUNCA** misturar tipos de documento

### **Princípio da Imutabilidade**

- Estruturas de template são **IMUTÁVEIS**
- Campos obrigatórios são **IMUTÁVEIS**
- Tipos de documento são **IMUTÁVEIS**
- Níveis de contexto são **IMUTÁVEIS**

---

## 📁 Convenções de Nomenclatura

### **Arquivos e Pastas - Arquitetura 2.0**

```yaml
# Estrutura obrigatória (Arquitetura 2.0)
projeto/
├── .cn_model/                    # Workspace Context Navigator 2.0
│   ├── workspace.yml            # Configuração do workspace (substitui .contextrc)
│   ├── components/              # Componentes documentados
│   ├── templates/               # Templates personalizados
│   ├── maps/                    # Mapas de contexto (substitui .context-map/)
│   │   ├── index.yml           # Índice principal
│   │   ├── connections.yml     # Conexões
│   │   ├── conflicts.yml       # Conflitos
│   │   └── architecture.yml    # Arquitetura
│   └── scripts/                # Scripts especializados (se necessário)
├── docs/                        # Documentação do projeto
│   ├── decisions/              # Decisões arquiteturais
│   ├── processes/              # Processos e runbooks
│   ├── references/             # APIs e referências
│   ├── architecture/           # Arquitetura e diagramas
│   ├── analysis/               # Análises e investigações
│   └── planning/               # Planejamento e roadmaps
└── src/                         # Código fonte (com marcações @cn:)
```

### **Busca Inteligente Multi-Nível**

```yaml
# Hierarquia de busca (WorkspaceManager 2.0)
1. Workspace Local:
  - .cn_model/ (diretório atual)
  - ../.cn_model/ (diretório pai)
  - ../../.cn_model/ (recursivo até raiz)

2. Instalação Global:
  - ~/.local/share/context-navigator/
  - ~/.context-navigator/ (fallback)

3. Sistema:
  - Templates sempre disponíveis
  - Scripts core sempre acessíveis
```

### **Nomes de Arquivos (Imutáveis)**

```yaml
# Padrão obrigatório
formato: "[nome-descritivo].md"
exemplos:
  - "user-authentication-decision.md"
  - "deployment-process.md"
  - "api-reference.md"
  - "system-architecture.md"
  - "performance-analysis.md"
  - "project-planning.md"

# Proibido
- Espaços em nomes
- Caracteres especiais exceto hífen
- Extensões diferentes de .md
- Nomes genéricos (doc1.md, arquivo.md)
```

### **Nomes de Templates (Imutáveis)**

```yaml
# Templates core (sempre disponíveis globalmente)
templates/
├── decisao.md               # Template DECISÃO
├── processo.md              # Template PROCESSO
├── referencia.md            # Template REFERÊNCIA
├── arquitetura.md           # Template ARQUITETURA
├── analise.md               # Template ANÁLISE
└── planejamento.md          # Template PLANEJAMENTO
```

---

## 🏗️ Convenções Estruturais - Arquitetura 2.0

### **Organização de Workspaces**

```yaml
# Workspace Local (projeto específico)
.cn_model/                    # Workspace do projeto
├── workspace.yml            # Configuração principal
├── components/              # Componentes do projeto
├── templates/               # Templates customizados
└── maps/                    # Mapas contextuais

# Instalação Global (sistema)
~/.local/share/context-navigator/
├── global_workspace.yml     # Configuração global
├── templates/               # Templates padrão
├── scripts/                 # Scripts organizados
│   ├── core/               # Scanner, engine
│   ├── validation/         # Validadores
│   ├── analysis/           # Analisadores
│   └── tools/              # Utilitários
└── cache/                   # Cache do sistema
```

### **Hierarquia de Documentos (Inalterada)**

```yaml
# Por contexto (mantém-se em 2.0)
c1_root/                   # Contexto raiz
├── strategic-decisions/   # Decisões estratégicas
├── system-architecture/   # Arquitetura de sistema
└── project-planning/      # Planejamento geral

c2_module/                 # Contexto módulo
├── module-decisions/      # Decisões específicas
├── module-processes/      # Processos do módulo
└── module-architecture/   # Arquitetura do módulo

c3_component/              # Contexto componente
├── component-analysis/    # Análises específicas
├── component-reference/   # Referências técnicas
└── component-processes/   # Processos detalhados
```

### **Componentização Code Bridge**

```yaml
# Marcações no código (nova funcionalidade 2.0)
# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component nome-componente
# @cn:doc arquivo-documentacao.md
# @cn:context-level c1_root|c2_module|c3_component
# @cn:context-type core|api|data|ui|infra|shared
# @cn:purpose "Descrição clara do propósito"
# @cn:depends-on doc1.md, doc2.md
# ============================================
```

---

## 🏷️ Convenções de Metadados (Inalteradas)

### **Campos Obrigatórios (Imutáveis)**

```yaml
---
doc_type: String # OBRIGATÓRIO
context_level: String # OBRIGATÓRIO
context_type: String # OBRIGATÓRIO
module: String # OBRIGATÓRIO
priority: String # OBRIGATÓRIO
status: String # OBRIGATÓRIO
connections: Object # OBRIGATÓRIO
created_date: String # OBRIGATÓRIO
last_updated: String # OBRIGATÓRIO
owner: String # OBRIGATÓRIO
---
```

### **Valores Permitidos (Imutáveis)**

```yaml
doc_type:
  - decision
  - process
  - reference
  - architecture
  - analysis
  - planning

context_level:
  - c1_root
  - c2_module
  - c3_component

context_type:
  - infra
  - shared
  - core
  - api
  - data
  - ui

priority:
  - low
  - medium
  - high
  - critical

status:
  - draft
  - active
  - deprecated
  - archived
```

### **Formato de Conexões (Imutável)**

```yaml
connections:
  references: [] # Array de strings
  impacts: [] # Array de strings
  depends_on: [] # Array de strings
  blocks: [] # Array de strings
  relates_to: [] # Array de strings
```

---

## 🛠️ Convenções de Scripts - Arquitetura 2.0

### **Organização por Responsabilidade**

```yaml
# Nova estrutura organizacional (2.0)
scripts/
├── core/                        # Processamento essencial
│   ├── context_scanner.py      # Scanner principal (WorkspaceManager)
│   └── context_engine.py       # Motor contextual
├── validation/                  # Validação de qualidade
│   ├── template_validator.py   # Validador de templates
│   ├── cn_consistency_validator.py # Validador de consistência
│   └── metrics_validator.py    # Validador de métricas
├── analysis/                    # Análise avançada
│   ├── pattern_detector.py     # Detector de padrões
│   ├── conflict_detector.py    # Detector de conflitos
│   ├── impact_analyzer.py      # Analisador de impactos
│   └── context_advisor.py      # Consultor inteligente
└── tools/                       # Utilitários
    ├── cn_component_explorer.py # Explorador de componentes
    ├── cn_component_parser.py   # Parser de componentes
    ├── context_demo.py          # Sistema de demonstração
    └── cn_global_launcher.py    # Launcher global
```

### **WorkspaceManager - Protocolo Obrigatório**

```yaml
# Todo script deve usar WorkspaceManager (2.0)
from core.workspace_manager import WorkspaceManager

def main():
    # OBRIGATÓRIO: Detectar workspace antes de processar
    workspace_manager = WorkspaceManager()
    workspace_path = workspace_manager.detect_workspace()

    if not workspace_path:
        print("❌ Nenhum workspace encontrado")
        return

    # Processar com workspace detectado
    process_with_workspace(workspace_path)
```

### **Saves em .cn_model/ (Obrigatório)**

```yaml
# Todos os dados devem ser salvos em .cn_model/ (2.0)
save_paths:
  - .cn_model/maps/index.yml # Índice principal
  - .cn_model/maps/connections.yml # Conexões
  - .cn_model/maps/conflicts.yml # Conflitos
  - .cn_model/components/ # Componentes
  - .cn_model/cache/ # Cache temporário

# PROIBIDO em 2.0
deprecated_paths:
  - .context-map/ # Arquitetura 1.0
  - .contextrc # Arquitetura 1.0
```

---

## 🔗 Convenções de Conexões (Inalteradas)

### **Tipos de Conexão (Imutáveis)**

```yaml
references:
  descrição: "Este documento referencia outros"
  direção: "saída"
  exemplo: ["api-spec.md", "auth-guide.md"]

impacts:
  descrição: "Este documento impacta outros"
  direção: "saída"
  exemplo: ["deployment-process.md", "monitoring.md"]

depends_on:
  descrição: "Este documento depende de outros"
  direção: "entrada"
  exemplo: ["infrastructure-decision.md", "security-policy.md"]

blocks:
  descrição: "Este documento bloqueia outros"
  direção: "saída"
  exemplo: ["migration-plan.md", "legacy-removal.md"]

relates_to:
  descrição: "Este documento se relaciona com outros"
  direção: "bidirecional"
  exemplo: ["user-stories.md", "acceptance-criteria.md"]
```

---

## 📊 Convenções de Templates (Inalteradas)

### **Template DECISÃO (Imutável)**

```yaml
estrutura_obrigatória:
  - "## Contexto e Problema"
  - "### Situação Atual"
  - "### Problema Identificado"
  - "### Motivação"
  - "## Análise Detalhada"
  - "### Fatores Considerados"
  - "### Restrições Identificadas"
  - "### Critérios de Avaliação"
  - "## Opções Consideradas"
  - "### Opção 1: [Nome]"
  - "### Opção 2: [Nome]"
  - "## Decisão Final"
  - "### Opção Escolhida"
  - "### Justificativa"
  - "### Fatores Decisivos"
  - "## Impactos e Consequências"
  - "### Impactos Positivos"
  - "### Impactos Negativos"
  - "### Plano de Mitigação"

validações_mínimas:
  - Mínimo 2 opções consideradas
  - Todos os prós/contras preenchidos
  - Justificativa clara da decisão
  - Impactos identificados
```

---

## 🎯 Convenções de Contexto (Inalteradas)

### **Contextos Hierárquicos (Imutáveis)**

```yaml
c1_root:
  descrição: "Contexto raiz - decisões que afetam todo o projeto"
  escopo: "Arquitetura geral, tecnologias principais, políticas"
  exemplos: ["tech-stack-decision.md", "deployment-strategy.md"]

c2_module:
  descrição: "Contexto módulo - decisões específicas de módulo"
  escopo: "Funcionalidades específicas, APIs internas, processos"
  exemplos: ["auth-module-design.md", "payment-process.md"]

c3_component:
  descrição: "Contexto componente - decisões de componente específico"
  escopo: "Implementação detalhada, configurações, referências"
  exemplos: ["jwt-implementation.md", "database-schema.md"]
```

---

## ✅ Convenções de Validação - Arquitetura 2.0

### **Critérios de Qualidade (Inalterados)**

```yaml
scores_mínimos:
  overall_score: 0.7 # 70% mínimo
  completeness_score: 0.8 # 80% mínimo
  quality_score: 0.6 # 60% mínimo

validações_obrigatórias:
  - Metadados completos
  - Estrutura do template seguida
  - Conteúdo em todas as seções
  - Conexões válidas
  - Formatação correta

tolerâncias_máximas:
  - 0 erros críticos
  - 3 warnings por documento
  - 5 suggestions por documento
  - 10% de campos opcionais ausentes
```

### **Comandos de Validação 2.0**

```bash
# Validação com arquitetura 2.0 (WorkspaceManager)
cn validate                      # Validação completa
cn validate metrics              # Métricas específicas
cn check                         # Verificação de consistência
cn conflicts                     # Detecção de conflitos

# Comandos legacy (ainda funcionam)
python3 -m context_navigator.scripts.validation.template_validator --file doc.md
python3 -m context_navigator.scripts.analysis.conflict_detector --type all
```

---

## 🔒 Convenções de Compliance - Arquitetura 2.0

### **Regras Não Negociáveis (Atualizadas)**

```yaml
# Estrutura
- Templates NÃO podem ser alterados
- Metadados obrigatórios NÃO podem ser omitidos
- WorkspaceManager DEVE ser usado em todos os scripts
- Saves DEVEM ir para .cn_model/ (não .context-map/)

# Processo
- context.rule DEVE ser carregado sempre
- Workspace DEVE ser detectado via WorkspaceManager
- Validação DEVE ser executada
- Busca inteligente DEVE ser respeitada

# Qualidade
- Score mínimo DEVE ser respeitado
- Erros críticos NÃO são tolerados
- Estrutura DEVE ser completa
- Componentização DEVE seguir protocolo @cn:
```

### **Comandos de Verificação 2.0**

```bash
#!/bin/bash
# health_check_2.0.sh

echo "=== CONTEXT NAVIGATOR 2.0 HEALTH CHECK ==="

# Verificar instalação global
echo "1. Verificando instalação global..."
which cn >/dev/null && echo "✅ Comando cn disponível" || echo "❌ cn não encontrado no PATH"

# Verificar workspace
echo "2. Verificando workspace..."
cn status >/dev/null && echo "✅ Workspace detectado" || echo "❌ Nenhum workspace"

# Verificar scripts organizados
echo "3. Verificando organização de scripts..."
cn explore >/dev/null && echo "✅ Scripts organizados" || echo "❌ Scripts com problemas"

# Verificar validação
echo "4. Verificando validação..."
cn validate >/dev/null && echo "✅ Validação OK" || echo "❌ Problemas de validação"

echo "=== FIM DO HEALTH CHECK 2.0 ==="
```

---

## 📚 Referência Rápida - Arquitetura 2.0

### **Checklist de Compliance 2.0**

```yaml
✅ Workspace:
  - [ ] WorkspaceManager detecta .cn_model/
  - [ ] workspace.yml configurado corretamente
  - [ ] Scripts salvam em .cn_model/maps/
  - [ ] Busca inteligente funcional

✅ Metadados (inalterados):
  - [ ] Todos os campos obrigatórios preenchidos
  - [ ] Valores dentro dos permitidos
  - [ ] Datas no formato correto
  - [ ] Conexões válidas

✅ Scripts:
  - [ ] Organizados por responsabilidade
  - [ ] Usam WorkspaceManager
  - [ ] Salvam em .cn_model/
  - [ ] Funcionam globalmente via cn

✅ Componentização:
  - [ ] Marcações @cn: no código
  - [ ] Documentação conectada
  - [ ] Hierarquia respeitada
  - [ ] Purpose e memory-aid definidos
```

### **Comandos Essenciais 2.0**

```bash
# Comandos principais (global)
cn init                          # Inicializar workspace
cn scan                          # Escanear documentos
cn validate                      # Validar qualidade
cn demo                          # Demonstração
cn status                        # Status do workspace

# Ferramentas especializadas
cn explore                       # Explorar componentes
cn conflicts                     # Detectar conflitos
cn metrics                       # Métricas de qualidade
cn advisor                       # Sugestões inteligentes
```

---

## 🎯 Evolução 1.0 → 2.0

### **Principais Mudanças**

```yaml
# Arquitetura
1.0: .contextrc + .context-map/
2.0: workspace.yml + .cn_model/

# Busca
1.0: Busca local apenas
2.0: Busca inteligente multi-nível

# Scripts
1.0: Pasta única
2.0: Organizados por responsabilidade

# Instalação
1.0: Local apenas
2.0: Global como padrão

# Componentização
1.0: Apenas documentação
2.0: Code Bridge (@cn:)
```

### **Compatibilidade**

```yaml
# Mantido em 2.0
- Templates (100% compatíveis)
- Metadados (100% compatíveis)
- Tipos de documento (100% compatíveis)
- Conexões (100% compatíveis)

# Migração automática
- .contextrc → workspace.yml
- .context-map/ → .cn_model/maps/
- Scripts reorganizados automaticamente
```

---

**📜 Este documento define as regras imutáveis do Context Navigator 2.0. A arquitetura evoluiu, mas os princípios fundamentais permanecem.**

_Convenções 2.0: Mais inteligentes, mais globais, mais conectadas._
