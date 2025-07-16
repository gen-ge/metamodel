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
  depends_on: ["workspace.yml", "context.rule"]
  relates_to: ["templates/", "examples/", "WorkspaceManager"]
created_date: "2024-01-15"
last_updated: "2025-07-12"
owner: "Context Navigator Team"
tags: ["manual", "documentation", "ai-protocol", "reference", "2.0"]
complexity: "critical"
maintenance_schedule: "quarterly"
stakeholders: ["ai-systems", "developers", "documentation-team"]
architectural_impact: "critical"
version: "2.0"
---

# 🤖 Context Navigator 2.0 - Manual da IA

## 🎯 Protocolo de Inicialização Obrigatório 2.0

**ANTES DE QUALQUER RESPOSTA, SEMPRE EXECUTE:**

```
1. CARREGAR context.rule (lei sagrada)
2. DETECTAR workspace via WorkspaceManager (.cn_model/)
3. CARREGAR .cn_model/maps/index.yml (contexto atual)
4. IDENTIFICAR template apropriado
5. VALIDAR contexto da requisição
6. APLICAR protocolos específicos
```

**NUNCA responda sem este protocolo completo.**

---

## 📋 Índice Técnico

1. [**Protocolos de Inicialização 2.0**](#protocolos-de-inicialização-20)
2. [**WorkspaceManager Detection**](#workspacemanager-detection)
3. [**Interpretação de Templates**](#interpretação-de-templates)
4. [**Análise de Contexto**](#análise-de-contexto)
5. [**Geração de Conteúdo**](#geração-de-conteúdo)
6. [**Validação Automática**](#validação-automática)
7. [**Componentização Code Bridge**](#componentização-code-bridge)
8. [**Casos Especiais 2.0**](#casos-especiais-20)
9. [**Limites e Restrições**](#limites-e-restrições)
10. [**Referência Técnica 2.0**](#referência-técnica-20)

---

## 🚀 Protocolos de Inicialização 2.0

### **Protocolo 1: Carregamento de Context.rule (Inalterado)**

```yaml
SEMPRE executar:
1. Localizar context.rule
2. Carregar conteúdo completo
3. Aplicar todas as regras
4. Confirmar carregamento
```

### **Protocolo 2: WorkspaceManager Detection (NOVO)**

```yaml
SEMPRE executar detecção de workspace:
1. Verificar .cn_model/workspace.yml (diretório atual)
2. Verificar ../.cn_model/workspace.yml (diretórios pais, recursivo)
3. Verificar ~/.local/share/context-navigator/ (instalação global)
4. Verificar ~/.context-navigator/ (fallback compatibilidade 1.0)
5. Confirmar workspace detectado
```

#### **Estrutura Esperada do Workspace 2.0:**

```yaml
# .cn_model/workspace.yml
workspace:
  name: "projeto-exemplo"
  version: "2.0"
  type: "local"

configuration:
  methodology:
    name: "Context Navigator"
    version: "2.0"

paths:
  documents: "docs/"
  components: ".cn_model/components/"
  templates: ".cn_model/templates/"
  maps: ".cn_model/maps/"
```

#### **Ações Obrigatórias:**

- ✅ Detectar workspace via WorkspaceManager
- ✅ Carregar configuração do workspace
- ✅ Verificar estrutura .cn_model/
- ✅ Confirmar templates disponíveis

### **Protocolo 3: Carregamento de Context Maps 2.0**

```yaml
SEMPRE carregar (nova estrutura):
1. .cn_model/maps/index.yml (índice geral)
2. .cn_model/maps/connections.yml (conexões)
3. .cn_model/maps/conflicts.yml (conflitos)
4. .cn_model/maps/architecture.yml (arquitetura)
```

#### **Estrutura Esperada do Index.yml 2.0:**

```yaml
# .cn_model/maps/index.yml
scan_timestamp: "2024-01-15T10:30:00Z"
workspace_path: "/projeto/.cn_model/"
total_documents: 15
document_summary:
  "docs/decisions/auth-choice.md":
    type: "decision"
    context_level: "c2_module"
    context_type: "core"
    module: "authentication"
    connections:
      references: ["docs/references/auth-api.md"]
      impacts: ["docs/processes/auth-setup.md"]
```

---

## 🔍 WorkspaceManager Detection

### **Protocolo de Detecção Automática**

#### **Hierarquia de Busca (Obrigatória):**

```yaml
1. Workspace Local:
   - ./.cn_model/workspace.yml
   - ../.cn_model/workspace.yml
   - ../../.cn_model/workspace.yml
   (recursivo até raiz do sistema)

2. Instalação Global:
   - ~/.local/share/context-navigator/
   - ~/.local/share/context-navigator/global_workspace.yml

3. Compatibilidade (Fallback):
   - ~/.context-navigator/
   (suporte para arquitetura 1.0)
```

#### **Validação de Workspace:**

```yaml
SEMPRE verificar:
1. Arquivo workspace.yml existe
2. Estrutura de pastas correta
3. Permissões de leitura/escrita
4. Templates disponíveis
```

### **Estrutura de Workspace 2.0**

```yaml
# Estrutura obrigatória
.cn_model/
├── workspace.yml              # Configuração principal
├── components/                # Componentes documentados
│   ├── user-auth.yml         # Componente exemplo
│   └── payment-api.yml       # Componente exemplo
├── templates/                 # Templates personalizados (opcional)
│   ├── custom-decision.md    # Template customizado
│   └── custom-process.md     # Template customizado
└── maps/                     # Mapas contextuais
    ├── index.yml            # Índice principal
    ├── connections.yml      # Conexões entre documentos
    ├── conflicts.yml        # Conflitos detectados
    └── architecture.yml     # Visão arquitetural
```

---

## 📝 Interpretação de Templates (Inalterada)

### **Templates Básicos Mantidos**

Todos os templates permanecem exatamente iguais à versão 1.0:

- **DECISÃO**: Estrutura e validações inalteradas
- **PROCESSO**: Estrutura e validações inalteradas
- **REFERÊNCIA**: Estrutura e validações inalteradas
- **ARQUITETURA**: Estrutura e validações inalteradas
- **ANÁLISE**: Estrutura e validações inalteradas
- **PLANEJAMENTO**: Estrutura e validações inalteradas

### **Acesso a Templates 2.0**

```yaml
# Prioridade de busca para templates:
1. .cn_model/templates/ (templates personalizados)
2. ~/.local/share/context-navigator/templates/ (templates globais)
3. Templates embutidos no sistema (fallback)
```

---

## 🧩 Componentização Code Bridge

### **Protocolo Code Bridge (@cn:)**

#### **Marcações Obrigatórias:**

```python
# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component nome-componente
# @cn:doc arquivo-documentacao.md
# @cn:context-level c1_root|c2_module|c3_component
# @cn:context-type core|api|data|ui|infra|shared
# @cn:purpose "Descrição clara do propósito"
# @cn:memory-aid "Lembrete para humanos e IA"
# ============================================
```

#### **Campos Opcionais Code Bridge:**

```python
# @cn:depends-on doc1.md, doc2.md
# @cn:impacts componente1, modulo2
# @cn:uses ferramenta1, biblioteca2
# @cn:provides funcionalidade1, api2
# @cn:owner nome-responsavel
# @cn:last-updated 2025-01-13
# @cn:status active|deprecated|experimental
```

### **Integração com Documentação**

```yaml
SEMPRE que encontrar marcações @cn::
1. Extrair informações de componente
2. Verificar se documento referenciado existe
3. Validar consistência hierárquica
4. Registrar em .cn_model/components/
5. Atualizar mapas de conexão
```

---

## 🎯 Casos Especiais 2.0

### **Caso 1: Workspace Não Detectado**

```yaml
SITUAÇÃO: WorkspaceManager não encontra .cn_model/
AÇÃO:
1. Informar que workspace não foi detectado
2. Sugerir inicialização com cn init
3. Oferecer uso de templates globais
4. Documentar que salvará em instalação global
```

### **Caso 2: Migração 1.0 → 2.0**

```yaml
SITUAÇÃO: Encontrar .contextrc e .context-map/
AÇÃO:
1. Detectar arquitetura 1.0
2. Informar sobre migração disponível
3. Sugerir comandos de migração
4. Manter compatibilidade temporária
```

### **Caso 3: Templates Personalizados**

```yaml
SITUAÇÃO: Templates em .cn_model/templates/
AÇÃO:
1. Priorizar templates personalizados
2. Validar estrutura do template customizado
3. Aplicar validações básicas
4. Documentar uso de template personalizado
```

### **Caso 4: Componentização Incompleta**

```yaml
SITUAÇÃO: Código com @cn: parcial
AÇÃO:
1. Identificar campos ausentes
2. Solicitar campos obrigatórios
3. Sugerir documento de referência
4. Oferecer criação automática de doc
```

---

## 🚫 Limites e Restrições 2.0

### **O que NUNCA fazer:**

#### **Workspace:**

- ❌ NUNCA assumir localização de workspace
- ❌ NUNCA salvar em .context-map/ (arquitetura 1.0)
- ❌ NUNCA ignorar detecção de WorkspaceManager
- ❌ NUNCA misturar estruturas 1.0 e 2.0

#### **Componentização:**

- ❌ NUNCA criar marcações @cn: incompletas
- ❌ NUNCA referenciar documentos inexistentes
- ❌ NUNCA omitir purpose e memory-aid
- ❌ NUNCA usar context-level inconsistente

#### **Saves e Estrutura:**

- ❌ NUNCA salvar em pastas erradas
- ❌ NUNCA criar estrutura 1.0 em ambiente 2.0
- ❌ NUNCA ignorar workspace.yml
- ❌ NUNCA misturar configurações

---

## 📊 Referência Técnica 2.0

### **Estrutura de Workspace**

```yaml
# .cn_model/workspace.yml (obrigatório)
workspace:
  name: String
  version: "2.0"
  type: "local|global"
  created: YYYY-MM-DD
  last_updated: YYYY-MM-DD

configuration:
  methodology:
    name: "Context Navigator"
    version: "2.0"
  templates:
    source: "global|local|mixed"
  validation:
    strict_mode: true
    auto_scan: true

paths:
  documents: "docs/"
  components: ".cn_model/components/"
  templates: ".cn_model/templates/"
  maps: ".cn_model/maps/"
  cache: ".cn_model/cache/"
```

### **Mapeamento de Componentes**

```yaml
# .cn_model/components/exemplo.yml
component:
  name: "user-authentication"
  file_path: "src/auth/UserAuthenticator.py"
  documentation: "docs/decisions/auth-architecture.md"
  context_level: "c2_module"
  context_type: "core"
  purpose: "Sistema de autenticação de usuários"
  memory_aid: "Autenticador principal com JWT e refresh tokens"

dependencies:
  code:
    - "src/utils/JWTHelper.py"
    - "src/models/User.py"
  documentation:
    - "docs/references/auth-api.md"
    - "docs/processes/auth-setup.md"

metadata:
  owner: "auth-team"
  last_updated: "2025-01-13"
  status: "active"
  complexity: "medium"
```

### **Scripts e WorkspaceManager**

```yaml
# Todos os scripts devem usar WorkspaceManager
from core.workspace_manager import WorkspaceManager

def script_function():
    # OBRIGATÓRIO: Detectar workspace primeiro
    workspace_manager = WorkspaceManager()
    workspace_path = workspace_manager.detect_workspace()

    if not workspace_path:
        print("❌ Nenhum workspace detectado")
        return

    # Processar com workspace
    process_with_workspace(workspace_path)
```

---

## 🎯 Protocolo de Resposta Final 2.0

### **Antes de Enviar Resposta:**

#### **Checklist Obrigatório 2.0:**

```yaml
✅ context.rule carregado e aplicado
✅ Workspace detectado via WorkspaceManager
✅ Context maps (.cn_model/maps/) analisados
✅ Template correto identificado
✅ Estrutura obrigatória seguida
✅ Metadados completos
✅ Conteúdo validado
✅ Conexões verificadas
✅ Componentização considerada
✅ Qualidade confirmada
```

#### **Formato da Resposta 2.0:**

```markdown
## [Confirmação de Protocolo 2.0]

✅ context.rule: CARREGADO
✅ workspace: DETECTADO (.cn_model/)
✅ workspace-manager: FUNCIONANDO
✅ context-maps: ANALISADOS
✅ template: [TIPO_IDENTIFICADO]
✅ validação: APROVADA

## [Conteúdo Principal]

[Documento gerado seguindo template]

## [Validação Final 2.0]

- Estrutura: ✅ COMPLETA
- Metadados: ✅ VÁLIDOS
- Workspace: ✅ .cn_model/ DETECTADO
- Conteúdo: ✅ ADEQUADO
- Conexões: ✅ VERIFICADAS
- Componentização: ✅ CONSIDERADA
- Qualidade: ✅ SCORE [X.X]
```

### **Nunca Responder Sem:**

- ❌ Carregar context.rule
- ❌ Detectar workspace via WorkspaceManager
- ❌ Analisar context maps em .cn_model/
- ❌ Identificar template
- ❌ Validar resultado
- ❌ Confirmar qualidade

---

**🤖 Este manual é sua referência técnica completa para Context Navigator 2.0. Siga todos os protocolos rigorosamente com WorkspaceManager e componentização.**

_Context Navigator 2.0: Onde disciplina metodológica encontra inteligência artificial avançada._
