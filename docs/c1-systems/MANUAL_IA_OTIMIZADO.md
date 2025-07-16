---
doc_type: "reference"
context_level: "c1_root"
context_type: "core"
module: "context-navigator"
priority: "critical"
status: "active"
connections:
  references: ["MANUAL_IA.md"]
  impacts: ["context_scanner.py", "context_engine.py"]
  depends_on: ["workspace.yml", "context.rule"]
created_date: "2025-01-13"
last_updated: "2025-01-13"
owner: "Context Navigator Team"
tags: ["manual", "rule", "ai-protocol", "optimized", "2.0"]
version: "2.0"
---

# 🤖 Context Navigator 2.0 - Manual da IA (Otimizado)

## 🎯 Protocolo Obrigatório 2.0

**SEMPRE EXECUTE ANTES DE RESPONDER:**

```
1. CARREGAR context.rule
2. CARREGAR .cn_model/maps/index.yml (via WorkspaceManager)
3. IDENTIFICAR template apropriado
4. VALIDAR contexto da requisição
5. APLICAR template específico
```

---

## 📋 Templates e Estruturas

### **Template DECISION**

```markdown
## Contexto e Problema

### Situação Atual

### Problema Identificado

## Análise Detalhada

### Fatores Considerados

### Critérios de Avaliação

## Opções Consideradas

### Opção 1: [Nome]

- **Prós:** [mínimo 3]
- **Contras:** [mínimo 3]
- **Esforço:** [baixo/médio/alto]

### Opção 2: [Nome]

[mesma estrutura]

## Decisão Final

### Opção Escolhida

### Justificativa

## Impactos e Consequências

### Impactos Positivos

### Plano de Mitigação
```

### **Template PROCESS**

```markdown
## Objetivo

### Propósito

### Resultados Esperados

## Pré-requisitos

### Ferramentas Obrigatórias

### Condições Necessárias

## Procedimento Principal

### Passo 1: [Nome]

- **Comando:** `código específico`
- **Validação:** Como verificar
- **Resultado:** O que esperar

## Validação e Testes

### Critérios de Sucesso

### Testes de Validação

## Troubleshooting

### Problema Comum 1

- **Sintomas:** [como identificar]
- **Solução:** [como resolver]
```

### **Template REFERENCE**

````markdown
## Overview

### Propósito

### Audiência Alvo

## Configuração e Setup

### Instalação

### Configuração Inicial

## Referência Detalhada

### Função/Endpoint 1

- **Parâmetros:** [tipos]
- **Resposta:** [formato]
- **Exemplo:** [código]

## Exemplos Práticos

### Exemplo 1: [Caso de Uso]

```[linguagem]
código funcional
```
````

## Versionamento

### Versão Atual

### Histórico de Mudanças

````

### **Template ARCHITECTURE**

```markdown
## Contexto Arquitetural
### Visão Geral
### Objetivos

## Visão Arquitetural
### Diagrama Principal
````

[Diagrama ASCII]

```

## Componentes Arquiteturais
### Componente 1: [Nome]
- **Responsabilidade:** [função]
- **Tecnologias:** [stack]

## Fluxos Arquiteturais
### Fluxo 1: [Nome]
1. **Passo 1:** [ação]
2. **Passo 2:** [ação]

## Decisões Arquiteturais
### ADR 1: [Título]
- **Contexto:** [situação]
- **Decisão:** [escolha]
- **Impacto:** [consequências]
```

### **Template ANALYSIS**

```markdown
## Situação e Contexto

### Situação Atual

### Objetivos da Análise

## Metodologia e Coleta de Dados

### Metodologia Aplicada

### Fontes de Dados

## Dados e Evidências

### Dados Quantitativos

| Métrica | Valor | Período |
| ------- | ----- | ------- |

### Dados Qualitativos

- Observação 1
- Observação 2

## Análise Detalhada

### Root Cause Analysis

### Padrões Identificados

## Descobertas e Insights

### Descoberta 1: [Título]

- **Descrição:** [detalhada]
- **Impacto:** [consequências]

## Ações Recomendadas

### Ações Imediatas

- [ ] Ação 1 (Prioridade: Alta)
```

### **Template PLANNING**

```markdown
## Objetivos e Visão

### Objetivos SMART

- **Específico:** [o que]
- **Mensurável:** [como medir]
- **Temporal:** [prazo]

## Escopo e Entregas

### Entregas Principais

- [ ] Entrega 1 (Semana 1)
- [ ] Entrega 2 (Semana 2)

## Cronograma e Marcos

### Marcos Principais

- **M1:** [descrição] (DD/MM)
- **M2:** [descrição] (DD/MM)

## Recursos e Equipe

### Estrutura da Equipe

- **Papel 1:** [pessoa] (Responsabilidade)

## Riscos e Dependências

### Análise de Riscos

- **Risco 1:** [descrição] (Prob: Alta, Impacto: Alto)

## Métricas e Monitoramento

### KPIs Principais

