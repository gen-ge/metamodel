---
# =============================================================================
# METADADOS OBRIGATÓRIOS (IMUTÁVEIS)
# =============================================================================

# Tipo do documento (OBRIGATÓRIO)
doc_type: "analysis"

# Título do documento (OBRIGATÓRIO)
title: "[PREENCHER] Título da Análise"

# Contexto hierárquico (OBRIGATÓRIO)
context_level: "c2_module" # c1_root | c2_module | c3_component

# Contexto especializado (OBRIGATÓRIO)
context_type: "core" # infra | shared | core | api | data | ui

# Módulo específico (OBRIGATÓRIO)
module: "[PREENCHER] Nome do Módulo"

# Conexões com outros documentos (OBRIGATÓRIO)
connections:
  references: ["referencia.md", "arquitetura.md"] # Referenciam dados e especificações
  impacts: ["decisao.md", "planejamento.md"] # Análises impactam decisões e planejamento
  depends_on: ["processo.md"] # Análises dependem de processos executados
  blocks: [] # Documentos bloqueados
  relates_to: [] # Documentos relacionados

# Datas (OBRIGATÓRIAS)
created_date: "2024-01-15"
last_updated: "2024-01-15"

# =============================================================================
# METADADOS OPCIONAIS (EXTENSÍVEIS)
# =============================================================================

# Prioridade da análise
priority: "high" # critical | high | medium | low

# Status atual
status: "active" # draft | review | active | completed | archived

# Responsável pela análise
owner: "[PREENCHER] Nome do Responsável"

# Tags para categorização
tags: ["analysis", "performance", "investigation"]

# Complexidade da análise
complexity: "medium" # low | medium | high | critical

# Agenda de manutenção
maintenance_schedule: "never" # never | monthly | quarterly | yearly

# Tipo de análise
analysis_type: "performance" # performance | bug | retrospective | investigation | metrics | security

# Objetivo da análise
analysis_objective: "optimization" # optimization | troubleshooting | monitoring | compliance | improvement

# Metodologia usada
methodology: "data-driven" # data-driven | observational | experimental | comparative | forensic

# Período analisado
analysis_period: "last_30_days" # last_24h | last_7_days | last_30_days | last_quarter | custom

# Ferramentas utilizadas
tools_used: ["grafana", "elk", "profiler", "monitoring"]

# Métricas principais
key_metrics: ["response_time", "throughput", "error_rate", "resource_usage"]

# Escopo da análise
scope: "system-wide" # component | service | system-wide | integration

# Criticidade dos achados
criticality: "medium" # low | medium | high | critical

# Confidencialidade
confidentiality: "internal" # public | internal | restricted | confidential

# Data limite para ações
action_deadline: "2024-02-15"

# Stakeholders envolvidos
stakeholders: ["dev-team", "ops-team", "product-team"]

# Impacto de negócio
business_impact: "medium" # low | medium | high | critical

# Custo estimado das ações
estimated_cost: "medium" # low | medium | high | critical

# Risco se não agir
risk_if_no_action: "high" # low | medium | high | critical
---

<!-- CONTEXT_META
template_version: "1.0.0"
template_type: "analysis"
generated_by: "context-navigator"
validation_status: "pending"
last_validated: "2024-01-15"
compliance_check: "passed"
metadata_completeness: "100%"
connection_accuracy: "pending"
context_consistency: "verified"
analysis_category: "performance"
investigation_depth: "detailed"
-->

# 🔍 [TÍTULO DA ANÁLISE]

> **Template:** Análise | **Contexto:** [CONTEXTO] | **Módulo:** [MÓDULO]  
> **Criado:** [DATA] | **Atualizado:** [DATA] | **Status:** [STATUS]

## 📋 Metadados da Análise

**Tipo:** [PERFORMANCE/BUG/RETROSPECTIVA/INVESTIGAÇÃO/MÉTRICAS/SEGURANÇA]  
**Objetivo:** [OTIMIZAÇÃO/TROUBLESHOOTING/MONITORAMENTO/COMPLIANCE/MELHORIA]  
**Metodologia:** [DATA-DRIVEN/OBSERVACIONAL/EXPERIMENTAL/COMPARATIVA/FORENSE]  
**Período:** [ÚLTIMAS 24H/7 DIAS/30 DIAS/TRIMESTRE/CUSTOMIZADO]  
**Criticidade:** [BAIXA/MÉDIA/ALTA/CRÍTICA]  
**Confidencialidade:** [PÚBLICA/INTERNA/RESTRITA/CONFIDENCIAL]

## 🎯 Situação e Contexto

### **Situação Atual**

[Descreva a situação atual que motivou esta análise]

### **Problema Identificado**

[Descreva claramente o problema ou questão a ser analisada]

