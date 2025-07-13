---
# =============================================================================
# METADADOS OBRIGATÓRIOS (IMUTÁVEIS)
# =============================================================================

# Tipo do documento (OBRIGATÓRIO)
doc_type: "process"

# Título do documento (OBRIGATÓRIO)
title: "[PREENCHER] Título do Processo"

# Contexto hierárquico (OBRIGATÓRIO)
context_level: "c2_module" # c1_root | c2_module | c3_component

# Contexto especializado (OBRIGATÓRIO)
context_type: "infra" # infra | shared | core | api | data | ui

# Módulo específico (OBRIGATÓRIO)
module: "[PREENCHER] Nome do Módulo"

# Conexões com outros documentos (OBRIGATÓRIO)
connections:
  references: ["referencia.md", "arquitetura.md"] # Referenciam documentação e arquitetura
  impacts: ["analise.md"] # Processos geram análises de resultados
  depends_on: ["decisao.md"] # Processos dependem de decisões
  blocks: [] # Documentos bloqueados
  relates_to: ["planejamento.md"] # Processos se relacionam com planejamento

# Datas (OBRIGATÓRIAS)
created_date: "2024-01-15"
last_updated: "2024-01-15"

# =============================================================================
# METADADOS OPCIONAIS (EXTENSÍVEIS)
# =============================================================================

# Prioridade do processo
priority: "high" # critical | high | medium | low

# Status atual
status: "active" # draft | review | active | deprecated | archived

# Responsável pelo processo
owner: "[PREENCHER] Nome do Responsável"

# Tags para categorização
tags: ["process", "operational", "infrastructure"]

# Complexidade do processo
complexity: "medium" # low | medium | high | critical

# Agenda de manutenção
maintenance_schedule: "monthly" # never | monthly | quarterly | yearly

# Tipo de processo
process_type: "operational" # operational | deployment | maintenance | troubleshooting | setup

# Automação disponível
automation_level: "partial" # none | partial | full

# Frequência de execução
execution_frequency: "on-demand" # daily | weekly | monthly | quarterly | on-demand | emergency

# Tempo estimado de execução
estimated_duration: "30 minutes"

# Nível de experiência necessário
skill_level: "intermediate" # beginner | intermediate | advanced | expert

# Ambiente de execução
target_environment: "production" # development | staging | production | all

# Ferramentas necessárias
required_tools: ["docker", "kubectl", "aws-cli"]

# Permissões necessárias
required_permissions: ["admin", "deploy"]

# Criticidade do processo
criticality: "high" # low | medium | high | critical

# Impacto em caso de falha
failure_impact: "medium" # low | medium | high | critical
---

<!-- CONTEXT_META
template_version: "1.0.0"
template_type: "process"
generated_by: "context-navigator"
validation_status: "pending"
last_validated: "2024-01-15"
compliance_check: "passed"
metadata_completeness: "100%"
connection_accuracy: "pending"
context_consistency: "verified"
process_category: "operational"
automation_ready: "partial"
-->

# 🔄 [TÍTULO DO PROCESSO]

> **Template:** Processo | **Contexto:** [CONTEXTO] | **Módulo:** [MÓDULO]  
> **Criado:** [DATA] | **Atualizado:** [DATA] | **Status:** [STATUS]

## 📋 Metadados do Processo

**Tipo:** [OPERACIONAL/DEPLOYMENT/MANUTENÇÃO/TROUBLESHOOTING/SETUP]  
**Criticidade:** [BAIXA/MÉDIA/ALTA/CRÍTICA]  
**Automação:** [NENHUMA/PARCIAL/COMPLETA]  
**Frequência:** [DIÁRIA/SEMANAL/MENSAL/ON-DEMAND/EMERGÊNCIA]  
**Duração:** [TEMPO ESTIMADO]  
**Skill Level:** [INICIANTE/INTERMEDIÁRIO/AVANÇADO/EXPERT]

## 🎯 Objetivo

### **Propósito Principal**

[Descreva claramente o que este processo visa alcançar]

### **Resultados Esperados**

- [Resultado 1]
- [Resultado 2]
- [Resultado 3]

### **Benefícios**

- [Benefício 1]
- [Benefício 2]
- [Benefício 3]

### **Quando Usar Este Processo**

- [Situação 1]
- [Situação 2]
- [Situação 3]

## 📚 Pré-requisitos

### **Conhecimentos Necessários**

- [Conhecimento 1]
- [Conhecimento 2]
- [Conhecimento 3]

### **Ferramentas Obrigatórias**

| Ferramenta     | Versão   | Instalação     | Configuração              |
| -------------- | -------- | -------------- | ------------------------- |
| [Ferramenta 1] | [Versão] | [Link/Comando] | [Configuração necessária] |
| [Ferramenta 2] | [Versão] | [Link/Comando] | [Configuração necessária] |

### **Permissões Necessárias**

- [Permissão 1]: [Descrição]
- [Permissão 2]: [Descrição]
- [Permissão 3]: [Descrição]

