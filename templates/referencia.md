---
# =============================================================================
# METADADOS OBRIGATÓRIOS (IMUTÁVEIS)
# =============================================================================

# Tipo do documento (OBRIGATÓRIO)
doc_type: "reference"

# Título do documento (OBRIGATÓRIO)
title: "[PREENCHER] Título da Referência"

# Contexto hierárquico (OBRIGATÓRIO)
context_level: "c2_module" # c1_root | c2_module | c3_component

# Contexto especializado (OBRIGATÓRIO)
context_type: "api" # infra | shared | core | api | data | ui

# Módulo específico (OBRIGATÓRIO)
module: "[PREENCHER] Nome do Módulo"

# Conexões com outros documentos (OBRIGATÓRIO)
connections:
  references: ["arquitetura.md"] # Referenciam especificações arquiteturais
  impacts: ["decisao.md", "processo.md"] # Referências impactam decisões e processos
  depends_on: [] # Dependências
  blocks: [] # Documentos bloqueados
  relates_to: ["analise.md", "planejamento.md"] # Relacionam com análises e planejamento

# Datas (OBRIGATÓRIAS)
created_date: "2024-01-15"
last_updated: "2024-01-15"

# =============================================================================
# METADADOS OPCIONAIS (EXTENSÍVEIS)
# =============================================================================

# Prioridade da referência
priority: "high" # critical | high | medium | low

# Status atual
status: "active" # draft | review | active | deprecated | archived

# Responsável pela referência
owner: "[PREENCHER] Nome do Responsável"

# Tags para categorização
tags: ["reference", "api", "documentation"]

# Complexidade da referência
complexity: "medium" # low | medium | high | critical

# Agenda de manutenção
maintenance_schedule: "quarterly" # never | monthly | quarterly | yearly

# Tipo de referência
reference_type: "api" # api | glossary | specification | technical-doc | schema

# Nível de estabilidade
stability_level: "stable" # experimental | beta | stable | deprecated

# Audiência alvo
target_audience: "developers" # developers | admins | users | all

# Versão da API/Spec
api_version: "v1.0"

# Protocolo ou padrão
protocol: "REST" # REST | GraphQL | gRPC | WebSocket | custom

# Formato de dados
data_format: "JSON" # JSON | XML | YAML | Protobuf | custom

# Autenticação necessária
auth_required: true # true | false

# Tipo de autenticação
auth_type: "Bearer Token" # Bearer Token | API Key | OAuth | Basic Auth | None

# Rate limiting
rate_limit: "100 requests/minute"

# Disponibilidade
availability: "99.9%" # SLA de disponibilidade

# Versioning strategy
versioning_strategy: "semantic" # semantic | date-based | incremental

# Ambiente de produção
production_url: "https://api.example.com"

# Ambiente de teste
staging_url: "https://staging-api.example.com"

# Documentação interativa
interactive_docs: "https://docs.example.com"
---

<!-- CONTEXT_META
template_version: "1.0.0"
template_type: "reference"
generated_by: "context-navigator"
validation_status: "pending"
last_validated: "2024-01-15"
compliance_check: "passed"
metadata_completeness: "100%"
connection_accuracy: "pending"
context_consistency: "verified"
reference_category: "api"
specification_level: "detailed"
-->

# 📚 [TÍTULO DA REFERÊNCIA]

> **Template:** Referência | **Contexto:** [CONTEXTO] | **Módulo:** [MÓDULO]  
> **Criado:** [DATA] | **Atualizado:** [DATA] | **Status:** [STATUS]

## 📋 Metadados da Referência

**Tipo:** [API/GLOSSÁRIO/ESPECIFICAÇÃO/DOCUMENTAÇÃO TÉCNICA/SCHEMA]  
**Versão:** [VERSÃO]  
**Estabilidade:** [EXPERIMENTAL/BETA/STABLE/DEPRECATED]  
**Audiência:** [DESENVOLVEDORES/ADMINS/USUÁRIOS/TODOS]  
**Autenticação:** [SIM/NÃO]  
**Rate Limit:** [LIMITE]

## 🎯 Overview

### **Propósito**

[Descreva claramente o propósito desta referência]

### **Escopo**

