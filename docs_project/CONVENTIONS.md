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
  depends_on: [".contextrc"]
  relates_to: ["context.rule"]
created_date: "2024-01-15"
last_updated: "2025-07-12"
owner: "Context Navigator Team"
tags: ["conventions", "immutable-rules", "methodology", "reference"]
complexity: "critical"
maintenance_schedule: "never"
stakeholders: ["developers", "ai-systems", "documentation-team"]
architectural_impact: "critical"
---

# 📜 Context Navigator - Convenções Imutáveis

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

### **Arquivos e Pastas**

```yaml
# Estrutura obrigatória
context-navigator/
├── .contextrc                 # Configuração (imutável)
├── context.rule              # Lei sagrada (imutável)
├── .context-map/             # Mapas automáticos
├── scripts/                  # Ferramentas
├── templates/                # Templates (imutáveis)
├── docs/                     # Documentação
└── examples/                 # Exemplos
```

### **Nomes de Arquivos**

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

### **Nomes de Templates**

```yaml
# Imutável
templates/
├── decisao.md               # Template DECISÃO
├── processo.md              # Template PROCESSO
├── referencia.md            # Template REFERÊNCIA
├── arquitetura.md           # Template ARQUITETURA
├── analise.md               # Template ANÁLISE
└── planejamento.md          # Template PLANEJAMENTO
```

---

## 🏗️ Convenções Estruturais

### **Organização de Pastas**

```yaml
# Metodologia (separada do projeto)
context-navigator/           # Pasta da metodologia
├── .contextrc              # Configuração central
├── context.rule            # Regras para IA
├── .context-map/           # Mapas gerados
│   ├── index.yml          # Índice principal
│   ├── connections.yml    # Conexões
│   ├── conflicts.yml      # Conflitos
│   ├── architecture.yml   # Arquitetura
│   └── contexts/          # Contextos específicos
├── scripts/               # Ferramentas Python
├── templates/             # Templates imutáveis
├── docs/                  # Documentação
└── examples/              # Exemplos práticos

# Documentos do projeto (separados)
project-docs/              # Documentos do projeto
├── decisions/             # Decisões
├── processes/             # Processos
├── references/            # Referências
├── architecture/          # Arquitetura
├── analysis/              # Análises
└── planning/              # Planejamento
```

### **Hierarquia de Documentos**

```yaml
# Por contexto
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

---

## 🏷️ Convenções de Metadados

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

### **Formato de Datas (Imutável)**

```yaml
# Formato ISO 8601
created_date: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"

# Exemplos válidos
created_date: "2024-01-15"
last_updated: "2024-01-15"

# Proibido
created_date: "15/01/2024"
created_date: "Jan 15, 2024"
created_date: "2024-1-15"
```

---

## 📝 Convenções de Conteúdo

### **Estrutura de Headers (Imutável)**

```yaml
# Formato obrigatório
"# "     # Título principal (apenas um por documento)
"## "    # Seções principais
"### "   # Subseções
"#### "  # Sub-subseções (raramente usado)

# Proibido
"#"      # Sem espaço
"##"     # Sem espaço
"##### " # Mais de 4 níveis
```

### **Formatação de Listas**

```yaml
# Listas não ordenadas
- Item 1
- Item 2
- Item 3

# Listas ordenadas
1. Primeiro item
2. Segundo item
3. Terceiro item

# Checklists
- [ ] Tarefa pendente
- [x] Tarefa concluída

# Proibido
* Item (usar hífen)
+ Item (usar hífen)
```

### **Formatação de Código**

````yaml
# Código inline
`código pequeno`

# Blocos de código
```linguagem
// Código com linguagem especificada
const exemplo = "valor";
````

# Comandos shell

```bash
# Comando específico
python script.py --option value
```

# Proibido

```
// Sem linguagem especificada
```

````

### **Formatação de Tabelas**
```yaml
# Formato obrigatório
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Valor 1  | Valor 2  | Valor 3  |
| Valor 4  | Valor 5  | Valor 6  |

# Alinhamento permitido
| Esquerda | Centro | Direita |
|:---------|:------:|--------:|
| Valor 1  | Valor 2| Valor 3 |
````

### **Formatação de Diagramas ASCII**

```yaml
# Componentes simples
┌─────────────┐
│ Componente  │
│   (Tech)    │
└─────────────┘

# Conexões
┌─────────────┐    ┌─────────────┐
│ Frontend    │───▶│ Backend     │
│ (React)     │    │ (Node.js)   │
└─────────────┘    └─────────────┘

