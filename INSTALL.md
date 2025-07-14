# 🚀 Context Navigator - Instalação

Sistema de documentação context-aware que se instala de forma isolada em qualquer workspace.

**Novidades:** 🌐 Instalação global, 🔍 busca inteligente, 📱 comando `cn`

## ⚡ **Instalação Rápida**

### **🌐 Opção 1: Instalação Global (Recomendada)**

```bash
# Script automático com instalação global
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# Adicionar ao PATH (permanente)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Testar instalação
cn help
cn status
```

### **📁 Opção 2: Instalação Local**

```bash
# Download manual
wget https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*

# Instalar no projeto atual
python3 install.py
```

### **🔗 Opção 3: Uma Linha (Local)**

```bash
wget -qO- https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz | tar -xz && cd context-navigator-* && python3 install.py
```

## 🎯 **Escolhendo o Tipo de Instalação**

### **🌐 Instalação Global**

**Vantagens:**

- ✅ Comando `cn` disponível em qualquer lugar
- ✅ Busca automática por `.context-navigator/` em diretórios pais
- ✅ Pode trabalhar em múltiplos projetos facilmente
- ✅ Não precisa lembrar comandos longos

**Uso:**

```bash
# Funciona de qualquer diretório
cd /qualquer/projeto/
cn scan
cn new decision "nome"
cn demo
```

### **📁 Instalação Local**

**Vantagens:**

- ✅ Isolamento total por projeto
- ✅ Controle de versão independente
- ✅ Sem dependências globais

**Uso:**

```bash
# Funciona apenas no projeto instalado
python3 -m context_navigator.cn_cli scan
python3 -m context_navigator.cn_cli new decision "nome"
python3 -m context_navigator.cn_cli demo
```

## 🔍 **Busca Inteligente**

Ambas as instalações agora têm **busca inteligente automática**:

```bash
# Estrutura de projeto
projeto/
├── .context-navigator/     # Instalação (local ou dados)
├── src/
│   └── components/
├── docs/
└── tests/

# Funciona de qualquer subdiretório:
cd projeto/src/components/
cn scan                     # ✅ Encontra automaticamente
cn new decision "nome"      # ✅ Cria no local correto
```

**Como funciona:**

1. Busca `.context-navigator/` no diretório atual
2. Se não encontrar, busca nos diretórios pais
3. Se não encontrar localmente, usa instalação global
4. Sempre cria documentos no local correto

## 📦 **Instalação Detalhada**

### **🌐 Instalação Global Passo a Passo**

```bash
# 1. Download do pacote
wget https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz

# 2. Extrair
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*

# 3. Instalar globalmente
python3 install.py --global

# 4. Configurar PATH
export PATH="$HOME/.local/bin:$PATH"

# 5. Tornar permanente
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# 6. Testar
cn help
```

### **📁 Instalação Local Passo a Passo**

```bash
# 1. Download do pacote
wget https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz

# 2. Extrair
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*

# 3. Ir para seu projeto
cd /caminho/para/seu/projeto

# 4. Instalar localmente
python3 /caminho/para/context-navigator-*/install.py

# 5. Testar
python3 -m context_navigator.cn_cli help
```

## ✅ **Verificação da Instalação**

### **🌐 Instalação Global**

```bash
# Verificar comando
which cn
# Deve mostrar: ~/.local/bin/cn

# Verificar versão
cn version

# Verificar funcionamento
cn status
# Em diretório sem .context-navigator/: usa instalação global
# Em diretório com .context-navigator/: usa instalação local
```

### **📁 Instalação Local**

```bash
# Verificar estrutura
ls -la .context-navigator/
# Deve mostrar: scripts/, templates/, docs/, etc.

# Verificar funcionamento
python3 -m context_navigator.cn_cli status
# Deve mostrar: ✅ Context Navigator encontrado
```

## 🎯 **O que é Instalado**

### **🌐 Instalação Global**

```bash
~/.local/share/context-navigator/    # Sistema completo
├── scripts/                         # Scripts do sistema
├── templates/                       # Templates de documentos
├── docs/                           # Documentação
├── examples/                       # Exemplos
├── cn_cli.py                       # CLI principal
├── context.rule                    # Regras para IA
└── .contextrc                      # Configurações

~/.local/bin/cn                     # Launcher global
```

### **📁 Instalação Local**

