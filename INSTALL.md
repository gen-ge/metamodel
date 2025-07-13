# 🚀 Context Navigator - Instalação

Sistema de documentação context-aware que se instala de forma isolada em qualquer workspace.

## ⚡ **Instalação Rápida**

### **Opção 1: Script Automático (Recomendado)**

```bash
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash
```

### **Opção 2: Download Manual**

```bash
wget https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*
python3 install.py
```

### **Opção 3: Uma Linha**

```bash
wget -qO- https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz | tar -xz && cd context-navigator-* && python3 install.py
```

## ✅ **Após Instalação**

```bash
./cn help      # Ver comandos
./cn demo      # Demonstração
./cn status    # Verificar instalação
```

## 🎯 **O que Instala**

- **`.context-navigator/`** - Sistema isolado (~200KB)
- **`.context-map/`** - Dados gerados pelo sistema
- **`cn`** - Launcher principal

## 🔧 **Requisitos**

- Python 3.7+
- Nenhuma dependência externa

---

📚 **Documentação:** [README.md](README.md) | [QUICK_START.md](QUICK_START.md)