# Fluxos
User ──▶ Auth ──▶ API ──▶ DB
     ◀──     ◀──     ◀──
```

---

## 🔗 Convenções de Conexões

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

### **Regras de Conexão (Imutáveis)**

```yaml
# Obrigatório
- Conexões devem apontar para arquivos existentes
- Nomes devem incluir extensão .md
- Caminhos devem ser relativos à pasta de documentos

# Proibido
- Conexões circulares diretas (A → B → A)
- Conexões para arquivos inexistentes
- Conexões vazias quando há relacionamentos
- Conexões incorretas (usar depends_on quando é references)
```

### **Validação de Conexões**

```yaml
# Verificar sempre
1. Arquivo referenciado existe
2. Tipo de conexão correto
3. Reciprocidade quando apropriado
4. Ausência de ciclos problemáticos

# Reciprocidade esperada
- Se A references B, então B pode ter A em impacts
- Se A depends_on B, então B deve ter A em impacts
- Se A blocks B, então B deve ter A em depends_on
```

---

## 📊 Convenções de Templates

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

### **Template PROCESSO (Imutável)**

```yaml
estrutura_obrigatória:
  - "## Objetivo"
  - "### Propósito"
  - "### Escopo"
  - "### Resultados Esperados"
  - "## Pré-requisitos"
  - "### Conhecimentos Necessários"
  - "### Ferramentas Obrigatórias"
  - "### Condições Necessárias"
  - "## Procedimento Principal"
  - "### Passo 1: [Nome]"
  - "### Passo 2: [Nome]"
  - "### Passo 3: [Nome]"
  - "## Validação e Testes"
  - "### Critérios de Sucesso"
  - "### Testes de Validação"
  - "### Métricas de Qualidade"
  - "## Troubleshooting"
  - "### Problema Comum 1"
  - "### Problema Comum 2"

validações_mínimas:
  - Mínimo 3 passos principais
  - Comandos verificáveis
  - Validação para cada passo
  - Troubleshooting abrangente
```

### **Template REFERÊNCIA (Imutável)**

```yaml
estrutura_obrigatória:
  - "## Overview"
  - "### Propósito"
  - "### Escopo"
  - "### Audiência Alvo"
  - "## Configuração e Setup"
  - "### Instalação"
  - "### Configuração Inicial"
  - "### Dependências"
  - "## Referência Detalhada"
  - "### Endpoint/Função 1"
  - "### Endpoint/Função 2"
  - "## Exemplos Práticos"
  - "### Exemplo 1: [Caso de Uso]"
  - "### Exemplo 2: [Caso de Uso]"
  - "## Versionamento"
  - "### Versão Atual"
  - "### Histórico de Mudanças"
  - "### Compatibilidade"

validações_mínimas:
  - Mínimo 2 exemplos práticos
  - Códigos de resposta documentados
  - Parâmetros com tipos definidos
  - Versionamento claro
```

### **Template ARQUITETURA (Imutável)**

```yaml
estrutura_obrigatória:
  - "## Contexto Arquitetural"
  - "### Visão Geral"
  - "### Objetivos"
  - "### Restrições Arquiteturais"
  - "## Visão Arquitetural"
  - "### Diagrama Principal"
  - "### Tecnologias Principais"
  - "## Componentes Arquiteturais"
  - "### Componente 1: [Nome]"
  - "### Componente 2: [Nome]"
  - "## Fluxos Arquiteturais"
  - "### Fluxo 1: [Nome]"
  - "### Fluxo 2: [Nome]"
  - "## Decisões Arquiteturais"
  - "### ADR 1: [Título]"
  - "### ADR 2: [Título]"

validações_mínimas:
  - Mínimo 2 componentes principais
  - Diagramas ASCII bem formados
  - Fluxos completos
  - ADRs com contexto/decisão/impacto
```

### **Template ANÁLISE (Imutável)**

```yaml
estrutura_obrigatória:
  - "## Situação e Contexto"
  - "### Situação Atual"
  - "### Contexto do Problema"
  - "### Objetivos da Análise"
  - "## Metodologia e Coleta de Dados"
  - "### Metodologia Aplicada"
  - "### Fontes de Dados"
  - "### Ferramentas Utilizadas"
  - "## Dados e Evidências"
  - "### Dados Quantitativos"
  - "### Dados Qualitativos"
  - "## Análise Detalhada"
  - "### Root Cause Analysis"
  - "### Correlações Encontradas"
  - "### Padrões Identificados"
  - "## Descobertas e Insights"
  - "### Descoberta 1: [Título]"
  - "### Descoberta 2: [Título]"
  - "## Ações Recomendadas"
  - "### Ações Imediatas"
  - "### Ações de Longo Prazo"