[Defina o que está incluído e o que está fora do escopo]

### **Audiência Alvo**

- **Desenvolvedores:** [Descrição específica]
- **Administradores:** [Descrição específica]
- **Usuários Finais:** [Descrição específica]

### **Pré-requisitos**

- [Pré-requisito 1]
- [Pré-requisito 2]
- [Pré-requisito 3]

### **Conceitos Chave**

| Conceito     | Definição   | Exemplo   |
| ------------ | ----------- | --------- |
| [Conceito 1] | [Definição] | [Exemplo] |
| [Conceito 2] | [Definição] | [Exemplo] |
| [Conceito 3] | [Definição] | [Exemplo] |

## 🏗️ Arquitetura e Estrutura

### **Visão Geral da Arquitetura**

[Descreva a arquitetura geral do sistema/API/componente]

### **Componentes Principais**

- **Componente 1:** [Descrição e responsabilidade]
- **Componente 2:** [Descrição e responsabilidade]
- **Componente 3:** [Descrição e responsabilidade]

### **Fluxo de Dados**

[Descreva como os dados fluem através do sistema]

### **Diagramas**

```
[Inclua diagramas ASCII ou referências para diagramas externos]
```

## 🔧 Configuração e Setup

### **Instalação**

```bash
# Comando de instalação
[comando de instalação]

# Verificar instalação
[comando de verificação]
```

### **Configuração Inicial**

```yaml
# Arquivo de configuração exemplo
config:
  api_key: "your-api-key"
  base_url: "https://api.example.com"
  timeout: 30
  retries: 3
```

### **Variáveis de Ambiente**

| Variável   | Descrição           | Valor Padrão              | Obrigatório |
| ---------- | ------------------- | ------------------------- | ----------- |
| `API_KEY`  | Chave de API        | -                         | Sim         |
| `BASE_URL` | URL base            | `https://api.example.com` | Não         |
| `TIMEOUT`  | Timeout em segundos | 30                        | Não         |

## 📖 Referência Detalhada

### **Endpoints da API**

#### **GET /api/v1/resources**

**Descrição:** Listar todos os recursos

**Parâmetros:**

- `page` (integer, opcional): Número da página (padrão: 1)
- `limit` (integer, opcional): Itens por página (padrão: 10)
- `filter` (string, opcional): Filtro de busca

**Headers:**

- `Authorization: Bearer {token}` (obrigatório)
- `Content-Type: application/json`

**Exemplo de Request:**

```bash
curl -X GET "https://api.example.com/api/v1/resources?page=1&limit=10" \
  -H "Authorization: Bearer your-token" \
  -H "Content-Type: application/json"
```

**Exemplo de Response:**

```json
{
  "data": [
    {
      "id": "123",
      "name": "Resource Name",
      "type": "example",
      "created_at": "2024-01-15T10:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 100,
    "pages": 10
  }
}
```

**Códigos de Status:**

- `200 OK`: Sucesso
- `400 Bad Request`: Parâmetros inválidos
- `401 Unauthorized`: Token inválido
- `429 Too Many Requests`: Rate limit excedido
- `500 Internal Server Error`: Erro interno

---

#### **POST /api/v1/resources**

**Descrição:** Criar um novo recurso

**Parâmetros:**

- `name` (string, obrigatório): Nome do recurso
- `type` (string, obrigatório): Tipo do recurso
- `description` (string, opcional): Descrição

**Headers:**

- `Authorization: Bearer {token}` (obrigatório)
- `Content-Type: application/json`

**Exemplo de Request:**

```bash
curl -X POST "https://api.example.com/api/v1/resources" \
  -H "Authorization: Bearer your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "New Resource",
    "type": "example",
    "description": "This is a new resource"
  }'
```

**Exemplo de Response:**

```json
{
  "data": {
    "id": "124",
    "name": "New Resource",
    "type": "example",
    "description": "This is a new resource",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
}
```

**Códigos de Status:**

- `201 Created`: Recurso criado com sucesso
- `400 Bad Request`: Dados inválidos
- `401 Unauthorized`: Token inválido
- `409 Conflict`: Recurso já existe
- `422 Unprocessable Entity`: Dados não processáveis

### **Schemas de Dados**

