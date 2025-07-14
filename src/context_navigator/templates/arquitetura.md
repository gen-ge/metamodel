---
# =============================================================================
# METADADOS OBRIGATÓRIOS (IMUTÁVEIS)
# =============================================================================

# Tipo do documento (OBRIGATÓRIO)
doc_type: "architecture"

# Título do documento (OBRIGATÓRIO)
title: "[PREENCHER] Título da Arquitetura"

# Contexto hierárquico (OBRIGATÓRIO)
context_level: "c1_root" # c1_root | c2_module | c3_component

# Contexto especializado (OBRIGATÓRIO)
context_type: "core" # infra | shared | core | api | data | ui

# Módulo específico (OBRIGATÓRIO)
module: "[PREENCHER] Nome do Módulo"

# Conexões com outros documentos (OBRIGATÓRIO)
connections:
  references: ["referencia.md"] # Referenciam especificações técnicas
  impacts: ["processo.md", "analise.md"] # Arquitetura impacta processos e análises
  depends_on: ["decisao.md"] # Arquitetura depende de decisões
  blocks: [] # Documentos bloqueados
  relates_to: ["planejamento.md"] # Relaciona com planejamento

# Datas (OBRIGATÓRIAS)
created_date: "2024-01-15"
last_updated: "2024-01-15"

# =============================================================================
# METADADOS OPCIONAIS (EXTENSÍVEIS)
# =============================================================================

# Prioridade da arquitetura
priority: "high" # critical | high | medium | low

# Status atual
status: "active" # draft | review | active | deprecated | archived

# Responsável pela arquitetura
owner: "[PREENCHER] Nome do Responsável"

# Tags para categorização
tags: ["architecture", "design", "system"]

# Complexidade da arquitetura
complexity: "high" # low | medium | high | critical

# Agenda de manutenção
maintenance_schedule: "quarterly" # never | monthly | quarterly | yearly

# Tipo de arquitetura
architecture_type: "system" # system | component | service | data | security

# Padrão arquitetural
architectural_pattern: "layered" # layered | microservices | event-driven | hexagonal | clean

# Nível de abstração
abstraction_level: "high" # low | medium | high | conceptual

# Estágio de desenvolvimento
development_stage: "design" # concept | design | implementation | production | legacy

# Escala alvo
target_scale: "medium" # small | medium | large | enterprise

# Disponibilidade alvo
target_availability: "99.9%" # 99% | 99.9% | 99.99% | 99.999%

# Performance alvo
target_performance: "< 200ms" # Tempo de resposta esperado

# Capacidade alvo
target_capacity: "10K concurrent users"

# Tecnologias principais
key_technologies: ["React", "Node.js", "PostgreSQL", "Docker"]

# Padrões de qualidade
quality_attributes:
  ["performance", "scalability", "security", "maintainability"]

# Stakeholders
stakeholders: ["development-team", "product-team", "devops-team"]

# Ambiente alvo
target_environment: "cloud" # on-premise | cloud | hybrid

# Orçamento estimado
estimated_budget: "medium" # low | medium | high | enterprise

# Prazo de implementação
implementation_timeline: "6 months"

# Nível de risco
risk_level: "medium" # low | medium | high | critical
---

<!-- CONTEXT_META
template_version: "1.0.0"
template_type: "architecture"
generated_by: "context-navigator"
validation_status: "pending"
last_validated: "2024-01-15"
compliance_check: "passed"
metadata_completeness: "100%"
connection_accuracy: "pending"
context_consistency: "verified"
architecture_category: "system"
design_level: "high-level"
-->

# 🏗️ [TÍTULO DA ARQUITETURA]

> **Template:** Arquitetura | **Contexto:** [CONTEXTO] | **Módulo:** [MÓDULO]  
> **Criado:** [DATA] | **Atualizado:** [DATA] | **Status:** [STATUS]

## 📋 Metadados da Arquitetura