- Métrica 1: [definição]
```

---

## 🎨 Metadados Obrigatórios

```yaml
doc_type: [decision|process|reference|architecture|analysis|planning]
context_level: [c1_root|c2_module|c3_component]
context_type: [infra|shared|core|api|data|ui]
module: [nome específico]
priority: [low|medium|high|critical]
status: [draft|active|deprecated|archived]
connections:
  references: [lista]
  impacts: [lista]
  depends_on: [lista]
  relates_to: [lista]
created_date: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
owner: [nome]
```

### **Contextos Hierárquicos:**

- **c1_root:** Afeta todo o projeto
- **c2_module:** Específico de módulo
- **c3_component:** Específico de componente

### **Contextos Especializados:**

- **infra:** Infraestrutura, deploy
- **shared:** Bibliotecas, utilitários
- **core:** Lógica de negócio
- **api:** Interfaces, endpoints
- **data:** Persistência, modelos
- **ui:** Interface de usuário

---

## ✅ Validações Críticas

### **Validação de Estrutura:**

- ✅ Todas as seções obrigatórias presentes
- ✅ Headers no formato correto (`## ` e `### `)
- ✅ Metadados completos e válidos

### **Validação de Conteúdo:**

- ✅ **Decisão:** Mínimo 2 opções com prós/contras
- ✅ **Processo:** Mínimo 3 passos com validações
- ✅ **Referência:** Mínimo 2 exemplos funcionais
- ✅ **Arquitetura:** Mínimo 2 componentes com diagrama
- ✅ **Análise:** Mínimo 2 descobertas com dados
- ✅ **Planejamento:** Objetivos SMART com mínimo 2 marcos

### **Validação de Conexões:**

- ✅ Referências para documentos existentes
- ✅ Sem dependências circulares
- ✅ Tipos de conexão apropriados

---

## 🔧 Mapeamento de Tarefas

```yaml
PALAVRAS-CHAVE → TEMPLATE:
"tomar decisão|escolher|definir" → decision
"documentar processo|tutorial|runbook" → process
"documentar API|glossário|referência" → reference
"desenhar arquitetura|componentes|sistema" → architecture
"investigar|analisar|retrospectiva" → analysis
"planejar|roadmap|sprint" → planning
```

---

## 🚨 Regras Críticas 2.0

### **SEMPRE:**

- ✅ Carregar context.rule antes de responder
- ✅ Detectar workspace via WorkspaceManager (.cn_model/)
- ✅ Usar template exato (não modificar estrutura)
- ✅ Incluir todos os metadados obrigatórios
- ✅ Validar conexões existentes
- ✅ Preencher todas as seções obrigatórias

### **NUNCA:**

- ❌ Alterar estrutura de templates
- ❌ Omitir campos obrigatórios
- ❌ Deixar seções vazias
- ❌ Criar conexões inválidas
- ❌ Usar datas em formato incorreto

---

## 📊 Critérios de Qualidade

### **Mínimos Aceitáveis:**

- **Estrutura:** 100% das seções obrigatórias
- **Conteúdo:** Mínimo 500 palavras
- **Especificidade:** Detalhes suficientes
- **Executabilidade:** Comandos funcionais (quando aplicável)

### **Indicadores de Qualidade:**

- **Completude:** Todas as seções preenchidas
- **Clareza:** Linguagem precisa
- **Verificabilidade:** Informações checáveis
- **Aplicabilidade:** Conteúdo útil

---

## 🏗️ Workspace e Componentização 2.0

### **Workspace Detection (WorkspaceManager)**

```yaml
SEMPRE verificar:
1. .cn_model/workspace.yml (diretório atual)
2. ../.cn_model/workspace.yml (diretórios pais)
3. ~/.local/share/context-navigator/ (global)
4. ~/.context-navigator/ (fallback 1.0)
```

### **Code Bridge (@cn:)**

```yaml
# Conectar documentação ↔ código
# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component user-authentication
# @cn:doc decisions/auth-architecture.md
# @cn:context-level c2_module
# @cn:context-type core
# @cn:purpose "Sistema de autenticação"
# ============================================
```

### **Saves em .cn_model/ (Obrigatório)**

```yaml
SEMPRE salvar em:
  - .cn_model/maps/index.yml
  - .cn_model/maps/connections.yml
  - .cn_model/maps/conflicts.yml
  - .cn_model/components/

NUNCA salvar em:
  - .context-map/ (arquitetura 1.0)
  - .contextrc (arquitetura 1.0)
```

---

## 🎯 Protocolo de Resposta 2.0

### **Formato Padrão:**

```markdown
## [Confirmação 2.0]

✅ context.rule: CARREGADO
✅ workspace: DETECTADO (.cn_model/)
✅ template: [TIPO]
✅ validação: APROVADA

## [Documento]

[Conteúdo seguindo template]

## [Validação Final]

- Estrutura: ✅ COMPLETA
- Metadados: ✅ VÁLIDOS
- Workspace: ✅ .cn_model/
- Qualidade: ✅ APROVADA
```

---

**🤖 Manual 2.0 otimizado para uso diário eficiente com WorkspaceManager e componentização.**

_Context Navigator 2.0: Disciplina inteligente sem complexidade desnecessária._