### **Acesso a Recursos**

- [Recurso 1]: [Como acessar]
- [Recurso 2]: [Como acessar]
- [Recurso 3]: [Como acessar]

### **Dependências**

- [Dependência 1]: [Status/Verificação]
- [Dependência 2]: [Status/Verificação]
- [Dependência 3]: [Status/Verificação]

## 🔍 Verificação de Pré-requisitos

### **Checklist de Preparação**

- [ ] Ferramentas instaladas e configuradas
- [ ] Permissões verificadas
- [ ] Acesso aos recursos confirmado
- [ ] Dependências satisfeitas
- [ ] Backup realizado (se aplicável)
- [ ] Ambiente de teste validado

### **Comandos de Verificação**

```bash
# Verificar ferramenta 1
[comando de verificação 1]

# Verificar ferramenta 2
[comando de verificação 2]

# Verificar conectividade
[comando de verificação 3]
```

## 🚀 Procedimento Principal

### **Passo 1: [NOME DO PASSO]**

**Objetivo:** [Objetivo específico deste passo]

**Tempo estimado:** [X minutos]

**Ações:**

1. [Ação detalhada 1]
2. [Ação detalhada 2]
3. [Ação detalhada 3]

**Comandos:**

```bash
# Descrição do comando
[comando específico]

# Exemplo de uso
[exemplo prático]
```

### **Validação**

- [ ] [Critério de validação 1]
- [ ] [Critério de validação 2]
- [ ] [Critério de validação 3]

### **Resultado Esperado**

[Descreva o resultado esperado após este passo]

---

### **Passo 2: [NOME DO PASSO]**

**Objetivo:** [Objetivo específico deste passo]

**Tempo estimado:** [X minutos]

**Ações:**

1. [Ação detalhada 1]
2. [Ação detalhada 2]
3. [Ação detalhada 3]

**Comandos:**

```bash
# Descrição do comando
[comando específico]

# Exemplo de uso
[exemplo prático]
```

### **Validação**

- [ ] [Critério de validação 1]
- [ ] [Critério de validação 2]
- [ ] [Critério de validação 3]

### **Resultado Esperado**

[Descreva o resultado esperado após este passo]

---

### **Passo 3: [NOME DO PASSO]**

**Objetivo:** [Objetivo específico deste passo]

**Tempo estimado:** [X minutos]

**Ações:**

1. [Ação detalhada 1]
2. [Ação detalhada 2]
3. [Ação detalhada 3]

**Comandos:**

```bash
# Descrição do comando
[comando específico]

# Exemplo de uso
[exemplo prático]
```

### **Validação**

- [ ] [Critério de validação 1]
- [ ] [Critério de validação 2]
- [ ] [Critério de validação 3]

### **Resultado Esperado**

[Descreva o resultado esperado após este passo]

## ✅ Validação e Testes

### **Testes de Funcionalidade**

1. **Teste 1:** [Descrição do teste]

   - **Comando:** `[comando de teste]`
   - **Resultado esperado:** [resultado]
   - **Critério de sucesso:** [critério]

2. **Teste 2:** [Descrição do teste]
   - **Comando:** `[comando de teste]`
   - **Resultado esperado:** [resultado]
   - **Critério de sucesso:** [critério]

### **Testes de Integração**

1. **Integração 1:** [Descrição]

   - **Verificação:** [como verificar]
   - **Resultado:** [resultado esperado]

2. **Integração 2:** [Descrição]
   - **Verificação:** [como verificar]
   - **Resultado:** [resultado esperado]

### **Testes de Performance**

1. **Performance 1:** [Métrica]
   - **Comando:** `[comando de medição]`
   - **Valor esperado:** [valor]
   - **Limite aceitável:** [limite]

### **Checklist de Validação Final**

- [ ] Todas as funcionalidades testadas
- [ ] Integrações validadas
- [ ] Performance dentro dos limites
- [ ] Logs verificados
- [ ] Monitoramento ativo
- [ ] Documentação atualizada

## 🔧 Troubleshooting

### **Problemas Comuns**

#### **Problema 1: [DESCRIÇÃO DO PROBLEMA]**

### **Sintomas**

- [Sintoma 1]
- [Sintoma 2]
- [Sintoma 3]

**Causa Provável:**
[Descrição da causa mais provável]

### **Solução**

1. [Passo da solução 1]
2. [Passo da solução 2]
3. [Passo da solução 3]

**Comando de diagnóstico:**

```bash
[comando para diagnosticar]
```

**Comando de correção:**

```bash
[comando para corrigir]
```

---

#### **Problema 2: [DESCRIÇÃO DO PROBLEMA]**

### **Sintomas**

- [Sintoma 1]
- [Sintoma 2]
- [Sintoma 3]

**Causa Provável:**
[Descrição da causa mais provável]

### **Solução**

1. [Passo da solução 1]
2. [Passo da solução 2]
3. [Passo da solução 3]

**Comando de diagnóstico:**