**Tipo:** [SISTEMA/COMPONENTE/SERVIÇO/DADOS/SEGURANÇA]  
**Padrão:** [LAYERED/MICROSERVICES/EVENT-DRIVEN/HEXAGONAL/CLEAN]  
**Escala:** [PEQUENA/MÉDIA/GRANDE/ENTERPRISE]  
**Disponibilidade:** [99%/99.9%/99.99%/99.999%]  
**Performance:** [TEMPO DE RESPOSTA ALVO]  
**Ambiente:** [ON-PREMISE/CLOUD/HYBRID]

## 🎯 Contexto Arquitetural

### **Visão Geral**

[Descreva a visão geral do sistema e seu propósito arquitetural]

### **Problema Arquitetural**

[Identifique o problema que esta arquitetura resolve]

### **Objetivos**

- [Objetivo arquitetural 1]
- [Objetivo arquitetural 2]
- [Objetivo arquitetural 3]

### **Restrições**

- **Técnicas:** [Limitações técnicas]
- **Orçamentárias:** [Limitações de orçamento]
- **Temporais:** [Limitações de tempo]
- **Regulamentares:** [Limitações regulamentares]
- **Organizacionais:** [Limitações organizacionais]

### **Premissas**

- [Premissa 1]
- [Premissa 2]
- [Premissa 3]

## 🔍 Requisitos Arquiteturais

### **Requisitos Funcionais**

| ID     | Requisito               | Prioridade | Status       |
| ------ | ----------------------- | ---------- | ------------ |
| RF-001 | [Requisito funcional 1] | Alta       | Implementado |
| RF-002 | [Requisito funcional 2] | Média      | Planejado    |
| RF-003 | [Requisito funcional 3] | Baixa      | Futuro       |

### **Requisitos Não-Funcionais**

| Atributo             | Requisito                      | Métrica          | Verificação    |
| -------------------- | ------------------------------ | ---------------- | -------------- |
| **Performance**      | [Requisito de performance]     | < 200ms          | Load testing   |
| **Escalabilidade**   | [Requisito de escala]          | 10K users        | Stress testing |
| **Disponibilidade**  | [Requisito de disponibilidade] | 99.9%            | Monitoring     |
| **Segurança**        | [Requisito de segurança]       | OWASP compliance | Security audit |
| **Manutenibilidade** | [Requisito de manutenção]      | < 4 horas MTTR   | Code metrics   |

### **Atributos de Qualidade**

- **Performance:** [Descrição e métricas]
- **Escalabilidade:** [Descrição e métricas]
- **Disponibilidade:** [Descrição e métricas]
- **Segurança:** [Descrição e métricas]
- **Manutenibilidade:** [Descrição e métricas]
- **Usabilidade:** [Descrição e métricas]

## 🏗️ Visão Arquitetural

### **Arquitetura de Alto Nível**

```
┌─────────────────────────────────────────────────────────────┐
│                        PRESENTATION LAYER                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Web App   │  │ Mobile App  │  │   Admin     │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Auth Service│  │ User Service│  │ Order Service│        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                        DATA LAYER                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Primary DB  │  │   Cache     │  │ Message Queue│        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### **Padrão Arquitetural Aplicado**

**Padrão:** [NOME DO PADRÃO]

**Justificativa:**
[Explique por que este padrão foi escolhido]

**Implementação:**
[Descreva como o padrão é implementado]

**Benefícios:**

- [Benefício 1]
- [Benefício 2]
- [Benefício 3]

**Trade-offs:**

- [Trade-off 1]
- [Trade-off 2]
- [Trade-off 3]

## 🧩 Componentes Arquiteturais

### **Componente 1: [NOME DO COMPONENTE]**

**Tipo:** [SERVICE/LIBRARY/DATABASE/QUEUE/CACHE]  
**Responsabilidade:** [Responsabilidade principal]

**Interfaces:**

- **Input:** [Interfaces de entrada]
- **Output:** [Interfaces de saída]
- **Dependencies:** [Dependências externas]

**Tecnologias:**

- [Tecnologia 1]
- [Tecnologia 2]
- [Tecnologia 3]

**Características:**

- **Escalabilidade:** [Estratégia de escala]
- **Disponibilidade:** [Estratégia de disponibilidade]
- **Performance:** [Características de performance]

**Configuração:**

```yaml
component_1:
  port: 8080
  database: postgresql
  cache: redis
  max_connections: 100
