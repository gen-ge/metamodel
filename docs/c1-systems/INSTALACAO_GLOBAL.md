---
doc_type: "reference"
context_level: "c1_root"
context_type: "core"
module: "context-navigator"
priority: "critical"
status: "active"
connections:
  references: ["MANUAL_HUMANO.md", "MANUAL_IA.md", "CONVENTIONS.md"]
  impacts:
    ["install.py", "cn_global_launcher.py", "installer/", "WorkspaceManager"]
  depends_on: ["install-context-navigator-latest.sh", "test_global_install.sh"]
  relates_to: ["context_scanner.py", "context_engine.py", "workspace.yml"]
created_date: "2025-01-13"
last_updated: "2025-01-13"
owner: "Context Navigator Team"
tags: ["installation", "global", "script", "automation", "deployment", "2.0"]
complexity: "medium"
maintenance_schedule: "monthly"
stakeholders: ["developers", "users", "system-admins"]
architectural_impact: "medium"
version: "2.0"
---

# 🌐 Context Navigator 2.0 - Instalação Global

## 🎯 Usar o Context Navigator de Qualquer Diretório

Com a **Arquitetura 2.0**, você pode usar o Context Navigator de qualquer diretório através do PATH do sistema com **busca inteligente automática de workspaces**!

## 🚀 Métodos de Instalação

### 1. 🌐 Instalação Global Automatizada (Recomendada)

**Script de Instalação Oficial**: `install-context-navigator-latest.sh`

```bash
# 1. Baixar e executar script oficial
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# 2. Configurar PATH (adicione ao ~/.bashrc)
export PATH="$HOME/.local/bin:$PATH"

# 3. Recarregar o shell
source ~/.bashrc

# 4. Usar de qualquer diretório
cn scan
cn demo
cn help
```

**Características do Script 2.0**:

- ✅ **Download automático** da versão mais recente
- ✅ **Verificação de dependências** (Python 3.7+, tar, wget/curl)
- ✅ **Instalação segura** com limpeza automática
- ✅ **Configuração do PATH** automática
- ✅ **Setup do WorkspaceManager** 2.0
- ✅ **Validação da instalação**

### 2. 📁 Instalação Manual Global

```bash
# 1. Instalar globalmente (Arquitetura 2.0)
python3 src/context_navigator/installer/install.py --global

# 2. Configurar PATH (adicione ao ~/.bashrc)
export PATH="$HOME/.local/bin:$PATH"

# 3. Recarregar o shell
source ~/.bashrc

# 4. Usar de qualquer diretório
cn scan
cn demo
cn help
```

### 3. 📁 Instalação Local + Launcher Global

```bash
# 1. Instalar localmente (cria .cn_model/)
python3 src/context_navigator/installer/install.py

# 2. Copiar launcher global para o PATH
cp src/context_navigator/scripts/tools/cn_global_launcher.py ~/.local/bin/cn
chmod +x ~/.local/bin/cn

# 3. Configurar PATH se necessário
export PATH="$HOME/.local/bin:$PATH"

# 4. Usar de qualquer diretório
cn scan
cn demo
cn help
```

### 4. 🔗 Criar Link Simbólico

```bash
# 1. Instalar localmente
python3 src/context_navigator/installer/install.py

# 2. Criar link simbólico no PATH
sudo ln -s $(pwd)/src/context_navigator/scripts/tools/cn_global_launcher.py /usr/local/bin/cn

# 3. Usar de qualquer diretório
cn scan
cn demo
cn help
```

## 🔍 Como Funciona a Busca Inteligente 2.0

O **WorkspaceManager** da Arquitetura 2.0 busca automaticamente por workspaces `.cn_model/` em:

1. **Diretório atual**: `./.cn_model/`
2. **Diretórios pais**: `../.cn_model/`, `../../.cn_model/`, etc. (recursivo até raiz)
3. **Instalação global**: `~/.local/share/context-navigator/`
4. **Fallback**: `~/.context-navigator/` (compatibilidade)

### Exemplo de Uso com Arquitetura 2.0