#### **Resource Schema**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Identificador único do recurso"
    },
    "name": {
      "type": "string",
      "description": "Nome do recurso",
      "maxLength": 255
    },
    "type": {
      "type": "string",
      "enum": ["example", "sample", "demo"],
      "description": "Tipo do recurso"
    },
    "description": {
      "type": "string",
      "description": "Descrição detalhada",
      "maxLength": 1000
    },
    "created_at": {
      "type": "string",
      "format": "date-time",
      "description": "Data de criação"
    },
    "updated_at": {
      "type": "string",
      "format": "date-time",
      "description": "Data de atualização"
    }
  },
  "required": ["id", "name", "type", "created_at", "updated_at"]
}
```

#### **Error Schema**

```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "object",
      "properties": {
        "code": {
          "type": "integer",
          "description": "Código de erro HTTP"
        },
        "message": {
          "type": "string",
          "description": "Mensagem de erro"
        },
        "details": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Detalhes adicionais do erro"
        }
      },
      "required": ["code", "message"]
    }
  },
  "required": ["error"]
}
```

## 💡 Exemplos Práticos

### **Exemplo 1: Listar Recursos com Filtro**

```javascript
// JavaScript/Node.js
const axios = require("axios");

async function listResources(filter = "") {
  try {
    const response = await axios.get(
      "https://api.example.com/api/v1/resources",
      {
        params: {
          filter: filter,
          limit: 20,
        },
        headers: {
          Authorization: `Bearer ${process.env.API_TOKEN}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data;
  } catch (error) {
    console.error("Erro ao listar recursos:", error.response?.data);
    throw error;
  }
}

// Uso
listResources("example").then((data) => {
  console.log("Recursos encontrados:", data.data.length);
});
```

### **Exemplo 2: Criar Recurso com Validação**

```python
# Python
import requests
import json

def create_resource(name, resource_type, description=None):
    url = "https://api.example.com/api/v1/resources"

    payload = {
        "name": name,
        "type": resource_type
    }

    if description:
        payload["description"] = description

    headers = {
        "Authorization": f"Bearer {os.environ.get('API_TOKEN')}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao criar recurso: {e}")
        raise

# Uso
resource = create_resource("My Resource", "example", "Description")
print(f"Recurso criado com ID: {resource['data']['id']}")
```

### **Exemplo 3: Tratamento de Erros**

```php
<?php
// PHP
function makeApiRequest($method, $endpoint, $data = null) {
    $url = "https://api.example.com/api/v1/" . $endpoint;

    $options = [
        'http' => [
            'method' => $method,
            'header' => [
                'Authorization: Bearer ' . $_ENV['API_TOKEN'],
                'Content-Type: application/json'
            ]
        ]
    ];

    if ($data) {
        $options['http']['content'] = json_encode($data);
    }

    $context = stream_context_create($options);
    $result = file_get_contents($url, false, $context);

    if ($result === FALSE) {
        $error = error_get_last();
        throw new Exception("API request failed: " . $error['message']);
    }

    return json_decode($result, true);
}

// Uso com tratamento de erro
try {
    $resources = makeApiRequest('GET', 'resources');
    echo "Success: " . count($resources['data']) . " resources found\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```

## 🔍 Casos de Uso Comuns

### **Caso de Uso 1: Integração Básica**

**Cenário:** Aplicação web precisa listar e criar recursos

**Implementação:**

1. Configurar autenticação
2. Implementar listagem com paginação
3. Implementar criação com validação
4. Tratar erros adequadamente

**Código exemplo:** [Ver Exemplo 1 e 2 acima]

### **Caso de Uso 2: Sincronização de Dados**

**Cenário:** Sistema precisa sincronizar dados periodicamente

**Implementação:**

1. Implementar polling com intervalo adequado
2. Usar filtros para dados incrementais
3. Implementar retry logic
4. Monitorar rate limits

### **Caso de Uso 3: Webhook Integration**

**Cenário:** Receber notificações em tempo real

**Implementação:**

1. Configurar endpoint para webhooks
2. Validar assinaturas
3. Processar eventos assincronamente
4. Implementar idempotência

## 📊 Limites e Restrições

### **Rate Limiting**

- **Requests por minuto:** 100
- **Requests por hora:** 5,000
- **Requests por dia:** 100,000

### **Tamanhos Máximos**

- **Request body:** 10MB
- **Nome do recurso:** 255 caracteres
- **Descrição:** 1,000 caracteres

### **Limitações Funcionais**

- Máximo 1,000 recursos por página
- Histórico mantido por 90 dias
- Busca limitada a 100 caracteres

## 🔒 Segurança

### **Autenticação**

- **Tipo:** Bearer Token
- **Header:** `Authorization: Bearer {token}`
- **Validade:** 24 horas
- **Renovação:** Automática

### **Autorização**

- **Roles:** admin, user, readonly
- **Permissions:** read, write, delete
- **Scope:** resource-level

### **Boas Práticas**

- Sempre usar HTTPS
- Validar todos os inputs
- Implementar rate limiting
- Monitorar tentativas de acesso

## 📈 Monitoramento e Métricas

### **Métricas Disponíveis**

- **Response time:** média, p95, p99
- **Error rate:** por endpoint
- **Throughput:** requests por segundo
- **Availability:** uptime percentage

### **Health Check**

```bash
curl -X GET "https://api.example.com/health" \
  -H "Content-Type: application/json"
```

### **Status Page**

- **URL:** https://status.example.com
- **Histórico:** 90 dias
- **Notificações:** email, webhook

## 🔄 Versionamento

### **Estratégia de Versionamento**

- **Semântico:** v1.0.0
- **URL:** /api/v1/
- **Headers:** `API-Version: 1.0`

### **Compatibilidade**

- **Backward compatible:** mudanças menores
- **Breaking changes:** nova versão major
- **Deprecated:** 6 meses de aviso

### **Migração**

- **Guias de migração:** disponíveis
- **Ferramentas:** scripts automatizados
- **Suporte:** durante período de transição

## 📚 Recursos Adicionais

### **Documentação Relacionada**

- [Guia de Introdução] - [Link]
- [Tutorial Avançado] - [Link]
- [Referência Completa] - [Link]

### **Ferramentas Úteis**

- **Postman Collection:** [Link]
- **OpenAPI Spec:** [Link]
- **SDK Oficial:** [Link]

### **Comunidade e Suporte**

- **Forum:** [Link]
- **GitHub:** [Link]
- **Stack Overflow:** [Tag]

### **Changelog**

| Versão | Data       | Mudanças       |
| ------ | ---------- | -------------- |
| v1.0.0 | 2024-01-15 | Versão inicial |

---

<!-- VALIDATION_CHECKLIST
[ ] Todos os metadados obrigatórios preenchidos
[ ] Overview claro e completo
[ ] Arquitetura bem documentada
[ ] Configuração e setup detalhados
[ ] Referência detalhada com exemplos
[ ] Schemas de dados definidos
[ ] Exemplos práticos funcionais
[ ] Casos de uso documentados
[ ] Limites e restrições claros
[ ] Segurança adequadamente documentada
[ ] Monitoramento e métricas incluídos
[ ] Versionamento definido
[ ] Recursos adicionais listados
[ ] Conexões com outros documentos mapeadas
-->

<!-- SCANNER_INSTRUCTIONS
Este template de referência deve ser usado para:
- Documentação de APIs REST/GraphQL
- Especificações técnicas
- Glossários de termos
- Documentação de bibliotecas
- Referências de configuração
- Schemas de dados

Campos obrigatórios para o scanner:
- doc_type: "reference"
- title: Título da referência
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
- Validar se há seções de overview, referência e exemplos
- Verificar se há pelo menos um exemplo prático
- Validar se há informações de versionamento
-->

<!-- CONTEXT_CONNECTIONS
Este documento se conecta com:
- Documentos de decisão (decision) via "depends_on"
- Documentos de arquitetura (architecture) via "references"
- Documentos de processo (process) via "relates_to"
- Outros documentos de referência (reference) via "relates_to"

Padrões de conexão:
- [[nome-do-documento]] para referências diretas
- {{nome-do-componente}} para componentes
- @contexto para referências de contexto
- /api/v1/endpoint para endpoints
- https://url para recursos externos
-->
