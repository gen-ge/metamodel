---
doc_type: "reference"
context_level: "c3_component"
context_type: "api"
module: "user-management"
priority: "medium"
status: "active"
connections:
  references: ["authentication-decision.md", "database-schema.md"]
  impacts: ["frontend-integration.md", "mobile-app-integration.md"]
  depends_on: ["user-model-design.md"]
  blocks: []
  relates_to: ["auth-api-reference.md", "profile-api-reference.md"]
created_date: "2024-01-15"
last_updated: "2024-01-15"
owner: "API Team"
---

# User API Reference

## Overview

### Propósito

Fornecer documentação completa da API de gerenciamento de usuários, incluindo endpoints para criação, consulta, atualização e exclusão de usuários do sistema.

### Escopo

Esta API cobre:

- Operações CRUD de usuários
- Gerenciamento de perfis
- Consultas e filtros avançados
- Upload de avatares
- Ativação/desativação de contas

**Não cobre:**

- Autenticação (ver auth-api-reference.md)
- Autorização e permissões
- Notificações de usuário

### Audiência Alvo

- **Desenvolvedores Frontend:** Integração com interfaces web
- **Desenvolvedores Mobile:** Integração com apps móveis
- **Desenvolvedores Backend:** Integração entre serviços
- **QA Engineers:** Testes automatizados de API

## Configuração e Setup

### Instalação

```bash
# Instalar cliente da API (opcional)
npm install @company/user-api-client

# Ou usar curl/fetch diretamente
# Base URL: https://api.company.com/v1
```

### Configuração Inicial

```javascript
// Node.js
const UserAPI = require("@company/user-api-client");
const client = new UserAPI({
  baseURL: "https://api.company.com/v1",
  apiKey: process.env.API_KEY,
  timeout: 30000,
});

// JavaScript (Browser)
const userAPI = new UserAPIClient({
  baseURL: "https://api.company.com/v1",
  token: localStorage.getItem("auth_token"),
});
```

### Dependências

- **Autenticação:** Token JWT obrigatório
- **Rate Limiting:** 1000 requests/hora por usuário
- **HTTPS:** Obrigatório em produção
- **Content-Type:** application/json

## Referência Detalhada

### Endpoint: GET /users

**Descrição:** Lista usuários com filtros e paginação

#### **Parâmetros:**

| Parâmetro | Tipo    | Obrigatório | Descrição                                     |
| --------- | ------- | ----------- | --------------------------------------------- |
| page      | integer | Não         | Número da página (default: 1)                 |
| limit     | integer | Não         | Items por página (default: 20, max: 100)      |
| status    | string  | Não         | Filtro por status: active, inactive, pending  |
| search    | string  | Não         | Busca por nome ou email                       |
| sort      | string  | Não         | Campo para ordenação: name, email, created_at |
| order     | string  | Não         | Direção: asc, desc (default: asc)             |

#### **Resposta:**

**Status:** 200 OK

```json
{
  "data": [
    {
      "id": "usr_123456789",
      "email": "john.doe@example.com",
      "name": "John Doe",
      "avatar": "https://cdn.company.com/avatars/123456789.jpg",
      "status": "active",
      "role": "user",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z",
      "last_login": "2024-01-15T14:22:00Z"
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 10,
    "total_items": 200,
    "items_per_page": 20,
    "has_next": true,
    "has_previous": false
  }
}
```

### Endpoint: GET /users/{id}

**Descrição:** Busca usuário específico por ID

#### **Parâmetros:**

| Parâmetro | Tipo   | Obrigatório | Descrição           |
| --------- | ------ | ----------- | ------------------- |
| id        | string | Sim         | ID único do usuário |

#### **Resposta:**

**Status:** 200 OK

```json
{
  "data": {
    "id": "usr_123456789",
    "email": "john.doe@example.com",
    "name": "John Doe",
    "first_name": "John",
    "last_name": "Doe",
    "avatar": "https://cdn.company.com/avatars/123456789.jpg",
    "status": "active",
    "role": "user",
    "phone": "+55 11 99999-9999",
    "address": {
      "street": "Rua das Flores, 123",
      "city": "São Paulo",
      "state": "SP",
      "zip_code": "01234-567",
      "country": "BR"
    },
    "preferences": {
      "language": "pt-BR",
      "timezone": "America/Sao_Paulo",
      "notifications": {
        "email": true,
        "push": false,
        "sms": true
      }
    },
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z",
    "last_login": "2024-01-15T14:22:00Z"
  }
}
```

### Endpoint: POST /users

**Descrição:** Cria novo usuário

#### **Parâmetros (Body):**

