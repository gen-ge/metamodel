---
doc_type: "architecture"
context_level: "c1_root"
context_type: "core"
module: "e-commerce-platform"
priority: "high"
status: "active"
connections:
  references: ["microservices-decision.md", "technology-stack-decision.md"]
  impacts: ["deployment-process.md", "monitoring-setup.md"]
  depends_on: ["system-requirements.md", "scalability-analysis.md"]
  blocks: []
  relates_to: ["api-gateway-design.md", "database-architecture.md"]
created_date: "2024-01-15"
last_updated: "2024-01-15"
owner: "Solution Architect"
---

# Arquitetura de Microserviços E-commerce

## Contexto Arquitetural

### Visão Geral

Este documento define a arquitetura de microserviços para a plataforma de e-commerce, suportando 100.000+ usuários simultâneos, processamento de 10.000+ pedidos/dia e crescimento sustentável.

### Objetivos

- **Escalabilidade:** Suportar crescimento de 10x em 2 anos
- **Disponibilidade:** 99.9% uptime (menos de 8h downtime/ano)
- **Performance:** Response time < 200ms para 95% das requests
- **Manutenibilidade:** Deploys independentes e rollbacks seguros
- **Resiliência:** Tolerância a falhas e degradação graciosa

### Restrições Arquiteturais

#### **Tecnológicas**

- Kubernetes como orquestrador
- PostgreSQL como banco principal
- Redis para cache e sessões
- Mensageria assíncrona obrigatória

#### **Organizacionais**

- Equipes de 5-7 pessoas por serviço
- DevOps integrado em cada equipe
- Autonomia de tecnologia por serviço

#### **Regulamentares**

- LGPD compliance
- PCI DSS para pagamentos
- SOX para auditoria financeira

## Visão Arquitetural

### Diagrama Principal

```
┌─────────────────────────────────────────────────────────────────┐
│                          Internet                               │
└─────────────────────────┬───────────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────────┐
│                    Load Balancer                                │
│                   (AWS ALB/NLB)                                 │
└─────────────────────────┬───────────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────────┐
│                   API Gateway                                   │
│              (Kong/Ambassador)                                  │
│   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐              │
│   │   Auth      │ │ Rate Limit  │ │  Routing    │              │
│   │ Middleware  │ │ Middleware  │ │ Middleware  │              │
│   └─────────────┘ └─────────────┘ └─────────────┘              │
└─────────────────────────┬───────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
┌───────▼──────┐ ┌───────▼──────┐ ┌───────▼──────┐
│  User Service│ │Order Service │ │Product Service│
│   (Node.js)  │ │  (Node.js)   │ │   (Python)   │
│              │ │              │ │              │
│  ┌────────┐  │ │  ┌────────┐  │ │  ┌────────┐  │
│  │  API   │  │ │  │  API   │  │ │  │  API   │  │
│  └────────┘  │ │  └────────┘  │ │  └────────┘  │
│  ┌────────┐  │ │  ┌────────┐  │ │  ┌────────┐  │
│  │Business│  │ │  │Business│  │ │  │Business│  │
│  │ Logic  │  │ │  │ Logic  │  │ │  │ Logic  │  │
│  └────────┘  │ │  └────────┘  │ │  └────────┘  │
│  ┌────────┐  │ │  ┌────────┐  │ │  ┌────────┐  │
│  │  Data  │  │ │  │  Data  │  │ │  │  Data  │  │
│  │ Access │  │ │  │ Access │  │ │  │ Access │  │
│  └────────┘  │ │  └────────┘  │ │  └────────┘  │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
┌──────▼───────┐ ┌──────▼───────┐ ┌──────▼───────┐
│   User DB    │ │   Order DB   │ │  Product DB  │
│ (PostgreSQL) │ │ (PostgreSQL) │ │ (PostgreSQL) │
└──────────────┘ └──────────────┘ └──────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    Message Bus                                  │
│                  (Apache Kafka)                                 │
│                                                                 │
│   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐              │
│   │  user.events│ │order.events │ │product.events│              │
│   └─────────────┘ └─────────────┘ └─────────────┘              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                   Shared Services                               │
│                                                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │    Redis     │ │  Monitoring  │ │   Logging    │            │
│  │   (Cache)    │ │ (Prometheus) │ │     (ELK)    │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
└─────────────────────────────────────────────────────────────────┘
```