validações_mínimas:
  - Mínimo 2 descobertas fundamentadas
  - Dados quantitativos quando possível
  - Root cause documentado
  - Ações priorizadas
```

### **Template PLANEJAMENTO (Imutável)**

```yaml
estrutura_obrigatória:
  - "## Objetivos e Visão"
  - "### Objetivos SMART"
  - "### Resultados Esperados"
  - "### Critérios de Sucesso"
  - "## Escopo e Entregas"
  - "### Escopo do Projeto"
  - "### Entregas Principais"
  - "### Fora do Escopo"
  - "## Cronograma e Marcos"
  - "### Marcos Principais"
  - "### Fases do Projeto"
  - "## Recursos e Equipe"
  - "### Estrutura da Equipe"
  - "### Orçamento Detalhado"
  - "## Riscos e Dependências"
  - "### Análise de Riscos"
  - "### Dependências Críticas"
  - "## Métricas e Monitoramento"
  - "### KPIs Principais"
  - "### Frequência de Revisão"

validações_mínimas:
  - Objetivos SMART completos
  - Mínimo 2 marcos principais
  - Riscos identificados
  - Métricas mensuráveis
```

---

## 🎯 Convenções de Contexto

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

### **Contextos Especializados (Imutáveis)**

```yaml
infra:
  descrição: "Infraestrutura, deploy, DevOps"
  patterns: ["docker", "kubernetes", "aws", "deploy", "cicd"]
  exemplos: ["deployment-pipeline.md", "monitoring-setup.md"]

shared:
  descrição: "Componentes compartilhados, utilitários"
  patterns: ["utils", "common", "library", "shared", "helper"]
  exemplos: ["logging-utility.md", "validation-library.md"]

core:
  descrição: "Lógica de negócio central, domínio"
  patterns: ["business", "domain", "logic", "service", "entity"]
  exemplos: ["user-management.md", "order-processing.md"]

api:
  descrição: "Interfaces, endpoints, contratos"
  patterns: ["endpoint", "api", "rest", "graphql", "interface"]
  exemplos: ["user-api.md", "payment-endpoints.md"]

data:
  descrição: "Persistência, modelos, schemas"
  patterns: ["database", "model", "schema", "repository", "storage"]
  exemplos: ["user-model.md", "database-design.md"]

ui:
  descrição: "Interface de usuário, componentes visuais"
  patterns: ["component", "view", "page", "frontend", "ui"]
  exemplos: ["login-component.md", "dashboard-layout.md"]
```

### **Regras de Contexto (Imutáveis)**

```yaml
# Obrigatório
- Contexto deve ser consistente com conteúdo
- Nível deve refletir escopo real do documento
- Tipo deve corresponder ao domínio técnico
- Módulo deve ser específico e identificável

# Hierarquia de especificidade
c1_root < c2_module < c3_component

# Especialização por domínio
infra, shared, core, api, data, ui (paralelos)

# Proibido
- Contexto genérico quando há específico
- Mistura de níveis hierárquicos
- Contexto inconsistente com conteúdo
- Módulo vago ou genérico
```

---

## ✅ Convenções de Validação

### **Critérios de Qualidade (Imutáveis)**

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

### **Validação de Metadados**

```yaml
# Campos obrigatórios
required_fields:
  - doc_type
  - context_level
  - context_type
  - module
  - priority
  - status
  - connections
  - created_date
  - last_updated
  - owner

# Validações específicas
doc_type: deve estar na lista permitida
context_level: deve estar na lista permitida
context_type: deve estar na lista permitida
priority: deve estar na lista permitida
status: deve estar na lista permitida
connections: deve ser object válido
created_date: deve ser YYYY-MM-DD
last_updated: deve ser YYYY-MM-DD
owner: deve ser string não vazia
```

### **Validação de Estrutura**

```yaml
# Headers obrigatórios
- Título principal com #
- Seções principais com ##
- Subseções com ###
- Ordem correta das seções
- Nomes exatos do template

# Conteúdo obrigatório
- Todas as seções preenchidas
- Mínimo 50 palavras por seção principal
- Exemplos práticos quando apropriado
- Comandos funcionais quando aplicável
```

### **Validação de Conexões**

```yaml
# Verificações obrigatórias
- Arquivos referenciados existem
- Tipos de conexão corretos
- Ausência de ciclos problemáticos
- Relacionamentos lógicos
- Formato correto dos arrays

