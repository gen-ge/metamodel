# ⚡ Quick Start - Context Navigator (15 minutos)

## 🎯 **O que é o Context Navigator?**

Um sistema que **conecta automaticamente** sua documentação, mostrando como cada documento se relaciona com os outros.

**Resultado:** Documentação 10x mais navegável e contextualizada!

**Status:** ✅ **PRONTO PARA USO** - Agora com busca inteligente e instalação global!

---

## 🚀 **Passo 1: Instalação (2 minutos)**

### **Opção 1: Instalação Global (Recomendada)**

```bash
# Download e instalação global
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# Configurar PATH
export PATH="$HOME/.local/bin:$PATH"

# Testar
cn help
```

### **Opção 2: Instalação Local**

```bash
# Download
wget https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*

# Instalar no projeto
cd /caminho/para/seu/projeto
python3 /caminho/para/context-navigator-*/install.py
```

---

## 📝 **Passo 2: Primeiro Teste (3 minutos)**

### **🌐 Com Instalação Global:**

```bash
# Navegar para qualquer projeto
cd /caminho/para/seu/projeto

# Verificar se funciona
cn status

# Se não há instalação local, você pode:
# 1. Instalar localmente no projeto atual
# 2. Ou usar apenas a instalação global
```

### **📁 Com Instalação Local:**

```bash
# Navegar para a pasta do projeto
cd /caminho/para/seu/projeto

# Verificar se funciona
python3 -m context_navigator.cn_cli status

# Se instalado, vai mostrar:
# ✅ Context Navigator encontrado em: .context-navigator/
```

---

## 🎯 **Passo 3: Seu Primeiro Documento (5 minutos)**

### **🌐 Com Instalação Global:**

```bash
# Criar documento usando comando global
cn new decision "minha-primeira-decisao"

# Outros tipos disponíveis:
cn new process "meu-processo"
cn new reference "minha-referencia"
cn new architecture "minha-arquitetura"
```

### **📁 Com Instalação Local:**

```bash
# Criar documento
python3 -m context_navigator.cn_cli new decision "minha-primeira-decisao"

# Outros tipos:
python3 -m context_navigator.cn_cli new process "meu-processo"
python3 -m context_navigator.cn_cli new reference "minha-referencia"
```

### **✅ Resultado:**

```bash
🎯 Criando documento tipo: decision
✅ Documento criado: .context-navigator/docs/decisions/minha-primeira-decisao.md
📁 Pasta: .context-navigator/docs/decisions
🎯 SEMPRE cria em: .context-navigator/docs/decisions/
```

### **📝 Editar o documento criado:**

```bash
# Abrir o arquivo gerado
nano .context-navigator/docs/decisions/minha-primeira-decisao.md

# Editar os metadados obrigatórios:
---
doc_type: "decision"
title: "Minha Primeira Decisão"
context_level: "c2_module"
context_type: "core"
module: "meu_modulo"
priority: "high"
status: "active"
connections:
  references: []
  impacts: []
created_date: "2025-01-14"
---
```

---

## 🔍 **Passo 4: Escanear e Validar (3 minutos)**

### **🌐 Com Instalação Global:**

```bash
# Escanear documentos
cn scan

# Validar métricas
cn validate

# Demo completa
cn demo
```

### **📁 Com Instalação Local:**

```bash
# Escanear documentos
python3 -m context_navigator.cn_cli scan

# Validar métricas
python3 -m context_navigator.cn_cli validate

# Demo completa
python3 -m context_navigator.cn_cli demo
```

**✅ Sucesso se:**

- Seu documento aparece na contagem
- Nenhum erro é detectado
- Conexões são mapeadas

---

## 🎯 **Passo 5: Busca Inteligente (2 minutos)**

### **🔍 Funciona de Qualquer Lugar:**

```bash
# Estrutura do projeto
projeto/
├── .context-navigator/     # Instalação
├── src/
│   └── components/
├── docs/
└── tests/

# Testar busca inteligente:
cd projeto/src/components/
cn status                   # ✅ Encontra automaticamente
cn new decision "componente-decisao"  # ✅ Cria no local correto

cd projeto/docs/
cn scan                     # ✅ Funciona de qualquer lugar
```

### **💡 Vantagens:**

- **Busca automática**: Procura `.context-navigator/` em diretórios pais
- **Cria no local certo**: Sempre em `.context-navigator/docs/`
- **Comando simples**: `cn` ao invés de comandos longos

---

## 📊 **Entendendo os Resultados**

### **Context Scanner (cn scan):**

```bash
📊 ESCANEAMENTO CONCLUÍDO
📄 Documentos encontrados: 1
✅ Documentos válidos: 1
⚠️  Avisos: 0
❌ Erros: 0
```

### **Validação (cn validate):**

```bash
📊 VALIDAÇÃO DE MÉTRICAS
✅ Estrutura: OK
✅ Metadados: OK
✅ Conexões: OK
🎯 Status: APROVADO
```

