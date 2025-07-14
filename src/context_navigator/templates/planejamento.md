---
# =============================================================================
# METADADOS OBRIGATÓRIOS (IMUTÁVEIS)
# =============================================================================

# Tipo do documento (OBRIGATÓRIO)
doc_type: "planning"

# Título do documento (OBRIGATÓRIO)
title: "[PREENCHER] Título do Planejamento"

# Contexto hierárquico (OBRIGATÓRIO)
context_level: "c1_root" # c1_root | c2_module | c3_component

# Contexto especializado (OBRIGATÓRIO)
context_type: "core" # infra | shared | core | api | data | ui

# Módulo específico (OBRIGATÓRIO)
module: "[PREENCHER] Nome do Módulo"

# Conexões com outros documentos (OBRIGATÓRIO)
connections:
  references: ["analise.md", "arquitetura.md"] # Referenciam análises e especificações
  impacts: ["decisao.md", "processo.md"] # Planejamento impacta decisões e processos
  depends_on: [] # Dependências
  blocks: [] # Documentos bloqueados
  relates_to: ["referencia.md"] # Relaciona com documentação de referência

# Datas (OBRIGATÓRIAS)
created_date: "2024-01-15"
last_updated: "2024-01-15"

# =============================================================================
# METADADOS OPCIONAIS (EXTENSÍVEIS)
# =============================================================================

# Prioridade do planejamento
priority: "high" # critical | high | medium | low

# Status atual
status: "active" # draft | review | active | completed | archived

# Responsável pelo planejamento
owner: "[PREENCHER] Nome do Responsável"

# Tags para categorização
tags: ["planning", "roadmap", "sprint"]

# Complexidade do planejamento
complexity: "medium" # low | medium | high | critical

# Agenda de manutenção
maintenance_schedule: "monthly" # never | monthly | quarterly | yearly

# Tipo de planejamento
planning_type: "roadmap" # roadmap | sprint | release | milestone | project

# Horizonte temporal
time_horizon: "quarterly" # daily | weekly | monthly | quarterly | yearly | multi-year

# Metodologia de planejamento
methodology: "agile" # waterfall | agile | lean | kanban | scrum | custom

# Nível de detalhamento
detail_level: "high" # low | medium | high | granular

# Frequência de revisão
review_frequency: "weekly" # daily | weekly | bi-weekly | monthly | quarterly

# Equipe responsável
responsible_team: "development" # development | product | design | ops | management

# Orçamento total
total_budget: "50000" # Valor em USD

# Recursos humanos
human_resources: 5 # Número de pessoas

# Data de início
start_date: "2024-02-01"

# Data de fim
end_date: "2024-05-01"

# Marco principal
main_milestone: "MVP Release"

# Critérios de sucesso
success_criteria:
  ["feature_complete", "performance_targets", "user_satisfaction"]

# Riscos principais
main_risks: ["resource_availability", "technical_complexity", "market_changes"]

# Dependências críticas
critical_dependencies:
  ["api_integration", "third_party_service", "infrastructure"]

# Stakeholders chave
key_stakeholders: ["product-owner", "tech-lead", "users"]

# Métricas de acompanhamento
tracking_metrics: ["velocity", "burn_rate", "quality_score"]

# Flexibilidade do cronograma
schedule_flexibility: "medium" # low | medium | high

# Tolerância a riscos
risk_tolerance: "medium" # low | medium | high
---

<!-- CONTEXT_META
template_version: "1.0.0"
template_type: "planning"
generated_by: "context-navigator"
validation_status: "pending"
last_validated: "2024-01-15"
compliance_check: "passed"
metadata_completeness: "100%"
connection_accuracy: "pending"
context_consistency: "verified"
planning_category: "roadmap"
execution_phase: "planning"
-->

# 📅 [TÍTULO DO PLANEJAMENTO]

> **Template:** Planejamento | **Contexto:** [CONTEXTO] | **Módulo:** [MÓDULO]  
> **Criado:** [DATA] | **Atualizado:** [DATA] | **Status:** [STATUS]

## 📋 Metadados do Planejamento

**Tipo:** [ROADMAP/SPRINT/RELEASE/MILESTONE/PROJETO]  
**Horizonte:** [DIÁRIO/SEMANAL/MENSAL/TRIMESTRAL/ANUAL/MULTI-ANUAL]  
**Metodologia:** [WATERFALL/AGILE/LEAN/KANBAN/SCRUM/CUSTOM]  
**Orçamento:** [VALOR TOTAL]  
**Equipe:** [NÚMERO DE PESSOAS]  
**Período:** [DATA INÍCIO - DATA FIM]

## 🎯 Objetivos e Visão

### **Visão Geral**

[Descreva a visão geral do que será planejado]

### **Objetivos Principais**

1. [Objetivo específico 1]
2. [Objetivo específico 2]
3. [Objetivo específico 3]

