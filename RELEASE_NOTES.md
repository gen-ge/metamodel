# 🧭 Context Navigator v2.0.0 - Arquitetura Revolucionária

## 🚀 Principais Inovações

### 🏗️ Arquitetura 2.0 Completamente Nova

- **Novo:** WorkspaceManager com busca inteligente automática
- **Novo:** Comando global `cn` funciona de qualquer diretório
- **Novo:** Estrutura .cn_model/ substitui .context-map/
- **Novo:** Code Bridge (@cn:) conecta documentação ↔ código
- **Novo:** Scripts organizados por responsabilidade (core/validation/analysis/tools)
- **Novo:** Performance 67x melhor (73ms vs 5s)

### 📚 Documentação Unificada

- **Consolidado:** README.md agora é o único ponto de entrada
- **Removido:** QUICK_START.md e INSTALL.md (redundantes)
- **Atualizado:** Toda documentação para arquitetura 2.0
- **Organizado:** Estrutura docs/c1-systems/, docs/c2-modules/, docs/c3-components/
- **Melhorado:** Manual da IA e convenções atualizados

### ⚡ Performance e Usabilidade

- **67x mais rápido:** Scanner agora executa em ~73ms
- **Busca inteligente:** Detecta workspace automaticamente
- **Zero configuração:** Funciona imediatamente após instalação
- **Compatibilidade:** Suporte completo à arquitetura 1.0

## 🎯 Como Usar v2.0

### Instalação Global (Recomendada)

```bash
curl -L https://github.com/gen-ge/metamodel/releases/latest/download/install-context-navigator-latest.sh | bash
export PATH="$HOME/.local/bin:$PATH"
cn help
```

### Comandos Modernos

```bash
# Setup e gerenciamento
cn init                         # Inicializar workspace
cn status                       # Status do workspace
cn scan                         # Escanear documentos
cn demo                         # Demonstração interativa

# Criação de documentos
cn new decision "nome"          # Decisão técnica
cn new process "nome"           # Processo/runbook
cn new reference "nome"         # API/referência
cn new architecture "nome"      # Arquitetura/diagrama

# Ferramentas avançadas
cn explore                      # Explorar componentes
cn conflicts                    # Detectar conflitos
cn metrics                      # Métricas de qualidade
cn advisor                      # Sugestões inteligentes
```

## 🧩 Componentização Code Bridge

```python
# ===== CONTEXT NAVIGATOR CODE BRIDGE =====
# @cn:component user-authentication
# @cn:doc decisions/auth-architecture.md
# @cn:context-level c2_module
# @cn:context-type core
# @cn:purpose "Sistema de autenticação de usuários"
# ============================================

class UserAuthenticator:
    pass
```

## 📦 Arquivos Disponíveis

- **`context-navigator-latest.tar.gz`** - Pacote principal
- **`install-context-navigator-latest.sh`** - Script de instalação automatizada
- **`test_global_install.sh`** - Script de teste da instalação

## 🏗️ Estrutura 2.0

### ✅ Nova Arquitetura de Workspace

```
projeto/
├── .cn_model/                  # Workspace Context Navigator 2.0
│   ├── workspace.yml          # Configuração principal (substitui .contextrc)
│   ├── components/            # Componentes documentados
│   ├── templates/             # Templates personalizados
│   └── maps/                  # Mapas contextuais (substitui .context-map/)
├── docs/                      # Documentação do projeto
│   ├── decisions/            # Decisões arquiteturais
│   ├── processes/            # Processos e runbooks
│   └── outros tipos...
└── src/                       # Código fonte (com marcações @cn:)
```

### 🛠️ Scripts Organizados por Responsabilidade

```
scripts/
├── core/           # Processamento essencial (2 scripts)
├── validation/     # Validação de qualidade (3 scripts)
├── analysis/       # Análise avançada (4 scripts)
└── tools/          # Utilitários (4 scripts)
```

## 🔄 Migração da v1.x

### Automática e Transparente

```bash
# Se detectar estrutura 1.0 (.contextrc + .context-map/)
cn init  # Migra automaticamente para 2.0

# Mantém compatibilidade:
✅ Templates idênticos
✅ Metadados preservados
✅ Conexões funcionais
✅ Zero perda de dados
```

### Breaking Changes

- **Estrutura:** `.context-map/` → `.cn_model/maps/`
- **Config:** `.contextrc` → `.cn_model/workspace.yml`
- **Scripts:** Reorganizados por responsabilidade
- **CLI:** Comando global `cn` (opcional, comandos antigos funcionam)

## 🎁 Benefícios da v2.0

### Para Desenvolvedores

✅ **Comando global** `cn` disponível em qualquer lugar  
✅ **Busca inteligente** automática de workspaces  
✅ **Performance 67x melhor** - scanner de 5s para 73ms  
✅ **Componentização** conecta docs ↔ código  
✅ **Zero configuração manual**

### Para Arquitetos

✅ **Visão componentizada** do sistema completo  
✅ **Rastreabilidade** decisão → implementação  
✅ **Code Bridge** conecta arquitetura ao código  
✅ **WorkspaceManager** detecta contexto automaticamente

### Para IAs

✅ **Context.rule 2.0** com protocolos atualizados  
✅ **WorkspaceManager detection** automático  
✅ **Code Bridge** para gerar código conectado  
✅ **Templates estruturados** padronizados

## 📊 Métricas de Performance

| Métrica                 | v1.0   | v2.0   | Melhoria       |
| ----------------------- | ------ | ------ | -------------- |
| **Scanner**             | ~5s    | ~73ms  | **67x**        |
| **Workspace Detection** | Manual | ~50ms  | **Automático** |
| **Memory Usage**        | ~50MB  | ~25MB  | **2x**         |
| **Startup Time**        | ~2s    | ~300ms | **6x**         |

## 🎯 Compatibilidade

- Python 3.7+
- Linux/macOS/Windows (Git Bash)
- **100% compatível** com projetos v1.x
- **Zero dependências externas**

## 🎁 Status: Produção

✅ **0 erros críticos** reportados  
✅ **13 scripts** totalmente funcionais  
✅ **WorkspaceManager** estável e testado  
✅ **Performance** muito superior às metas  
✅ **Documentação** completa e consistente

---

**📖 Documentação Única:** [README.md](README.md) - Ponto de entrada completo

**🏗️ Esta versão marca a maturidade arquitetural do Context Navigator com busca inteligente, componentização e performance excepcional!**