### Tecnologias Principais

| Componente           | Tecnologia         | Versão   | Justificativa                         |
| -------------------- | ------------------ | -------- | ------------------------------------- |
| **API Gateway**      | Kong               | 3.0+     | Performance, plugins, escalabilidade  |
| **Orquestração**     | Kubernetes         | 1.24+    | Padrão da indústria, maturidade       |
| **Backend Services** | Node.js/Python     | 18+/3.9+ | Performance, ecosystem, produtividade |
| **Banco Principal**  | PostgreSQL         | 14+      | ACID, performance, JSON support       |
| **Cache**            | Redis              | 7.0+     | Performance, data structures          |
| **Message Bus**      | Apache Kafka       | 3.0+     | Throughput, durabilidade              |
| **Monitoring**       | Prometheus/Grafana | Latest   | Observabilidade, alertas              |
| **Logging**          | ELK Stack          | 8.0+     | Centralized logging, search           |

## Componentes Arquiteturais

### Componente 1: API Gateway

#### **Responsabilidade:**

- Ponto único de entrada para clientes externos
- Autenticação e autorização
- Rate limiting e throttling
- Roteamento e load balancing
- Coleta de métricas e logs

#### **Interfaces:**

- **Externa:** REST API HTTP/HTTPS (porta 80/443)
- **Interna:** HTTP para microserviços (porta 8080)
- **Admin:** API de configuração (porta 8001)

#### **Tecnologias:**

- **Kong:** API Gateway principal
- **PostgreSQL:** Configuração e plugins
- **Prometheus:** Métricas de performance

#### **Configuração:**

```yaml
# Kong Configuration
services:
  - name: user-service
    url: http://user-service:8080
    routes:
      - name: users
        paths: ["/api/users"]
        methods: ["GET", "POST", "PUT", "DELETE"]
    plugins:
      - name: jwt
      - name: rate-limiting
        config:
          minute: 100
```

### Componente 2: User Service

#### **Responsabilidade:**

- Gestão completa de usuários
- Autenticação e autorização
- Perfis e preferências
- Integração com sistemas externos

#### **Interfaces:**

- **API REST:** CRUD de usuários
- **Events:** Publicação de eventos de usuário
- **Database:** Acesso exclusivo ao User DB

#### **Tecnologias:**

- **Node.js + Express:** Runtime e framework
- **JWT:** Tokens de autenticação
- **bcrypt:** Hash de senhas
- **Joi:** Validação de dados

#### **Modelo de Dados:**

```sql
-- User Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- User Profiles
CREATE TABLE user_profiles (
    user_id UUID REFERENCES users(id),
    phone VARCHAR(50),
    address JSONB,
    preferences JSONB,
    avatar_url VARCHAR(500)
);
```

### Componente 3: Order Service

#### **Responsabilidade:**

- Gestão de pedidos e carrinho
- Processamento de pagamentos
- Workflow de fulfillment
- Integração com sistemas de entrega

#### **Interfaces:**

- **API REST:** Operações de pedidos
- **Events:** Order lifecycle events
- **Integration:** Payment gateways

#### **Tecnologias:**

- **Node.js + Fastify:** Performance otimizada
- **State Machine:** Workflow de pedidos
- **Stripe SDK:** Processamento de pagamentos

#### **Fluxo de Estados:**

```
CART → CHECKOUT → PAYMENT_PENDING → PAID →
PROCESSING → SHIPPED → DELIVERED → COMPLETED
                ↓
             CANCELLED
```

