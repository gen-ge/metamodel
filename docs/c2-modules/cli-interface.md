---
# =============================================================================
# METADADOS OBRIGATÓRIOS (IMUTÁVEIS)
# =============================================================================

# Tipo do documento (OBRIGATÓRIO)
doc_type: "process"

# Título do documento (OBRIGATÓRIO)
title: "CLI Interface - Interface de Linha de Comando"

# Contexto hierárquico (OBRIGATÓRIO)
context_level: "c2_module"

# Contexto especializado (OBRIGATÓRIO)
context_type: "interface"

# Módulo específico (OBRIGATÓRIO)
module: "cli-interface"

# Conexões com outros documentos (OBRIGATÓRIO)
connections:
  references: ["MANUAL_HUMANO.md", "context.rule"]
  impacts: ["user-experience", "workflow-automation", "developer-productivity"]
  depends_on: ["context-navigator-system.md"]
  blocks: []
  relates_to:
    [
      "context-engine.md",
      "cn-component-parser.md",
      "cn-consistency-validator.md",
    ]

# Datas (OBRIGATÓRIAS)
created_date: "2025-01-13"
last_updated: "2025-01-13"

# =============================================================================
# METADADOS OPCIONAIS (EXTENSÍVEIS)
# =============================================================================

# Prioridade do módulo
priority: "critical"

# Status atual
status: "active"

# Responsável pelo módulo
owner: "Context Navigator Team"

# Tags para categorização
tags: ["module", "cli", "interface", "user-interaction", "commands"]

# Complexidade do módulo
complexity: "medium"

# Agenda de manutenção
maintenance_schedule: "monthly"

# Tipo de interface
interface_type: "command-line"

# Ambiente de execução
runtime_environment: "terminal"

# Tecnologias principais
key_technologies: ["Python", "argparse", "subprocess", "pathlib"]

# Stakeholders
stakeholders: ["developers", "content-creators", "project-managers"]

# Nível de criticidade
criticality: "high"
---

<!-- CONTEXT_META
template_version: "1.0.0"
template_type: "process"
generated_by: "context-navigator"
validation_status: "pending"
last_validated: "2025-01-13"
compliance_check: "passed"
metadata_completeness: "100%"
connection_accuracy: "verified"
context_consistency: "verified"
module_category: "interface-layer"
implementation_file: "src/context_navigator/cn_cli.py"
-->

# 🖥️ CLI Interface - Interface de Linha de Comando

> **Template:** Processo | **Contexto:** c2_module | **Módulo:** cli-interface  
> **Criado:** 2025-01-13 | **Atualizado:** 2025-01-13 | **Status:** active

## 📋 Metadados do Módulo

**Tipo:** Interface/Portal de Entrada  
**Ambiente:** Terminal/Linha de Comando  
**Criticidade:** Alta  
**Arquivo:** `src/context_navigator/cn_cli.py`

## 🎯 Objetivo

### **Propósito Principal**

O CLI Interface é o **portal de entrada** do Context Navigator, fornecendo uma interface de linha de comando intuitiva e poderosa para interagir com todo o sistema de navegação contextual.

### **Resultados Esperados**

- **Experiência de usuário fluida** na linha de comando
- **Acesso simplificado** a todas as funcionalidades do sistema
- **Automação de workflows** de documentação
- **Integração transparente** com ferramentas de desenvolvimento

## 🔧 Pré-requisitos

### **Ferramentas Obrigatórias**

- **Python 3.8+** instalado no sistema
- **Permissões de execução** em scripts Python
- **Terminal/Shell** compatível (bash, zsh, cmd, powershell)

### **Condições Necessárias**

- **Projeto inicializado** com Context Navigator
- **Arquivo .contextrc** presente no projeto
- **Estrutura mínima** de diretórios (docs/, .context-navigator/)

### **Dependências do Sistema**

- **Context Engine** - Motor de processamento contextual
- **Component Parser** - Análise de marcações @cn:
- **Consistency Validator** - Validação de sincronização
- **Template System** - Sistema de templates do CN

## 📋 Procedimento Principal

### **Passo 1: Instalação e Configuração**

**Comando:**