```json
{
  "email": "string (required)",
  "name": "string (required)",
  "password": "string (required, min: 8 chars)",
  "phone": "string (optional)",
  "role": "string (optional, default: user)",
  "address": {
    "street": "string (optional)",
    "city": "string (optional)",
    "state": "string (optional)",
    "zip_code": "string (optional)",
    "country": "string (optional)"
  },
  "preferences": {
    "language": "string (optional, default: pt-BR)",
    "timezone": "string (optional)",
    "notifications": {
      "email": "boolean (optional, default: true)",
      "push": "boolean (optional, default: true)",
      "sms": "boolean (optional, default: false)"
    }
  }
}
```

#### **Resposta:**

**Status:** 201 Created

```json
{
  "data": {
    "id": "usr_987654321",
    "email": "jane.smith@example.com",
    "name": "Jane Smith",
    "status": "pending",
    "role": "user",
    "created_at": "2024-01-15T15:45:00Z"
  },
  "message": "User created successfully. Verification email sent."
}
```

### Endpoint: PUT /users/{id}

**Descrição:** Atualiza usuário existente

#### **Parâmetros:**

| Parâmetro | Tipo   | Obrigatório | Descrição           |
| --------- | ------ | ----------- | ------------------- |
| id        | string | Sim         | ID único do usuário |

#### **Parâmetros (Body):**

```json
{
  "name": "string (optional)",
  "phone": "string (optional)",
  "address": {
    "street": "string (optional)",
    "city": "string (optional)",
    "state": "string (optional)",
    "zip_code": "string (optional)",
    "country": "string (optional)"
  },
  "preferences": {
    "language": "string (optional)",
    "timezone": "string (optional)",
    "notifications": {
      "email": "boolean (optional)",
      "push": "boolean (optional)",
      "sms": "boolean (optional)"
    }
  }
}
```

#### **Resposta:**

**Status:** 200 OK

```json
{
  "data": {
    "id": "usr_123456789",
    "email": "john.doe@example.com",
    "name": "John Updated Name",
    "updated_at": "2024-01-15T16:20:00Z"
  },
  "message": "User updated successfully."
}
```

### Endpoint: DELETE /users/{id}

**Descrição:** Remove usuário do sistema (soft delete)

#### **Parâmetros:**

| Parâmetro | Tipo   | Obrigatório | Descrição           |
| --------- | ------ | ----------- | ------------------- |
| id        | string | Sim         | ID único do usuário |

#### **Resposta:**

**Status:** 200 OK

```json
{
  "message": "User deleted successfully.",
  "data": {
    "id": "usr_123456789",
    "status": "deleted",
    "deleted_at": "2024-01-15T17:10:00Z"
  }
}
```

### Endpoint: POST /users/{id}/avatar

**Descrição:** Upload de avatar do usuário

#### **Parâmetros:**

| Parâmetro | Tipo   | Obrigatório | Descrição                                             |
| --------- | ------ | ----------- | ----------------------------------------------------- |
| id        | string | Sim         | ID único do usuário                                   |
| avatar    | file   | Sim         | Arquivo de imagem (max: 5MB, formatos: jpg, png, gif) |

#### **Content-Type:** multipart/form-data

#### **Resposta:**

**Status:** 200 OK

```json
{
  "data": {
    "avatar_url": "https://cdn.company.com/avatars/123456789_new.jpg",
    "uploaded_at": "2024-01-15T18:30:00Z"
  },
  "message": "Avatar uploaded successfully."
}
```

## Exemplos Práticos

### Exemplo 1: Buscar Lista de Usuários Ativos

```javascript
// JavaScript/Node.js
async function getActiveUsers() {
  try {
    const response = await fetch('https://api.company.com/v1/users?status=active&limit=50', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });

    const data = await response.json();
    console.log('Active users:', data.data);
    return data;
  } catch (error) {
    console.error('Error fetching users:', error);
  }
}

// Resultado esperado
{
  "data": [...],
  "pagination": {
    "current_page": 1,
    "total_pages": 3,
    "total_items": 127,
    "items_per_page": 50
  }
}
```

```python
# Python
import requests

def get_active_users(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(
        'https://api.company.com/v1/users',
        headers=headers,
        params={'status': 'active', 'limit': 50}
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'API Error: {response.status_code}')

# Uso
users = get_active_users('your_token_here')
print(f"Found {len(users['data'])} active users")
```

```php
// PHP
function getActiveUsers($token) {
    $ch = curl_init();

    curl_setopt_array($ch, [
        CURLOPT_URL => 'https://api.company.com/v1/users?status=active&limit=50',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => [
            'Authorization: Bearer ' . $token,
            'Content-Type: application/json'
        ]
    ]);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode === 200) {
        return json_decode($response, true);
    }

    throw new Exception("API Error: $httpCode");
}

// Uso
$users = getActiveUsers('your_token_here');
echo "Found " . count($users['data']) . " active users\n";
```

