---
doc_type: "reference"
context_level: "c1_root"
context_type: "core"
module: "context-navigator"
priority: "critical"
status: "active"
connections:
  references: ["MANUAL_IA.md", "CONVENTIONS.md"]
  impacts: ["context_scanner.py", "context_engine.py", "template_validator.py"]
  depends_on: [".contextrc", "context.rule"]
  relates_to: ["templates/", "examples/"]
created_date: "2024-01-15"
last_updated: "2025-07-12"
owner: "Context Navigator Team"
tags: ["manual", "documentation", "human-operator", "reference"]
complexity: "high"
maintenance_schedule: "quarterly"
stakeholders: ["developers", "documentation-team"]
architectural_impact: "high"
---

# 📖 Context Navigator - Manual do Operador Humano

## 🎯 Bem-vindo ao Context Navigator

O **Context Navigator** é uma metodologia de parceria humano-IA que revoluciona como você documenta e mantém contexto em projetos complexos. Este manual o guiará através de cada aspecto da metodologia.

---

## 📋 Índice

1. [**Fundamentos**](#fundamentos)
2. [**Instalação e Setup**](#instalação-e-setup)
3. [**Fluxo de Trabalho Diário**](#fluxo-de-trabalho-diário)
4. [**Templates Detalhados**](#templates-detalhados)
5. [**Scripts e Ferramentas**](#scripts-e-ferramentas)
6. [**Melhores Práticas**](#melhores-práticas)
7. [**Casos de Uso Práticos**](#casos-de-uso-práticos)
8. [**Troubleshooting**](#troubleshooting)
9. [**Manutenção e Evolução**](#manutenção-e-evolução)
10. [**Referência Rápida**](#referência-rápida)

---

## 🧠 Fundamentos

### **O que é Context Navigator?**

Context Navigator é uma **metodologia pessoal** que:

- Disciplina a IA através de regras cristalinas
- Padroniza interação humano-IA
- Permite automação completa de leitura documental
- Mantém contexto atualizado automaticamente

### **Princípios Fundamentais**

#### **1. Lei Sagrada para IA**

```
TODA interação com IA deve começar carregando:
1. context.rule (regras metodológicas)
2. .context-map/index.yml (contexto atual)
3. Validação de template apropriado
```

#### **2. Metadados Imutáveis**

```yaml
# Campos que NUNCA mudam
doc_type: "decision|process|reference|architecture|analysis|planning"
context_level: "c1_root|c2_module|c3_component"
context_type: "infra|shared|core|api|data|ui"
```

#### **3. Conexões Explícitas**

```yaml
connections:
  references: ["doc1.md", "doc2.md"]
  impacts: ["doc3.md"]
  depends_on: ["doc4.md"]
  blocks: ["doc5.md"]
  relates_to: ["doc6.md"]
```

#### **4. Pasta Metodológica Separada**

```
context-navigator/    # Metodologia (não projeto)
├── .contextrc       # Configuração
├── context.rule     # Lei sagrada
├── .context-map/    # Mapas automáticos
├── scripts/         # Ferramentas
├── templates/       # Templates
├── docs/            # Documentação
└── examples/        # Exemplos
```

---

## 🚀 Instalação e Setup

### **Passo 1: Criar Estrutura**

```bash
# Criar pasta da metodologia
mkdir context-navigator
cd context-navigator

# Criar subpastas
mkdir -p .context-map/contexts scripts templates docs examples
```

### **Passo 2: Configurar .contextrc**

Use o `.contextrc` fornecido ou customize:

```yaml
# Configuração básica
methodology:
  name: "Context Navigator"
  version: "1.0.0"

document_types:
  decision:
    usage_percentage: 40
    description: "Decisões técnicas e arquiteturais"
  process:
    usage_percentage: 20
    description: "Procedimentos e processos"
  # ... outros tipos
```

### **Passo 3: Instalar Dependências Python**

```bash
# Se usar scripts Python
pip install pyyaml pathlib datetime typing dataclasses
```

### **Passo 4: Configurar context.rule**

Copie o `context.rule` fornecido para seu projeto e ajuste se necessário.

### **Passo 5: Validar Setup**

```bash
# Testar scanner
python scripts/context_scanner.py --validate

# Testar engine
python scripts/context_engine.py --patterns

# Testar validator
python scripts/template_validator.py --templates
```

---

## 🔄 Fluxo de Trabalho Diário

### **Cenário 1: Criar Novo Documento**

#### **Passo 1: Escolher Template**

```bash
# Analisar conteúdo existente
python scripts/context_engine.py --analyze "rascunho.md"

# Ou usar tabela de decisão:
# - Tomando decisão? → DECISÃO
# - Documentando processo? → PROCESSO
# - Criando referência? → REFERÊNCIA
# - Definindo arquitetura? → ARQUITETURA
# - Fazendo análise? → ANÁLISE
# - Planejando? → PLANEJAMENTO
```

#### **Passo 2: Copiar Template**

```bash
# Copiar template apropriado
cp templates/decisao.md meu_documento.md

# Ou usar engine para sugerir
python scripts/context_engine.py --suggest-template "meu_conteudo.txt"
```

#### **Passo 3: Preencher Metadados**

```yaml
---
doc_type: "decision"
context_level: "c2_module"
context_type: "core"
module: "authentication"
priority: "high"
status: "draft"
connections:
  references: []
  impacts: []
  depends_on: []
  blocks: []
  relates_to: []
created_date: "2024-01-15"
last_updated: "2024-01-15"
owner: "seu_nome"
---
```

#### **Passo 4: Desenvolver Conteúdo**

- Siga a estrutura do template
- Preencha todas as seções obrigatórias
- Use checklists quando aplicável
- Adicione diagramas ASCII quando necessário

#### **Passo 5: Validar Documento**

```bash
# Validar estrutura
python scripts/template_validator.py --file meu_documento.md

# Executar scanner
python scripts/context_scanner.py --scan docs/

# Detectar conflitos
python scripts/conflict_detector.py --type all
```

#### **Passo 6: Integrar com IA**

```
1. Carregar context.rule
2. Ler .context-map/index.yml
3. Aplicar template apropriado
4. Pedir para IA revisar/expandir
5. Validar resultado
```

### **Cenário 2: Atualizar Documento Existente**

#### **Passo 1: Carregar Contexto**

```bash
# Ver contexto atual
python scripts/context_engine.py --analyze documento.md

# Ver conexões
grep -A 10 "connections:" documento.md
```

#### **Passo 2: Validar Antes da Mudança**

```bash
# Baseline atual
python scripts/template_validator.py --file documento.md > baseline.txt

# Detectar conflitos atuais
python scripts/conflict_detector.py --type all > conflitos_pre.txt
```

#### **Passo 3: Fazer Alterações**

- Atualizar `last_updated` nos metadados
- Manter estrutura do template
- Atualizar conexões se necessário

#### **Passo 4: Validar Após Mudança**

```bash
# Validar novamente
python scripts/template_validator.py --file documento.md

# Verificar novos conflitos
python scripts/conflict_detector.py --type all

# Executar scanner completo
python scripts/context_scanner.py --scan docs/
```

### **Cenário 3: Manutenção Periódica**

#### **Semanal:**

```bash
# Executar scanner completo
python scripts/context_scanner.py --scan docs/

# Detectar conflitos
python scripts/conflict_detector.py --type all

# Gerar relatório de qualidade
python scripts/template_validator.py --templates
```

#### **Mensal:**

```bash
# Analisar padrões
python scripts/context_engine.py --patterns

# Verificar documentos desatualizados
find docs/ -name "*.md" -mtime +30

# Revisar conexões quebradas
python scripts/conflict_detector.py --type dependency
```

---

## 📝 Templates Detalhados

### **Template DECISÃO (40% dos casos)**

#### **Quando Usar:**

- Definir arquitetura
- Escolher tecnologia
- Resolver trade-offs
- Criar ADRs/RFCs
- Tomar decisões técnicas

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

- **Prós:** [listar vantagens]
- **Contras:** [listar desvantagens]
- **Esforço:** [estimar complexidade]
- **Risco:** [avaliar riscos]

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

#### **Dicas de Qualidade:**

- Mínimo 2 opções consideradas
- Análise de trade-offs explícita
- Justificativa clara e objetiva
- Impactos bem documentados

### **Template PROCESSO (20% dos casos)**

#### **Quando Usar:**

- Documentar procedimentos
- Criar runbooks
- Fazer tutoriais
- Definir workflows
- Padronizar operações

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

- **Comando:** `código ou comando`
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

### Problema Comum 2

[mesma estrutura]
```

#### **Dicas de Qualidade:**

- Mínimo 3 passos detalhados
- Comandos verificáveis
- Validação para cada passo
- Troubleshooting abrangente

### **Template REFERÊNCIA (15% dos casos)**

#### **Quando Usar:**

- Documentar APIs
- Criar glossários
- Fazer especificações
- Referenciar bibliotecas
- Documentar interfaces

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

### Endpoint/Função 2

[mesma estrutura]

## Exemplos Práticos

### Exemplo 1: [Caso de Uso]

```javascript
// Código exemplo
const result = api.call(params);
```
````

### Exemplo 2: [Caso de Uso]

[mesma estrutura]

## Versionamento

### Versão Atual

### Histórico de Mudanças

### Compatibilidade

````

#### **Dicas de Qualidade:**
- Mínimo 2 exemplos práticos
- Códigos de resposta HTTP
- Parâmetros bem documentados
- Exemplos funcionais

### **Template ARQUITETURA (10% dos casos)**

#### **Quando Usar:**
- Definir componentes
- Desenhar fluxos
- Modelar sistemas
- Documentar padrões
- Criar visões arquiteturais

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
│ Frontend │───▶│ Backend │
│ (React) │ │ (Node) │
└─────────────┘ └─────────────┘

```

### Tecnologias Principais

## Componentes Arquiteturais
### Componente 1: [Nome]
- **Responsabilidade:** [função principal]
- **Interfaces:** [como se conecta]
- **Tecnologias:** [stack usado]

### Componente 2: [Nome]
[mesma estrutura]

## Fluxos Arquiteturais
### Fluxo 1: [Nome]
1. **Passo 1:** [ação]
2. **Passo 2:** [ação]
3. **Passo 3:** [ação]

## Decisões Arquiteturais
### ADR 1: [Título]
- **Contexto:** [situação]
- **Decisão:** [escolha]
- **Impacto:** [consequências]
```

#### **Dicas de Qualidade:**

- Mínimo 2 componentes principais
- Diagramas ASCII claros
- Fluxos bem documentados
- ADRs integradas

### **Template ANÁLISE (10% dos casos)**

#### **Quando Usar:**

- Investigar problemas
- Analisar performance
- Fazer retrospectivas
- Estudar dados
- Root cause analysis

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
| Memory  | 2GB   | 1 hora  |

### Dados Qualitativos

- Observação 1
- Observação 2

## Análise Detalhada

### Root Cause Analysis

### Correlações Encontradas

### Padrões Identificados

## Descobertas e Insights

### Descoberta 1: [Título]

- **Descrição:** [detalhe]
- **Impacto:** [consequência]
- **Evidência:** [prova]

### Descoberta 2: [Título]

[mesma estrutura]

## Ações Recomendadas

### Ações Imediatas

- [ ] Ação 1 (Prioridade: Alta)
- [ ] Ação 2 (Prioridade: Média)

### Ações de Longo Prazo

- [ ] Ação 3 (Prioridade: Baixa)
```

#### **Dicas de Qualidade:**

- Mínimo 2 descobertas fundamentadas
- Dados quantitativos quando possível
- Root cause bem documentado
- Ações priorizadas

### **Template PLANEJAMENTO (5% dos casos)**

#### **Quando Usar:**

- Planejar projetos
- Definir roadmaps
- Organizar sprints
- Estabelecer marcos
- Gerenciar recursos

#### **Estrutura Obrigatória:**

```markdown
## Objetivos e Visão

### Objetivos SMART

- **Específico:** [o que]
- **Mensurável:** [métrica]
- **Atingível:** [viabilidade]
- **Relevante:** [importância]
- **Temporal:** [prazo]

### Resultados Esperados

### Critérios de Sucesso

## Escopo e Entregas

### Escopo do Projeto

### Entregas Principais

- [ ] Entrega 1 (Semana 1)
- [ ] Entrega 2 (Semana 2)

### Fora do Escopo

## Cronograma e Marcos

### Marcos Principais

- **M1:** [descrição] (Data: 15/01)
- **M2:** [descrição] (Data: 30/01)

### Fases do Projeto

1. **Fase 1:** [nome] (Semanas 1-2)
2. **Fase 2:** [nome] (Semanas 3-4)

## Recursos e Equipe

### Estrutura da Equipe

- **Papel 1:** [pessoa] (Responsabilidade)
- **Papel 2:** [pessoa] (Responsabilidade)

### Orçamento Detalhado

| Item  | Custo | Período |
| ----- | ----- | ------- |
| Dev   | $5000 | 1 mês   |
| Infra | $1000 | 1 mês   |

## Riscos e Dependências

### Análise de Riscos

- **Risco 1:** [descrição] (Probabilidade: Alta, Impacto: Alto)
- **Risco 2:** [descrição] (Probabilidade: Baixa, Impacto: Médio)

### Dependências Críticas

- [ ] Dependência 1 (Responsável: X)
- [ ] Dependência 2 (Responsável: Y)

## Métricas e Monitoramento

### KPIs Principais

- Métrica 1: [definição]
- Métrica 2: [definição]

### Frequência de Revisão

- Daily: [o que revisar]
- Weekly: [o que revisar]
- Monthly: [o que revisar]
```

#### **Dicas de Qualidade:**

- Objetivos SMART bem definidos
- Mínimo 2 marcos principais
- Riscos identificados e mitigados
- Métricas mensuráveis

---

## 🛠️ Scripts e Ferramentas

### **context_scanner.py - Scanner Principal**

#### **Funcionalidades:**

- Escaneia pasta de documentos
- Extrai metadados automaticamente
- Detecta tipos de documento
- Mapeia conexões entre documentos
- Gera context maps automáticos
- Valida consistência estrutural

#### **Uso Básico:**

```bash
# Escanear pasta atual
python scripts/context_scanner.py

# Escanear pasta específica
python scripts/context_scanner.py --path docs/

# Modo verbose
python scripts/context_scanner.py --verbose

# Apenas validar
python scripts/context_scanner.py --validate
```

#### **Uso Avançado:**

```bash
# Escanear com filtros
python scripts/context_scanner.py --types decision,process

# Salvar em arquivo
python scripts/context_scanner.py --output scan_results.json

# Modo incremental
python scripts/context_scanner.py --incremental
```

### **context_engine.py - Engine Inteligente**

#### **Funcionalidades:**

- Análise de conteúdo semântica
- Recomendação de templates
- Sugestão de contextos
- Detecção de conexões
- Análise de padrões
- Score de qualidade

#### **Uso Básico:**

```bash
# Analisar documento
python scripts/context_engine.py --analyze documento.md

# Detectar padrões gerais
python scripts/context_engine.py --patterns

# Recomendar template
python scripts/context_engine.py --suggest-template conteudo.txt
```

#### **Uso Avançado:**

```bash
# Análise completa com JSON
python scripts/context_engine.py --analyze doc.md --json > analysis.json

# Sugerir conexões
python scripts/context_engine.py --suggest-connections doc.md

# Análise de qualidade
python scripts/context_engine.py --quality-score doc.md
```

### **template_validator.py - Validador Especializado**

#### **Funcionalidades:**

- Validação estrutural profunda
- Verificação de metadados
- Análise de completude
- Detecção de problemas
- Sugestões de melhoria
- Relatórios detalhados

#### **Uso Básico:**

```bash
# Validar documento
python scripts/template_validator.py --file documento.md

# Validar todos os templates
python scripts/template_validator.py --templates

# Saída JSON
python scripts/template_validator.py --file doc.md --json
```

#### **Uso Avançado:**

```bash
# Validação específica por tipo
python scripts/template_validator.py --templates --type decision

# Relatório de qualidade
python scripts/template_validator.py --quality-report

# Validação em lote
find docs/ -name "*.md" -exec python scripts/template_validator.py --file {} \;
```

### **conflict_detector.py - Detector de Conflitos**

#### **Funcionalidades:**

- 8 tipos de conflitos
- Detecção automática
- Análise de dependências
- Sugestões de resolução
- Relatórios estruturados
- Priorização inteligente

#### **Uso Básico:**

```bash
# Detectar todos os conflitos
python scripts/conflict_detector.py

# Detectar tipo específico
python scripts/conflict_detector.py --type dependency

# Filtrar por severidade
python scripts/conflict_detector.py --severity high
```

#### **Uso Avançado:**

```bash
# Saída JSON para processamento
python scripts/conflict_detector.py --json > conflicts.json

# Apenas conflitos críticos
python scripts/conflict_detector.py --severity critical --json

# Resolver conflito específico
python scripts/conflict_detector.py --resolve abc123ef
```

---

## 🏆 Melhores Práticas

### **1. Disciplina de Metadados**

#### **✅ Faça:**

- Preencha TODOS os campos obrigatórios
- Use valores consistentes
- Mantenha datas atualizadas
- Documente conexões explicitamente

#### **❌ Não Faça:**

- Deixar campos vazios
- Usar valores inconsistentes
- Esquecer de atualizar last_updated
- Criar conexões implícitas

### **2. Estrutura de Conteúdo**

#### **✅ Faça:**

- Siga rigorosamente o template
- Use headers consistentes
- Mantenha seções bem definidas
- Adicione checklists quando apropriado

#### **❌ Não Faça:**

- Alterar estrutura do template
- Misturar tipos de conteúdo
- Pular seções obrigatórias
- Criar headers personalizados

### **3. Conexões e Relacionamentos**

#### **✅ Faça:**

- Mapeie conexões explicitamente
- Use tipos de conexão corretos
- Valide referências regularmente
- Mantenha relacionamentos atualizados

#### **❌ Não Faça:**

- Assumir conexões implícitas
- Usar tipos errados
- Ignorar referências quebradas
- Criar dependências circulares

### **4. Qualidade de Conteúdo**

#### **✅ Faça:**

- Escreva conteúdo claro e objetivo
- Use exemplos práticos
- Adicione diagramas quando necessário
- Mantenha informações atualizadas

#### **❌ Não Faça:**

- Usar linguagem ambígua
- Omitir exemplos importantes
- Ignorar aspectos visuais
- Deixar informações obsoletas

### **5. Manutenção Regular**

#### **✅ Faça:**

- Execute scanner semanalmente
- Resolva conflitos imediatamente
- Atualize documentos regularmente
- Monitore qualidade continuamente

#### **❌ Não Faça:**

- Acumular validações
- Ignorar conflitos menores
- Deixar documentos obsoletos
- Negligenciar manutenção

---

## 💡 Casos de Uso Práticos

### **Caso 1: Desenvolvendo Nova Feature**

#### **Cenário:**

Você precisa desenvolver autenticação OAuth2 para sua aplicação.

#### **Abordagem Context Navigator:**

**Passo 1: Decisão Arquitetural**

```bash
# Criar documento de decisão
cp templates/decisao.md docs/oauth2-architecture-decision.md

# Preencher metadados
doc_type: "decision"
context_level: "c2_module"
context_type: "core"
module: "authentication"
```

**Passo 2: Análise de Opções**

```markdown
## Opções Consideradas

### Opção 1: JWT com sessões

- **Prós:** Stateless, escalável
- **Contras:** Revogação complexa
- **Esforço:** Médio
- **Risco:** Baixo

### Opção 2: OAuth2 com refresh tokens

- **Prós:** Padrão da indústria
- **Contras:** Mais complexo
- **Esforço:** Alto
- **Risco:** Médio
```

**Passo 3: Documentar Processo**

```bash
# Após decisão, documentar implementação
cp templates/processo.md docs/oauth2-implementation-process.md

# Conexões
connections:
  depends_on: ["oauth2-architecture-decision.md"]
  references: ["oauth2-api-reference.md"]
```

**Passo 4: Referência da API**

```bash
# Documentar endpoints
cp templates/referencia.md docs/oauth2-api-reference.md

# Conexões
connections:
  impacts: ["oauth2-implementation-process.md"]
  relates_to: ["oauth2-architecture-decision.md"]
```

**Passo 5: Validação**

```bash
# Validar todo o conjunto
python scripts/context_scanner.py --path docs/
python scripts/conflict_detector.py --type all
```

### **Caso 2: Investigando Problema de Performance**

#### **Cenário:**

Aplicação está lenta, CPU alta, usuários reclamando.

#### **Abordagem Context Navigator:**

**Passo 1: Análise Inicial**

```bash
# Documento de análise
cp templates/analise.md docs/performance-investigation.md

# Metadados
doc_type: "analysis"
context_level: "c1_root"
context_type: "infra"
module: "performance"
```

**Passo 2: Coleta de Dados**

```markdown
## Dados e Evidências

### Dados Quantitativos

| Métrica  | Valor | Período |
| -------- | ----- | ------- |
| CPU      | 95%   | 2 horas |
| Memory   | 3.2GB | 2 horas |
| Latência | 2.5s  | 2 horas |

### Dados Qualitativos

- Usuários reportam lentidão às 14h
- Picos coincidem com backup
- Logs mostram timeout em queries
```

**Passo 3: Root Cause Analysis**

```markdown
## Análise Detalhada

### Root Cause Analysis

1. **Backup simultâneo:** IO intensivo
2. **Queries N+1:** Falta de otimização
3. **Cache expirado:** Reconstrução frequente

### Correlações Encontradas

- CPU alta = Backup em execução
- Latência alta = Queries não otimizadas
```

**Passo 4: Plano de Ação**

```markdown
## Ações Recomendadas

### Ações Imediatas

- [ ] Mover backup para 3h (Prioridade: Alta)
- [ ] Implementar query batching (Prioridade: Alta)

### Ações de Longo Prazo

- [ ] Implementar cache distribuído (Prioridade: Média)
- [ ] Monitoramento proativo (Prioridade: Baixa)
```

**Passo 5: Implementação e Decisões**

```bash
# Documentar decisões tomadas
cp templates/decisao.md docs/performance-optimization-decisions.md

# Conexões
connections:
  depends_on: ["performance-investigation.md"]
  impacts: ["system-architecture.md"]
```

### **Caso 3: Planejando Migração de Sistema**

#### **Cenário:**

Migrar aplicação monolítica para microserviços.

#### **Abordagem Context Navigator:**

**Passo 1: Planejamento Estratégico**

```bash
# Documento de planejamento
cp templates/planejamento.md docs/microservices-migration-plan.md

# Metadados
doc_type: "planning"
context_level: "c1_root"
context_type: "core"
module: "migration"
```

**Passo 2: Arquitetura Target**

```bash
# Definir arquitetura alvo
cp templates/arquitetura.md docs/microservices-target-architecture.md

# Conexões
connections:
  impacts: ["microservices-migration-plan.md"]
  relates_to: ["current-monolith-architecture.md"]
```

**Passo 3: Processos de Migração**

```bash
# Para cada serviço
cp templates/processo.md docs/user-service-migration-process.md
cp templates/processo.md docs/order-service-migration-process.md

# Conexões
connections:
  depends_on: ["microservices-target-architecture.md"]
  blocks: ["monolith-decommissioning.md"]
```

**Passo 4: Análise de Riscos**

```bash
# Análise de riscos
cp templates/analise.md docs/migration-risk-analysis.md

# Conexões
connections:
  references: ["microservices-migration-plan.md"]
  impacts: ["migration-rollback-plan.md"]
```

**Passo 5: Validação Completa**

```bash
# Validar todo o plano
python scripts/context_scanner.py --path docs/
python scripts/conflict_detector.py --type all
python scripts/template_validator.py --templates
```

---

## 🔧 Troubleshooting

### **Problemas Comuns e Soluções**

#### **Problema: Scanner não encontra documentos**

```bash
# Sintomas
$ python scripts/context_scanner.py
INFO - Nenhum documento encontrado

# Diagnóstico
ls -la docs/  # Verificar se arquivos existem
head -20 docs/exemplo.md  # Verificar formato de metadados

# Solução
# Verificar se metadados estão no formato correto:
---
doc_type: "decision"
# ... outros campos
---
```

#### **Problema: Metadados inválidos**

```bash
# Sintomas
ERROR - Erro ao parsear metadados: invalid yaml

# Diagnóstico
python -c "import yaml; print(yaml.safe_load(open('doc.md').read().split('---')[1]))"

# Solução
# Verificar sintaxe YAML:
- Indentação correta
- Aspas balanceadas
- Campos obrigatórios preenchidos
```

#### **Problema: Conflitos de dependência**

```bash
# Sintomas
WARNING - Dependência circular detectada

# Diagnóstico
python scripts/conflict_detector.py --type dependency

# Solução
# Revisar conexões:
1. Identificar ciclo
2. Remover dependência desnecessária
3. Refatorar se necessário
4. Validar novamente
```

#### **Problema: Templates não validando**

```bash
# Sintomas
ERROR - Seção obrigatória não encontrada

# Diagnóstico
python scripts/template_validator.py --file doc.md

# Solução
# Verificar estrutura:
1. Headers no formato correto (## Seção)
2. Seções obrigatórias presentes
3. Subseções recomendadas
4. Conteúdo adequado
```

#### **Problema: Context maps não atualizando**

```bash
# Sintomas
INFO - Context maps desatualizados

# Diagnóstico
ls -la .context-map/
cat .context-map/index.yml

# Solução
# Forçar atualização:
rm -rf .context-map/
python scripts/context_scanner.py --scan docs/
```

#### **Problema: IA não seguindo context.rule**

```bash
# Sintomas
IA gera conteúdo inconsistente com metodologia

# Diagnóstico
cat context.rule  # Verificar regras
grep -n "context.rule" prompt.txt  # Verificar se carregou

# Solução
# Sempre incluir no início do prompt:
"""
CARREGAR OBRIGATORIAMENTE:
1. context.rule (lei sagrada)
2. .context-map/index.yml (contexto)
3. Template apropriado
"""
```

### **Comandos de Diagnóstico**

#### **Verificação de Saúde Geral**

```bash
#!/bin/bash
# health_check.sh

echo "=== CONTEXT NAVIGATOR HEALTH CHECK ==="

# Verificar estrutura
echo "1. Verificando estrutura..."
ls -la .contextrc context.rule 2>/dev/null || echo "❌ Arquivos de configuração ausentes"

# Verificar scripts
echo "2. Verificando scripts..."
python scripts/context_scanner.py --validate 2>/dev/null && echo "✅ Scanner OK" || echo "❌ Scanner com problemas"

# Verificar templates
echo "3. Verificando templates..."
python scripts/template_validator.py --templates 2>/dev/null && echo "✅ Templates OK" || echo "❌ Templates com problemas"

# Verificar conflitos
echo "4. Verificando conflitos..."
python scripts/conflict_detector.py --json 2>/dev/null | jq '.total_conflicts' || echo "❌ Detector com problemas"

echo "=== FIM DO HEALTH CHECK ==="
```

#### **Limpeza de Cache**

```bash
#!/bin/bash
# clean_cache.sh

echo "Limpando cache do Context Navigator..."

# Remover mapas temporários
rm -rf .context-map/

# Remover logs
rm -f *.log

# Remover arquivos temporários
rm -f temp_*.md

# Recriar estrutura
mkdir -p .context-map/contexts

echo "Cache limpo. Execute o scanner para regenerar:"
echo "python scripts/context_scanner.py --scan docs/"
```

---

## 🔄 Manutenção e Evolução

### **Manutenção Preventiva**

#### **Diária (5 minutos)**

```bash
# Verificar documentos modificados
find docs/ -name "*.md" -mtime -1

# Validar rapidamente
python scripts/template_validator.py --file documento_modificado.md
```

#### **Semanal (30 minutos)**

```bash
# Scan completo
python scripts/context_scanner.py --scan docs/

# Detectar conflitos
python scripts/conflict_detector.py --type all

# Verificar qualidade
python scripts/template_validator.py --templates | grep -E "(ERROR|WARNING)"
```

#### **Mensal (2 horas)**

```bash
# Análise de padrões
python scripts/context_engine.py --patterns

# Revisão de documentos desatualizados
find docs/ -name "*.md" -mtime +30

# Auditoria de conexões
python scripts/conflict_detector.py --type dependency

# Limpeza de cache
rm -rf .context-map/
python scripts/context_scanner.py --scan docs/
```

### **Evolução da Metodologia**

#### **Adicionando Novo Tipo de Documento**

**Passo 1: Atualizar .contextrc**

```yaml
document_types:
  # ... tipos existentes
  tutorial:
    usage_percentage: 5
    description: "Tutoriais e guias educacionais"
    required_sections: ["introducao", "prerequisitos", "passos", "exercicios"]
```

**Passo 2: Criar Template**

```bash
# Criar novo template
cp templates/processo.md templates/tutorial.md

# Customizar estrutura
# Editar seções apropriadas
```

**Passo 3: Atualizar Scripts**

```python
# Em template_validator.py
self.tutorial_rules = {
    'required_sections': ['introducao', 'prerequisitos', 'passos', 'exercicios'],
    'min_exercises': 3,
    'quality_indicators': ['exemplo', 'pratica', 'exercicio']
}
```

**Passo 4: Testar Nova Funcionalidade**

```bash
# Criar documento de teste
cp templates/tutorial.md docs/test-tutorial.md

# Validar
python scripts/template_validator.py --file docs/test-tutorial.md
```

#### **Customizando Contextos**

**Passo 1: Identificar Necessidade**

```bash
# Analisar padrões atuais
python scripts/context_engine.py --patterns

# Verificar contextos mais usados
grep -r "context_type:" docs/ | sort | uniq -c | sort -nr
```

**Passo 2: Definir Novo Contexto**

```yaml
# Em .contextrc
contexts:
  # ... contextos existentes
  mobile:
    description: "Contexto de aplicações móveis"
    patterns: ["android", "ios", "flutter", "react-native"]
    parent_context: "ui"
```

**Passo 3: Atualizar Engine**

```python
# Em context_engine.py
self.context_patterns = {
    # ... padrões existentes
    'mobile': ['android', 'ios', 'flutter', 'react-native', 'mobile', 'app']
}
```

**Passo 4: Migrar Documentos**

```bash
# Encontrar documentos que devem usar novo contexto
grep -r "mobile\|android\|ios" docs/

# Atualizar metadados
# Editar cada arquivo relevante
```

### **Monitoramento de Qualidade**

#### **Métricas de Qualidade**

```bash
#!/bin/bash
# quality_metrics.sh

echo "=== MÉTRICAS DE QUALIDADE ==="

# Documentos por tipo
echo "1. Distribuição por tipo:"
grep -r "doc_type:" docs/ | cut -d'"' -f2 | sort | uniq -c | sort -nr

# Documentos desatualizados
echo "2. Documentos desatualizados (>30 dias):"
find docs/ -name "*.md" -mtime +30 | wc -l

# Conflitos por tipo
echo "3. Conflitos por tipo:"
python scripts/conflict_detector.py --json | jq '.conflicts_by_type'

# Score médio de qualidade
echo "4. Score médio de qualidade:"
python scripts/template_validator.py --templates --json | jq '.[] | .overall_score' | awk '{sum+=$1} END {print sum/NR}'
```

#### **Dashboard de Qualidade**

```python
#!/usr/bin/env python3
# quality_dashboard.py

import json
import subprocess

def get_quality_metrics():
    """Gera dashboard de qualidade"""

    # Executar scripts e coletar dados
    scanner_result = subprocess.run(['python', 'scripts/context_scanner.py', '--json'],
                                   capture_output=True, text=True)

    conflicts_result = subprocess.run(['python', 'scripts/conflict_detector.py', '--json'],
                                     capture_output=True, text=True)

    # Processar dados
    scanner_data = json.loads(scanner_result.stdout)
    conflicts_data = json.loads(conflicts_result.stdout)

    # Gerar dashboard
    dashboard = {
        'total_documents': scanner_data['total_documents'],
        'total_conflicts': conflicts_data['total_conflicts'],
        'quality_score': calculate_quality_score(scanner_data, conflicts_data),
        'recommendations': generate_recommendations(conflicts_data)
    }

    return dashboard

def calculate_quality_score(scanner_data, conflicts_data):
    """Calcula score geral de qualidade"""
    base_score = 100

    # Penalizar conflitos
    critical_conflicts = conflicts_data['conflicts_by_severity'].get('critical', 0)
    high_conflicts = conflicts_data['conflicts_by_severity'].get('high', 0)

    penalty = (critical_conflicts * 10) + (high_conflicts * 5)

    return max(0, base_score - penalty)

def generate_recommendations(conflicts_data):
    """Gera recomendações baseadas em conflitos"""
    recommendations = []

    for conflict_type, count in conflicts_data['conflicts_by_type'].items():
        if count > 0:
            recommendations.append(f"Resolver {count} conflitos de {conflict_type}")

    return recommendations

if __name__ == '__main__':
    dashboard = get_quality_metrics()
    print(json.dumps(dashboard, indent=2))
```

---

## 📚 Referência Rápida

### **Comandos Essenciais**

```bash
# Scan completo
python scripts/context_scanner.py --scan docs/

# Validar documento
python scripts/template_validator.py --file documento.md

# Detectar conflitos
python scripts/conflict_detector.py --type all

# Analisar documento
python scripts/context_engine.py --analyze documento.md

# Health check
python scripts/context_scanner.py --validate
```

### **Metadados Obrigatórios**

```yaml
---
doc_type: "decision|process|reference|architecture|analysis|planning"
context_level: "c1_root|c2_module|c3_component"
context_type: "infra|shared|core|api|data|ui"
module: "nome_do_modulo"
priority: "low|medium|high|critical"
status: "draft|active|deprecated|archived"
connections:
  references: []
  impacts: []
  depends_on: []
  blocks: []
  relates_to: []
created_date: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
owner: "nome_responsavel"
---
```

### **Estrutura de Pastas**

```
context-navigator/
├── .contextrc                    # Configuração principal
├── context.rule                  # Lei sagrada para IA
├── .context-map/                 # Mapas automáticos
│   ├── index.yml                 # Índice geral
│   ├── architecture.yml          # Visão arquitetural
│   ├── connections.yml           # Conexões
│   ├── conflicts.yml             # Conflitos
│   └── contexts/                 # Contextos específicos
├── scripts/                      # Ferramentas
│   ├── context_scanner.py        # Scanner principal
│   ├── context_engine.py         # Engine inteligente
│   ├── template_validator.py     # Validador
│   └── conflict_detector.py      # Detector de conflitos
├── templates/                    # Templates
│   ├── decisao.md               # Template decisão
│   ├── processo.md              # Template processo
│   ├── referencia.md            # Template referência
│   ├── arquitetura.md           # Template arquitetura
│   ├── analise.md               # Template análise
│   └── planejamento.md          # Template planejamento
├── docs/                        # Manuais
│   ├── MANUAL_HUMANO.md         # Este manual
│   ├── MANUAL_IA.md             # Manual para IA
│   └── CONVENTIONS.md           # Convenções
└── examples/                    # Exemplos
    └── exemplo_*.md             # Exemplos práticos
```

### **Tipos de Conexão**

- **references**: Documentos que este documento referencia
- **impacts**: Documentos que este documento impacta
- **depends_on**: Documentos dos quais este documento depende
- **blocks**: Documentos que este documento bloqueia
- **relates_to**: Documentos relacionados genericamente

### **Níveis de Contexto**

- **c1_root**: Contexto raiz do projeto
- **c2_module**: Contexto de módulo específico
- **c3_component**: Contexto de componente específico

### **Tipos de Contexto**

- **infra**: Infraestrutura e deploy
- **shared**: Componentes compartilhados
- **core**: Lógica de negócio central
- **api**: Interfaces e contratos
- **data**: Persistência e dados
- **ui**: Interface de usuário

### **Severidade de Conflitos**

- **CRITICAL**: Impede funcionamento
- **HIGH**: Impacta qualidade significativamente
- **MEDIUM**: Problemas moderados
- **LOW**: Melhorias menores
- **INFO**: Informações relevantes

---

## 🎯 Conclusão

O **Context Navigator** é uma metodologia poderosa que transforma como você trabalha com documentação e IA. Seguindo este manual, você será capaz de:

✅ **Manter contexto perfeito** em projetos complexos
✅ **Disciplinar a IA** com regras cristalinas
✅ **Automatizar validação** de documentos
✅ **Detectar conflitos** antes que se tornem problemas
✅ **Escalar documentação** sem perder qualidade

### **Próximos Passos**

1. **Implementar setup** básico seguindo o guia
2. **Criar primeiros documentos** usando templates
3. **Executar ferramentas** para validação
4. **Estabelecer rotina** de manutenção
5. **Evoluir metodologia** conforme necessidades

### **Suporte e Comunidade**

- **Manual da IA**: `docs/MANUAL_IA.md`
- **Convenções**: `docs/CONVENTIONS.md`
- **Exemplos**: `examples/`

---

**🚀 Bem-vindo ao futuro da documentação inteligente!**

_Context Navigator: Onde humano e IA trabalham em perfeita harmonia._
