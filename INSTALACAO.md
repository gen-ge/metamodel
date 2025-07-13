# 🚀 Context Navigator - Instalação

## 📋 **Resumo Rápido**

O Context Navigator agora pode ser instalado em qualquer workspace de forma isolada, sem interferir na estrutura do seu projeto.

### **🎯 Estrutura Instalada**

```
seu-projeto/
├── .context-navigator/          # Sistema isolado
│   ├── scripts/                 # Scripts funcionais
│   ├── templates/               # Templates de documentos
│   ├── docs/                    # Documentação
│   └── [outros arquivos]
├── .context-map/                # Dados gerados
├── cn                           # Launcher principal
└── [seus arquivos de projeto]
```

---

## 🔧 **Instalação**

### **Opção 1: Download Manual**

1. **Baixar** o pacote:

   ```bash
   wget https://github.com/[repo]/releases/download/v1.0.1/context-navigator-1.0.1.tar.gz
   ```

2. **Extrair** e instalar:
   ```bash
   tar -xzf context-navigator-1.0.1.tar.gz
   cd context-navigator-1.0.1
   python3 install.py
   ```

### **Opção 2: Instalador Automático**

1. **Baixar** e executar:
   ```bash
   curl -L https://github.com/[repo]/releases/download/v1.0.1/install-context-navigator-1.0.1.py | python3
   ```

### **Opção 3: Build Local**

1. **Clonar** o repositório:

   ```bash
   git clone [repo-url]
   cd context-navigator
   ```

2. **Gerar** e instalar:
   ```bash
   python3 build.py
   cd dist
   tar -xzf context-navigator-*.tar.gz
   cd context-navigator-*
   python3 install.py
   ```

---

## 🧪 **Teste da Instalação**

### **Verificar Status**

```bash
./cn status
```

### **Testar Sistema**

```bash
./cn demo
```

### **Criar Primeiro Documento**

```bash
./cn new decision minha_primeira_decisao
```

### **Escanear Documentos**

```bash
./cn scan
```

---

## 📋 **Comandos Principais**

### **📊 Comandos Essenciais**

```bash
cn scan                    # Escanear documentos
cn demo                    # Demonstração completa
cn validate                # Validar métricas
cn check                   # Verificar sistema
```

### **📝 Criar Documentos**

```bash
cn new decision nome       # Nova decisão
cn new process nome        # Novo processo
cn new reference nome      # Nova referência
cn new architecture nome   # Nova arquitetura
cn new analysis nome       # Nova análise
cn new planning nome       # Novo planejamento
```

### **🔧 Comandos Avançados**

```bash
cn patterns               # Detectar padrões
cn conflicts              # Detectar conflitos
cn impact                 # Analisar impacto
cn templates              # Validar templates
```

### **ℹ️ Informações**

```bash
cn help                   # Ajuda completa
cn status                 # Status da instalação
cn version                # Versão instalada
```

---

## 🔄 **Fluxo de Uso**

### **1. Instalar** (uma vez)

```bash
python3 install.py
```

### **2. Criar** documentos

```bash
./cn new decision auth_strategy
```

### **3. Escanear** regularmente

```bash
./cn scan
```

### **4. Validar** métricas

```bash
./cn validate
```

---

## 🎯 **Requisitos**

- **Python 3.7+** (nenhuma dependência externa)
- **Workspace** com permissões de escrita
- **~200KB** de espaço em disco

---

## 🔧 **Solução de Problemas**

### **Context Navigator não encontrado**

```bash
# Verificar se está instalado
ls -la .context-navigator/

# Recriar launcher se necessário
python3 .context-navigator/scripts/context_scanner.py
```

### **Comandos não funcionam**

```bash
# Verificar permissões
chmod +x cn

# Testar diretamente
python3 .context-navigator/scripts/context_scanner.py
```

### **Templates não encontrados**

```bash
# Verificar templates
ls .context-navigator/templates/

# Usar nome em português
./cn new decisao nome_documento
```

---

## 📤 **Distribuição**

### **Para Distribuidores**

1. **Fazer** fork do repositório
2. **Customizar** se necessário
3. **Gerar** build:
   ```bash
   python3 build.py --version SUA_VERSAO
   ```
4. **Publicar** arquivos da pasta `dist/`

### **Para Usuários**

1. **Baixar** pacote da release
2. **Instalar** com `python3 install.py`
3. **Usar** com `./cn`

---

## 🎉 **Conclusão**

O Context Navigator está pronto para uso em qualquer workspace!

**Próximos passos:**

1. 📖 Leia `./cn help` para comandos completos
2. 📚 Consulte `.context-navigator/README.md` para documentação
3. 🎯 Comece criando seu primeiro documento com `./cn new decision`

**🚀 Transforme sua documentação em navegação inteligente!**
