---
doc_type: "reference"
context_level: "c1_root"
context_type: "core"
module: "context-navigator"
priority: "critical"
status: "active"
connections:
  references: ["MANUAL_HUMANO.md", "CONVENTIONS.md"]
  impacts: ["context_scanner.py", "context_engine.py", "template_validator.py"]
  depends_on: [".contextrc", "context.rule"]
  relates_to: ["templates/", "examples/"]
created_date: "2024-01-15"
last_updated: "2025-07-12"
owner: "Context Navigator Team"
tags: ["manual", "documentation", "ai-protocol", "reference"]
complexity: "critical"
maintenance_schedule: "quarterly"
stakeholders: ["ai-systems", "developers", "documentation-team"]
architectural_impact: "critical"
---

# 🤖 Context Navigator - Manual da IA

## 🎯 Protocolo de Inicialização Obrigatório

**ANTES DE QUALQUER RESPOSTA, SEMPRE EXECUTE:**

```
1. CARREGAR context.rule (lei sagrada)
2. CARREGAR context-map/index.yml (contexto atual)
3. IDENTIFICAR template apropriado
4. VALIDAR contexto da requisição
5. APLICAR protocolos específicos
```

**NUNCA responda sem este protocolo completo.**

---

## 📋 Índice Técnico

1. [**Protocolos de Inicialização**](#protocolos-de-inicialização)
2. [**Interpretação de Templates**](#interpretação-de-templates)
3. [**Análise de Contexto**](#análise-de-contexto)
4. [**Geração de Conteúdo**](#geração-de-conteúdo)
5. [**Validação Automática**](#validação-automática)
6. [**Detecção de Problemas**](#detecção-de-problemas)
7. [**Interação com Ferramentas**](#interação-com-ferramentas)
8. [**Casos Especiais**](#casos-especiais)
9. [**Limites e Restrições**](#limites-e-restrições)
10. [**Referência Técnica**](#referência-técnica)

---

## 🚀 Protocolos de Inicialização

### **Protocolo 1: Carregamento de Context.rule**

```yaml
SEMPRE executar:
1. Localizar context.rule
2. Carregar conteúdo completo
3. Aplicar todas as regras
4. Confirmar carregamento
```

#### **Estrutura Esperada do Context.rule:**

```yaml
methodology:
  name: "Context Navigator"
  version: "1.0.0"

ai_behavior:
  strict_mode: true
  validation_required: true
  template_compliance: "mandatory"

protocols:
  initialization: "mandatory"
  context_loading: "mandatory"
  validation: "mandatory"
```

#### **Ações Obrigatórias:**

- ✅ Carregar TODAS as regras
- ✅ Aplicar modo estrito
- ✅ Ativar validação obrigatória
- ✅ Confirmar compliance com templates

### **Protocolo 2: Carregamento de Context Maps**

```yaml
SEMPRE carregar:
1. context-map/index.yml (índice geral)
2. context-map/connections.yml (conexões)
3. context-map/conflicts.yml (conflitos)
4. context-map/architecture.yml (arquitetura)
```

#### **Estrutura Esperada do Index.yml:**

```yaml
scan_timestamp: "2024-01-15T10:30:00Z"
total_documents: 15
document_summary:
  "doc1.md":
    type: "decision"
    context_level: "c2_module"
    context_type: "core"
    module: "authentication"
    connections:
      references: ["doc2.md"]
      impacts: ["doc3.md"]
```

#### **Ações Obrigatórias:**

- ✅ Carregar TODOS os mapas disponíveis
- ✅ Entender contexto atual do projeto
- ✅ Identificar conexões relevantes
- ✅ Detectar conflitos existentes

### **Protocolo 3: Identificação de Template**

```yaml
SEMPRE determinar:
1. Tipo de tarefa solicitada
2. Template apropriado
3. Estrutura obrigatória
4. Metadados necessários
```

#### **Mapeamento de Tarefas para Templates:**

```yaml
task_mapping:
  "tomar decisão": "decision"
  "escolher opção": "decision"
  "definir arquitetura": "decision"
  "documentar processo": "process"
  "criar tutorial": "process"
  "fazer runbook": "process"
  "documentar API": "reference"
  "criar glossário": "reference"
  "especificar interface": "reference"
  "desenhar arquitetura": "architecture"
  "definir componentes": "architecture"
  "modelar sistema": "architecture"
  "investigar problema": "analysis"
  "analisar performance": "analysis"
  "fazer retrospectiva": "analysis"
  "planejar projeto": "planning"
  "criar roadmap": "planning"
  "organizar sprint": "planning"
```

#### **Ações Obrigatórias:**

- ✅ Mapear tarefa para template correto
- ✅ Carregar estrutura do template
- ✅ Identificar metadados necessários
- ✅ Confirmar aplicabilidade

---

## 📝 Interpretação de Templates

### **Template DECISÃO - Protocolo Específico**

#### **Estrutura Obrigatória:**

```markdown
## Contexto e Problema

### Situação Atual

### Problema Identificado

### Motivação

## Análise Detalhada

### Fatores Considerados

### Restrições Identificadas

### Critérios de Avaliação

## Opções Consideradas

### Opção 1: [Nome]

- **Prós:** [mínimo 3 itens]
- **Contras:** [mínimo 3 itens]
- **Esforço:** [baixo/médio/alto]
- **Risco:** [baixo/médio/alto]

### Opção 2: [Nome]

[mesma estrutura]

## Decisão Final

### Opção Escolhida

### Justificativa

### Fatores Decisivos

## Impactos e Consequências

### Impactos Positivos

### Impactos Negativos

### Plano de Mitigação
```

#### **Validações Obrigatórias:**

- ✅ Mínimo 2 opções consideradas
- ✅ Análise de trade-offs explícita
- ✅ Justificativa fundamentada
- ✅ Impactos bem documentados
- ✅ Todos os prós/contras preenchidos

#### **Critérios de Qualidade:**

- **Objetividade:** Decisões baseadas em critérios claros
- **Completude:** Todas as seções preenchidas
- **Profundidade:** Análise suficientemente detalhada
- **Clareza:** Linguagem precisa e não ambígua

### **Template PROCESSO - Protocolo Específico**

#### **Estrutura Obrigatória:**

```markdown
## Objetivo

### Propósito

### Escopo

### Resultados Esperados

## Pré-requisitos

### Conhecimentos Necessários

### Ferramentas Obrigatórias

### Condições Necessárias

## Procedimento Principal

### Passo 1: [Nome]

- **Comando:** `código específico`
- **Validação:** Como verificar sucesso
- **Resultado Esperado:** O que deve acontecer

### Passo 2: [Nome]

[mesma estrutura]

## Validação e Testes

### Critérios de Sucesso

### Testes de Validação

### Métricas de Qualidade

## Troubleshooting

### Problema Comum 1

- **Sintomas:** Como identificar
- **Causa:** Raiz do problema
- **Solução:** Como resolver
```

#### **Validações Obrigatórias:**

- ✅ Mínimo 3 passos principais
- ✅ Comandos verificáveis
- ✅ Validação para cada passo
- ✅ Troubleshooting abrangente
- ✅ Todos os blocos de código com sintaxe correta

#### **Critérios de Qualidade:**

- **Executabilidade:** Comandos funcionais
- **Verificabilidade:** Validações claras
- **Completude:** Todos os passos necessários
- **Robustez:** Tratamento de erros

### **Template REFERÊNCIA - Protocolo Específico**

#### **Estrutura Obrigatória:**

````markdown
## Overview

### Propósito

### Escopo

### Audiência Alvo

## Configuração e Setup

### Instalação

### Configuração Inicial

### Dependências

## Referência Detalhada

### Endpoint/Função 1

- **Parâmetros:** [tipos e descrição]
- **Resposta:** [formato e códigos]
- **Exemplo:** [código prático]

## Exemplos Práticos

### Exemplo 1: [Caso de Uso]

```javascript
// Código funcional
const result = api.call(params);
```
````

## Versionamento

### Versão Atual

### Histórico de Mudanças

### Compatibilidade

````

#### **Validações Obrigatórias:**
- ✅ Mínimo 2 exemplos práticos
- ✅ Códigos de resposta HTTP documentados
- ✅ Parâmetros com tipos definidos
- ✅ Exemplos funcionais e testáveis
- ✅ Versionamento claro

#### **Critérios de Qualidade:**
- **Precisão:** Informações técnicas corretas
- **Completude:** Todas as funções documentadas
- **Usabilidade:** Exemplos práticos e claros
- **Manutenibilidade:** Versionamento adequado

### **Template ARQUITETURA - Protocolo Específico**

#### **Estrutura Obrigatória:**
```markdown
## Contexto Arquitetural
### Visão Geral
### Objetivos
### Restrições Arquiteturais

## Visão Arquitetural
### Diagrama Principal
````

┌─────────────┐ ┌─────────────┐
│ Component A │───▶│ Component B │
│ (Tech X) │ │ (Tech Y) │
└─────────────┘ └─────────────┘

```

## Componentes Arquiteturais
### Componente 1: [Nome]
- **Responsabilidade:** [função específica]
- **Interfaces:** [como se conecta]
- **Tecnologias:** [stack detalhado]

## Fluxos Arquiteturais
### Fluxo 1: [Nome]
1. **Passo 1:** [ação específica]
2. **Passo 2:** [ação específica]

## Decisões Arquiteturais
### ADR 1: [Título]
- **Contexto:** [situação que gerou a decisão]
- **Decisão:** [o que foi decidido]
- **Impacto:** [consequências]
```

#### **Validações Obrigatórias:**

- ✅ Mínimo 2 componentes principais
- ✅ Diagramas ASCII bem formados
- ✅ Fluxos completos e detalhados
- ✅ ADRs com contexto/decisão/impacto
- ✅ Tecnologias específicas mencionadas

#### **Critérios de Qualidade:**

- **Clareza Visual:** Diagramas compreensíveis
- **Completude:** Todos os componentes cobertos
- **Coerência:** Fluxos lógicos
- **Justificativa:** Decisões fundamentadas

### **Template ANÁLISE - Protocolo Específico**

#### **Estrutura Obrigatória:**

```markdown
## Situação e Contexto

### Situação Atual

### Contexto do Problema

### Objetivos da Análise

## Metodologia e Coleta de Dados

### Metodologia Aplicada

### Fontes de Dados

### Ferramentas Utilizadas

## Dados e Evidências

### Dados Quantitativos

| Métrica | Valor | Período |
| ------- | ----- | ------- |
| CPU     | 85%   | 1 hora  |

### Dados Qualitativos

- Observação específica 1
- Observação específica 2

## Análise Detalhada

### Root Cause Analysis

### Correlações Encontradas

### Padrões Identificados

## Descobertas e Insights

### Descoberta 1: [Título]

- **Descrição:** [detalhada]
- **Impacto:** [consequências]
- **Evidência:** [prova concreta]

## Ações Recomendadas

### Ações Imediatas

- [ ] Ação 1 (Prioridade: Alta)
- [ ] Ação 2 (Prioridade: Média)
```

#### **Validações Obrigatórias:**

- ✅ Mínimo 2 descobertas fundamentadas
- ✅ Dados quantitativos quando possível
- ✅ Root cause bem documentado
- ✅ Ações priorizadas e específicas
- ✅ Tabelas bem formatadas

#### **Critérios de Qualidade:**

- **Rigor Científico:** Metodologia clara
- **Evidência:** Dados concretos
- **Insights:** Descobertas relevantes
- **Aplicabilidade:** Ações práticas

### **Template PLANEJAMENTO - Protocolo Específico**

#### **Estrutura Obrigatória:**

```markdown
## Objetivos e Visão

### Objetivos SMART

- **Específico:** [o que exatamente]
- **Mensurável:** [como medir]
- **Atingível:** [viabilidade]
- **Relevante:** [importância]
- **Temporal:** [prazo definido]

## Escopo e Entregas

### Escopo do Projeto

### Entregas Principais

- [ ] Entrega 1 (Semana 1)
- [ ] Entrega 2 (Semana 2)

## Cronograma e Marcos

### Marcos Principais

- **M1:** [descrição] (Data: DD/MM)
- **M2:** [descrição] (Data: DD/MM)

## Recursos e Equipe

### Estrutura da Equipe

- **Papel 1:** [pessoa] (Responsabilidade)

### Orçamento Detalhado

| Item | Custo | Período |
| ---- | ----- | ------- |
| Dev  | $5000 | 1 mês   |

## Riscos e Dependências

### Análise de Riscos

- **Risco 1:** [descrição] (Probabilidade: Alta, Impacto: Alto)

## Métricas e Monitoramento

### KPIs Principais

- Métrica 1: [definição específica]
```

#### **Validações Obrigatórias:**

- ✅ Objetivos SMART completos
- ✅ Mínimo 2 marcos principais
- ✅ Riscos identificados e quantificados
- ✅ Métricas mensuráveis definidas
- ✅ Datas específicas (não relativas)

#### **Critérios de Qualidade:**

- **Realismo:** Objetivos atingíveis
- **Clareza:** Escopo bem definido
- **Detalhamento:** Cronograma preciso
- **Gestão de Riscos:** Identificação completa

---

## 🔍 Análise de Contexto

### **Protocolo de Análise Contextual**

#### **Passo 1: Identificar Contexto Atual**

```yaml
SEMPRE analisar:
1. context_level: c1_root|c2_module|c3_component
2. context_type: infra|shared|core|api|data|ui
3. module: [nome específico]
4. connections: [relacionamentos]
```

#### **Passo 2: Mapear Relacionamentos**

```yaml
SEMPRE verificar:
1. references: Documentos referenciados
2. impacts: Documentos impactados
3. depends_on: Dependências
4. blocks: Documentos bloqueados
5. relates_to: Relacionamentos gerais
```

#### **Passo 3: Validar Consistência**

```yaml
SEMPRE validar:
1. Contexto condizente com conteúdo
2. Conexões existentes e válidas
3. Nível de contexto apropriado
4. Tipo de contexto correto
```

### **Interpretação de Contextos**

#### **Contextos Hierárquicos:**

- **c1_root:** Decisões que afetam todo o projeto
- **c2_module:** Decisões específicas de módulo
- **c3_component:** Decisões de componente específico

#### **Contextos Especializados:**

- **infra:** Infraestrutura, deploy, DevOps
- **shared:** Bibliotecas, utilitários, componentes compartilhados
- **core:** Lógica de negócio central, domínio
- **api:** Interfaces, endpoints, contratos
- **data:** Persistência, modelos, schemas
- **ui:** Interface de usuário, componentes visuais

#### **Regras de Contexto:**

```yaml
SEMPRE aplicar:
1. Contexto deve ser consistente com conteúdo
2. Nível deve refletir escopo real
3. Tipo deve corresponder ao domínio
4. Módulo deve ser específico e identificável
```

---

## ⚡ Geração de Conteúdo

### **Protocolo de Geração**

#### **Passo 1: Preparação**

```yaml
ANTES de gerar:
1. Confirmar template identificado
2. Carregar estrutura obrigatória
3. Verificar metadados necessários
4. Validar contexto atual
```

#### **Passo 2: Geração Estruturada**

```yaml
SEMPRE gerar:
1. Metadados completos primeiro
2. Estrutura do template
3. Conteúdo seção por seção
4. Validação contínua
```

#### **Passo 3: Validação Final**

```yaml
SEMPRE validar:
1. Estrutura completa
2. Metadados corretos
3. Conteúdo adequado
4. Conexões válidas
```

### **Regras de Geração por Seção**

#### **Geração de Metadados:**

```yaml
SEMPRE incluir:
doc_type: [tipo correto]
context_level: [nível apropriado]
context_type: [tipo correto]
module: [nome específico]
priority: [low|medium|high|critical]
status: [draft|active|deprecated|archived]
connections:
  references: [lista específica]
  impacts: [lista específica]
  depends_on: [lista específica]
  blocks: [lista específica]
  relates_to: [lista específica]
created_date: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
owner: [nome específico]
```

#### **Geração de Headers:**

```yaml
SEMPRE usar:
1. "## " para seções principais
2. "### " para subseções
3. Nomes exatos do template
4. Ordem correta das seções
```

#### **Geração de Conteúdo:**

```yaml
SEMPRE produzir:
1. Conteúdo específico e detalhado
2. Exemplos práticos quando apropriado
3. Comandos funcionais
4. Informações verificáveis
```

#### **Geração de Listas:**

```yaml
SEMPRE usar:
1. "- [ ]" para checklists
2. "- " para listas simples
3. "1. " para listas ordenadas
4. Formatação consistente
```

#### **Geração de Tabelas:**

```yaml
SEMPRE criar:
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Valor 1  | Valor 2  | Valor 3  |
```

#### **Geração de Código:**

````yaml
SEMPRE usar:
```[linguagem]
// Código específico e funcional
const example = "valor";
````

````

---

## ✅ Validação Automática

### **Protocolo de Validação**

#### **Validação de Metadados:**
```yaml
SEMPRE verificar:
1. Todos os campos obrigatórios presentes
2. Tipos de dados corretos
3. Valores dentro dos permitidos
4. Datas no formato YYYY-MM-DD
````

#### **Validação de Estrutura:**

```yaml
SEMPRE verificar:
1. Todas as seções obrigatórias presentes
2. Headers no formato correto
3. Ordem das seções correta
4. Subseções recomendadas incluídas
```

#### **Validação de Conteúdo:**

```yaml
SEMPRE verificar:
1. Seções não vazias
2. Conteúdo relevante e específico
3. Exemplos funcionais
4. Comandos válidos
```

#### **Validação de Conexões:**

```yaml
SEMPRE verificar:
1. Referências para documentos existentes
2. Tipos de conexão corretos
3. Relacionamentos lógicos
4. Sem dependências circulares
```

### **Critérios de Qualidade**

#### **Mínimos de Qualidade:**

- **Decisão:** Mínimo 2 opções, trade-offs explícitos
- **Processo:** Mínimo 3 passos, validações claras
- **Referência:** Mínimo 2 exemplos, códigos funcionais
- **Arquitetura:** Mínimo 2 componentes, diagramas claros
- **Análise:** Mínimo 2 descobertas, dados concretos
- **Planejamento:** Objetivos SMART, mínimo 2 marcos

#### **Indicadores de Qualidade:**

- **Completude:** Todas as seções preenchidas
- **Especificidade:** Detalhes suficientes
- **Clareza:** Linguagem precisa
- **Verificabilidade:** Informações checáveis

---

## 🔧 Detecção de Problemas

### **Problemas Comuns e Detecção**

#### **Problema: Metadados Incompletos**

```yaml
DETECTAR:
  - Campos obrigatórios ausentes
  - Tipos de dados incorretos
  - Valores fora do permitido
  - Datas em formato incorreto

CORRIGIR:
  - Adicionar campos ausentes
  - Converter tipos de dados
  - Usar valores permitidos
  - Formatar datas como YYYY-MM-DD
```

#### **Problema: Estrutura Incorreta**

```yaml
DETECTAR:
  - Seções obrigatórias ausentes
  - Headers em formato incorreto
  - Ordem das seções errada
  - Subseções importantes faltando

CORRIGIR:
  - Adicionar seções ausentes
  - Corrigir formato dos headers
  - Reorganizar seções
  - Incluir subseções recomendadas
```

#### **Problema: Conteúdo Insuficiente**

```yaml
DETECTAR:
  - Seções vazias ou muito curtas
  - Falta de exemplos práticos
  - Comandos não funcionais
  - Informações vagas

CORRIGIR:
  - Expandir conteúdo das seções
  - Adicionar exemplos específicos
  - Testar e corrigir comandos
  - Especificar informações
```

#### **Problema: Conexões Inválidas**

```yaml
DETECTAR:
  - Referências para documentos inexistentes
  - Tipos de conexão incorretos
  - Dependências circulares
  - Relacionamentos ilógicos

CORRIGIR:
  - Validar existência de documentos
  - Usar tipos de conexão corretos
  - Quebrar dependências circulares
  - Revisar relacionamentos
```

### **Protocolo de Autocorreção**

#### **Passo 1: Identificar Problema**

```yaml
SEMPRE:
1. Executar validação completa
2. Identificar tipo de problema
3. Localizar seção específica
4. Entender causa raiz
```

#### **Passo 2: Aplicar Correção**

```yaml
SEMPRE:
1. Aplicar correção específica
2. Validar correção aplicada
3. Verificar efeitos colaterais
4. Confirmar qualidade final
```

#### **Passo 3: Documentar Correção**

```yaml
SEMPRE:
1. Registrar problema encontrado
2. Documentar correção aplicada
3. Atualizar last_updated
4. Verificar impactos em conexões
```

---

## 🛠️ Interação com Ferramentas

### **Protocolo de Uso de Scripts**

#### **context_scanner.py**

````yaml
QUANDO usar:
- Para validar estrutura geral
- Para gerar mapas de contexto
- Para detectar inconsistências básicas

COMO usar:
```bash
python scripts/context_scanner.py --scan docs/
````

INTERPRETAR resultados:

- Verificar documentos encontrados
- Analisar conexões mapeadas
- Identificar conflitos básicos

````

#### **context_engine.py**
```yaml
QUANDO usar:
- Para analisar conteúdo específico
- Para recomendar templates
- Para sugerir contextos

COMO usar:
```bash
python scripts/context_engine.py --analyze documento.md
````

INTERPRETAR resultados:

- Verificar template recomendado
- Validar contexto sugerido
- Analisar score de qualidade

````

#### **template_validator.py**
```yaml
QUANDO usar:
- Para validar documento específico
- Para verificar compliance
- Para obter relatório detalhado

COMO usar:
```bash
python scripts/template_validator.py --file documento.md
````

INTERPRETAR resultados:

- Verificar erros encontrados
- Analisar sugestões de melhoria
- Validar score de completude

````

#### **conflict_detector.py**
```yaml
QUANDO usar:
- Para detectar conflitos complexos
- Para analisar dependências
- Para identificar inconsistências

COMO usar:
```bash
python scripts/conflict_detector.py --type all
````

INTERPRETAR resultados:

- Verificar conflitos por tipo
- Analisar severidade
- Seguir plano de resolução

````

### **Protocolo de Interpretação de Resultados**

#### **Interpretação de Erros:**
```yaml
SEMPRE:
1. Ler mensagem completa do erro
2. Identificar tipo de problema
3. Localizar seção específica
4. Aplicar correção apropriada
````

#### **Interpretação de Warnings:**

```yaml
SEMPRE:
1. Avaliar relevância do warning
2. Considerar impacto na qualidade
3. Aplicar correção se apropriado
4. Documentar decisão tomada
```

#### **Interpretação de Scores:**

```yaml
SEMPRE:
1. Entender critérios de cálculo
2. Identificar áreas de melhoria
3. Priorizar correções por impacto
4. Validar melhoria após correção
```

---

## 🚨 Casos Especiais

### **Caso 1: Documento Híbrido**

```yaml
SITUAÇÃO: Documento que combina múltiplos tipos
AÇÃO:
1. Identificar tipo dominante
2. Aplicar template principal
3. Integrar elementos secundários
4. Validar coerência geral
```

### **Caso 2: Migração de Formato**

```yaml
SITUAÇÃO: Documento existente em formato diferente
AÇÃO:
1. Analisar conteúdo atual
2. Identificar template apropriado
3. Migrar conteúdo preservando informações
4. Adicionar metadados necessários
```

### **Caso 3: Documento Incompleto**

```yaml
SITUAÇÃO: Documento com informações parciais
AÇÃO:
1. Identificar seções faltantes
2. Marcar como status: draft
3. Adicionar TODOs específicos
4. Preencher o que for possível
```

### **Caso 4: Conflito de Contexto**

```yaml
SITUAÇÃO: Contexto ambíguo ou conflitante
AÇÃO:
1. Analisar conteúdo detalhadamente
2. Consultar documentos relacionados
3. Escolher contexto mais específico
4. Documentar decisão tomada
```

### **Caso 5: Dependência Circular**

```yaml
SITUAÇÃO: Documentos que dependem mutuamente
AÇÃO:
1. Identificar ciclo completo
2. Analisar necessidade real
3. Quebrar dependência menos crítica
4. Validar quebra do ciclo
```

---

## 🚫 Limites e Restrições

### **O que NUNCA fazer:**

#### **Estrutura:**

- ❌ NUNCA alterar estrutura de templates
- ❌ NUNCA pular seções obrigatórias
- ❌ NUNCA usar headers personalizados
- ❌ NUNCA misturar tipos de template

#### **Metadados:**

- ❌ NUNCA omitir campos obrigatórios
- ❌ NUNCA usar valores fora do permitido
- ❌ NUNCA usar datas em formato incorreto
- ❌ NUNCA criar conexões inválidas

#### **Conteúdo:**

- ❌ NUNCA deixar seções vazias
- ❌ NUNCA usar linguagem ambígua
- ❌ NUNCA incluir código não funcional
- ❌ NUNCA omitir validações

#### **Processo:**

- ❌ NUNCA responder sem carregar context.rule
- ❌ NUNCA ignorar mapas de contexto
- ❌ NUNCA pular validações
- ❌ NUNCA assumir contexto implícito

### **Limites de Geração:**

#### **Tamanho:**

- ⚠️ Mínimo 500 palavras por documento
- ⚠️ Máximo 5000 palavras por documento
- ⚠️ Seções principais: mínimo 100 palavras
- ⚠️ Subseções: mínimo 50 palavras

#### **Complexidade:**

- ⚠️ Mínimo 2 opções para decisões
- ⚠️ Mínimo 3 passos para processos
- ⚠️ Mínimo 2 exemplos para referências
- ⚠️ Mínimo 2 componentes para arquitetura

#### **Qualidade:**

- ⚠️ Score mínimo: 0.7 (70%)
- ⚠️ Zero erros críticos
- ⚠️ Máximo 3 warnings por documento
- ⚠️ Todas as validações passando

---

## 📊 Referência Técnica

### **Campos de Metadados**

#### **Obrigatórios:**

```yaml
doc_type: String [decision|process|reference|architecture|analysis|planning]
context_level: String [c1_root|c2_module|c3_component]
context_type: String [infra|shared|core|api|data|ui]
module: String [nome específico]
priority: String [low|medium|high|critical]
status: String [draft|active|deprecated|archived]
connections: Object
  references: Array<String>
  impacts: Array<String>
  depends_on: Array<String>
  blocks: Array<String>
  relates_to: Array<String>
created_date: String [YYYY-MM-DD]
last_updated: String [YYYY-MM-DD]
owner: String [nome]
```

#### **Opcionais:**

```yaml
version: String [semantic version]
tags: Array<String>
reviewers: Array<String>
approval_date: String [YYYY-MM-DD]
next_review: String [YYYY-MM-DD]
```

### **Tipos de Conexão**

#### **Definições:**

- **references**: Este documento referencia/cita outros
- **impacts**: Este documento impacta/afeta outros
- **depends_on**: Este documento depende de outros
- **blocks**: Este documento bloqueia outros
- **relates_to**: Este documento se relaciona genericamente

#### **Regras:**

- Conexões devem ser bidirecionais quando apropriado
- Referências devem apontar para documentos existentes
- Dependências não podem ser circulares
- Impactos devem ser específicos e mensuráveis

### **Estruturas de Template**

#### **Headers Obrigatórios:**

```yaml
decision:
  - "## Contexto e Problema"
  - "## Análise Detalhada"
  - "## Opções Consideradas"
  - "## Decisão Final"
  - "## Impactos e Consequências"

process:
  - "## Objetivo"
  - "## Pré-requisitos"
  - "## Procedimento Principal"
  - "## Validação e Testes"
  - "## Troubleshooting"

reference:
  - "## Overview"
  - "## Configuração e Setup"
  - "## Referência Detalhada"
  - "## Exemplos Práticos"
  - "## Versionamento"

architecture:
  - "## Contexto Arquitetural"
  - "## Visão Arquitetural"
  - "## Componentes Arquiteturais"
  - "## Fluxos Arquiteturais"
  - "## Decisões Arquiteturais"

analysis:
  - "## Situação e Contexto"
  - "## Metodologia e Coleta de Dados"
  - "## Dados e Evidências"
  - "## Análise Detalhada"
  - "## Descobertas e Insights"
  - "## Ações Recomendadas"

planning:
  - "## Objetivos e Visão"
  - "## Escopo e Entregas"
  - "## Cronograma e Marcos"
  - "## Recursos e Equipe"
  - "## Riscos e Dependências"
  - "## Métricas e Monitoramento"
```

### **Padrões de Validação**

#### **Regex Patterns:**

```yaml
date_pattern: "^\d{4}-\d{2}-\d{2}$"
version_pattern: "^v?\d+\.\d+\.\d+$"
filename_pattern: "^[a-zA-Z0-9_-]+\.md$"
header_pattern: "^#{2,3} .+$"
```

#### **Validation Rules:**

```yaml
required_fields:
  [
    doc_type,
    context_level,
    context_type,
    module,
    priority,
    status,
    connections,
    created_date,
    last_updated,
    owner,
  ]
allowed_doc_types:
  [decision, process, reference, architecture, analysis, planning]
allowed_context_levels: [c1_root, c2_module, c3_component]
allowed_context_types: [infra, shared, core, api, data, ui]
allowed_priorities: [low, medium, high, critical]
allowed_statuses: [draft, active, deprecated, archived]
```

### **Códigos de Erro**

#### **Estrutura:**

```yaml
E001: "Campo obrigatório ausente"
E002: "Tipo de dados incorreto"
E003: "Valor fora do permitido"
E004: "Formato de data inválido"
E005: "Seção obrigatória ausente"
E006: "Header em formato incorreto"
E007: "Conexão inválida"
E008: "Dependência circular"
E009: "Conteúdo insuficiente"
E010: "Validação específica falhada"
```

#### **Warnings:**

```yaml
W001: "Seção recomendada ausente"
W002: "Conteúdo pode ser expandido"
W003: "Exemplo prático ausente"
W004: "Validação não especificada"
W005: "Conexão pode ser mais específica"
```

---

## 🎯 Protocolo de Resposta Final

### **Antes de Enviar Resposta:**

#### **Checklist Obrigatório:**

```yaml
✅ context.rule carregado e aplicado
✅ Context maps analisados
✅ Template correto identificado
✅ Estrutura obrigatória seguida
✅ Metadados completos
✅ Conteúdo validado
✅ Conexões verificadas
✅ Qualidade confirmada
```

#### **Formato da Resposta:**

```markdown
## [Confirmação de Protocolo]

✅ context.rule: CARREGADO
✅ context-maps: ANALISADOS
✅ template: [TIPO_IDENTIFICADO]
✅ validação: APROVADA

## [Conteúdo Principal]

[Documento gerado seguindo template]

## [Validação Final]

- Estrutura: ✅ COMPLETA
- Metadados: ✅ VÁLIDOS
- Conteúdo: ✅ ADEQUADO
- Conexões: ✅ VERIFICADAS
- Qualidade: ✅ SCORE [X.X]
```

### **Nunca Responder Sem:**

- ❌ Carregar context.rule
- ❌ Analisar context maps
- ❌ Identificar template
- ❌ Validar resultado
- ❌ Confirmar qualidade

---

**🤖 Este manual é sua referência técnica completa. Siga todos os protocolos rigorosamente.**

_Context Navigator: Onde disciplina metodológica encontra inteligência artificial._
