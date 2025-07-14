# 🧭 Context Navigator v1.0.26 - Documentação Atualizada

## 🎯 Principais Melhorias

### 🌐 Instalação Global

- **Novo:** Comando `cn` disponível globalmente
- **Novo:** Instalação em `~/.local/share/context-navigator/`
- **Melhorado:** Script de instalação com opções

### 🔍 Busca Inteligente

- **Novo:** Busca automática por `.context-navigator/` em diretórios pais
- **Melhorado:** Funciona de qualquer subdiretório do projeto
- **Melhorado:** Sempre cria documentos no local correto

### 📚 Documentação Atualizada

- **Corrigido:** README.md com instruções corretas
- **Atualizado:** QUICK_START.md com comandos que funcionam
- **Expandido:** INSTALL.md com opções globais e locais
- **Novo:** Guia de instalação global completo

## 🚀 Como Usar

### Instalação Global (Recomendada)

```bash
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash
export PATH="$HOME/.local/bin:$PATH"
cn help
```

### Instalação Local

```bash
wget https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*
python3 install.py
```

## 📦 Arquivos Disponíveis

- **`context-navigator-latest.tar.gz`** - Pacote principal
- **`install-context-navigator-latest.sh`** - Script de instalação
- **`install-context-navigator-latest.txt`** - Instalador Python

## 🔧 Compatibilidade

- Python 3.7+
- Linux/macOS/Windows (Git Bash)
- Nenhuma dependência externa

## 🎯 Vantagens

✅ **Comando simples**: `cn` ao invés de comandos longos  
✅ **Busca inteligente**: Funciona de qualquer subdiretório  
✅ **Instalação flexível**: Local ou global  
✅ **Documentação atualizada**: Instruções que funcionam

---

**📖 Documentação:** [README.md](README.md) | [QUICK_START.md](QUICK_START.md) | [INSTALL.md](INSTALL.md)