### **Objetivos SMART**

| Objetivo     | Específico | Mensurável | Atingível | Relevante       | Temporal |
| ------------ | ---------- | ---------- | --------- | --------------- | -------- |
| [Objetivo 1] | [Sim/Não]  | [Métrica]  | [Sim/Não] | [Justificativa] | [Prazo]  |
| [Objetivo 2] | [Sim/Não]  | [Métrica]  | [Sim/Não] | [Justificativa] | [Prazo]  |
| [Objetivo 3] | [Sim/Não]  | [Métrica]  | [Sim/Não] | [Justificativa] | [Prazo]  |

### **Resultados Esperados**

- [Resultado esperado 1]
- [Resultado esperado 2]
- [Resultado esperado 3]

### **Definição de Sucesso**

- [Critério de sucesso 1]
- [Critério de sucesso 2]
- [Critério de sucesso 3]

### **Benefícios Esperados**

- **Para o Usuário:** [Benefício para o usuário]
- **Para o Negócio:** [Benefício para o negócio]
- **Para a Equipe:** [Benefício para a equipe]

## 📋 Escopo e Entregas

### **Escopo Incluído**

- [Item de escopo 1]
- [Item de escopo 2]
- [Item de escopo 3]

### **Escopo Excluído**

- [Item excluído 1]
- [Item excluído 2]
- [Item excluído 3]

### **Entregas Principais**

| Entrega     | Descrição   | Responsável | Prazo  | Status   |
| ----------- | ----------- | ----------- | ------ | -------- |
| [Entrega 1] | [Descrição] | [Nome]      | [Data] | [Status] |
| [Entrega 2] | [Descrição] | [Nome]      | [Data] | [Status] |
| [Entrega 3] | [Descrição] | [Nome]      | [Data] | [Status] |

### **Critérios de Aceitação**

- [Critério 1]
- [Critério 2]
- [Critério 3]

### **Definição de Pronto**

- [ ] [Critério técnico 1]
- [ ] [Critério técnico 2]
- [ ] [Critério de qualidade 1]
- [ ] [Critério de qualidade 2]
- [ ] [Critério de documentação]

## 📅 Cronograma e Marcos

### **Cronograma de Alto Nível**

```
Janeiro 2024        Fevereiro 2024        Março 2024
    |                     |                     |
    ▼                     ▼                     ▼
Planejamento          Desenvolvimento        Validação
    |                     |                     |
    ├─ Análise            ├─ Sprint 1          ├─ Testes
    ├─ Design             ├─ Sprint 2          ├─ Review
    └─ Aprovação          └─ Sprint 3          └─ Deploy
```

### **Marcos Principais**

| Marco | Descrição | Data Alvo | Critérios   | Responsável |
| ----- | --------- | --------- | ----------- | ----------- |
| M1    | [Marco 1] | [Data]    | [Critérios] | [Nome]      |
| M2    | [Marco 2] | [Data]    | [Critérios] | [Nome]      |
| M3    | [Marco 3] | [Data]    | [Critérios] | [Nome]      |

### **Fases do Projeto**

#### **Fase 1: [NOME DA FASE]**

**Duração:** [Duração estimada]  
**Objetivo:** [Objetivo específico da fase]

**Atividades:**

- [Atividade 1]
- [Atividade 2]
- [Atividade 3]

**Entregas:**

- [Entrega 1]
- [Entrega 2]

**Critérios de Conclusão:**

- [Critério 1]
- [Critério 2]

---

#### **Fase 2: [NOME DA FASE]**

**Duração:** [Duração estimada]  
**Objetivo:** [Objetivo específico da fase]

**Atividades:**

- [Atividade 1]
- [Atividade 2]
- [Atividade 3]

**Entregas:**

- [Entrega 1]
- [Entrega 2]

**Critérios de Conclusão:**

- [Critério 1]
- [Critério 2]

---

#### **Fase 3: [NOME DA FASE]**

**Duração:** [Duração estimada]  
**Objetivo:** [Objetivo específico da fase]

**Atividades:**

- [Atividade 1]
- [Atividade 2]
- [Atividade 3]

**Entregas:**

- [Entrega 1]
- [Entrega 2]

**Critérios de Conclusão:**

- [Critério 1]
- [Critério 2]

### **Cronograma Detalhado**

| Semana | Atividade     | Responsável | Esforço (horas) | Dependências   |
| ------ | ------------- | ----------- | --------------- | -------------- |
| W1     | [Atividade 1] | [Nome]      | [Horas]         | [Dependências] |
| W2     | [Atividade 2] | [Nome]      | [Horas]         | [Dependências] |
| W3     | [Atividade 3] | [Nome]      | [Horas]         | [Dependências] |

## 👥 Recursos e Equipe

### **Estrutura da Equipe**