```bash
# Estrutura do projeto (Arquitetura 2.0)
projeto/
├── .cn_model/                    # Workspace Context Navigator 2.0
│   ├── workspace.yml            # Configuração do workspace
│   ├── components/              # Componentes documentados
│   ├── templates/               # Templates personalizados
│   └── maps/                    # Mapas de contexto
├── docs/
├── src/
│   └── components/
└── tests/

# Você pode usar de qualquer lugar:
cd projeto/                      # cn scan ✅ (encontra ./.cn_model/)
cd projeto/src/                  # cn scan ✅ (encontra ../.cn_model/)
cd projeto/src/components/       # cn scan ✅ (encontra ../../.cn_model/)
cd /qualquer/outro/lugar/        # cn scan ✅ (usa instalação global)
```

## 📋 Comandos Disponíveis 2.0

### 🌐 Com Instalação Global (Recomendado)

```bash
# Comandos principais
cn init                          # Inicializar workspace (.cn_model/)
cn scan                          # Escanear documentos
cn demo                          # Demonstração completa
cn validate                      # Validar qualidade
cn status                        # Status do workspace

# Criação de documentos
cn new decision nome             # Criar nova decisão
cn new process nome              # Criar novo processo
cn new reference nome            # Criar nova referência
cn new architecture nome         # Criar nova arquitetura
cn new analysis nome             # Criar nova análise
cn new planning nome             # Criar novo planejamento

# Ferramentas especializadas
cn explore                       # Explorar componentes
cn parse                         # Parser de componentes
cn conflicts                     # Detectar conflitos
cn metrics                       # Métricas de qualidade
cn advisor                       # Sugestões inteligentes

# Ajuda
cn help                          # Ver todos os comandos
```

### 📁 Com Instalação Local (método legacy ainda funciona)

```bash
python3 -m context_navigator.cn_cli_legacy scan
python3 -m context_navigator.cn_cli_legacy demo
python3 -m context_navigator.cn_cli_legacy validate
# etc...
```

## 🎯 Prioridade de Busca (WorkspaceManager 2.0)

1. **Workspace Local**: Se encontrar `.cn_model/` no diretório atual ou pais
2. **Instalação Global**: Se não encontrar workspace local
3. **Compatibilidade**: Fallback para `.context-navigator/` (arquitetura 1.0)

## 🔧 Configuração do PATH

### Bash/Zsh (Linux/macOS)

```bash
# Adicione ao ~/.bashrc ou ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"

# Recarregue o shell
source ~/.bashrc  # ou ~/.zshrc
```

### Fish Shell

```bash
# Adicione ao ~/.config/fish/config.fish
set -x PATH $HOME/.local/bin $PATH
```

## 🧪 Testando a Instalação 2.0

### Script de Teste Automatizado

**Script de Teste**: `test_global_install.sh`

```bash
# Executar teste completo da Arquitetura 2.0
./test_global_install.sh
```

**O script testa**:

- ✅ Disponibilidade do comando `cn`
- ✅ Funcionamento do comando `cn help`
- ✅ Inicialização de workspace (`.cn_model/`)
- ✅ Criação de documentos
- ✅ Scanner de contexto com WorkspaceManager
- ✅ Busca inteligente funcionando
- ✅ Scripts organizados (core, validation, analysis, tools)
- ✅ Configuração do PATH

### Testes Manuais

```bash
# Verificar se o comando está disponível
which cn

# Testar busca inteligente e workspace
cn status

# Inicializar workspace se necessário
cn init

# Testar funcionalidade completa
cn demo

# Verificar organização de scripts
cn explore
```

## 🎯 Vantagens da Instalação Global 2.0

- ✅ **Usar de qualquer diretório** com busca inteligente
- ✅ **Comando mais simples**: `cn` ao invés de `python3 -m context_navigator.cn_cli_legacy`
- ✅ **WorkspaceManager automático** detecta `.cn_model/`
- ✅ **Scripts organizados** por responsabilidade (core/validation/analysis/tools)
- ✅ **Compatível com arquitetura 1.0** (fallback automático)
- ✅ **Não interfere com o comportamento atual**
- ✅ **Instalação automatizada** com script
- ✅ **Testes automatizados** de validação
- ✅ **Componentização** Code Bridge (@cn:)

## 🔄 Migração do Método Antigo

Se você já usa o Context Navigator com o método antigo:

```bash
# Método legacy (ainda funciona)
python3 -m context_navigator.cn_cli_legacy scan

# Método novo 2.0 (recomendado)
cn scan
```

