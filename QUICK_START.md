# ⚡ Quick Start - Context Navigator (15 minutos)

## 🎯 **O que é o Context Navigator?**

Um sistema que **conecta automaticamente** sua documentação, mostrando como cada documento se relaciona com os outros.

**Resultado:** Documentação 10x mais navegável e contextualizada!

**Status:** ✅ **PRONTO PARA USO** (Score: 83.9%)

---

## 🚀 **Passo 1: Verificação (2 minutos)**

```bash
# Navegar para a pasta do projeto
cd /caminho/para/seu/metamodelo

# Verificar se funciona
python3 scripts/context_scanner.py
```

**✅ Sucesso se ver:**

- `13 documentos processados`
- `0 erros detectados`
- `Score: 83.9%`

---

## 📝 **Passo 2: Seu Primeiro Documento (5 minutos)**

### **Criar documento usando template:**

```bash
# Copiar template (escolha um)
cp templates/decisao.md minha_decisao.md
# OU
cp templates/processo.md meu_processo.md
# OU
cp templates/referencia.md minha_referencia.md
```

### **Editar metadados obrigatórios:**

```yaml
---
doc_type: "decision" # Tipo: decision, process, reference, etc.
context_level: "c2" # Nível: c1_root, c2_module, c3_component
context_type: "core" # Contexto: core, api, ui, infra, etc.
module: "authentication" # Módulo do projeto
priority: "high" # Prioridade: high, medium, low
status: "active" # Status: active, draft, deprecated
connections:
  references: ["UserService.md"] # Documentos que referencia
  impacts: ["LoginFlow.md"] # Documentos que impacta
created_date: "2025-07-13" # Data de criação
---
```

### **Escrever conteúdo seguindo o template:**

```markdown
# Título do Documento

## Contexto

(Descreva o problema/situação)

## Análise

(Analise as opções disponíveis)

## Decisão

(Qual decisão foi tomada)

## Impactos

(Quais são as consequências)
```

---

## 🔍 **Passo 3: Validar e Conectar (3 minutos)**

```bash
# Escanear novamente
python3 scripts/context_scanner.py

# Verificar se seu documento aparece
# Validar conexões
python3 scripts/metrics_validator.py
```

**✅ Sucesso se:**

- Seu documento aparece na contagem
- Score mantém > 80%
- Conexões são detectadas

---

## 💡 **Passo 4: Explorar Conexões (3 minutos)**

```bash
# Ver demonstração completa
python3 scripts/context_demo.py --full

# Analisar impacto do seu documento
python3 scripts/impact_analyzer.py --document minha_decisao.md
```

**O que vai ver:**

- Mapa de todos os documentos
- Conexões entre eles
- Contextos detectados
- Sugestões de relacionamentos

---

## 🎯 **Passo 5: Comandos Essenciais (2 minutos)**

### **Comandos que você vai usar todo dia:**

```bash
# Scanner básico (sempre use)
python3 scripts/context_scanner.py

# Validar métricas
python3 scripts/metrics_validator.py

# Demo para explorar
python3 scripts/context_demo.py --full
```

### **Templates disponíveis:**

- `decisao.md` - Para ADRs, PRDs, escolhas técnicas
- `processo.md` - Para runbooks, tutoriais, procedimentos
- `referencia.md` - Para APIs, documentação técnica
- `arquitetura.md` - Para diagramas, modelagem
- `analise.md` - Para debugging, investigações
- `planejamento.md` - Para roadmaps, sprints

---

## 📊 **Entendendo os Resultados**

### **Context Scanner:**

```bash
📄 DOCUMENTOS PROCESSADOS: 14    # +1 com seu documento
✅ VALIDAÇÃO: 0 erros            # Tudo OK
⚠️ CONFLITOS: 8                  # Normal (referências duplicadas)
```

### **Metrics Validator:**

```bash
🎯 SCORE GERAL: 83.9%           # > 80% = Aprovado
✅ MÉTRICAS APROVADAS: 7/9      # Maioria aprovada
✅ Status: PRONTO PARA PRODUÇÃO
```

---

## 🔧 **Troubleshooting Rápido**

### **Documento não aparece?**

```bash
# Verificar metadados
grep -n "doc_type:" meu_documento.md

# Deve ter todos os campos obrigatórios:
# doc_type, context_level, context_type, module
```

### **Score baixo?**

```bash
# Adicionar mais conexões
connections:
  references: ["doc1.md", "doc2.md"]
  relates_to: ["doc3.md"]
```

### **Erro nos scripts?**

```bash
# Verificar se está na pasta correta
ls scripts/    # Deve mostrar os scripts

# Testar com demo
python3 scripts/context_demo.py
```

---

## 🎯 **Próximos Passos**

### **Agora você pode:**

1. **Criar mais documentos** usando os templates
2. **Conectar documentos** existentes via `connections:`
3. **Explorar com demo** para entender relacionamentos
4. **Monitorar score** para manter qualidade

### **Para se aprofundar:**

- 📖 **GUIA_IMPLEMENTACAO.md** - Tutorial completo
- 📚 **docs/MANUAL_HUMANO.md** - Manual detalhado
- 🎯 **examples/** - Exemplos práticos
- 🔧 **scripts/** - Ferramentas avançadas

---

## 🏆 **Parabéns!**

Em 15 minutos você:

- ✅ Verificou que o sistema funciona
- ✅ Criou seu primeiro documento
- ✅ Entendeu como conectar documentos
- ✅ Aprendeu os comandos essenciais

**🚀 Agora sua documentação está 10x mais organizada e navegável!**

---

## 📞 **Ajuda Rápida**

### **Comandos de emergência:**

```bash
# Se algo der errado
python3 scripts/context_demo.py --full

# Reescanear tudo
python3 scripts/context_scanner.py
```

### **Estrutura mínima de documento:**

```yaml
---
doc_type: "decision"
context_level: "c2"
context_type: "core"
module: "meu_modulo"
---
# Título

## Conteúdo aqui
```

### **Tipos de contexto mais comuns:**

- `core` - Lógica de negócio
- `api` - Interfaces e endpoints
- `ui` - Interface de usuário
- `infra` - Infraestrutura
- `shared` - Componentes compartilhados

---

**🎯 Happy documenting! 🚀**