| Papel     | Nome   | Responsabilidades   | Disponibilidade |
| --------- | ------ | ------------------- | --------------- |
| [Papel 1] | [Nome] | [Responsabilidades] | [%]             |
| [Papel 2] | [Nome] | [Responsabilidades] | [%]             |
| [Papel 3] | [Nome] | [Responsabilidades] | [%]             |

### **Matriz RACI**

| Atividade     | Responsável | Aprovador | Consultado | Informado |
| ------------- | ----------- | --------- | ---------- | --------- |
| [Atividade 1] | [Nome]      | [Nome]    | [Nome]     | [Nome]    |
| [Atividade 2] | [Nome]      | [Nome]    | [Nome]     | [Nome]    |
| [Atividade 3] | [Nome]      | [Nome]    | [Nome]     | [Nome]    |

### **Recursos Técnicos**

- **Infraestrutura:** [Recursos de infraestrutura]
- **Ferramentas:** [Ferramentas necessárias]
- **Licenças:** [Licenças necessárias]
- **Hardware:** [Hardware necessário]

### **Orçamento Detalhado**

| Categoria          | Item             | Custo   | Justificativa   |
| ------------------ | ---------------- | ------- | --------------- |
| **Pessoal**        | [Recurso humano] | [Custo] | [Justificativa] |
| **Ferramentas**    | [Ferramenta]     | [Custo] | [Justificativa] |
| **Infraestrutura** | [Recurso]        | [Custo] | [Justificativa] |
| **Terceiros**      | [Serviço]        | [Custo] | [Justificativa] |

**Total Estimado:** [Valor total]

## ⚠️ Riscos e Dependências

### **Análise de Riscos**

| Risco     | Probabilidade      | Impacto            | Exposição          | Mitigação    |
| --------- | ------------------ | ------------------ | ------------------ | ------------ |
| [Risco 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Alta/Média/Baixa] | [Estratégia] |
| [Risco 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Alta/Média/Baixa] | [Estratégia] |
| [Risco 3] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Alta/Média/Baixa] | [Estratégia] |

### **Dependências Críticas**

| Dependência     | Tipo              | Status   | Impacto se Atrasada | Ação   |
| --------------- | ----------------- | -------- | ------------------- | ------ |
| [Dependência 1] | [Interna/Externa] | [Status] | [Impacto]           | [Ação] |
| [Dependência 2] | [Interna/Externa] | [Status] | [Impacto]           | [Ação] |
| [Dependência 3] | [Interna/Externa] | [Status] | [Impacto]           | [Ação] |

### **Premissas**

- [Premissa 1]
- [Premissa 2]
- [Premissa 3]

### **Restrições**

- [Restrição 1]
- [Restrição 2]
- [Restrição 3]

### **Planos de Contingência**

- **Cenário 1:** [Situação] → [Ação]
- **Cenário 2:** [Situação] → [Ação]
- **Cenário 3:** [Situação] → [Ação]

## 📊 Métricas e Monitoramento

### **KPIs Principais**

| KPI     | Valor Atual | Meta   | Prazo   | Responsável |
| ------- | ----------- | ------ | ------- | ----------- |
| [KPI 1] | [Valor]     | [Meta] | [Prazo] | [Nome]      |
| [KPI 2] | [Valor]     | [Meta] | [Prazo] | [Nome]      |
| [KPI 3] | [Valor]     | [Meta] | [Prazo] | [Nome]      |

### **Métricas de Processo**

- **Velocity:** [Pontos por sprint]
- **Burn Rate:** [Taxa de queima do orçamento]
- **Quality Score:** [Pontuação de qualidade]
- **Team Satisfaction:** [Satisfação da equipe]

### **Dashboards de Acompanhamento**

- **Dashboard de Progresso:** [Link/Descrição]
- **Dashboard de Qualidade:** [Link/Descrição]
- **Dashboard de Recursos:** [Link/Descrição]

### **Relatórios Regulares**

- **Diário:** [Standup report]
- **Semanal:** [Status report]
- **Mensal:** [Executive summary]

### **Critérios de Alerta**

- **Verde:** [Critérios para status verde]
- **Amarelo:** [Critérios para status amarelo]
- **Vermelho:** [Critérios para status vermelho]

## 🔄 Governança e Comunicação

### **Estrutura de Governança**

- **Sponsor:** [Nome e papel]
- **Steering Committee:** [Membros]
- **Project Manager:** [Nome]
- **Tech Lead:** [Nome]

### **Cadência de Reuniões**

| Reunião     | Frequência   | Participantes   | Objetivo   |
| ----------- | ------------ | --------------- | ---------- |
| [Reunião 1] | [Frequência] | [Participantes] | [Objetivo] |
| [Reunião 2] | [Frequência] | [Participantes] | [Objetivo] |
| [Reunião 3] | [Frequência] | [Participantes] | [Objetivo] |