### Componente 4: Product Service

#### **Responsabilidade:**

- Catálogo de produtos
- Busca e filtros
- Gestão de inventário
- Recomendações

#### **Interfaces:**

- **API REST:** CRUD de produtos
- **Search API:** Elasticsearch integration
- **Events:** Inventory updates

#### **Tecnologias:**

- **Python + FastAPI:** Performance e typing
- **Elasticsearch:** Busca e recomendações
- **S3:** Armazenamento de imagens

## Fluxos Arquiteturais

### Fluxo 1: Criação de Usuário

#### **Sequência:**

1. **Cliente** → POST /api/users → **API Gateway**
2. **API Gateway** → Validação e roteamento → **User Service**
3. **User Service** → Validação de dados → **Business Logic**
4. **Business Logic** → Hash password → **Data Access**
5. **Data Access** → INSERT user → **PostgreSQL**
6. **User Service** → Publish event → **Kafka**
7. **User Service** → Response → **API Gateway**
8. **API Gateway** → Response → **Cliente**

#### **Passos Detalhados:**

```javascript
// 1. API Gateway - Rate limiting e auth
kong.rateLimit(request);
kong.authenticate(request);

// 2. User Service - Validação
const userData = joi.validate(request.body, userSchema);

// 3. Business Logic - Regras de negócio
const hashedPassword = await bcrypt.hash(userData.password, 10);
const user = await userRepository.create({
  ...userData,
  password: hashedPassword,
});

// 4. Event Publishing
await eventBus.publish("user.created", {
  userId: user.id,
  email: user.email,
  timestamp: new Date(),
});

// 5. Response
response.status(201).json({ user: user.toPublic() });
```

### Fluxo 2: Processamento de Pedido

#### **Sequência:**

1. **Cliente** → POST /api/orders → **API Gateway**
2. **API Gateway** → Auth check → **Order Service**
3. **Order Service** → Validate cart → **Product Service**
4. **Product Service** → Check inventory → **Database**
5. **Order Service** → Process payment → **Payment Gateway**
6. **Order Service** → Create order → **Database**
7. **Order Service** → Publish events → **Kafka**
8. **Fulfillment Service** → Process shipment
9. **Notification Service** → Send confirmations

#### **Passos Detalhados:**

```javascript
// 1. Validate cart items
const cartValidation = await productService.validateCart(cart);
if (!cartValidation.valid) {
  throw new Error("Invalid cart items");
}

// 2. Process payment
const payment = await paymentGateway.charge({
  amount: cart.total,
  currency: "BRL",
  source: paymentMethod,
});

// 3. Create order with saga pattern
const saga = new OrderSaga({
  cart,
  payment,
  customer,
});

await saga.execute();
```

### Fluxo 3: Busca de Produtos

#### **Sequência:**

1. **Cliente** → GET /api/products/search → **API Gateway**
2. **API Gateway** → Cache check → **Redis**
3. **Redis** → Cache miss → **Product Service**
4. **Product Service** → Search query → **Elasticsearch**
5. **Elasticsearch** → Results → **Product Service**
6. **Product Service** → Enrich data → **Database**
7. **Product Service** → Cache results → **Redis**
8. **Product Service** → Response → **Cliente**

## Decisões Arquiteturais

### ADR 1: Adoção de Microserviços

#### **Contexto:**

Sistema monolítico atingiu limites de escalabilidade e manutenibilidade. Equipe cresceu para 20+ desenvolvedores, deployments se tornaram complexos.

#### **Decisão:**

Migrar para arquitetura de microserviços com 4 serviços principais: User, Order, Product, Payment.

#### **Impacto:**

- **Positivo:** Escalabilidade independente, tecnologias diferentes por serviço, deploys mais rápidos
- **Negativo:** Complexidade operacional, eventual consistency, debugging distribuído

### ADR 2: Event-Driven Architecture

#### **Contexto:**