### **Demo (cn demo):**

```bash
# Vai mostrar:
# - Todos os documentos encontrados
# - Conexões entre eles
# - Estrutura do projeto
# - Sugestões de melhorias
```

---

## 🔧 **Comandos Essenciais**

### **🌐 Com Instalação Global:**

```bash
# Comandos básicos
cn help                     # Ajuda completa
cn status                   # Status da instalação
cn scan                     # Escanear documentos
cn validate                 # Validar métricas
cn demo                     # Demonstração

# Criar documentos
cn new decision "nome"      # Nova decisão
cn new process "nome"       # Novo processo
cn new reference "nome"     # Nova referência
cn new architecture "nome"  # Nova arquitetura
cn new analysis "nome"      # Nova análise
cn new planning "nome"      # Novo planejamento

# Avançado
cn patterns                 # Detectar padrões
cn conflicts                # Detectar conflitos
cn impact                   # Analisar impacto
```

### **📁 Com Instalação Local:**

```bash
# Comandos básicos
python3 -m context_navigator.cn_cli help
python3 -m context_navigator.cn_cli status
python3 -m context_navigator.cn_cli scan
python3 -m context_navigator.cn_cli validate
python3 -m context_navigator.cn_cli demo

# Criar documentos
python3 -m context_navigator.cn_cli new decision "nome"
python3 -m context_navigator.cn_cli new process "nome"
# etc...
```

---

## 🎯 **Tipos de Documentos**

### **📋 Templates Disponíveis:**

- **`decision`** - Para ADRs, PRDs, escolhas técnicas
- **`process`** - Para runbooks, tutoriais, procedimentos
- **`reference`** - Para APIs, documentação técnica
- **`architecture`** - Para diagramas, modelagem
- **`analysis`** - Para debugging, investigações
- **`planning`** - Para roadmaps, sprints

### **🗂️ Organização Automática:**

```bash
.context-navigator/docs/
├── decisions/              # Decisões arquiteturais
├── processes/              # Processos e workflows
├── references/             # Referências e APIs
├── architecture/           # Documentação de arquitetura
├── analysis/               # Análises e investigações
└── planning/               # Planejamento e roadmaps
```

---

## 🔧 **Troubleshooting Rápido**

### **Comando não encontrado?**

```bash
# Verificar PATH
which cn

# Se não encontrar, adicionar ao ~/.bashrc:
export PATH="$HOME/.local/bin:$PATH"
source ~/.bashrc
```

### **Documento não aparece?**

```bash
# Verificar metadados obrigatórios
head -20 .context-navigator/docs/decisions/meu-documento.md

# Deve ter pelo menos:
# doc_type, title, context_level, context_type, module
```

### **Erro de instalação?**

```bash
# Verificar Python
python3 --version  # Deve ser 3.7+

# Verificar permissões
ls -la ~/.local/bin/

# Reinstalar se necessário
rm ~/.local/bin/cn
python3 install.py --global
```

---

## 💡 **Próximos Passos**

### **🎯 Agora você pode:**

1. **Criar mais documentos** usando `cn new <type> <name>`
2. **Conectar documentos** editando os metadados `connections:`
3. **Explorar com demo** para entender relacionamentos
4. **Validar regularmente** com `cn validate`

### **📚 Para se aprofundar:**

- [📖 Manual Completo](docs/MANUAL_HUMANO.md) - Guia detalhado
- [🌐 Instalação Global](docs/INSTALACAO_GLOBAL.md) - Uso através do PATH
- [🎯 Exemplos Práticos](examples/) - Casos de uso reais
- [🔧 Configurações](docs/CONVENTIONS.md) - Personalizações

---

## 🏆 **Parabéns!**

Em 15 minutos você:

- ✅ Instalou o Context Navigator (global ou local)
- ✅ Criou seu primeiro documento
- ✅ Aprendeu a busca inteligente
- ✅ Dominou os comandos essenciais
- ✅ Entendeu como validar documentos

**🚀 Agora sua documentação está 10x mais organizada e navegável!**

---

## 📞 **Ajuda Rápida**

### **Comandos de emergência:**

```bash
# Ajuda completa
cn help

# Status da instalação
cn status

# Reescanear tudo
cn scan

# Validar estrutura
cn validate
```

### **Estrutura mínima de documento:**

```yaml
---
doc_type: "decision"
title: "Minha Decisão"
context_level: "c2_module"
context_type: "core"
module: "meu_modulo"
status: "active"
---
# Título

## Conteúdo aqui
```

### **Tipos de contexto mais comuns:**

- **`core`** - Lógica de negócio
- **`api`** - Interfaces e endpoints
- **`ui`** - Interface de usuário
- **`infra`** - Infraestrutura
- **`shared`** - Componentes compartilhados

---

**🎯 Happy documenting! 🚀**
