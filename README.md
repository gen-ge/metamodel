# 🧭 Context Navigator 0.1.0-alpha - Early Access

> **Sistema de documentação contextual para projetos de software - Primeira versão funcional**

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-alpha--functional-orange.svg)]()

⚠️ **ALPHA VERSION:** Esta é a primeira versão funcional. Core features implementadas e testadas, mas ainda em desenvolvimento ativo.

## 🎯 O que é o Context Navigator?

**Context Navigator 0.1.0-alpha** é um sistema de documentação inteligente que ajuda desenvolvedores a criar e manter documentação técnica estruturada em seus projetos.

### 🌟 **Por que usar?**

- **📝 Documentação padronizada** - Templates para decisões técnicas (ADRs), processos, APIs e arquitetura
- **🌐 Funciona globalmente** - Comando `cn` disponível em qualquer lugar do sistema
- **📋 Registry inteligente** - Detecta automaticamente seus projetos registrados
- **🎯 Zero configuração** - Instala uma vez, funciona em todos os projetos
- **⚡ Detecção automática** - Funciona em qualquer subdiretório do projeto

### 🎨 **Tipos de Documentação**

| Template         | Para que usar               | Exemplo                         |
| ---------------- | --------------------------- | ------------------------------- |
| **Decision**     | Decisões técnicas (ADRs)    | "Por que escolhemos React?"     |
| **Process**      | Processos e runbooks        | "Como fazer deploy?"            |
| **Reference**    | APIs e documentação técnica | "Documentação da API Users"     |
| **Architecture** | Diagramas e arquitetura     | "Arquitetura dos microservices" |
| **Analysis**     | Investigações técnicas      | "Análise de performance"        |
| **Planning**     | Roadmaps e planejamentos    | "Roadmap Q1 2025"               |

## 🚀 Instalação Rápida

```bash
# 1. Download do projeto
git clone https://github.com/gen-ge/metamodel.git
cd metamodel

# 2. Instalar automaticamente
python3 src/context_navigator/installer/install.py

# 3. Adicionar ao PATH (se necessário)
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# 4. Testar instalação
cn help
```

## ⚡ Primeiros Passos

### **1. Registrar seu Projeto**

```bash
# Vá para o diretório do seu projeto
cd meu-projeto/

# Registre o projeto no Context Navigator
cn init
# ✅ Projeto registrado no sistema global
```

### **2. Explorar Templates**

```bash
# Ver todos os templates disponíveis
cn templates

# Saída:
# 📋 Templates disponíveis:
# • decision    - Decisões técnicas (ADRs)
# • process     - Processos e runbooks
# • reference   - APIs e documentação técnica
# • architecture - Arquitetura e diagramas
# • analysis    - Análises e investigações
# • planning    - Planejamentos e roadmaps
```

### **3. Criar Primeira Documentação**

```bash
# Criar uma decisão técnica
cn new decision "escolha-do-framework"
# ✅ Criado: .cn_model/docs/decisions/escolha-do-framework.md

# Criar documentação de processo
cn new process "deploy-producao"
# ✅ Criado: .cn_model/docs/processes/deploy-producao.md

# Criar documentação de API
cn new reference "api-usuarios"
# ✅ Criado: .cn_model/docs/references/api-usuarios.md
```

## 🎯 Como Funciona

### **Sistema Global e Inteligente**

O Context Navigator usa um **registry global** para detectar seus projetos:

```bash
# 1. Registrar projeto uma vez
cd projeto/
cn init                         # Registra no sistema

# 2. Funciona de qualquer lugar do projeto
cd projeto/                     # cn scan ✅
cd projeto/src/                 # cn scan ✅
cd projeto/src/components/      # cn scan ✅

# 3. Comportamento consistente sempre
cn info                         # Mostra informações do projeto
cn new decision "teste"         # Cria documentação no local correto
```

### **Estrutura Criada no seu Projeto**

```
seu-projeto/
├── .cn_model/                  # 📁 Documentação gerada pelo Context Navigator
│   ├── docs/                   # 📝 Documentos organizados por tipo
│   │   ├── decisions/          # 🎯 Decisões técnicas (ADRs)
│   │   ├── processes/          # ⚙️ Processos e runbooks
│   │   ├── references/         # 📚 APIs e documentação técnica
│   │   ├── architecture/       # 🏗️ Arquitetura e diagramas
│   │   ├── analysis/           # 🔍 Análises e investigações
│   │   └── planning/           # 📅 Planejamentos e roadmaps
│   └── templates/              # 📄 Templates customizados (opcional)
├── src/                        # 💻 Seu código fonte
└── ...                         # 📁 Outros arquivos do projeto
```