```

---

### **Componente 2: [NOME DO COMPONENTE]**

**Tipo:** [SERVICE/LIBRARY/DATABASE/QUEUE/CACHE]  
**Responsabilidade:** [Responsabilidade principal]

**Interfaces:**

- **Input:** [Interfaces de entrada]
- **Output:** [Interfaces de saída]
- **Dependencies:** [Dependências externas]

**Tecnologias:**

- [Tecnologia 1]
- [Tecnologia 2]
- [Tecnologia 3]

**Características:**

- **Escalabilidade:** [Estratégia de escala]
- **Disponibilidade:** [Estratégia de disponibilidade]
- **Performance:** [Características de performance]

**Configuração:**

```yaml
component_2:
  port: 8081
  storage: s3
  timeout: 30s
  retry_count: 3
```

## 🔄 Fluxos Arquiteturais

### **Fluxo 1: [NOME DO FLUXO]**

**Descrição:** [Descrição do fluxo]

**Sequência:**

```
User → Web App → API Gateway → Auth Service → User Service → Database
  ↓        ↓           ↓            ↓             ↓           ↓
Response ← Response ← Response ← Response ← Response ← Response
```

**Passos Detalhados:**

1. **Usuário inicia ação:** [Descrição]
2. **Web App processa:** [Descrição]
3. **API Gateway roteia:** [Descrição]
4. **Auth Service valida:** [Descrição]
5. **User Service executa:** [Descrição]
6. **Database persiste:** [Descrição]
7. **Response é retornada:** [Descrição]

**Tratamento de Erros:**

- **Erro de autenticação:** [Tratamento]
- **Erro de validação:** [Tratamento]
- **Erro de sistema:** [Tratamento]

**Métricas:**

- **Latência:** [Valor esperado]
- **Throughput:** [Valor esperado]
- **Error rate:** [Valor esperado]

---

### **Fluxo 2: [NOME DO FLUXO]**

**Descrição:** [Descrição do fluxo]

**Sequência:**

```
Event → Message Queue → Event Handler → Business Logic → Database
  ↓          ↓              ↓               ↓            ↓
Ack ← Ack ← Processing ← Validation ← Persistence
```

**Passos Detalhados:**

1. **Event é publicado:** [Descrição]
2. **Queue processa:** [Descrição]
3. **Handler recebe:** [Descrição]
4. **Business Logic executa:** [Descrição]
5. **Database é atualizado:** [Descrição]

## 📊 Modelos de Dados

### **Modelo Conceitual**

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    User     │────▶│    Order    │────▶│   Product   │
│             │     │             │     │             │
│ - id        │     │ - id        │     │ - id        │
│ - name      │     │ - user_id   │     │ - name      │
│ - email     │     │ - total     │     │ - price     │
│ - created   │     │ - created   │     │ - stock     │
└─────────────┘     └─────────────┘     └─────────────┘
```

### **Modelo Lógico**

```sql
-- Tabela de usuários
CREATE TABLE users (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de pedidos
CREATE TABLE orders (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    total DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de produtos
CREATE TABLE products (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### **Estratégias de Dados**

- **Particionamento:** [Estratégia de particionamento]
- **Replicação:** [Estratégia de replicação]
- **Backup:** [Estratégia de backup]
- **Archiving:** [Estratégia de arquivamento]

## 🔐 Segurança Arquitetural

### **Modelo de Segurança**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Client    │───▶│   Gateway   │───▶│   Service   │
│             │    │             │    │             │
│ - TLS 1.3   │    │ - Auth      │    │ - mTLS      │
│ - JWT       │    │ - Rate Limit│    │ - Validation│
│ - CORS      │    │ - Firewall  │    │ - RBAC      │
└─────────────┘    └─────────────┘    └─────────────┘
```