```bash
# Instalar Context Navigator
pip install context-navigator

# Ou usar localmente
python -m context_navigator.cn_cli --help
```

**Validação:**

```bash
cn --version
# Resultado esperado: Context Navigator v1.1.0
```

**Resultado:** CLI disponível globalmente no sistema

---

### **Passo 2: Inicialização de Projeto**

**Comando:**

```bash
# Inicializar projeto com CN
cn init

# Ou inicializar com template específico
cn init --template python-project
```

**Validação:**

```bash
ls -la .context-navigator/
# Resultado: Estrutura básica criada
```

**Resultado:** Projeto configurado para usar Context Navigator

---

### **Passo 3: Comandos de Análise e Descoberta**

#### **3.1 Scan de Projeto**

**Comando:**

```bash
# Escanear projeto atual
cn scan

# Escanear com análise profunda
cn scan --deep --suggest-templates
```

**Validação:** Arquivo `.context-map/index.yml` atualizado

#### **3.2 Exploração de Componentes**

**Comando:**

```bash
# Explorar estrutura componentizada
cn component explore

# Explorar sistema específico
cn component explore context-navigator
```

**Resultado:** Árvore hierárquica de componentes

---

### **Passo 4: Comandos de Validação**

#### **4.1 Validação de Consistência**

**Comando:**

```bash
# Validar consistência básica
cn validate

# Validação rigorosa
cn validate consistency --strict
```

**Validação:**

```bash
echo $?
# Resultado: 0 se válido, 1 se erro
```

#### **4.2 Validação de Templates**

**Comando:**

```bash
# Validar templates específicos
cn validate templates

# Validar documento específico
cn validate docs/exemplo.md
```

**Resultado:** Relatório de conformidade com templates

---

### **Passo 5: Comandos de Geração**

#### **5.1 Geração de Documentação**

**Comando:**

```bash
# Gerar documentação ausente
cn generate docs --all-missing

# Gerar documentação para componente
cn generate docs --component payment-processor
```

#### **5.2 Geração de Mapas**

**Comando:**

```bash
# Gerar component-map atualizado
cn generate component-map

# Gerar relatório de componentes
cn component report --format yaml
```

---

### **Passo 6: Comandos de Desenvolvimento**

#### **6.1 Criação de Componentes**

**Comando:**

```bash
# Criar novo componente
cn component create user-validator --type validation --parent user-module

# Criar com template completo
cn component create payment-api --template api-module --docs
```

#### **6.2 Análise de Impacto**

**Comando:**

```bash
# Analisar impacto de mudanças
cn impact analyze payment-processor

# Sugerir refatorações
cn refactor suggest --component legacy-code
```

## 🎯 Fluxo de Trabalho Típico

### **Workflow 1: Projeto Novo**

```bash
1. cn init --template python-api          # Inicializar
2. cn scan --suggest-templates             # Analisar conteúdo
3. cn generate docs --all-missing          # Gerar documentação
4. cn validate consistency                 # Validar tudo
```

### **Workflow 2: Projeto Existente**

```bash
1. cn migrate project --scan-existing      # Migrar projeto
2. cn component explore                    # Entender estrutura
3. cn validate --fix-suggestions          # Corrigir problemas
4. cn generate component-map               # Gerar mapeamento
```

### **Workflow 3: Desenvolvimento Diário**

```bash
1. cn scan --incremental                   # Scan rápido
2. cn validate templates                   # Validar mudanças
3. cn sync verify                          # Verificar sincronização
4. cn component report --changed           # Ver mudanças
```

## 🔍 Validação e Testes

### **Testes de Funcionalidade**

#### **Teste 1: Comandos Básicos**

```bash
# Testar comandos essenciais
cn --help                    # ✅ Deve mostrar ajuda
cn --version                 # ✅ Deve mostrar versão
cn scan --dry-run           # ✅ Deve simular scan
```

#### **Teste 2: Integração com Componentes**

```bash
# Testar integração
cn component explore         # ✅ Deve mostrar hierarquia
cn validate consistency      # ✅ Deve validar sem erro
cn generate component-map    # ✅ Deve gerar YAML válido
```

#### **Teste 3: Tratamento de Erros**