### **Motivação para Análise**

[Explique por que esta análise é necessária agora]

### **Objetivos da Análise**

- [Objetivo específico 1]
- [Objetivo específico 2]
- [Objetivo específico 3]

### **Escopo da Análise**

- **Incluído:** [O que está incluído na análise]
- **Excluído:** [O que está fora do escopo]
- **Limitações:** [Limitações conhecidas]

### **Hipóteses Iniciais**

1. [Hipótese 1]
2. [Hipótese 2]
3. [Hipótese 3]

## 📊 Metodologia e Coleta de Dados

### **Metodologia Aplicada**

**Abordagem:** [NOME DA METODOLOGIA]

**Justificativa:**
[Por que esta metodologia foi escolhida]

**Passos da Metodologia:**

1. [Passo 1]
2. [Passo 2]
3. [Passo 3]
4. [Passo 4]

### **Fontes de Dados**

| Fonte     | Tipo           | Período   | Confiabilidade     |
| --------- | -------------- | --------- | ------------------ |
| [Fonte 1] | [Tipo de dado] | [Período] | [Alta/Média/Baixa] |
| [Fonte 2] | [Tipo de dado] | [Período] | [Alta/Média/Baixa] |
| [Fonte 3] | [Tipo de dado] | [Período] | [Alta/Média/Baixa] |

### **Ferramentas Utilizadas**

- **Monitoramento:** [Ferramenta de monitoramento]
- **Análise:** [Ferramenta de análise]
- **Visualização:** [Ferramenta de visualização]
- **Processamento:** [Ferramenta de processamento]

### **Métricas Coletadas**

| Métrica     | Unidade   | Frequência   | Fonte   |
| ----------- | --------- | ------------ | ------- |
| [Métrica 1] | [Unidade] | [Frequência] | [Fonte] |
| [Métrica 2] | [Unidade] | [Frequência] | [Fonte] |
| [Métrica 3] | [Unidade] | [Frequência] | [Fonte] |

## 📈 Dados e Evidências

### **Dados Quantitativos**

#### **Métricas de Performance**

```
Tempo de Resposta:
- Baseline: 150ms (média)
- Atual: 350ms (média)
- Deterioração: +133%

Throughput:
- Baseline: 1000 req/s
- Atual: 600 req/s
- Redução: -40%

Error Rate:
- Baseline: 0.1%
- Atual: 2.5%
- Aumento: +2400%
```

#### **Tendências Temporais**

```
Semana 1: Response Time = 150ms, Errors = 0.1%
Semana 2: Response Time = 180ms, Errors = 0.3%
Semana 3: Response Time = 250ms, Errors = 1.2%
Semana 4: Response Time = 350ms, Errors = 2.5%
```

#### **Distribuição por Componente**

| Componente     | Tempo Médio | Erro Rate | Impacto |
| -------------- | ----------- | --------- | ------- |
| [Componente 1] | 100ms       | 0.5%      | Alto    |
| [Componente 2] | 200ms       | 1.0%      | Médio   |
| [Componente 3] | 50ms        | 0.1%      | Baixo   |

### **Dados Qualitativos**

#### **Observações Operacionais**

- [Observação 1]
- [Observação 2]
- [Observação 3]

#### **Feedback dos Usuários**

- [Feedback 1]
- [Feedback 2]
- [Feedback 3]

#### **Logs e Eventos Relevantes**

```
2024-01-15 10:30:00 - ERROR: Connection timeout to database
2024-01-15 10:31:00 - WARN: High memory usage detected (85%)
2024-01-15 10:32:00 - ERROR: Service unavailable
```

## 🔬 Análise Detalhada

### **Análise de Root Cause**

#### **Problema Principal**

[Identifique o problema principal baseado nos dados]

#### **Análise dos 5 Porquês**

1. **Por que** o sistema está lento?

   - **Porque** as consultas ao banco estão demoradas

2. **Por que** as consultas estão demoradas?

   - **Porque** não há índices adequados

3. **Por que** não há índices adequados?

   - **Porque** o schema mudou recentemente

4. **Por que** o schema mudou sem considerar índices?

   - **Porque** não há processo de review de schema

5. **Por que** não há processo de review?
   - **Porque** não foi estabelecido nas práticas da equipe

**Root Cause:** Falta de processo de review de mudanças de schema

#### **Análise de Espinha de Peixe**

```
                    Sistema Lento
                         │
    ┌────────────────────┼────────────────────┐
    │                    │                    │
  People              Process             Technology
    │                    │                    │
  - Falta de           - Sem review         - Índices
    expertise          - Sem monitoring       inadequados
  - Sobrecarga         - Sem alertas        - Query
    de trabalho        - Sem documentação     otimization
```