Necessidade de integração entre serviços sem acoplamento forte. Requisitos de eventual consistency aceitáveis.

#### **Decisão:**

Implementar message bus com Apache Kafka para comunicação assíncrona entre serviços.

#### **Impacto:**

- **Positivo:** Desacoplamento, resilência, scalabilidade
- **Negativo:** Complexidade de debugging, eventual consistency

### ADR 3: Database per Service

#### **Contexto:**

Microserviços precisam de autonomia completa, incluindo dados. Diferentes serviços têm diferentes necessidades de dados.

#### **Decisão:**

Cada serviço terá sua própria instância de banco de dados PostgreSQL.

#### **Impacto:**

- **Positivo:** Autonomia completa, otimização por serviço
- **Negativo:** Joins entre serviços impossíveis, eventual consistency

### ADR 4: API Gateway Pattern

#### **Contexto:**

Múltiplos serviços precisam de ponto único de entrada. Necessidade de cross-cutting concerns (auth, rate limiting).

#### **Decisão:**

Implementar Kong como API Gateway para todas as requests externas.

#### **Impacto:**

- **Positivo:** Ponto único de controle, cross-cutting concerns centralizados
- **Negativo:** Potencial single point of failure, latência adicional

## Estratégias de Resiliência

### Circuit Breaker Pattern

```javascript
const CircuitBreaker = require("opossum");

const options = {
  timeout: 3000,
  errorThresholdPercentage: 50,
  resetTimeout: 30000,
};

const breaker = new CircuitBreaker(paymentService.charge, options);
```

### Retry with Exponential Backoff

```javascript
const retry = require("async-retry");

await retry(
  async () => {
    return await externalAPI.call();
  },
  {
    retries: 3,
    factor: 2,
    minTimeout: 1000,
    maxTimeout: 5000,
  }
);
```

### Graceful Degradation

```javascript
try {
  const recommendations = await recommendationService.get(userId);
  return { products, recommendations };
} catch (error) {
  logger.warn("Recommendation service down, falling back");
  return { products, recommendations: [] };
}
```

## Monitoramento e Observabilidade

### Métricas de Sistema

- **SLI:** Response time p95 < 200ms
- **SLI:** Error rate < 0.1%
- **SLI:** Throughput > 1000 RPS
- **SLO:** Availability 99.9%

### Healthchecks

```javascript
// Service health endpoint
app.get("/health", async (req, res) => {
  const checks = await Promise.all([
    database.ping(),
    redis.ping(),
    kafka.ping(),
  ]);

  const healthy = checks.every((check) => check.ok);
  res.status(healthy ? 200 : 503).json({
    status: healthy ? "healthy" : "unhealthy",
    checks,
  });
});
```

### Distributed Tracing

```javascript
const tracer = require("dd-trace").init();

app.use((req, res, next) => {
  const span = tracer.startSpan("http.request");
  span.setTag("http.method", req.method);
  span.setTag("http.url", req.url);

  req.span = span;
  next();
});
```

## Roadmap de Evolução

### Fase 1: MVP (Q1 2024)

- [ ] Implementação dos 4 microserviços básicos
- [ ] API Gateway com Kong
- [ ] Banco de dados por serviço
- [ ] Messaging básico com Kafka

### Fase 2: Otimização (Q2 2024)

- [ ] Cache distribuído com Redis
- [ ] Monitoramento com Prometheus/Grafana
- [ ] CI/CD pipeline completo
- [ ] Testes de carga automatizados

### Fase 3: Expansão (Q3 2024)

- [ ] Recommendation Service
- [ ] Search Service com Elasticsearch
- [ ] Mobile API optimization
- [ ] Advanced analytics

### Fase 4: Scale (Q4 2024)

- [ ] Multi-region deployment
- [ ] Advanced security features
- [ ] AI/ML integration
- [ ] Real-time analytics

---

**Arquitetura E-commerce v1.0 - Base sólida para crescimento sustentável.**