```bash
[comando para diagnosticar]
```

**Comando de correção:**

```bash
[comando para corrigir]
```

### **Logs e Monitoramento**

- **Logs principais:** [Localização dos logs]
- **Comandos úteis:**

  ```bash
  # Ver logs em tempo real
  [comando de logs]

  # Verificar status
  [comando de status]
  ```

### **Escalação**

- **Nível 1:** [Equipe/Pessoa responsável]
- **Nível 2:** [Equipe/Pessoa responsável]
- **Nível 3:** [Equipe/Pessoa responsável]

## 📊 Monitoramento e Métricas

### **Métricas de Sucesso**

- [Métrica 1]: [Valor alvo]
- [Métrica 2]: [Valor alvo]
- [Métrica 3]: [Valor alvo]

### **Comandos de Monitoramento**

```bash
# Verificar métrica 1
[comando de verificação]

# Verificar métrica 2
[comando de verificação]

# Dashboard de monitoramento
[link ou comando]
```

### **Alertas**

- **Alerta 1:** [Condição] → [Ação]
- **Alerta 2:** [Condição] → [Ação]
- **Alerta 3:** [Condição] → [Ação]

## 🔄 Rollback e Recuperação

### **Procedimento de Rollback**

1. [Passo de rollback 1]
2. [Passo de rollback 2]
3. [Passo de rollback 3]

### **Comandos de Rollback**

```bash
# Rollback principal
[comando de rollback]

# Verificar rollback
[comando de verificação]
```

### **Recuperação de Dados**

- **Backup:** [Localização do backup]
- **Restore:** [Procedimento de restore]
- **Validação:** [Como validar o restore]

## 🔧 Automação

### **Scripts Disponíveis**

- **Script 1:** [Nome] - [Descrição]
  - **Localização:** [Path]
  - **Uso:** `[comando]`
- **Script 2:** [Nome] - [Descrição]
  - **Localização:** [Path]
  - **Uso:** `[comando]`

### **Oportunidades de Automação**

1. [Oportunidade 1]: [Descrição]
2. [Oportunidade 2]: [Descrição]
3. [Oportunidade 3]: [Descrição]

### **Roadmap de Automação**

- **Fase 1:** [Automação básica]
- **Fase 2:** [Automação intermediária]
- **Fase 3:** [Automação completa]

## 📚 Referências e Recursos

### **Documentação Relacionada**

- [Documento 1] - [Descrição]
- [Documento 2] - [Descrição]
- [Documento 3] - [Descrição]

### **Recursos Externos**

- [Recurso 1] - [Link/Descrição]
- [Recurso 2] - [Link/Descrição]
- [Recurso 3] - [Link/Descrição]

### **Contatos de Suporte**

- **Equipe Responsável:** [Nome/Contato]
- **Suporte Técnico:** [Nome/Contato]
- **Escalação:** [Nome/Contato]

### **Histórico de Versões**

| Versão | Data       | Autor  | Mudanças       |
| ------ | ---------- | ------ | -------------- |
| 1.0    | 2024-01-15 | [Nome] | Versão inicial |

## 🏷️ Anexos

### **Anexo A: Scripts**

[Inclua scripts importantes aqui]

### **Anexo B: Configurações**

[Inclua configurações relevantes]

### **Anexo C: Exemplos**

[Inclua exemplos práticos]

---

<!-- VALIDATION_CHECKLIST
[ ] Todos os metadados obrigatórios preenchidos
[ ] Objetivo claramente definido
[ ] Pré-requisitos listados e verificáveis
[ ] Procedimento dividido em passos claros
[ ] Validação definida para cada passo
[ ] Troubleshooting com problemas comuns
[ ] Comandos testados e funcionais
[ ] Monitoramento e métricas definidas
[ ] Procedimento de rollback documentado
[ ] Referências e recursos incluídos
[ ] Histórico de versões iniciado
[ ] Conexões com outros documentos mapeadas
[ ] Automação considerada e documentada
-->

<!-- SCANNER_INSTRUCTIONS
Este template de processo deve ser usado para:
- Procedimentos operacionais
- Runbooks de infraestrutura
- Playbooks de deployment
- Guias de troubleshooting
- Tutoriais passo-a-passo
- Procedimentos de manutenção

Campos obrigatórios para o scanner:
- doc_type: "process"
- title: Título do processo
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
- Validar se há pelo menos 3 passos no procedimento
- Verificar se há seção de troubleshooting
- Verificar se há validação para cada passo
-->

<!-- CONTEXT_CONNECTIONS
Este documento se conecta com:
- Documentos de decisão (decision) via "depends_on"
- Documentos de arquitetura (architecture) via "references"
- Documentos de referência (reference) via "references"
- Outros documentos de processo (process) via "relates_to"

Padrões de conexão:
- [[nome-do-documento]] para referências diretas
- {{nome-do-componente}} para componentes
- @contexto para referências de contexto
- [comando] para comandos executáveis
- /path/to/resource para recursos do sistema
-->
