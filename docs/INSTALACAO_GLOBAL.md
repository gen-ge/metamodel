# 🌐 Context Navigator - Instalação Global

## 🎯 Usar o Context Navigator de Qualquer Diretório

Agora você pode usar o Context Navigator de qualquer diretório através do PATH do sistema!

## 🚀 Métodos de Instalação

### 1. 🌐 Instalação Global (Recomendada)

```bash
# 1. Instalar globalmente
python3 install.py --global

# 2. Configurar PATH (adicione ao ~/.bashrc)
export PATH="$HOME/.local/bin:$PATH"

# 3. Recarregar o shell
source ~/.bashrc

# 4. Usar de qualquer diretório
cn scan
cn demo
cn help
```

### 2. 📁 Instalação Local + Launcher Global

```bash
# 1. Instalar localmente (método atual)
python3 install.py

# 2. Copiar launcher global para o PATH
cp .context-navigator/scripts/cn_global_launcher.py ~/.local/bin/cn
chmod +x ~/.local/bin/cn

# 3. Configurar PATH se necessário
export PATH="$HOME/.local/bin:$PATH"

# 4. Usar de qualquer diretório
cn scan
cn demo
cn help
```

### 3. 🔗 Criar Link Simbólico

```bash
# 1. Instalar localmente
python3 install.py

# 2. Criar link simbólico no PATH
sudo ln -s $(pwd)/.context-navigator/scripts/cn_global_launcher.py /usr/local/bin/cn

# 3. Usar de qualquer diretório
cn scan
cn demo
cn help
```

## 🔍 Como Funciona a Busca Inteligente

O Context Navigator agora busca automaticamente por `.context-navigator/` em:

1. **Diretório atual**: `./`
2. **Diretórios pais**: `../`, `../../`, etc.
3. **Instalação global**: `~/.local/share/context-navigator/`

### Exemplo de Uso

```bash
# Estrutura do projeto
projeto/
├── .context-navigator/     # Instalação local
├── docs/
├── src/
│   └── components/
└── tests/

# Você pode usar de qualquer lugar:
cd projeto/                 # cn scan ✅
cd projeto/src/            # cn scan ✅ (busca em ../
cd projeto/src/components/ # cn scan ✅ (busca em ../../)
cd /qualquer/lugar/        # cn scan ✅ (usa instalação global)
```

## 📋 Comandos Disponíveis

### 🌐 Com Instalação Global

```bash
cn scan                    # Escanear documentos
cn demo                    # Demonstração completa
cn validate                # Validar métricas
cn new decision nome       # Criar nova decisão
cn new process nome        # Criar novo processo
cn new reference nome      # Criar nova referência
cn help                    # Ver todos os comandos
```

### 📁 Com Instalação Local (método antigo ainda funciona)

```bash
python3 -m context_navigator.cn_cli scan
python3 -m context_navigator.cn_cli demo
python3 -m context_navigator.cn_cli validate
# etc...
```

## 🎯 Prioridade de Busca

1. **Instalação Local**: Se encontrar `.context-navigator/` no diretório atual ou pais
2. **Instalação Global**: Se não encontrar instalação local

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

## 🧪 Testando a Instalação

```bash
# Verificar se o comando está disponível
which cn

# Testar busca inteligente
cn status

# Testar funcionalidade completa
cn demo
```

## 🎯 Vantagens da Instalação Global

- ✅ **Usar de qualquer diretório**
- ✅ **Comando mais simples**: `cn` ao invés de `python3 -m context_navigator.cn_cli`
- ✅ **Busca inteligente automática**
- ✅ **Compatível com instalações locais**
- ✅ **Não interfere com o comportamento atual**

## 🔄 Migração do Método Antigo

Se você já usa o Context Navigator com o método antigo:

```bash
# Método antigo (ainda funciona)
python3 -m context_navigator.cn_cli scan

# Método novo (mais simples)
cn scan
```

Ambos os métodos funcionam simultaneamente!

## 📝 Exemplo Prático

```bash
# 1. Criar novo projeto
mkdir meu-projeto
cd meu-projeto

# 2. Instalar Context Navigator globalmente
python3 install.py --global

# 3. Inicializar projeto
cn new decision "Arquitetura do Sistema"
cn new process "Deploy em Produção"

# 4. Trabalhar de qualquer subdiretório
cd src/components/
cn scan                    # Funciona!
cn validate               # Funciona!

# 5. Trabalhar em outro projeto
cd /outro/projeto/
cn scan                   # Usa busca inteligente
```

## 🎯 Resumo

O Context Navigator agora é **muito mais flexível**:

- 🌐 **Instalação Global**: Use `cn` de qualquer lugar
- 🔍 **Busca Inteligente**: Encontra `.context-navigator/` automaticamente
- 📁 **Compatibilidade**: Métodos antigos ainda funcionam
- 🎯 **Simplicidade**: Comando mais curto e intuitivo

**Recomendação**: Use a instalação global para uma experiência mais fluida!