```bash
.context-navigator/                 # Sistema completo (~200KB)
├── scripts/                        # Scripts do sistema
├── templates/                      # Templates de documentos
├── docs/                          # Documentação
├── examples/                      # Exemplos
├── cn_cli.py                      # CLI principal
├── context.rule                   # Regras para IA
└── .contextrc                     # Configurações

.context-map/                      # Dados gerados
├── index.yml                      # Índice principal
├── connections.yml                # Conexões
└── conflicts.yml                  # Conflitos
```

## 🔧 **Requisitos**

### **Sistema**

- Python 3.7+
- Sistema Unix/Linux/macOS ou Windows com Git Bash
- ~200KB de espaço em disco

### **Dependências**

- **Nenhuma dependência externa!**
- Usa apenas bibliotecas padrão do Python

### **Ferramentas para Download**

- `wget` ou `curl`
- `tar`
- `bash` (para script automático)

## 🛠️ **Configuração Avançada**

### **🌐 Configurar PATH Permanente**

**Bash/Zsh:**

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Fish:**

```bash
echo 'set -x PATH $HOME/.local/bin $PATH' >> ~/.config/fish/config.fish
```

**Zsh:**

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### **🔗 Alternativas de Instalação Global**

**Opção 1: Link Simbólico**

```bash
# Instalar localmente primeiro
python3 install.py

# Criar link global
sudo ln -s $(pwd)/.context-navigator/scripts/cn_global_launcher.py /usr/local/bin/cn
```

**Opção 2: Copiar Launcher**

```bash
# Instalar localmente primeiro
python3 install.py

# Copiar launcher para PATH
cp .context-navigator/scripts/cn_global_launcher.py ~/.local/bin/cn
chmod +x ~/.local/bin/cn
```

## 📊 **Comparação das Opções**

| Característica                 | Global | Local                                 |
| ------------------------------ | ------ | ------------------------------------- |
| **Comando**                    | `cn`   | `python3 -m context_navigator.cn_cli` |
| **Funciona de qualquer lugar** | ✅     | ❌                                    |
| **Busca inteligente**          | ✅     | ✅                                    |
| **Isolamento por projeto**     | ❌     | ✅                                    |
| **Fácil de usar**              | ✅     | ⚠️                                    |
| **Configuração**               | PATH   | Nenhuma                               |

## 🔧 **Troubleshooting**

### **Comando `cn` não encontrado**

```bash
# Verificar PATH
echo $PATH | grep -o "$HOME/.local/bin"

# Adicionar se não estiver
export PATH="$HOME/.local/bin:$PATH"

# Verificar arquivo
ls -la ~/.local/bin/cn
```

### **Erro de permissão**

```bash
# Tornar executável
chmod +x ~/.local/bin/cn

# Verificar permissões
ls -la ~/.local/bin/cn
```

### **Python não encontrado**

```bash
# Verificar versão
python3 --version

# Instalar Python se necessário (Ubuntu/Debian)
sudo apt update
sudo apt install python3
```

### **Instalação não funciona**

```bash
# Verificar arquivos
ls -la .context-navigator/

# Reinstalar
rm -rf .context-navigator/
python3 install.py

# Ou global
rm -rf ~/.local/share/context-navigator/
rm ~/.local/bin/cn
python3 install.py --global
```

## 🎯 **Próximos Passos**

### **📚 Após Instalação**

1. **Testar funcionamento**

   ```bash
   cn help                    # Global
   # ou
   python3 -m context_navigator.cn_cli help  # Local
   ```

2. **Criar primeiro documento**

   ```bash
   cn new decision "minha-decisao"
   ```

3. **Explorar funcionalidades**
   ```bash
   cn demo
   cn scan
   cn validate
   ```

### **📖 Documentação**

- [⚡ Guia de Início Rápido](QUICK_START.md) - 15 minutos
- [🌐 Instalação Global](docs/INSTALACAO_GLOBAL.md) - Uso através do PATH
- [📖 Manual Completo](docs/MANUAL_HUMANO.md) - Documentação detalhada
- [🎯 Exemplos Práticos](examples/) - Casos de uso reais

---

**🎯 Transforme sua documentação em navegação inteligente!**

**📧 Suporte:** Abra uma [issue](https://github.com/gen-ge/metamodel/issues) para problemas de instalação.
