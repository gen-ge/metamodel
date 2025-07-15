# 🧭 Context Navigator

> Sistema de documentação que conecta automaticamente seus documentos e mantém a IA sempre contextualizada

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-stable-green.svg)]()

## 🎯 O que faz?

Transforma sua documentação em uma **rede inteligente** onde:

- **Documentos se conectam automaticamente** (decisões ↔ processos ↔ referências)
- **IA sempre tem contexto** do seu projeto via `context-map/`
- **Templates padronizados** para decisões, processos, APIs, arquitetura
- **Busca inteligente** funciona de qualquer pasta do projeto

## 🚀 Instalação (1 comando)

```bash
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash
```

## ⚡ Primeiros Passos

```bash
# 1. Criar primeiro documento
cn new decision "escolha_de_banco_de_dados"

# 2. Escanear e conectar tudo
cn scan

# 3. Ver como funciona
cn demo
```

## 📋 Comandos Essenciais

```bash
# Criar documentos
cn new decision "nome"      # Decisões técnicas (ADRs)
cn new process "nome"       # Processos e tutoriais
cn new reference "nome"     # APIs e referências
cn new architecture "nome"  # Arquitetura e diagramas

# Gerenciar projeto
cn scan                     # Escanear e conectar documentos
cn demo                     # Ver demonstração completa
cn validate                 # Validar qualidade
cn help                     # Ver todos os comandos
```

## 🎯 Tipos de Documento

- **📋 Decisões**: ADRs, escolhas técnicas, trade-offs
- **⚙️ Processos**: Runbooks, tutoriais, procedimentos
- **📖 Referências**: APIs, documentação técnica, specs
- **🏗️ Arquitetura**: Diagramas, componentes, fluxos
- **🔍 Análises**: Debugging, investigações, métricas
- **📅 Planejamento**: Roadmaps, sprints, projetos

## 🔧 Como Funciona

### 1. **Templates Inteligentes**

Cada documento segue estrutura padronizada com metadados que conectam automaticamente

### 2. **Busca Inteligente**

Funciona de qualquer subdiretório - sempre encontra seu `.context-navigator/`

### 3. **IA Contextualizada**

Via `context.rule` e `context-map/` - IA sempre sabe o estado do seu projeto

### 4. **Validação Automática**

Detecta problemas, conflitos e sugere melhorias

## 📚 Documentação

- **⚡ [Guia Rápido](QUICK_START.md)** - 15 minutos para dominar
- **⚙️ [Manual de Instalação](INSTALL.md)** - Todas as opções
- **📖 [Manual Completo](docs/MANUAL_HUMANO.md)** - Guia detalhado
- **🤖 [Manual da IA](docs/MANUAL_IA.md)** - Para sistemas de IA
- **🎯 [Exemplos](examples/)** - Casos de uso reais

## 🎁 O que você ganha?

- ✅ **Documentação sempre conectada** - sem perder contexto
- ✅ **IA sempre contextualizada** - prompts mais eficientes
- ✅ **Templates padronizados** - consistência automática
- ✅ **Busca inteligente** - funciona de qualquer lugar
- ✅ **Validação automática** - detecta problemas antes

## 🔧 Requisitos

- Python 3.7+
- ~200KB de espaço
- Nenhuma dependência externa

## 🤝 Contribuindo

Contribuições são bem-vindas! Abra uma [issue](https://github.com/gen-ge/metamodel/issues) ou envie um pull request.

## 📄 Licença

[MIT License](LICENSE) - Use como quiser!

---

**🚀 Transforme sua documentação em navegação inteligente!**

📧 **Suporte:** [Issues](https://github.com/gen-ge/metamodel/issues) | 💬 **Discussões:** [GitHub Discussions](https://github.com/gen-ge/metamodel/discussions)
