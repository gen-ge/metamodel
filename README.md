# 🧭 Context Navigator

> Sistema de documentação context-aware para parceria humano-IA

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-stable-green.svg)]()

## 🎯 O que é?

O **Context Navigator** resolve o problema de **perda de contexto** em projetos complexos. Ele conecta automaticamente documentos, detecta relacionamentos e mantém a IA sempre contextualizada.

### 💡 Problema → Solução

| 🔴 **Problema**                                | ✅ **Solução**                          |
| ---------------------------------------------- | --------------------------------------- |
| Perda de contexto em projetos complexos        | Navegação inteligente entre documentos  |
| Retrabalho por falta de documentação conectada | Detecção automática de conexões         |
| IA descontextualizada em prompts               | Contexto automático via `.context-map/` |
| Desenvolvimento solo ineficiente               | Sugestões contextuais baseadas em IA    |

### 🎯 Para quem é?

- **Desenvolvedores solo** que precisam manter contexto em projetos complexos
- **Equipes pequenas** que documentam decisões e processos
- **Usuários de IA** que querem prompts sempre contextualizados
- **Arquitetos de software** que precisam rastrear dependências

## 🚀 Instalação (30 segundos)

```bash
# Instalação global (recomendada)
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# Usar de qualquer lugar
cn scan                          # Escanear documentos
cn demo                          # Ver demonstração
cn new decision "minha-decisao"  # Criar documento
```

## ⚡ Exemplo Prático

```bash
# 1. Instalar
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# 2. Criar primeiro documento
cn new decision "escolha_de_banco_de_dados"

# 3. Escanear e conectar
cn scan

# 4. Ver mágica acontecer
cn demo
```

## 📋 O que você ganha?

- **📝 Templates padronizados** para decisões, processos, referências
- **🔍 Busca inteligente** funciona de qualquer subdiretório
- **🤖 IA contextualizada** via regras automáticas
- **📊 Métricas de qualidade** da sua documentação
- **🔗 Conexões automáticas** entre documentos relacionados

## 🎯 Documentação Completa

- **⚡ [Guia de 15 minutos](QUICK_START.md)** - Aprenda o básico
- **⚙️ [Manual de Instalação](INSTALL.md)** - Todas as opções
- **📖 [Documentação Completa](docs/)** - Guias detalhados
- **🎯 [Exemplos Práticos](examples/)** - Casos de uso reais

## 🔧 Requisitos

- Python 3.7+
- ~200KB de espaço
- Nenhuma dependência externa

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para começar.

## 📄 Licença

[MIT License](LICENSE) - Use como quiser!

---

**🚀 Transforme sua documentação em navegação inteligente!**

📧 **Suporte:** [Issues](https://github.com/gen-ge/metamodel/issues) | 💬 **Discussões:** [GitHub Discussions](https://github.com/gen-ge/metamodel/discussions)