**Migração automática**:

- `.context-navigator/` → `.cn_model/` (automática)
- `.contextrc` → `workspace.yml` (automática)
- Scripts reorganizados automaticamente

Ambos os métodos funcionam simultaneamente!

## 📝 Exemplo Prático 2.0

### Instalação Completa com Script

```bash
# 1. Instalação automatizada (Arquitetura 2.0)
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# 2. Configurar PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# 3. Testar instalação
./test_global_install.sh

# 4. Usar em qualquer projeto
mkdir meu-projeto
cd meu-projeto
cn init                        # Cria .cn_model/workspace.yml
cn new decision "Arquitetura do Sistema"
cn new process "Deploy em Produção"

# 5. Trabalhar de qualquer subdiretório
cd src/components/
cn scan                        # Funciona! (encontra ../../.cn_model/)
cn validate                    # Funciona!
cn explore                     # Explorar componentes

# 6. Trabalhar em outro projeto
cd /outro/projeto/
cn scan                        # Usa busca inteligente (WorkspaceManager)
```

## 🛠️ Scripts de Instalação e Teste 2.0

### Script Principal: `install-context-navigator-latest.sh`

**Funcionalidades 2.0**:

- 📥 Download automático da versão mais recente
- 🔍 Verificação de dependências
- 🧹 Limpeza automática de arquivos temporários
- ⚙️ Configuração automática do PATH
- 🎯 Criação do launcher global
- 🏗️ Setup do WorkspaceManager 2.0
- 📁 Configuração de scripts organizados

### Script de Teste: `test_global_install.sh`

**Funcionalidades 2.0**:

- 🧪 Teste completo da instalação
- ✅ Validação de comandos globais
- 🔍 Verificação do PATH
- 📝 Teste de criação de documentos
- 🎯 Verificação do scanner e WorkspaceManager
- 🏗️ Teste de busca inteligente
- 📊 Verificação de scripts organizados

## 🏗️ Arquitetura de Scripts 2.0

### **Organização por Responsabilidade**

```
~/.local/share/context-navigator/scripts/
├── core/                        # Processamento essencial
│   ├── context_scanner.py      # Scanner com WorkspaceManager
│   └── context_engine.py       # Motor contextual
├── validation/                  # Validação de qualidade
│   ├── template_validator.py   # Validador de templates
│   ├── cn_consistency_validator.py # Consistência
│   └── metrics_validator.py    # Métricas
├── analysis/                    # Análise avançada
│   ├── pattern_detector.py     # Padrões
│   ├── conflict_detector.py    # Conflitos
│   ├── impact_analyzer.py      # Impactos
│   └── context_advisor.py      # Sugestões
└── tools/                       # Utilitários
    ├── cn_component_explorer.py # Explorador
    ├── cn_component_parser.py   # Parser
    ├── context_demo.py          # Demo
    └── cn_global_launcher.py    # Launcher
```

## 🎯 Resumo da Arquitetura 2.0

O Context Navigator 2.0 é **muito mais inteligente e flexível**:

- 🌐 **Instalação Global**: Use `cn` de qualquer lugar
- 🧠 **WorkspaceManager**: Busca inteligente automática de `.cn_model/`
- 📁 **Compatibilidade**: Métodos antigos ainda funcionam
- 🎯 **Simplicidade**: Comando mais curto e intuitivo
- 🤖 **Automatização**: Scripts de instalação e teste
- 🛡️ **Confiabilidade**: Verificação automática de dependências
- 🏗️ **Organização**: Scripts categorizados por responsabilidade
- 🧩 **Componentização**: Code Bridge conecta docs ↔ código

**Recomendação**: Use a instalação global automatizada para uma experiência moderna e confiável com a Arquitetura 2.0!

---

## 🔗 Arquivos Relacionados

- **Scripts**: `install-context-navigator-latest.sh`, `test_global_install.sh`
- **Instalador**: `src/context_navigator/installer/install.py`
- **Launcher**: `src/context_navigator/scripts/tools/cn_global_launcher.py`
- **WorkspaceManager**: `src/context_navigator/core/workspace_manager.py`
- **Documentação**: `MANUAL_HUMANO.md`, `MANUAL_IA.md`, `CONVENTIONS.md`
- **Templates**: Disponíveis globalmente via WorkspaceManager
