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
  depends_on: ["workspace.yml", "context.rule"]
  relates_to: ["templates/", "examples/", "WorkspaceManager"]
created_date: "2024-01-15"
last_updated: "2025-07-12"
owner: "Context Navigator Team"
tags: ["manual", "documentation", "human-operator", "reference", "2.0"]
complexity: "high"
maintenance_schedule: "quarterly"
stakeholders: ["developers", "documentation-team"]
architectural_impact: "high"
version: "2.0"
---

# 📖 Context Navigator 2.0 - Manual do Operador Humano

## 🎯 Bem-vindo ao Context Navigator 2.0

O **Context Navigator 2.0** é uma metodologia avançada de parceria humano-IA que revoluciona como você documenta e mantém contexto em projetos complexos. Com **WorkspaceManager**, **busca inteligente** e **componentização**, este manual o guiará através de cada aspecto da metodologia.

---

## 📋 Índice

1. [**Fundamentos 2.0**](#fundamentos-20)
2. [**Instalação Global**](#instalação-global)
3. [**Fluxo de Trabalho 2.0**](#fluxo-de-trabalho-20)
4. [**Templates Detalhados**](#templates-detalhados)
5. [**Scripts Especializados**](#scripts-especializados)
6. [**Melhores Práticas 2.0**](#melhores-práticas-20)
7. [**Casos de Uso Práticos**](#casos-de-uso-práticos)
8. [**Troubleshooting 2.0**](#troubleshooting-20)
9. [**Manutenção e Evolução**](#manutenção-e-evolução)
10. [**Referência Rápida 2.0**](#referência-rápida-20)

---

## 🧠 Fundamentos 2.0

### **O que é Context Navigator 2.0?**

Context Navigator 2.0 é uma **metodologia inteligente** que:

- **🧠 WorkspaceManager**: Busca automática de workspaces
- **🔍 Busca inteligente**: Funciona de qualquer diretório
- **🧩 Componentização**: Conecta documentação ↔ código
- **📋 Templates estruturados**: Padronização automática
- **⚡ Validação em tempo real**: Detecta problemas instantaneamente
- **🌐 Comando global**: `cn` disponível em qualquer lugar

### **Princípios Fundamentais 2.0**

#### **1. Lei Sagrada para IA (Atualizada)**

```
TODA interação com IA deve começar carregando:
1. context.rule (regras metodológicas)
2. .cn_model/maps/index.yml (contexto atual via WorkspaceManager)
3. Validação de template apropriado
4. Workspace detectado automaticamente
```

#### **2. Metadados Imutáveis (Inalterados)**

```yaml
# Campos que NUNCA mudam
doc_type: "decision|process|reference|architecture|analysis|planning"
context_level: "c1_root|c2_module|c3_component"
context_type: "infra|shared|core|api|data|ui"
```

#### **3. Conexões Explícitas (Inalteradas)**

```yaml
connections:
  references: ["doc1.md", "doc2.md"]
  impacts: ["doc3.md"]
  depends_on: ["doc4.md"]
  blocks: ["doc5.md"]
  relates_to: ["doc6.md"]
```

#### **4. Workspace Inteligente (Arquitetura 2.0)**

```
projeto/                          # Qualquer projeto
├── .cn_model/                   # Workspace Context Navigator 2.0
│   ├── workspace.yml           # Configuração (substitui .contextrc)
│   ├── components/             # Componentes documentados
│   ├── templates/              # Templates personalizados
│   └── maps/                   # Mapas contextuais (substitui .context-map/)
│       ├── index.yml          # Índice principal
│       ├── connections.yml    # Conexões
│       └── conflicts.yml      # Conflitos
├── docs/                       # Documentação do projeto
└── src/                        # Código fonte (com marcações @cn:)
```

---

## 🚀 Instalação Global

### **Instalação Única Recomendada (2.0)**

```bash
# 1. Instalação global automatizada
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# 2. Configurar PATH (uma única vez)
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# 3. Usar de qualquer lugar
cn help
```

### **Verificação da Instalação**

```bash
# Verificar se comando global funciona
which cn

# Testar funcionalidade básica
cn init    # Inicializar workspace
cn demo    # Ver demonstração
cn status  # Status do workspace
```

### **Busca Inteligente Automática**

O **WorkspaceManager 2.0** busca automaticamente:

1. **`.cn_model/`** no diretório atual
2. **`../.cn_model/`** nos diretórios pais (recursivo)
3. **`~/.local/share/context-navigator/`** instalação global
4. **`~/.context-navigator/`** fallback (compatibilidade 1.0)

```bash
# Funciona de qualquer lugar!
cd qualquer/pasta/profunda/
cn scan  # ✅ Encontra workspace automaticamente
```

---

## 🔄 Fluxo de Trabalho 2.0

### **Cenário 1: Inicializar Novo Projeto**

#### **Passo 1: Inicializar Workspace**

```bash
# Em qualquer projeto
cd meu-projeto/
cn init  # Cria .cn_model/workspace.yml
```

#### **Passo 2: Criar Primeiro Documento**

```bash
# Usar comando global
cn new decision "arquitetura-do-sistema"

# Resultado: docs/decisions/arquitetura-do-sistema.md
```

#### **Passo 3: Escanear e Validar**

```bash
# Escanear documentos (WorkspaceManager automático)
cn scan

# Validar qualidade
cn validate

# Ver demonstração completa
cn demo
```

### **Cenário 2: Trabalhar em Projeto Existente**

#### **Passo 1: Detectar Workspace**

```bash
# WorkspaceManager detecta automaticamente
cd projeto/src/components/
cn status  # ✅ Encontra ../../.cn_model/
```

#### **Passo 2: Explorar Estrutura**

```bash
# Explorar componentes existentes
cn explore

# Verificar conflitos
cn conflicts

# Analisar métricas
cn metrics
```

#### **Passo 3: Criar Novo Documento**

```bash
# De qualquer subdiretório
cn new process "deploy-processo"

# Validar automaticamente
cn validate
```

---

## 📝 Templates Detalhados

### **Templates Inalterados mas Melhorados**

Os templates permanecem os mesmos da versão 1.0, mas agora com:

- ✅ **Acesso global** via WorkspaceManager
- ✅ **Validação automática** em tempo real
- ✅ **Busca inteligente** de templates
- ✅ **Componentização** Code Bridge

### **Uso Moderno dos Templates**

```bash
# Comandos globais para templates
cn new decision "nome"          # ADRs e decisões técnicas
cn new process "nome"           # Runbooks e procedimentos
cn new reference "nome"         # APIs e documentação
cn new architecture "nome"      # Diagramas e arquitetura
cn new analysis "nome"          # Investigações e análises
cn new planning "nome"          # Roadmaps e planejamento

# Com contexto específico
cn new decision "auth-choice" --context-type core --level c2_module
```

---

## 🛠️ Scripts Especializados

### **Organização por Responsabilidade (2.0)**

```
scripts/
├── core/                        # Processamento essencial
│   ├── context_scanner.py      # Scanner com WorkspaceManager
│   └── context_engine.py       # Motor contextual
├── validation/                  # Validação de qualidade
│   ├── template_validator.py   # Validador de templates
│   ├── cn_consistency_validator.py # Validador de consistência
│   └── metrics_validator.py    # Validador de métricas
├── analysis/                    # Análise avançada
│   ├── pattern_detector.py     # Detector de padrões
│   ├── conflict_detector.py    # Detector de conflitos
│   ├── impact_analyzer.py      # Analisador de impactos
│   └── context_advisor.py      # Consultor inteligente
└── tools/                       # Utilitários
    ├── cn_component_explorer.py # Explorador de componentes
    ├── cn_component_parser.py   # Parser de componentes
    ├── context_demo.py          # Sistema de demonstração
    └── cn_global_launcher.py    # Launcher global
```

### **Comandos Modernos**

```bash
# Comandos principais (WorkspaceManager automático)
cn init                         # Inicializar workspace
cn scan                         # Escanear com WorkspaceManager
cn validate                     # Validação completa
cn demo                         # Demonstração interativa
cn status                       # Status do workspace

# Ferramentas especializadas
cn explore                      # Explorar componentes (component_explorer)
cn parse                        # Parser de componentes (component_parser)
cn conflicts                    # Detectar conflitos (conflict_detector)
cn metrics                      # Métricas de qualidade (metrics_validator)
cn advisor                      # Sugestões inteligentes (context_advisor)
```

### **Scripts Legados (ainda funcionam)**

```bash
# Métodos antigos mantidos para compatibilidade
python3 -m context_navigator.scripts.core.context_scanner --scan docs/
python3 -m context_navigator.scripts.validation.template_validator --file doc.md
```

---

## 🏆 Melhores Práticas 2.0

### **1. Aproveitamento do WorkspaceManager**

#### **✅ Faça:**

- Use `cn init` ao começar novos projetos
- Confie na busca inteligente automática
- Trabalhe de qualquer subdiretório
- Use comandos globais `cn`

#### **❌ Não Faça:**

- Não configure manualmente caminhos
- Não assuma localização de workspace
- Não use comandos legacy sem necessidade

### **2. Componentização Code Bridge**

#### **✅ Faça:**

```python
# Conecte código com documentação
# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component user-authentication
# @cn:doc decisions/auth-architecture.md
# @cn:context-level c2_module
# @cn:context-type core
# @cn:purpose "Sistema de autenticação de usuários"
# ============================================

class UserAuthenticator:
    pass
```

#### **❌ Não Faça:**

- Código sem documentação conectada
- Marcações @cn: incompletas
- Documentação sem referência ao código

### **3. Validação Automática**

#### **✅ Faça:**

```bash
# Validação contínua
cn validate                     # Validação completa
cn conflicts                    # Verificar conflitos
cn metrics                      # Monitorar qualidade
```

#### **❌ Não Faça:**

- Acumular validações
- Ignorar warnings
- Deixar conflitos sem resolver

---

## 🔧 Troubleshooting 2.0

### **Problema: Comando `cn` não encontrado**

```bash
# Diagnóstico
which cn  # Deve retornar caminho

# Solução
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### **Problema: Workspace não detectado**

```bash
# Diagnóstico
cn status  # Mostra status de detecção

# Solução 1: Inicializar workspace
cn init

# Solução 2: Verificar estrutura
ls -la .cn_model/  # Deve existir workspace.yml
```

### **Problema: Scripts organizados não funcionam**

```bash
# Diagnóstico
cn explore  # Deve listar componentes

# Solução: Reinstalar globalmente
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash
```

### **Problema: Validação falhando**

```bash
# Diagnóstico detalhado
cn validate --verbose

# Verificar workspace
cn status

# Resolver problemas específicos
cn conflicts  # Ver conflitos específicos
```

---

## 📚 Referência Rápida 2.0

### **Comandos Essenciais**

```bash
# Setup inicial
cn init                         # Inicializar workspace

# Criação de documentos
cn new decision "nome"          # Decisão técnica
cn new process "nome"           # Processo/runbook
cn new reference "nome"         # API/referência
cn new architecture "nome"      # Arquitetura/diagrama
cn new analysis "nome"          # Análise/investigação
cn new planning "nome"          # Planejamento/roadmap

# Gerenciamento
cn scan                         # Escanear documentos
cn validate                     # Validar qualidade
cn demo                         # Demonstração
cn status                       # Status workspace

# Ferramentas avançadas
cn explore                      # Explorar componentes
cn conflicts                    # Detectar conflitos
cn metrics                      # Métricas qualidade
cn advisor                      # Sugestões IA
```

### **Estrutura Workspace 2.0**

```
projeto/
├── .cn_model/                  # Workspace Context Navigator 2.0
│   ├── workspace.yml          # Configuração principal
│   ├── components/            # Componentes documentados
│   ├── templates/             # Templates customizados
│   └── maps/                  # Mapas contextuais
│       ├── index.yml         # Índice principal
│       ├── connections.yml   # Conexões entre docs
│       └── conflicts.yml     # Conflitos detectados
├── docs/                      # Documentação projeto
│   ├── decisions/            # Decisões arquiteturais
│   ├── processes/            # Processos e runbooks
│   ├── references/           # APIs e referências
│   ├── architecture/         # Arquitetura e diagramas
│   ├── analysis/             # Análises e investigações
│   └── planning/             # Planejamento e roadmaps
└── src/                       # Código fonte (com @cn:)
```

### **Arquitetura Scripts 2.0**

```
~/.local/share/context-navigator/scripts/
├── core/                      # Scanner, engine
├── validation/                # Validadores
├── analysis/                  # Analisadores
└── tools/                     # Utilitários
```

### **Metadados Obrigatórios (Inalterados)**

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

---

## 🎯 Conclusão 2.0

O **Context Navigator 2.0** representa uma evolução significativa:

✅ **WorkspaceManager inteligente** - Busca automática  
✅ **Comandos globais** - Use `cn` de qualquer lugar  
✅ **Scripts organizados** - Por responsabilidade  
✅ **Componentização** - Code Bridge conecta tudo  
✅ **Busca inteligente** - Funciona automaticamente  
✅ **Compatibilidade** - Métodos antigos ainda funcionam

### **Próximos Passos**

1. **Instalar globalmente** com script automatizado
2. **Inicializar workspace** com `cn init`
3. **Criar documentos** com comandos `cn new`
4. **Validar continuamente** com `cn validate`
5. **Explorar componentes** com `cn explore`

### **Suporte**

- **Manual da IA**: `MANUAL_IA.md` (protocolo para IAs)
- **Convenções**: `CONVENTIONS.md` (regras imutáveis)
- **Instalação**: `INSTALACAO_GLOBAL.md` (setup detalhado)
- **Exemplos**: `examples/` (casos práticos)

---

**🚀 Bem-vindo ao futuro da documentação contextual com Context Navigator 2.0!**

_Onde inteligência humana e artificial trabalham em perfeita harmonia._