### **Análise de Correlação**

| Variável A   | Variável B   | Correlação | Significância |
| ------------ | ------------ | ---------- | ------------- |
| [Variável 1] | [Variável 2] | 0.85       | Alta          |
| [Variável 3] | [Variável 4] | 0.45       | Média         |
| [Variável 5] | [Variável 6] | -0.2       | Baixa         |

### **Análise de Padrões**

- **Padrão Temporal:** [Padrão identificado]
- **Padrão Geográfico:** [Padrão identificado]
- **Padrão de Uso:** [Padrão identificado]

### **Análise de Impacto**

- **Impacto Técnico:** [Descrição do impacto]
- **Impacto no Usuário:** [Descrição do impacto]
- **Impacto no Negócio:** [Descrição do impacto]

## 🎯 Descobertas e Insights

### **Descobertas Principais**

#### **Descoberta 1: [TÍTULO]**

**Descrição:** [Descrição detalhada da descoberta]

**Evidências:**

- [Evidência 1]
- [Evidência 2]
- [Evidência 3]

**Impacto:** [Impacto desta descoberta]

**Confiança:** [Alta/Média/Baixa]

---

#### **Descoberta 2: [TÍTULO]**

**Descrição:** [Descrição detalhada da descoberta]

**Evidências:**

- [Evidência 1]
- [Evidência 2]
- [Evidência 3]

**Impacto:** [Impacto desta descoberta]

**Confiança:** [Alta/Média/Baixa]

---

#### **Descoberta 3: [TÍTULO]**

**Descrição:** [Descrição detalhada da descoberta]

**Evidências:**

- [Evidência 1]
- [Evidência 2]
- [Evidência 3]

**Impacto:** [Impacto desta descoberta]

**Confiança:** [Alta/Média/Baixa]

### **Insights Estratégicos**

1. [Insight estratégico 1]
2. [Insight estratégico 2]
3. [Insight estratégico 3]

### **Padrões Identificados**

- [Padrão 1]
- [Padrão 2]
- [Padrão 3]

### **Anomalias Detectadas**

- [Anomalia 1]
- [Anomalia 2]
- [Anomalia 3]

## ⚡ Ações Recomendadas

### **Ações Imediatas (24-48h)**

#### **Ação 1: [TÍTULO]**

**Prioridade:** [CRÍTICA/ALTA/MÉDIA/BAIXA]  
**Esforço:** [BAIXO/MÉDIO/ALTO]  
**Impacto:** [BAIXO/MÉDIO/ALTO]

**Descrição:** [Descrição da ação]

**Passos:**

1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

**Recursos necessários:**

- [Recurso 1]
- [Recurso 2]

**Responsável:** [Nome do responsável]

**Prazo:** [Prazo específico]

---

#### **Ação 2: [TÍTULO]**

**Prioridade:** [CRÍTICA/ALTA/MÉDIA/BAIXA]  
**Esforço:** [BAIXO/MÉDIO/ALTO]  
**Impacto:** [BAIXO/MÉDIO/ALTO]

**Descrição:** [Descrição da ação]

**Passos:**

1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

**Recursos necessários:**

- [Recurso 1]
- [Recurso 2]

**Responsável:** [Nome do responsável]

**Prazo:** [Prazo específico]

### **Ações de Curto Prazo (1-2 semanas)**

#### **Ação 3: [TÍTULO]**

**Prioridade:** [CRÍTICA/ALTA/MÉDIA/BAIXA]  
**Esforço:** [BAIXO/MÉDIO/ALTO]  
**Impacto:** [BAIXO/MÉDIO/ALTO]

**Descrição:** [Descrição da ação]

**Justificativa:** [Por que esta ação é necessária]

**Benefícios esperados:**

- [Benefício 1]
- [Benefício 2]

**Riscos:**

- [Risco 1]
- [Risco 2]

**Responsável:** [Nome do responsável]

**Prazo:** [Prazo específico]

### **Ações de Médio Prazo (1-3 meses)**

#### **Ação 4: [TÍTULO]**

**Prioridade:** [CRÍTICA/ALTA/MÉDIA/BAIXA]  
**Esforço:** [BAIXO/MÉDIO/ALTO]  
**Impacto:** [BAIXO/MÉDIO/ALTO]

**Descrição:** [Descrição da ação]

**Planejamento:**

- **Fase 1:** [Fase 1]
- **Fase 2:** [Fase 2]
- **Fase 3:** [Fase 3]

**Recursos necessários:**

- [Recurso 1]
- [Recurso 2]

**Responsável:** [Nome do responsável]

**Prazo:** [Prazo específico]

## 📊 Monitoramento e Acompanhamento

### **Métricas de Acompanhamento**

