# 🤖 GitHub Automations - Context Navigator

Esta pasta contém **automações do GitHub** que tornam o desenvolvimento mais eficiente!

## 📁 O que tem aqui?

### **🔄 `workflows/ci.yml`** - Testes Automáticos

Sempre que você fizer **push** ou **pull request**, o GitHub executa automaticamente:

- ✅ **Testa Python 3.7 até 3.11** - Garante compatibilidade
- ✅ **Roda `./cndev.sh`** - Testa seus comandos de desenvolvimento
- ✅ **Testa `python3 build.py`** - Verifica se build funciona
- ✅ **Testa instalação** - Verifica se pacote instala corretamente
- ✅ **Valida código** - Verifica sintaxe Python

### **📋 `ISSUE_TEMPLATE.md`** - Template para Bugs/Sugestões

Quando alguém cria uma **issue**, já vem com um formulário organizado:

- 🐛 **Bug reports** estruturados
- 💡 **Feature requests** padronizados
- 📚 **Dúvidas de documentação**

### **🔀 `PULL_REQUEST_TEMPLATE.md`** - Template para Contribuições

Quando alguém cria **pull request**, já vem com checklist:

- ✅ **Checklist de testes**
- 📝 **Descrição padronizada**
- 🧪 **Comandos para testar**

## 🚀 Release Automático (NOVO!)

### **Como funciona:**

```bash
# 1. Criar release (1 comando!)
make release-tag VERSION=2.0.8

# 2. GitHub Actions automaticamente:
# ✅ Testa tudo
# ✅ Cria build
# ✅ Cria release no GitHub
# ✅ Envia arquivos (tar.gz, zip, instaladores)
# ✅ Cria página de release bonita
```

### **Antes vs Agora:**

| **❌ Antes (manual)**           | **✅ Agora (automático)**        |
| ------------------------------- | -------------------------------- |
| `python3 build.py`              | `make release-tag VERSION=2.0.8` |
| Upload manual para GitHub       | ✅ Upload automático             |
| Criar release page manualmente  | ✅ Release page automática       |
| Testar em várias versões Python | ✅ Testes automáticos            |

## 🎯 Vantagens para Você

### **🔒 Qualidade Garantida**

- **Todo push** é testado automaticamente
- **Impossível** quebrar o build sem avisar
- **Múltiplas versões** Python testadas

### **⚡ Release Super Rápido**

- **1 comando** para lançar versão nova
- **Automático** - sem work manual
- **Profissional** - página de release bonita

### **🤝 Contribuições Facilitadas**

- **Templates** ajudam novos contribuidores
- **Padronização** automática
- **Checklist** evita erros

## 💡 Para Novatos - Como Usar?

### **🚀 Para fazer release:**

```bash
# Quando quiser lançar versão nova:
make release-tag VERSION=2.0.8

# Depois acompanhe em:
# https://github.com/gen-ge/metamodel/actions
```

### **🐛 Para reportar bug:**

1. Ir em **Issues** no GitHub
2. Clicar **New Issue**
3. Formulário já vem pronto! 📋

### **🔀 Para contribuir:**

1. Fazer suas mudanças
2. Criar **Pull Request**
3. Template já vem pronto! ✅

## 🎉 Resultado


- ✅ **CI/CD** completo
- ✅ **Release automático**
- ✅ **Templates** para colaboração
- ✅ **Qualidade** garantida

