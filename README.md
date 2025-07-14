# 🧭 Context Navigator

> Sistema de documentação context-aware para parceria humano-IA

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-stable-green.svg)]()

## 🎯 Sobre o Projeto

O **Context Navigator** é uma metodologia de documentação que revoluciona como você mantém contexto em projetos complexos, especializando-se na parceria humano-IA através de estruturas padronizadas e automação inteligente.

## 🚀 Instalação

### 🌐 Instalação Global (Recomendada)

```bash
# Opção 1: Script automático
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# Opção 2: Download manual
wget https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*
python3 install.py --global

# Configurar PATH
export PATH="$HOME/.local/bin:$PATH"
```

### 📁 Instalação Local

```bash
# Download e instalação
wget https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*
python3 install.py

# Usar no projeto
cd seu-projeto/
python3 install.py
```

## 📋 Como Usar

### 🌐 Com Instalação Global

```bash
# Usar de qualquer diretório
cn scan                          # Escanear documentos
cn demo                          # Demonstração completa
cn new decision "nome-decisao"   # Criar nova decisão
cn new process "nome-processo"   # Criar novo processo
cn validate                      # Validar métricas
cn help                          # Ver todos os comandos
```

### 📁 Com Instalação Local

```bash
# Instalar no projeto
cd seu-projeto/
python3 path/to/install.py

# Usar os comandos
python3 -m context_navigator.cn_cli scan
python3 -m context_navigator.cn_cli demo
python3 -m context_navigator.cn_cli new decision "nome"
python3 -m context_navigator.cn_cli help
```

## 🔍 Busca Inteligente

O Context Navigator agora busca automaticamente por `.context-navigator/` em:

- Diretório atual
- Diretórios pais (busca recursiva)
- Permite usar de qualquer subdiretório do projeto

```bash
# Exemplo prático
projeto/
├── .context-navigator/        # Instalação local
├── src/
│   └── components/
└── docs/

# Funciona de qualquer lugar:
cd projeto/src/components/
cn scan                        # ✅ Encontra automaticamente
cn new decision "componente"   # ✅ Cria no local correto
```

## 🎯 Sistema Instalado

### 📁 Estrutura Local

```
seu-projeto/
├── .context-navigator/        # 🔧 Sistema completo (~200KB)
│   ├── scripts/              # Scripts do sistema
│   ├── templates/            # Templates disponíveis
│   ├── docs/                 # Documentação
│   └── examples/             # Exemplos
├── .context-map/             # 🗺️ Dados gerados
│   ├── index.yml            # Índice principal
│   ├── connections.yml      # Conexões entre documentos
│   └── conflicts.yml        # Conflitos detectados
└── docs/                     # 📝 Seus documentos
    ├── decisions/            # Decisões arquiteturais
    ├── processes/            # Processos e workflows
    ├── references/           # Referências e APIs
    └── architecture/         # Documentação de arquitetura
```

### 🌐 Estrutura Global

```
~/.local/share/context-navigator/    # Sistema global
~/.local/bin/cn                      # Launcher global
[workspace]/.context-navigator/      # Instalações locais
```

## 🏗️ Estrutura de Desenvolvimento

### Para Desenvolvedores

```
context-navigator/
├── src/                      # 📁 Código fonte
│   └── context_navigator/    # Pacote principal
│       ├── scripts/          # Scripts do sistema
│       ├── templates/        # Templates de documentos
│       ├── installer/        # Módulo de instalação
│       └── core/             # Funcionalidades principais
├── docs/                     # 📚 Documentação do projeto
├── examples/                 # 🎯 Exemplos práticos
├── build.py                  # 🔧 Script de build
├── requirements.txt          # 📦 Dependências
└── README.md                 # 📖 Este arquivo
```

## 📚 Documentação

- [⚡ Guia de Início Rápido](QUICK_START.md) - 15 minutos
- [⚙️ Manual de Instalação](INSTALL.md) - Todas as opções
- [🌐 Instalação Global](docs/INSTALACAO_GLOBAL.md) - Uso através do PATH
- [📖 Manual Completo](docs/MANUAL_HUMANO.md) - Documentação detalhada
- [🎯 Exemplos Práticos](examples/) - Casos de uso reais

## 🔧 Desenvolvimento

### Setup do ambiente

```bash
git clone https://github.com/gen-ge/metamodel.git
cd metamodel
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Testar
python3 src/context_navigator/cn_cli.py help
```

### Build do projeto

```bash
# Gerar pacotes
python3 build.py --version 1.0.x

# Testar instalação
cd dist/
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*
python3 install.py --global
```

## 🎯 Vantagens

### ✅ Facilidade de Uso

- **Comando simples**: `cn` ao invés de comandos longos
- **Busca inteligente**: Funciona de qualquer subdiretório
- **Instalação flexível**: Local ou global

### ✅ Funcionalidades Avançadas

- **Templates padronizados**: Para decisões, processos, referências
- **Validação automática**: Detecta problemas na documentação
- **Conexões inteligentes**: Mapeia relacionamentos entre documentos
- **Métricas de qualidade**: Score de documentação

### ✅ Integração com IA

- **Regras claras**: Disciplina a IA com `context.rule`
- **Contexto automático**: Carrega `.context-map/index.yml`
- **Templates específicos**: Para cada tipo de documento

## 🔧 Requisitos

- Python 3.7+
- Nenhuma dependência externa
- ~200KB de espaço em disco

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Autores

- **Context Navigator Team** - _Desenvolvimento inicial_ - [GitHub](https://github.com/gen-ge)

## 🙏 Agradecimentos

- Comunidade Python pela excelente documentação
- Contribuidores que ajudaram a melhorar o projeto
- Beta testers que forneceram feedback valioso

---

**📧 Suporte:** Abra uma [issue](https://github.com/gen-ge/metamodel/issues) para relatar bugs ou solicitar features.

**🎯 Transforme sua documentação em navegação inteligente!**