### **Canais de Comunicação**

- **Slack:** [Canal específico]
- **Email:** [Lista de distribuição]
- **Confluência:** [Espaço do projeto]
- **Jira:** [Board do projeto]

### **Processo de Mudanças**

1. [Passo 1 do processo]
2. [Passo 2 do processo]
3. [Passo 3 do processo]

### **Aprovações Necessárias**

- [Aprovação 1]: [Responsável]
- [Aprovação 2]: [Responsável]
- [Aprovação 3]: [Responsável]

## 🎯 Plano de Execução

### **Estratégia de Execução**

[Descreva a estratégia geral de execução]

### **Metodologia de Desenvolvimento**

- **Framework:** [Scrum/Kanban/Waterfall]
- **Sprint Duration:** [Duração]
- **Team Size:** [Tamanho da equipe]
- **Definition of Done:** [Critérios]

### **Plano de Testes**

- **Teste Unitário:** [Cobertura alvo]
- **Teste de Integração:** [Estratégia]
- **Teste de Aceitação:** [Critérios]
- **Teste de Performance:** [Metas]

### **Plano de Deploy**

- **Ambientes:** [Desenvolvimento → Staging → Produção]
- **Estratégia:** [Blue-green/Rolling/Canary]
- **Rollback:** [Procedimento]
- **Monitoramento:** [Métricas pós-deploy]

### **Plano de Treinamento**

- **Equipe de Desenvolvimento:** [Treinamentos necessários]
- **Usuários Finais:** [Treinamento de uso]
- **Suporte:** [Treinamento de suporte]

## 📈 Revisão e Melhoria Contínua

### **Pontos de Revisão**

- **Revisão Semanal:** [Objetivo e participantes]
- **Revisão de Sprint:** [Objetivo e participantes]
- **Revisão de Marco:** [Objetivo e participantes]

### **Critérios de Go/No-Go**

- [Critério 1]
- [Critério 2]
- [Critério 3]

### **Lições Aprendidas**

- [Lição 1]
- [Lição 2]
- [Lição 3]

### **Melhorias Identificadas**

- [Melhoria 1]
- [Melhoria 2]
- [Melhoria 3]

### **Retrospectivas**

- **Frequência:** [Frequência das retrospectivas]
- **Formato:** [Formato usado]
- **Ações:** [Como ações são priorizadas]

## 📚 Referências e Recursos

### **Documentação Relacionada**

- [Documento 1] - [Descrição]
- [Documento 2] - [Descrição]
- [Documento 3] - [Descrição]

### **Ferramentas de Planejamento**

- **Cronograma:** [Ferramenta usada]
- **Tracking:** [Ferramenta de acompanhamento]
- **Comunicação:** [Ferramentas de comunicação]

### **Templates e Padrões**

- [Template 1] - [Uso]
- [Template 2] - [Uso]
- [Template 3] - [Uso]

### **Histórico de Versões**

| Versão | Data       | Autor  | Mudanças       |
| ------ | ---------- | ------ | -------------- |
| 1.0    | 2024-01-15 | [Nome] | Versão inicial |

---

<!-- VALIDATION_CHECKLIST
[ ] Todos os metadados obrigatórios preenchidos
[ ] Objetivos SMART definidos
[ ] Escopo claramente delimitado
[ ] Cronograma e marcos estabelecidos
[ ] Recursos e equipe definidos
[ ] Riscos identificados e mitigados
[ ] Métricas e KPIs estabelecidos
[ ] Governança e comunicação definidas
[ ] Plano de execução detalhado
[ ] Pontos de revisão estabelecidos
[ ] Referências e recursos incluídos
[ ] Conexões com outros documentos mapeadas
[ ] Orçamento detalhado e aprovado
-->

<!-- SCANNER_INSTRUCTIONS
Este template de planejamento deve ser usado para:
- Roadmaps de produto
- Planejamento de sprints
- Planejamento de releases
- Marcos de projeto
- Cronogramas de desenvolvimento
- Planejamento estratégico

Campos obrigatórios para o scanner:
- doc_type: "planning"
- title: Título do planejamento
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
- Validar se há objetivos SMART definidos
- Verificar se há cronograma e marcos
- Validar se há recursos e orçamento
-->

<!-- CONTEXT_CONNECTIONS
Este documento se conecta com:
- Documentos de decisão (decision) via "depends_on"
- Documentos de arquitetura (architecture) via "references"
- Documentos de processo (process) via "relates_to"
- Documentos de análise (analysis) via "relates_to"
- Outros documentos de planejamento (planning) via "relates_to"

Padrões de conexão:
- [[nome-do-documento]] para referências diretas
- {{nome-do-componente}} para componentes planejados
- @contexto para referências de contexto
- #milestone-name para marcos específicos
- $budget-item para itens de orçamento
-->