### Exemplo 2: Criar Novo Usuário

```javascript
// JavaScript/Node.js
async function createUser(userData) {
  try {
    const response = await fetch("https://api.company.com/v1/users", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: userData.email,
        name: userData.name,
        password: userData.password,
        phone: userData.phone,
        address: {
          street: userData.address.street,
          city: userData.address.city,
          state: userData.address.state,
          zip_code: userData.address.zipCode,
          country: "BR",
        },
        preferences: {
          language: "pt-BR",
          timezone: "America/Sao_Paulo",
          notifications: {
            email: true,
            push: true,
            sms: false,
          },
        },
      }),
    });

    const data = await response.json();

    if (response.status === 201) {
      console.log("User created:", data.data);
      return data;
    } else {
      throw new Error(data.message);
    }
  } catch (error) {
    console.error("Error creating user:", error);
  }
}

// Uso
const newUser = await createUser({
  email: "maria.silva@example.com",
  name: "Maria Silva",
  password: "securePassword123",
  phone: "+55 11 98765-4321",
  address: {
    street: "Av. Paulista, 1000",
    city: "São Paulo",
    state: "SP",
    zipCode: "01310-100",
  },
});
```

### Exemplo 3: Upload de Avatar

```javascript
// JavaScript (Browser)
async function uploadAvatar(userId, fileInput) {
  const formData = new FormData();
  formData.append('avatar', fileInput.files[0]);

  try {
    const response = await fetch(`https://api.company.com/v1/users/${userId}/avatar`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`
        // Não definir Content-Type para multipart/form-data
      },
      body: formData
    });

    const data = await response.json();

    if (response.ok) {
      console.log('Avatar uploaded:', data.data.avatar_url);
      return data.data.avatar_url;
    } else {
      throw new Error(data.message);
    }
  } catch (error) {
    console.error('Error uploading avatar:', error);
  }
}

// HTML
<input type="file" id="avatar" accept="image/*" />
<button onclick="uploadAvatar('usr_123456789', document.getElementById('avatar'))">
  Upload Avatar
</button>
```

## Códigos de Resposta HTTP

| Código | Descrição             | Quando Ocorre                              |
| ------ | --------------------- | ------------------------------------------ |
| 200    | OK                    | Operação realizada com sucesso             |
| 201    | Created               | Recurso criado com sucesso                 |
| 400    | Bad Request           | Dados inválidos ou ausentes                |
| 401    | Unauthorized          | Token inválido ou ausente                  |
| 403    | Forbidden             | Sem permissão para acessar recurso         |
| 404    | Not Found             | Usuário não encontrado                     |
| 409    | Conflict              | Email já cadastrado                        |
| 422    | Unprocessable Entity  | Dados válidos mas regra de negócio violada |
| 429    | Too Many Requests     | Rate limit excedido                        |
| 500    | Internal Server Error | Erro interno do servidor                   |

## Estrutura de Erros

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "message": "Email is required"
      },
      {
        "field": "password",
        "message": "Password must be at least 8 characters"
      }
    ]
  }
}
```

## Rate Limiting

- **Limite:** 1000 requests por hora por usuário autenticado
- **Headers de resposta:**
  - `X-RateLimit-Limit`: Limite total
  - `X-RateLimit-Remaining`: Requests restantes
  - `X-RateLimit-Reset`: Timestamp de reset do limite

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1642265400
```

## Versionamento

### Versão Atual

- **v1.2.4** (Estável)
- Lançada em: 15/01/2024
- Suportada até: 15/01/2025

### Histórico de Mudanças

#### v1.2.4 (15/01/2024)

- Adicionado campo `phone` para usuários
- Melhorias na validação de email
- Correção de bug no upload de avatar

#### v1.2.3 (10/01/2024)

- Adicionado suporte a soft delete
- Melhorias na paginação
- Otimizações de performance

#### v1.2.2 (05/01/2024)

- Adicionado endpoint de upload de avatar
- Correções de segurança
- Melhorias na documentação

### Compatibilidade

- **Backward Compatible:** Sim, com v1.2.x
- **Breaking Changes:** Nenhuma desde v1.2.0
- **Depreciações:** Endpoint `/users/bulk` será removido em v1.3.0

### Migração

Para migrar para versões futuras:

1. Verificar changelog detalhado
2. Testar em ambiente de staging
3. Atualizar código conforme breaking changes
4. Deployar em produção

---

**API User Management v1.2.4 - Documentação completa e atualizada.**