### **Princípios de Segurança**

- **Defense in Depth:** [Implementação]
- **Least Privilege:** [Implementação]
- **Zero Trust:** [Implementação]
- **Fail Secure:** [Implementação]

### **Controles de Segurança**

| Controle         | Implementação     | Verificação      |
| ---------------- | ----------------- | ---------------- |
| **Autenticação** | JWT + OAuth 2.0   | Security testing |
| **Autorização**  | RBAC + Claims     | Access audit     |
| **Criptografia** | TLS 1.3 + AES-256 | Crypto audit     |
| **Monitoring**   | SIEM + Alerts     | Log analysis     |

## 🚀 Deployment e Infraestrutura

### **Arquitetura de Deployment**

```
┌─────────────────────────────────────────────────────────────┐
│                        CLOUD PROVIDER                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │  Region 1   │  │  Region 2   │  │  Region 3   │        │
│  │             │  │             │  │             │        │
│  │ ┌─────────┐ │  │ ┌─────────┐ │  │ ┌─────────┐ │        │
│  │ │   AZ-A  │ │  │ │   AZ-A  │ │  │ │   AZ-A  │ │        │
│  │ │   AZ-B  │ │  │ │   AZ-B  │ │  │ │   AZ-B  │ │        │
│  │ └─────────┘ │  │ └─────────┘ │  │ └─────────┘ │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### **Estratégias de Deployment**

- **Blue-Green:** [Implementação]
- **Rolling Update:** [Implementação]
- **Canary Release:** [Implementação]
- **Feature Flags:** [Implementação]

### **Infraestrutura como Código**

```yaml
# Kubernetes deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
        - name: user-service
          image: user-service:latest
          ports:
            - containerPort: 8080
          env:
            - name: DB_CONNECTION
              value: postgresql://...
```

## 📈 Monitoramento e Observabilidade

### **Estratégia de Monitoramento**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Metrics   │───▶│   Logging   │───▶│   Tracing   │
│             │    │             │    │             │
│ - Prometheus│    │ - ELK Stack │    │ - Jaeger    │
│ - Grafana   │    │ - Fluentd   │    │ - OpenTel   │
│ - Alerts    │    │ - Kibana    │    │ - Zipkin    │
└─────────────┘    └─────────────┘    └─────────────┘
```

### **Métricas Chave**

- **Business Metrics:** [Métricas de negócio]
- **Application Metrics:** [Métricas de aplicação]
- **Infrastructure Metrics:** [Métricas de infraestrutura]

### **SLIs e SLOs**

| Indicador           | Objetivo                  | Alerta    |
| ------------------- | ------------------------- | --------- |
| **Latência**        | < 200ms (95th percentile) | > 500ms   |
| **Disponibilidade** | 99.9%                     | < 99.5%   |
| **Error Rate**      | < 0.1%                    | > 1%      |
| **Throughput**      | > 1000 RPS                | < 500 RPS |

## 🔄 Decisões Arquiteturais

### **ADR-001: Escolha do Padrão Arquitetural**

**Status:** Aceito  
**Contexto:** [Contexto da decisão]  
**Decisão:** [Decisão tomada]  
**Consequências:** [Consequências da decisão]

### **ADR-002: Seleção de Tecnologia**

**Status:** Aceito  
**Contexto:** [Contexto da decisão]  
**Decisão:** [Decisão tomada]  
**Consequências:** [Consequências da decisão]

### **ADR-003: Estratégia de Dados**

**Status:** Proposto  
**Contexto:** [Contexto da decisão]  
**Decisão:** [Decisão tomada]  
**Consequências:** [Consequências da decisão]

## 🚧 Roadmap e Evolução

### **Fase 1: Fundação (Meses 1-2)**