```bash
# Testar cenários de erro
cn scan /diretorio-inexistente    # ✅ Deve mostrar erro claro
cn validate arquivo-invalido.md   # ✅ Deve reportar problemas
cn component create ""             # ✅ Deve rejeitar nome vazio
```

### **Verificação de Saída**

- **Exit Codes:** 0 = sucesso, 1 = erro, 2 = aviso
- **Formato de Saída:** Consistente entre comandos
- **Logging:** Níveis appropriados (INFO, WARNING, ERROR)
- **Progress Indicators:** Para operações longas

## 🚨 Tratamento de Erros

### **Cenários Comuns de Erro**

#### **1. Projeto Não Inicializado**

```bash
Erro: Context Navigator não inicializado neste projeto
Solução: Execute 'cn init' para configurar
```

#### **2. Dependências Ausentes**

```bash
Erro: context.rule não encontrado
Solução: Verifique instalação ou execute 'cn repair'
```

#### **3. Permissões Insuficientes**

```bash
Erro: Não foi possível escrever em .context-navigator/
Solução: Verifique permissões do diretório
```

#### **4. Templates Inválidos**

```bash
Erro: Template decisao.md contém erros de sintaxe
Solução: Execute 'cn validate templates --fix'
```

### **Estratégias de Recuperação**

- **Auto-repair:** `cn repair --auto` para problemas comuns
- **Fallback graceful:** Continuar operação com funcionalidade reduzida
- **Suggestions:** Sempre sugerir comando de correção
- **Backup:** Criar backup antes de operações destrutivas

## 📊 Comandos Disponíveis

### **Comandos Principais**

| Comando       | Descrição            | Exemplo                  |
| ------------- | -------------------- | ------------------------ |
| `cn init`     | Inicializar projeto  | `cn init --template api` |
| `cn scan`     | Escanear e analisar  | `cn scan --deep`         |
| `cn validate` | Validar consistência | `cn validate --strict`   |
| `cn generate` | Gerar artefatos      | `cn generate docs`       |

### **Comandos de Componentes**

| Comando                | Descrição           | Exemplo                        |
| ---------------------- | ------------------- | ------------------------------ |
| `cn component explore` | Explorar hierarquia | `cn component explore system`  |
| `cn component create`  | Criar componente    | `cn component create api-auth` |
| `cn component report`  | Relatório detalhado | `cn component report --yaml`   |

### **Comandos de Utilidade**

| Comando      | Descrição               | Exemplo               |
| ------------ | ----------------------- | --------------------- |
| `cn repair`  | Reparar problemas       | `cn repair --auto`    |
| `cn sync`    | Sincronizar docs-código | `cn sync verify`      |
| `cn metrics` | Métricas do projeto     | `cn metrics coverage` |

## 🔧 Configuração Avançada

### **Arquivo .contextrc**

```yaml
cli:
  default_format: "text" # text, yaml, json
  verbose_mode: false # Modo verboso
  auto_suggest: true # Sugestões automáticas
  color_output: true # Colorir saída

commands:
  scan:
    deep_analysis: false # Análise profunda padrão
    suggest_templates: true # Sugerir templates

  validate:
    strict_mode: false # Modo rigoroso padrão
    fix_suggestions: true # Sugerir correções

  component:
    show_hierarchy: true # Mostrar hierarquia
    include_metadata: false # Incluir metadados
```

### **Variáveis de Ambiente**

```bash
# Configurações via ambiente
export CN_CONFIG_PATH="/custom/path/.contextrc"
export CN_VERBOSE=true
export CN_NO_COLOR=false
export CN_AUTO_REPAIR=true
```

## 🚀 Evolução e Roadmap

### **Funcionalidades Planejadas**

- **Autocompletion:** Para bash, zsh, fish
- **Interactive Mode:** CLI interativo
- **Plugin System:** Extensões de terceiros
- **Remote Projects:** Análise de projetos remotos

### **Melhorias de UX**

- **Progress Bars:** Para operações longas
- **Colored Output:** Saída colorida e formatada
- **Smart Suggestions:** Sugestões contextuais
- **Undo/Redo:** Para operações reversíveis

---

**🎯 O CLI Interface é a porta de entrada amigável para todo o poder do Context Navigator!**
