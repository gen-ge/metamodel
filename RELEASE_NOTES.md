# 🧭 Context Navigator v1.1.0 - Documentação Melhorada

## 🎯 Principais Melhorias

### 📚 Documentação Completamente Reescrita

- **Novo:** README.md mais conciso e funcional
- **Corrigido:** Estrutura `context-map/` corrigida em todos os manuais
- **Melhorado:** Manual da IA com protocolos mais claros
- **Melhorado:** Manual Humano com exemplos práticos
- **Consistente:** Todos os manuais agora consistentes

### 🔧 Correções Estruturais

- **Corrigido:** Referências incorretas a `.context-map/` (agora `context-map/`)
- **Validado:** Estrutura real confirmada via instalação de teste
- **Padronizado:** Versionamento consistente em todos os arquivos
- **Melhorado:** Scripts de build com instruções claras

### 🎯 Experiência do Usuário

- **Simplificado:** README focado no essencial para começar
- **Organizado:** Comandos essenciais bem estruturados
- **Claro:** Tipos de documento bem explicados
- **Prático:** Fluxo de uso mais direto

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

### Comandos Essenciais

```bash
# Criar documentos
cn new decision "nome"      # Decisões técnicas (ADRs)
cn new process "nome"       # Processos e tutoriais
cn new reference "nome"     # APIs e referências
cn new architecture "nome"  # Arquitetura e diagramas

# Gerenciar projeto
cn scan                     # Escanear e conectar documentos
cn demo                     # Ver demonstração completa
cn validate                 # Validar qualidade
cn help                     # Ver todos os comandos
```

## 📦 Arquivos Disponíveis

- **`context-navigator-latest.tar.gz`** - Pacote principal
- **`install-context-navigator-latest.sh`** - Script de instalação automatizada
- **`test_global_install.sh`** - Script de teste da instalação

## 🔧 Estrutura Corrigida

### ✅ Estrutura Real Confirmada

```
.context-navigator/                    # Diretório principal
├── context-map/                       # Mapas de contexto (sem ponto)
│   ├── index.yml                      # Índice geral
│   ├── connections.yml                # Conexões entre documentos
│   ├── conflicts.yml                  # Conflitos detectados
│   └── architecture.yml               # Visão arquitetural
├── docs/                              # Documentos do usuário
│   ├── decisions/                     # Decisões criadas
│   ├── processes/                     # Processos criados
│   └── outros tipos...
├── scripts/                           # Scripts de ferramentas
├── templates/                         # Templates
├── cn_cli.py                          # CLI principal
├── context.rule                       # Regras para IA
└── .contextrc                         # Configurações
```

## 🎯 Compatibilidade

- Python 3.7+
- Linux/macOS/Windows (Git Bash)
- Nenhuma dependência externa

## 🎁 Vantagens da v1.1.0

✅ **Documentação profissional**: Manuais consistentes e corretos  
✅ **Experiência melhorada**: README focado no essencial  
✅ **Estrutura validada**: Testado com instalação real  
✅ **Versionamento padronizado**: Consistente em todos os arquivos  
✅ **Pronto para uso**: Versão estável e confiável

## 🔄 Migração da v1.0.x

Não há breaking changes. A migração é transparente:

```bash
# Basta reinstalar
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash
```

---

**📖 Documentação:** [README.md](README.md) | [QUICK_START.md](QUICK_START.md) | [INSTALL.md](INSTALL.md)

**🎯 Esta versão marca um marco de estabilidade e qualidade da documentação!**
