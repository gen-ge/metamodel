# 🧭 Context Navigator 2.0

> Sistema inteligente de documentação contextual que funciona globalmente

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-production--ready-brightgreen.svg)]()

## 🎯 O que é o Context Navigator?

**Context Navigator 2.0** é um sistema revolucionário de documentação que:

- **🌐 Funciona globalmente** - Use `cn` de qualquer diretório
- **🔍 Busca inteligente** - Encontra workspaces automaticamente
- **🧩 Conecta documentação com código** - Links bidirecionais
- **📋 Templates padronizados** - Estruturas prontas para tudo
- **⚡ Validação automática** - Detecta problemas em tempo real

## 🚀 Instalação (1 Comando)

```bash
# Instalar globalmente (funciona de qualquer lugar)
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# Adicionar ao PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Testar instalação
cn help
```

## ⚡ Primeiros Passos

### **1. Inicializar Workspace**

```bash
cd seu-projeto/
cn init                    # Configura workspace
cn scan                    # Mapeia documentação existente
```

### **2. Criar Documentação**

```bash
# Templates principais
cn new decision "escolha-banco-dados"      # Decisões técnicas (ADRs)
cn new process "deploy-producao"           # Processos e runbooks
cn new reference "api-usuarios"            # APIs e referências
cn new architecture "microservicos"       # Arquitetura e diagramas

# Resultado: documentos padronizados em docs/
```

### **3. Trabalhar Globalmente**

```bash
# Funciona de qualquer lugar no projeto!
cd projeto/                     # cn scan ✅
cd projeto/src/                 # cn scan ✅ (busca automaticamente)
cd projeto/src/components/      # cn scan ✅ (busca em ../)
```

## 📋 Comandos Essenciais

### **Documentação**

```bash
cn new decision "nome"          # Decisões técnicas (ADRs)
cn new process "nome"           # Processos e runbooks
cn new reference "nome"         # APIs e documentação técnica
cn new architecture "nome"      # Arquitetura e diagramas
```

### **Validação**

```bash
cn validate                     # Validar todos os documentos
cn scan                         # Mapear documentação
cn demo                         # Demonstração interativa
cn status                       # Status do workspace
```

### **Exploração**

```bash
cn explore                      # Explorar componentes
cn conflicts                    # Detectar conflitos
cn metrics                      # Métricas de qualidade
```

## 🧩 Sistema de Componentização

### **Conectando Documentação ↔ Código**

```python
# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component user-authentication
# @cn:doc decisions/auth-architecture.md
# @cn:context-level c2_module
# @cn:context-type core
# ============================================

class UserAuthenticator:
    """Sistema de autenticação integrado ao Context Navigator"""
    pass
```

### **Níveis de Contexto**

- **c1_root** - Decisões de sistema (arquitetura geral)
- **c2_module** - Decisões de módulo (funcionalidades específicas)
- **c3_component** - Decisões de componente (implementação detalhada)

## 📚 Tipos de Documento

| Tipo                | Uso                      | Exemplo                        |
| ------------------- | ------------------------ | ------------------------------ |
| **📋 Decision**     | ADRs, escolhas técnicas  | "Escolha do banco de dados"    |
| **⚙️ Process**      | Runbooks, tutoriais      | "Deploy em produção"           |
| **📖 Reference**    | APIs, documentação       | "API de autenticação"          |
| **🏗️ Architecture** | Diagramas, componentes   | "Arquitetura de microserviços" |
| **🔍 Analysis**     | Debugging, investigações | "Análise de performance"       |
| **📅 Planning**     | Roadmaps, sprints        | "Roadmap Q1 2024"              |

## 💡 Exemplo Prático

```bash
# 1. Configurar projeto
cd meu-projeto/
cn init

# 2. Documentar decisão técnica
cn new decision "escolha-react-framework"
# Cria: docs/c2-modules/decisions/escolha-react-framework.md

# 3. Documentar processo
cn new process "deploy-aws"
# Cria: docs/c2-modules/processes/deploy-aws.md

# 4. Validar tudo
cn validate
# ✅ Documentos validados: 2/2
# ✅ Métricas de qualidade: 95%
```

## 🌟 Recursos Avançados

- **🔍 Busca Inteligente** - Encontra workspaces automaticamente
- **🧩 Code Bridges** - Conecta código com documentação
- **📊 Métricas de Qualidade** - Monitora qualidade da documentação
- **🤖 Validação Automática** - Detecta problemas em tempo real
- **📋 Templates Padronizados** - Estruturas consistentes
- **🌐 Funcionamento Global** - Use de qualquer diretório

## 📖 Documentação Completa

- **[📘 Manual do Usuário](docs/c1-systems/MANUAL_HUMANO.md)** - Guia completo de uso
- **[🤖 Manual para IA](docs/c1-systems/MANUAL_IA.md)** - Integração com assistentes
- **[🏗️ Arquitetura](docs/c1-systems/ARCHITECTURE_2_0_OVERVIEW.md)** - Visão técnica do sistema

## 🤝 Contribuir

Quer contribuir? Adoramos colaborações!

- **🐛 [Reportar bugs](https://github.com/gen-ge/metamodel/issues)**
- **💡 [Sugerir funcionalidades](https://github.com/gen-ge/metamodel/discussions)**
- **🛠️ [Contribuir código](CONTRIBUTING.md)** - Guia completo para desenvolvedores

### **Setup de Desenvolvimento (30s)**

```bash
git clone https://github.com/gen-ge/metamodel.git
cd metamodel && make setup

# Desenvolvimento com mudanças imediatas
./cndev.sh help
```

Ver **[CONTRIBUTING.md](CONTRIBUTING.md)** para workflow completo.

## 📄 Licença

[MIT License](LICENSE) - Use livremente em qualquer projeto!

---

## 🚀 Comece Agora!

```bash
# 1 comando para instalar
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# Usar imediatamente
cn init
cn demo
```

**Transforme sua documentação hoje mesmo!** 🎯

---

📧 **Suporte:** [Issues](https://github.com/gen-ge/metamodel/issues) | 💬 **Discussões:** [GitHub Discussions](https://github.com/gen-ge/metamodel/discussions) | 📖 **Docs:** [Manual Completo](docs/c1-systems/MANUAL_HUMANO.md)