- [ ] Infraestrutura base
- [ ] Componentes core
- [ ] Integração básica
- [ ] Testes unitários

### **Fase 2: Expansão (Meses 3-4)**

- [ ] Novos componentes
- [ ] Integração avançada
- [ ] Performance tuning
- [ ] Testes de integração

### **Fase 3: Otimização (Meses 5-6)**

- [ ] Otimizações
- [ ] Monitoramento avançado
- [ ] Automação completa
- [ ] Documentação final

### **Futuro (Meses 7+)**

- [ ] Novas funcionalidades
- [ ] Migração para cloud
- [ ] Machine learning
- [ ] Expansão global

## ⚠️ Riscos e Mitigações

### **Riscos Técnicos**

| Risco                      | Probabilidade | Impacto | Mitigação                     |
| -------------------------- | ------------- | ------- | ----------------------------- |
| **Falha de componente**    | Média         | Alto    | Redundância + Circuit breaker |
| **Gargalo de performance** | Alta          | Médio   | Load testing + Optimization   |
| **Vulnerabilidade**        | Baixa         | Crítico | Security audit + Monitoring   |

### **Riscos de Negócio**

| Risco                     | Probabilidade | Impacto | Mitigação            |
| ------------------------- | ------------- | ------- | -------------------- |
| **Mudança de requisitos** | Alta          | Médio   | Arquitetura flexível |
| **Prazo apertado**        | Média         | Alto    | MVP + Iteração       |
| **Orçamento limitado**    | Baixa         | Alto    | Cloud + Automação    |

## 📚 Referências e Recursos

### **Documentação Técnica**

- [Documento de Requisitos] - [Link]
- [Guia de Implementação] - [Link]
- [Padrões de Código] - [Link]

### **Padrões e Práticas**

- [Clean Architecture] - [Link]
- [Domain-Driven Design] - [Link]
- [Microservices Patterns] - [Link]

### **Ferramentas e Tecnologias**

- [Docker Documentation] - [Link]
- [Kubernetes Guide] - [Link]
- [AWS Best Practices] - [Link]

### **Histórico de Versões**

| Versão | Data       | Autor  | Mudanças       |
| ------ | ---------- | ------ | -------------- |
| 1.0    | 2024-01-15 | [Nome] | Versão inicial |

---

<!-- VALIDATION_CHECKLIST
[ ] Todos os metadados obrigatórios preenchidos
[ ] Contexto arquitetural claro
[ ] Requisitos bem definidos
[ ] Visão arquitetural documentada
[ ] Componentes detalhados
[ ] Fluxos arquiteturais mapeados
[ ] Modelos de dados definidos
[ ] Segurança considerada
[ ] Deployment planejado
[ ] Monitoramento definido
[ ] Decisões arquiteturais documentadas
[ ] Roadmap estabelecido
[ ] Riscos identificados
[ ] Referências incluídas
[ ] Conexões com outros documentos mapeadas
-->

<!-- SCANNER_INSTRUCTIONS
Este template de arquitetura deve ser usado para:
- Arquitetura de sistema
- Design de componentes
- Modelagem de dados
- Padrões arquiteturais
- Decisões técnicas
- Roadmap técnico

Campos obrigatórios para o scanner:
- doc_type: "architecture"
- title: Título da arquitetura
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
- Validar se há diagramas ou descrições arquiteturais
- Verificar se há componentes definidos
- Validar se há decisões arquiteturais documentadas
-->

<!-- CONTEXT_CONNECTIONS
Este documento se conecta com:
- Documentos de decisão (decision) via "depends_on"
- Documentos de processo (process) via "impacts"
- Documentos de referência (reference) via "references"
- Outros documentos de arquitetura (architecture) via "relates_to"

Padrões de conexão:
- [[nome-do-documento]] para referências diretas
- {{nome-do-componente}} para componentes
- @contexto para referências de contexto
- /path/to/diagram para diagramas
- #adr-001 para decisões arquiteturais
-->
