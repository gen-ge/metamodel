# 🧭 Context Navigator

**Sistema de Documentação Context-Aware para Desenvolvimento Solo**

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## 🎯 **O que é o Context Navigator?**

O Context Navigator é uma **metodologia de parceria humano-IA** que resolve o problema de perda de contexto em projetos complexos. Ele conecta automaticamente documentos, detecta relacionamentos e mantém o contexto sempre atualizado.

### **💡 Problema Resolvido**

- 🔴 **Perda de contexto** em projetos complexos
- 🔴 **Retrabalho** por falta de documentação conectada
- 🔴 **IA descontextualizada** em prompts
- 🔴 **Desenvolvimento solo ineficiente**

### **✅ Solução Entregue**

- ✅ **Navegação inteligente** entre documentos
- ✅ **Detecção automática** de contextos e conexões
- ✅ **Análise de impacto** em tempo real
- ✅ **Sugestões contextuais** baseadas em IA

---

## 🚀 **Instalação**

### **Script Automático (Recomendado)**

```bash
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash
```

### **Download Manual**

```bash
wget https://github.com/gen-ge/metamodel/releases/latest/download/context-navigator-latest.tar.gz
tar -xzf context-navigator-latest.tar.gz
cd context-navigator-*
python3 install.py
```

**📋 Detalhes:** [INSTALL.md](INSTALL.md)

---

## ⚡ **Uso Básico**

### **Comandos Essenciais**

```bash
./cn help                   # Ver todos os comandos
./cn demo                   # Demonstração completa
./cn scan                   # Escanear documentos
./cn validate               # Validar métricas
```

### **Criar Documentos**

```bash
./cn new decision nome      # Nova decisão
./cn new process nome       # Novo processo
./cn new reference nome     # Nova referência
```

### **Tutorial Completo**

📚 **[QUICK_START.md](QUICK_START.md)** - Tutorial de 15 minutos

---

## 🎯 **O que Instala**

```
seu-projeto/
├── .context-navigator/     # Sistema isolado (~200KB)
│   ├── scripts/           # Scripts funcionais
│   ├── templates/         # Templates de documentos
│   └── docs/             # Documentação
├── .context-map/          # Dados gerados
├── cn                     # Launcher principal
└── [seus arquivos]
```

---

## 📋 **Templates Disponíveis**

- **decisao.md** - ADRs, PRDs, escolhas técnicas
- **processo.md** - Runbooks, tutoriais, procedimentos
- **referencia.md** - APIs, documentação técnica
- **arquitetura.md** - Diagramas, modelagem
- **analise.md** - Debugging, investigações
- **planejamento.md** - Roadmaps, sprints

---

## 🔧 **Exemplo de Uso**

```bash
# 1. Instalar
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash

# 2. Criar primeiro documento
./cn new decision "escolha_de_banco_de_dados"

# 3. Editar metadados e conteúdo
# (preencher doc_type, context_level, etc.)

# 4. Escanear e conectar
./cn scan

# 5. Ver demonstração
./cn demo
```

---

## 🎯 **Requisitos**

- **Python 3.7+** (nenhuma dependência externa)
- **~200KB** de espaço em disco
- **Workspace** com permissões de escrita

---

## 🤝 **Contribuindo**

O Context Navigator é open source! Contribuições são bem-vindas.

### **Estrutura do Projeto**

```
├── scripts/              # Scripts funcionais
├── templates/            # Templates de documentos
├── docs/                # Documentação do sistema
├── examples/            # Exemplos práticos
└── context.rule         # Regras para IA
```

---

## 📄 **Licença**

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🚀 **Próximos Passos**

1. 📖 **Instale:** [INSTALL.md](INSTALL.md)
2. ⚡ **Aprenda:** [QUICK_START.md](QUICK_START.md) (15 minutos)
3. 🎯 **Use:** `./cn help` para comandos

**🎯 Transforme sua documentação em navegação inteligente!**