## 📋 Comandos Essenciais

### **Gestão de Projetos**

```bash
cn init                         # Registrar projeto atual
cn info                         # Informações do projeto
cn remove                       # Remover projeto do sistema
```

### **Criação de Documentação**

```bash
cn new decision "nome"          # ADR - Decisão técnica
cn new process "nome"           # Processo ou runbook
cn new reference "nome"         # Documentação de API/componente
cn new architecture "nome"      # Diagrama de arquitetura
cn new analysis "nome"          # Análise técnica
cn new planning "nome"          # Planejamento/roadmap
```

### **Análise e Mapeamento**

```bash
cn scan                         # Mapear documentação existente
cn demo                         # Demonstração interativa do sistema
# cn validate                   # TODO: Implementar validação
```

## 💡 Exemplo Prático Completo

```bash
# 1. Configurar projeto React
cd meu-app-react/
cn init
# ✅ Projeto 'meu-app-react' registrado

# 2. Documentar decisão técnica
cn new decision "escolha-react-vs-vue"
# ✅ Criado: .cn_model/docs/decisions/escolha-react-vs-vue.md
# Template preenchido com estrutura de ADR

# 3. Documentar processo de deploy
cn new process "deploy-aws-s3"
# ✅ Criado: .cn_model/docs/processes/deploy-aws-s3.md

# 4. Documentar API
cn new reference "api-usuarios"
# ✅ Criado: .cn_model/docs/references/api-usuarios.md

# 5. Usar de qualquer lugar do projeto
cd src/components/
cn info                         # ✅ Detecta projeto via registry
cn new decision "estrutura-componentes"
# ✅ Cria em: ../../.cn_model/docs/decisions/estrutura-componentes.md

# 6. Mapear toda documentação
cn scan
# ✅ Lista todos os documentos criados e organizados
```

## 🧪 **Validação de Funcionamento**

**Teste se sua instalação funciona:**

```bash
# Execute nosso teste automatizado (16 testes)
./test_real_install.sh

# Ou teste manualmente:
cn --version      # Deve mostrar versão
cn help          # Deve listar comandos
cd novo-projeto/
cn init          # Deve criar .cn_model/
cn templates     # Deve listar 6 tipos
cn new decision teste  # Deve criar arquivo
cn info          # Deve mostrar informações
```

## 🎨 Templates Inteligentes

### **Templates Prontos para Usar**

Cada comando `cn new` cria um documento com estrutura profissional:

- **`cn new decision`** → Template de ADR (Architecture Decision Record)
- **`cn new process`** → Template de runbook com checklist
- **`cn new reference`** → Template de documentação de API
- **`cn new architecture`** → Template para diagramas e componentes
- **`cn new analysis`** → Template para investigações técnicas
- **`cn new planning`** → Template para roadmaps e sprints

### **Personalização de Templates**

```bash
# Copiar template para customização
mkdir -p .cn_model/templates/
cp ~/.local/share/context-navigator/templates/decisao.md .cn_model/templates/

# Editar template customizado
# O Context Navigator usará automaticamente sua versão customizada
```

## 🧩 Integração com Código

### **Code Bridges - Conectando Documentação e Código**

```python
# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component user-authentication
# @cn:doc decisions/auth-architecture.md
# @cn:context-level c2_module
# ============================================

class UserAuthenticator:
    """
    Sistema de autenticação integrado ao Context Navigator.

    Documentação: .cn_model/docs/decisions/auth-architecture.md
    """
    def authenticate(self, user_credentials):
        # Implementação documentada na decisão técnica
        pass
```

### **Níveis de Contexto**

- **c1_root** - Decisões de sistema (arquitetura geral)
- **c2_module** - Decisões de módulo (funcionalidades específicas)
- **c3_component** - Decisões de componente (implementação detalhada)

## 🎯 Casos de Uso Reais

### **🏢 Empresa de Software**

```bash
# Documentar arquitetura de microservices
cn new architecture "microservices-overview"

# Documentar processo de code review
cn new process "code-review-checklist"

# Documentar decisão sobre banco de dados
cn new decision "postgresql-vs-mongodb"

# Documentar API principal
cn new reference "core-api-v2"
```

### **🚀 Startup/Projeto Pessoal**

```bash
# Roadmap do produto
cn new planning "mvp-roadmap"

# Processo de deploy
cn new process "deploy-heroku"

# Análise de performance
cn new analysis "database-bottlenecks"
```

### **🎓 Projeto Acadêmico**