# Tipos permitidos
references: []     # Array de strings
impacts: []        # Array de strings
depends_on: []     # Array de strings
blocks: []         # Array de strings
relates_to: []     # Array de strings
```

---

## 🔒 Convenções de Compliance

### **Regras Não Negociáveis**

```yaml
# Estrutura
- Templates NÃO podem ser alterados
- Metadados obrigatórios NÃO podem ser omitidos
- Ordem das seções NÃO pode ser mudada
- Nomes das seções NÃO podem ser alterados

# Processo
- context.rule DEVE ser carregado sempre
- Context maps DEVEM ser consultados
- Validação DEVE ser executada
- Qualidade DEVE ser verificada

# Qualidade
- Score mínimo DEVE ser respeitado
- Erros críticos NÃO são tolerados
- Estrutura DEVE ser completa
- Conteúdo DEVE ser relevante
```

### **Exceções Permitidas**

```yaml
# Conteúdo
- Linguagem específica do domínio
- Exemplos adaptados ao contexto
- Tecnologias específicas mencionadas
- Detalhes técnicos apropriados

# Estrutura menor
- Subseções adicionais SE necessário
- Exemplos extras SE apropriado
- Tabelas extras SE relevante
- Diagramas extras SE útil

# Metadados opcionais
- Campos extras SE documentados
- Tags SE categorizadas
- Reviewers SE processo requer
- Versioning SE aplicável
```

### **Auditoria e Monitoramento**

```yaml
# Verificações regulares
- Scan completo semanal
- Validação automática contínua
- Detecção de conflitos diária
- Análise de qualidade mensal

# Métricas de compliance
- % documentos conformes
- % metadados completos
- % conexões válidas
- % qualidade mínima

# Ações corretivas
- Notificação de problemas
- Sugestões de correção
- Bloqueio de não conformes
- Relatório de compliance
```

---

## 📚 Referência Rápida

### **Checklist de Compliance**

```yaml
✅ Metadados:
  - [ ] Todos os campos obrigatórios preenchidos
  - [ ] Valores dentro dos permitidos
  - [ ] Datas no formato correto
  - [ ] Conexões válidas

✅ Estrutura:
  - [ ] Template correto identificado
  - [ ] Todas as seções obrigatórias presentes
  - [ ] Headers no formato correto
  - [ ] Ordem das seções correta

✅ Conteúdo:
  - [ ] Todas as seções preenchidas
  - [ ] Conteúdo relevante e específico
  - [ ] Exemplos práticos incluídos
  - [ ] Comandos funcionais

✅ Qualidade:
  - [ ] Score mínimo atingido
  - [ ] Zero erros críticos
  - [ ] Máximo 3 warnings
  - [ ] Validação aprovada
```

### **Comandos de Verificação**

```bash
# Validação completa
python scripts/template_validator.py --file documento.md

# Detecção de conflitos
python scripts/conflict_detector.py --type all

# Scan geral
python scripts/context_scanner.py --scan docs/

# Análise de qualidade
python scripts/context_engine.py --analyze documento.md
```

### **Padrões de Erro Comuns**

```yaml
# Metadados
- Campo obrigatório ausente
- Valor fora do permitido
- Data em formato incorreto
- Conexão para arquivo inexistente

# Estrutura
- Seção obrigatória ausente
- Header em formato incorreto
- Ordem das seções errada
- Nome de seção alterado

# Conteúdo
- Seção vazia
- Conteúdo insuficiente
- Exemplo não funcional
- Comando com erro
```

---

## 🎯 Aplicação das Convenções

### **Para Humanos**

1. **Consulte** este documento antes de criar documentos
2. **Use** os templates exatamente como especificado
3. **Valide** sempre antes de finalizar
4. **Corrija** problemas imediatamente

### **Para IA**

1. **Carregue** estas convenções em toda interação
2. **Aplique** rigorosamente todas as regras
3. **Valide** automaticamente o que produz
4. **Corrija** desvios detectados

### **Para Ferramentas**

1. **Implementem** todas as validações
2. **Detectem** desvios automaticamente
3. **Reportem** problemas claramente
4. **Sugiram** correções específicas

---

**📜 Este documento define as regras imutáveis do Context Navigator. Não há exceções.**

_Convenções são a base da consistência metodológica._