| Métrica     | Valor Atual | Meta   | Prazo   |
| ----------- | ----------- | ------ | ------- |
| [Métrica 1] | [Valor]     | [Meta] | [Prazo] |
| [Métrica 2] | [Valor]     | [Meta] | [Prazo] |
| [Métrica 3] | [Valor]     | [Meta] | [Prazo] |

### **Alertas e Thresholds**

- **Crítico:** [Condição crítica]
- **Alto:** [Condição alta]
- **Médio:** [Condição média]

### **Cronograma de Revisão**

- **Revisão semanal:** [Responsável e objetivo]
- **Revisão mensal:** [Responsável e objetivo]
- **Revisão trimestral:** [Responsável e objetivo]

### **Dashboards**

- **Dashboard 1:** [Link e descrição]
- **Dashboard 2:** [Link e descrição]
- **Dashboard 3:** [Link e descrição]

### **Relatórios Automáticos**

- **Diário:** [Descrição do relatório]
- **Semanal:** [Descrição do relatório]
- **Mensal:** [Descrição do relatório]

## 🔄 Lições Aprendidas

### **O que Funcionou Bem**

1. [Lição aprendida 1]
2. [Lição aprendida 2]
3. [Lição aprendida 3]

### **O que Não Funcionou**

1. [Lição aprendida 1]
2. [Lição aprendida 2]
3. [Lição aprendida 3]

### **Melhorias no Processo**

1. [Melhoria 1]
2. [Melhoria 2]
3. [Melhoria 3]

### **Recomendações para Futuras Análises**

1. [Recomendação 1]
2. [Recomendação 2]
3. [Recomendação 3]

## 📚 Referências e Anexos

### **Documentação Relacionada**

- [Documento 1] - [Descrição]
- [Documento 2] - [Descrição]
- [Documento 3] - [Descrição]

### **Ferramentas e Recursos**

- [Ferramenta 1] - [Link/Descrição]
- [Ferramenta 2] - [Link/Descrição]
- [Ferramenta 3] - [Link/Descrição]

### **Dados Brutos**

- [Dataset 1] - [Localização]
- [Dataset 2] - [Localização]
- [Dataset 3] - [Localização]

### **Scripts e Queries**

```sql
-- Query para análise de performance
SELECT component, AVG(response_time), COUNT(*) as requests
FROM performance_log
WHERE timestamp BETWEEN '2024-01-01' AND '2024-01-31'
GROUP BY component
ORDER BY AVG(response_time) DESC;
```

### **Histórico de Versões**

| Versão | Data       | Autor  | Mudanças       |
| ------ | ---------- | ------ | -------------- |
| 1.0    | 2024-01-15 | [Nome] | Versão inicial |

---

<!-- VALIDATION_CHECKLIST
[ ] Todos os metadados obrigatórios preenchidos
[ ] Situação e contexto claramente definidos
[ ] Metodologia aplicada documentada
[ ] Dados coletados e analisados
[ ] Descobertas principais identificadas
[ ] Ações recomendadas priorizadas
[ ] Monitoramento e acompanhamento definidos
[ ] Lições aprendidas documentadas
[ ] Referências e anexos incluídos
[ ] Conexões com outros documentos mapeadas
[ ] Evidências suficientes para conclusões
[ ] Análise de root cause realizada
[ ] Impacto de negócio avaliado
-->

<!-- SCANNER_INSTRUCTIONS
Este template de análise deve ser usado para:
- Análise de performance
- Investigação de bugs
- Retrospectivas de projetos
- Análise de métricas
- Investigações de segurança
- Análise de incidentes

Campos obrigatórios para o scanner:
- doc_type: "analysis"
- title: Título da análise
- context_level: c1_root | c2_module | c3_component
- context_type: infra | shared | core | api | data | ui
- module: Nome do módulo
- connections: Mapeamento de relacionamentos
- created_date: Data de criação
- last_updated: Data de atualização

Validações automáticas:
- Verificar se todos os metadados obrigatórios estão preenchidos
- Validar formato das datas
- Verificar se as conexões apontam para documentos existentes
- Validar consistência do contexto
- Verificar se o template está sendo usado corretamente
- Validar se há dados e evidências
- Verificar se há descobertas e ações
- Validar se há metodologia definida
-->

<!-- CONTEXT_CONNECTIONS
Este documento se conecta com:
- Documentos de decisão (decision) via "impacts"
- Documentos de arquitetura (architecture) via "references"
- Documentos de processo (process) via "relates_to"
- Outros documentos de análise (analysis) via "relates_to"

Padrões de conexão:
- [[nome-do-documento]] para referências diretas
- {{nome-do-componente}} para componentes analisados
- @contexto para referências de contexto
- #metric-name para métricas específicas
- /path/to/data para datasets
-->