```bash
# Documentar escolhas técnicas
cn new decision "framework-machine-learning"

# Processo de experimentos
cn new process "experimento-modelo-ia"

# Documentar resultados
cn new analysis "resultados-experimento-1"
```

## 🌟 Vantagens do Context Navigator

### **📚 Para Desenvolvedores**

- ✅ **Documentação consistente** - Templates padronizados
- ✅ **Processo ágil** - Criação rápida com `cn new`
- ✅ **Organização automática** - Estrutura de pastas inteligente
- ✅ **Histórico de decisões** - ADRs para rastreabilidade

### **👥 Para Equipes**

- ✅ **Padrão unificado** - Toda equipe usa mesma estrutura
- ✅ **Onboarding facilitado** - Novos membros encontram documentação facilmente
- ✅ **Knowledge base** - Decisões e processos centralizados
- ✅ **Code review** - Documentação integrada ao código

### **🏢 Para Projetos**

- ✅ **Manutenibilidade** - Documentação evolui com o código
- ✅ **Compliance** - Estrutura adequada para auditorias
- ✅ **Escalabilidade** - Funciona de projetos pequenos a grandes
- ✅ **Portabilidade** - Sistema global, funciona em qualquer projeto

## 🐛 **Problemas Conhecidos (Alpha)**

### **Limitações Atuais:**

- ⚠️ **Sistema single-user** - cada usuário instala separadamente
- ⚠️ **Registry simples** - YAML básico, não suporta cenários complexos
- ⚠️ **Sem migração** de versões anteriores (se existirem)

### **Comandos Futuros (Não Implementados):**

- ❌ `cn status` - status detalhado do workspace
- ❌ `cn conflicts` - detecção de conflitos
- ❌ `cn metrics` - métricas de qualidade
- ❌ `cn advisor` - sugestões automáticas

**Nota:** Estes comandos podem ser implementados em versões futuras ou removidos se não forem úteis.

## ❓ FAQ

### **"Preciso aprender alguma sintaxe especial?"**

Não! O Context Navigator cria arquivos Markdown normais. Você edita com qualquer editor.

### **"Funciona com meu editor favorito?"**

Sim! Os arquivos são Markdown padrão, funcionam com VS Code, nano, gedit, JetBrains, etc.

### **"E se eu mudar de computador?"**

Instale o Context Navigator no novo computador e execute `cn init` nos seus projetos.

### **"Posso usar em projetos existentes?"**

Sim! Execute `cn init` em qualquer projeto existente.

### **"Como backup da documentação?"**

A pasta `.cn_model/` são arquivos normais - use Git, backup em nuvem, etc.

## 📚 Documentação Completa

- **[🤝 Guia de Contribuição](CONTRIBUTING.md)** - Como contribuir para o projeto
- **[🏗️ Arquitetura](docs/ARQUITETURA_SIMPLIFICADA.md)** - Visão técnica simplificada
- **[📖 Manual Completo](docs/c1-systems/MANUAL_HUMANO.md)** - Documentação detalhada
- **[🤖 Manual para IA](docs/c1-systems/MANUAL_IA.md)** - Integração com assistentes

## 🤝 Contribuir

Quer ajudar a melhorar o Context Navigator?

- **🐛 [Reportar bugs](https://github.com/gen-ge/metamodel/issues)**
- **💡 [Sugerir funcionalidades](https://github.com/gen-ge/metamodel/discussions)**
- **🛠️ [Contribuir código](CONTRIBUTING.md)** - Guia para desenvolvedores

## 📄 Licença

[MIT License](LICENSE) - Use livremente em qualquer projeto!

---

## 🚀 Comece Agora (Alpha)!

```bash
# 1. Baixar e instalar
git clone https://github.com/gen-ge/metamodel.git
cd metamodel
python3 src/context_navigator/installer/install.py

# 2. Validar instalação
./test_real_install.sh  # Opcional: validar que funciona

# 3. Usar em seu projeto
cd seu-projeto/
cn init                 # Criar workspace
cn templates            # Ver tipos disponíveis
cn new decision "primeira-decisao"  # Criar primeiro documento
```

**Context Navigator 0.1.0-alpha: Funciona de verdade!** 🎯

⚠️ **Lembre-se:** Esta é uma versão alpha. Reporte problemas [aqui](https://github.com/gen-ge/metamodel/issues).

---

📧 **Suporte:** [Issues](https://github.com/gen-ge/metamodel/issues) | 💬 **Discussões:** [GitHub Discussions](https://github.com/gen-ge/metamodel/discussions) | 📖 **Docs:** [Manual Completo](docs/c1-systems/MANUAL_HUMANO.md)
