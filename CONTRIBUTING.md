# 🤝 Contributing to Context Navigator

Obrigado por considerar contribuir para o Context Navigator! Este guia ajudará você a configurar um ambiente de desenvolvimento e entender nossa arquitetura unificada.

> **⚠️ Importante:** Este documento é sobre **desenvolvimento do próprio Context Navigator**, não sobre usar o Context Navigator para documentar seus projetos. Para usar o software, veja [README.md](README.md).

## 🚀 Quick Start para Desenvolvedores

### 1. **Fork e Clone**

```bash
# Fork no GitHub primeiro, depois:
git clone https://github.com/SEU-USERNAME/metamodel.git
cd metamodel
```

### 2. **Setup de Desenvolvimento (Zero dependências)**

```bash
# O Context Navigator tem um sistema de desenvolvimento especial
# que não requer instalação no sistema

# Script de desenvolvimento (substitui `cn` durante desenvolvimento)
chmod +x cndev.sh

# Testar funcionamento imediato
./cndev.sh help
```

### 3. **Diferença: Desenvolvimento vs Produção**

**Por que `./cndev.sh` existe?**

- **🎯 Produção**: Usuários instalam com `python3 install.py` → comando `cn` no PATH
- **🛠️ Desenvolvimento**: Desenvolvedores usam `./cndev.sh` → sem precisar instalar no sistema

```bash
# ✅ DESENVOLVIMENTO (não polui o sistema)
./cndev.sh help                    # Sistema unificado para desenvolvimento
./cndev.sh init                    # Registry local: src/context_navigator/workspaces-registry.yml
./cndev.sh new decision "teste"    # Comandos nativos funcionando

# ✅ PRODUÇÃO (depois de instalar)
cn help                           # Sistema idêntico, mas instalado
cn init                           # Registry global: ~/.local/share/context-navigator/
cn new decision "teste"           # Mesmo comportamento
```

### 4. **Workflow de Desenvolvimento**

```bash
# Desenvolver funcionalidades
./cndev.sh init                    # Inicializar workspace de desenvolvimento
./cndev.sh new decision "nova-feature"  # Testar comandos
./cndev.sh scan                    # Testar scripts

# Testar instalação
python3 src/context_navigator/installer/install.py --dry-run
python3 src/context_navigator/installer/install.py --path /tmp/test

# Validar mudanças
./test_e2e.sh                     # Teste end-to-end completo
```

## 🎯 Arquitetura Unificada - Como Funciona

### **Princípio: Um Sistema, Dois Modos**

O Context Navigator tem arquitetura cristalina com **um sistema que funciona em dois modos**:

#### **🛠️ Modo Desenvolvimento (`./cndev.sh`)**

```bash
# Como funciona internamente:
./cndev.sh comando
# ↓
# 1. cndev.sh detecta: estou no diretório fonte?
# 2. Executa: python3 src/context_navigator/core/cn_global.py comando
# 3. cn_global.py detecta: modo desenvolvimento (path contém src/)
# 4. Usa registry: src/context_navigator/workspaces-registry.yml
```

#### **🎯 Modo Produção (`cn`)**

```bash
# Como funciona internalmente:
cn comando
# ↓
# 1. Launcher ~/.local/bin/cn detecta: instalação em ~/.local/share/
# 2. Executa: python3 ~/.local/share/context-navigator/core/cn_global.py comando
# 3. cn_global.py detecta: modo produção (path contém .local/share/)
# 4. Usa registry: ~/.local/share/context-navigator/workspaces-registry.yml
```

#### **🧠 Sistema Unificado: `cn_global.py`**

**Um só arquivo, comportamento determinístico:**

```python
# src/context_navigator/core/cn_global.py
class GlobalCommandRouter:
    def __init__(self):
        # Auto-detecta modo baseado no próprio path
        current_file = Path(__file__).resolve()

        if 'src/context_navigator' in str(current_file):
            # Modo desenvolvimento
            self.mode = 'development'
            self.registry_path = current_file.parent.parent / 'workspaces-registry.yml'
        else:
            # Modo produção
            self.mode = 'production'
            self.registry_path = current_file.parent.parent / 'workspaces-registry.yml'

    def route_command(self, args):
        # Mesmo código para ambos os modos!
        workspace = self.workspace_manager.detect_current_workspace()

        if workspace:
            return self._handle_workspace_command(workspace, command, args)
        else:
            return self._handle_global_command(command, args)
```

### **Registry como Fonte da Verdade**

```yaml
# DESENVOLVIMENTO: src/context_navigator/workspaces-registry.yml
workspaces:
  metamodelo-dev:
    name: metamodelo
    path: /home/dev/metamodelo
    status: active

# PRODUÇÃO: ~/.local/share/context-navigator/workspaces-registry.yml
workspaces:
  projeto-usuario:
    name: meu-projeto
    path: /home/user/meu-projeto
    status: active
```

**Comportamento idêntico, registries separados!**

## 🛠️ Estrutura do Projeto

```
metamodelo/
├── src/context_navigator/           # 📦 O software que desenvolvedores usam
│   ├── core/                       # 🧠 CONTROLE (entry point, roteamento)
│   │   ├── cn_global.py            # ⭐ Sistema unificado (desenvolvimento + produção)
│   │   ├── workspace_manager.py    # Detecção de workspace via registry
│   │   └── daemon_manager.py       # Gerenciamento de daemon
│   ├── scripts/                    # ⚙️ EXECUÇÃO (processamento especializado)
│   │   ├── engines/                # 🔄 Engines de processamento
│   │   │   ├── context_scanner.py     # Scanner de código/documentação
│   │   │   └── context_engine.py      # Engine de processamento contextual
│   │   ├── validation/             # ✅ Validação de qualidade
│   │   ├── analysis/               # 📊 Análise avançada
│   │   └── tools/                  # 🛠️ Ferramentas utilitárias
│   ├── templates/                  # 📄 Templates de documentação
│   ├── installer/                  # 📦 Sistema de instalação
│   │   └── install.py              # Instalador unificado
│   └── workspaces-registry.yml     # 📋 Registry local (desenvolvimento)
├── docs/                           # 📚 Documentação do projeto
├── tests/                          # 🧪 Testes automatizados
├── cndev.sh                        # 🛠️ Script de desenvolvimento
├── test_e2e.sh                     # 🧪 Teste end-to-end completo
├── build.py                        # 🏗️ Build simplificado
└── Makefile                        # 🎯 Interface de build
```

### **Separação Clara: Controle vs Execução**

#### **🧠 `core/` - CONTROLE**

- **cn_global.py**: Entry point único, detecta modo, roteia comandos
- **workspace_manager.py**: Detecta workspace via registry, gerencia estado
- **daemon_manager.py**: Controla daemon de monitoramento

#### **⚙️ `scripts/` - EXECUÇÃO**

- **engines/**: Processamento pesado (scanner, context engine)
- **validation/**: Validadores de consistência e qualidade
- **analysis/**: Análise de padrões, conflitos, impacto
- **tools/**: Ferramentas específicas (explorer, demo)

**Princípio**: `core/` decide o que fazer, `scripts/` executa como fazer.

## 📝 Comandos de Desenvolvimento

### **Comandos Básicos (substitui `cn` durante desenvolvimento)**

```bash
# Sistema básico
./cndev.sh help                    # Ajuda do sistema unificado
./cndev.sh version                 # Versão atual

# Workspace de desenvolvimento
./cndev.sh init                    # Registrar diretório atual como workspace
./cndev.sh info                    # Informações do workspace
./cndev.sh remove                  # Remover workspace do registry
```

### **Comandos Nativos (implementados em `cn_global.py`)**

```bash
# Templates e criação de documentos
./cndev.sh templates               # Listar templates disponíveis
./cndev.sh new decision "teste"    # Criar decisão técnica (ADR)
./cndev.sh new process "teste"     # Criar processo/runbook
./cndev.sh new reference "teste"   # Criar documentação de API
./cndev.sh new architecture "teste" # Criar diagrama de arquitetura
./cndev.sh new analysis "teste"    # Criar análise técnica
./cndev.sh new planning "teste"    # Criar planejamento/roadmap
```

### **Scripts Especializados (executam em `scripts/`)**

```bash
# Análise e mapeamento
./cndev.sh scan                    # Mapear documentação/código existente
./cndev.sh validate                # Validar consistência da documentação
./cndev.sh demo                    # Demonstração interativa

# Ferramentas avançadas
./cndev.sh component explore       # Explorar componentes do código
./cndev.sh component parse         # Parser de componentes
```

### **Comandos de Desenvolvimento Específicos**

```bash
# Testar instalação sem instalar
python3 src/context_navigator/installer/install.py --dry-run
# Saída: onde seria instalado, mas não instala

# Instalar temporariamente para teste
python3 src/context_navigator/installer/install.py --path /tmp/test-install
/tmp/test-install/bin/cn help      # Testar instalação
rm -rf /tmp/test-install           # Limpar teste

# Teste end-to-end completo
./test_e2e.sh                     # 30 testes automatizados
```

## 🧪 Sistema de Testes

### **Teste End-to-End Automatizado**

```bash
# Valida toda a funcionalidade de forma automatizada
./test_e2e.sh

# O teste simula um usuário completo:
# ✅ 1. Instala o sistema temporariamente
# ✅ 2. Inicializa um workspace
# ✅ 3. Cria todos os tipos de documento
# ✅ 4. Testa comandos de análise
# ✅ 5. Valida funcionamento em subdiretórios
# ✅ 6. Testa comportamento fora de workspace
# ✅ 7. Limpa tudo automaticamente
```

### **Ciclo de Desenvolvimento com Testes**

```bash
# 1. Fazer mudança no código
# nano src/context_navigator/core/cn_global.py
# code src/context_navigator/core/cn_global.py  # VS Code
# gedit src/context_navigator/core/cn_global.py # Editor gráfico

# 2. Testar localmente com desenvolvimento
./cndev.sh init
./cndev.sh new decision "teste-mudanca"

# 3. Validar com teste completo
./test_e2e.sh
# Deve passar: "✅ Todos os 30 testes passaram!"

# 4. Testar instalação real
python3 src/context_navigator/installer/install.py --path /tmp/test
/tmp/test/bin/cn help
rm -rf /tmp/test

# 5. Commit da mudança
git add .
git commit -m "feat: minha mudança"
```

### **Debug de Problemas**

```bash
# Modo debug para desenvolvimento
export CN_DEBUG=1
./cndev.sh scan                   # Ver prints de debug

# Verificar registry local
cat src/context_navigator/workspaces-registry.yml

# Testar detecção de workspace
./cndev.sh info                   # Deve mostrar workspace atual
```

## 🔧 Build e Distribuição

### **Sistema de Build Simplificado**

```bash
# Interface simples via Makefile
make help                         # Ver comandos disponíveis
make build                        # Build completo
make test                         # Executar testes
make clean                        # Limpar arquivos temporários

# Build direto (caso o Makefile não funcione)
python3 build.py                  # Script simplificado (120 linhas)
```

### **Instalador Unificado**

```bash
# O instalador funciona para desenvolvimento E produção
python3 src/context_navigator/installer/install.py

# Opções do instalador:
--global          # Instalar globalmente (padrão: ~/.local/share/)
--path /custom    # Instalar em local customizado
--dry-run         # Apenas mostrar onde instalaria
--force           # Forçar reinstalação
```

## 🎯 Áreas de Contribuição

### **🔥 Prioridades Altas**

- 🐛 **Bug fixes no sistema unificado** - cn_global.py é crítico
- 🧪 **Expandir testes E2E** - Mais cenários no test_e2e.sh
- 📚 **Manter documentação atualizada** - README, CONTRIBUTING, etc.
- 🚀 **Otimizar performance** - cn_global.py e workspace_manager.py

### **💡 Funcionalidades Novas**

- 🤖 **Templates com lógica** - Templates que se adaptam ao contexto
- 📊 **Registry management avançado** - Comandos para gerenciar workspaces
- 🔌 **Sistema de plugins** - Extensões para o cn_global.py
- 🌐 **Multi-registry** - Suporte a múltiplos registries

### **🎨 Melhorias de Sistema**

- 📱 **CLI mais intuitivo** - Melhorar UX do cn_global.py
- ⚡ **Performance otimizada** - Acelerar detecção de workspace
- 🔍 **Ferramentas de debug** - Melhor debugging do registry
- 📦 **Packaging avançado** - Distribuição via PyPI

## 📋 Processo de Pull Request

### **Antes de Submeter**

```bash
# 1. Validar sistema de desenvolvimento
./cndev.sh help                   # Sistema funciona?
./cndev.sh init                   # Registry local funciona?
./cndev.sh new decision "teste-pr" # Comandos nativos funcionam?

# 2. Executar teste completo
./test_e2e.sh                    # Deve passar todos os 30 testes
# ✅ Esperado: "Todos os testes passaram!"

# 3. Testar instalação
python3 src/context_navigator/installer/install.py --dry-run
# ✅ Esperado: mostra onde seria instalado

# 4. Cleanup de arquivos de teste
rm -rf .cn_model/docs/decisions/teste-pr.md
git status                        # Verificar que não há arquivos não versionados
```

### **Checklist de PR**

```markdown
## 🎯 Objetivo

Descreva o que esta PR resolve/adiciona no Context Navigator

## 🛠️ Mudanças no Sistema

- [ ] `cn_global.py`: [descrever mudanças no sistema unificado]
- [ ] `workspace_manager.py`: [mudanças no gerenciamento de workspace]
- [ ] `installer/install.py`: [mudanças no instalador]
- [ ] Templates: [novos/modificados templates]
- [ ] Scripts: [mudanças em engines/tools/validation]

## 🧪 Validação Executada

- [ ] `./cndev.sh help` funciona corretamente
- [ ] `./cndev.sh init` e comandos básicos funcionam
- [ ] `./cndev.sh new decision teste` cria documento
- [ ] `./test_e2e.sh` passa todos os 30 testes
- [ ] `python3 install.py --dry-run` executa sem erro
- [ ] Testado em Python 3.7+ (se possível)

## 📋 Tipo de Mudança

- [ ] 🐛 Bug fix (não quebra funcionalidade existente)
- [ ] ✨ Nova funcionalidade (não quebra funcionalidade existente)
- [ ] 💥 Breaking change (mudança que quebra funcionalidade existente)
- [ ] 📚 Documentação (mudança apenas de documentação)
- [ ] 🧪 Testes (mudança apenas de testes)

## 🎯 Impacto

- **Sistema unificado**: [como afeta cn_global.py]
- **Compatibilidade**: [mantém compatibilidade com workspaces existentes?]
- **Performance**: [impacto na velocidade de execução]
```

### **Revisão Focada**

Focamos a revisão em:

- **✅ Sistema unificado**: Não introduz duplicação ou confusão
- **✅ Registry consistency**: Mantém comportamento determinístico
- **✅ Testes E2E**: Mudanças passam em todos os 30 testes
- **✅ Backward compatibility**: Não quebra workspaces existentes
- **✅ Performance**: Não degrada velocidade do sistema

## 🌟 Estado Atual - Sistema Cristalino

### **✅ Arquitetura Unificada Concluída**

- ✅ **cn_global.py**: Sistema único para desenvolvimento + produção
- ✅ **Registry determinístico**: Detecção baseada em arquivo, não busca hierárquica
- ✅ **Comandos nativos integrados**: new, templates, info implementados nativamente
- ✅ **Sistema legacy eliminado**: cn_cli_legacy.py removido completamente
- ✅ **Instalador unificado**: install.py funciona para todos os cenários
- ✅ **Teste E2E completo**: 30 testes validando toda funcionalidade

### **📊 Métricas de Qualidade**

- 🧪 **Testes E2E**: 30/30 passando (100%)
- ⚡ **Sistema unificado**: 1 implementação (antes: 2 sistemas confusos)
- 📋 **Registry consistency**: 100% determinístico via arquivo
- 🚀 **Zero dependências**: Funciona apenas com Python padrão
- 🎯 **Zero legacy**: Sistema completamente limpo

### **🔄 Fluxo de Desenvolvimento Estável**

```bash
# Ciclo confiável e rápido
./cndev.sh comando → modificar código → ./test_e2e.sh → commit
```

## 📞 Comunicação e Suporte

### **Canais Oficiais**

- 🐛 **[Issues](https://github.com/gen-ge/metamodel/issues)** - Bugs e problemas específicos
- 💬 **[Discussions](https://github.com/gen-ge/metamodel/discussions)** - Discussões sobre arquitetura e funcionalidades
- 📧 **Email direto**: Para questões sensíveis sobre segurança

### **Guidelines de Comunicação**

- **🇧🇷 Português primeiro** - Idioma principal do projeto, English welcome
- **🎯 Sistema unificado** - Sempre referencie cn_global.py como centro
- **📋 Registry-first thinking** - Pense em termos de registry, não busca hierárquica
- **🧪 Test-driven** - Mudanças devem ser validadas com test_e2e.sh

### **Respondemos Rapidamente Para:**

- ❓ Dúvidas sobre arquitetura unificada
- 🐛 Bugs que quebram test_e2e.sh
- 💡 Ideias para melhorar cn_global.py
- 📚 Sugestões de documentação

## 🎁 Benefícios para Contribuidores

### **📚 Aprendizado Técnico**

- **🏗️ Arquitetura sistema único**: Como unificar desenvolvimento + produção
- **🐍 Python avançado**: Registry-based programming, auto-detection patterns
- **📋 CLI design**: Como criar interfaces determinísticas e intuitivas
- **🚀 Instalação portável**: Como criar systems que funcionam anywhere

### **🌟 Reconhecimento**

- 🏆 **Contributors.md**: Todos os contribuidores listados
- 🎉 **Release notes**: Contribuições destacadas em releases
- 📈 **Portfolio real**: Sistema em produção usado por desenvolvedores
- 🤝 **Network profissional**: Conectar com outros desenvolvedores

### **💼 Experience Valiosa**

- **System design**: Arquitetura crystal clear
- **User experience**: CLI design focado no usuário
- **Testing strategy**: Test-driven development com E2E
- **Documentation**: Como manter docs sempre atualizadas

---

## 🚀 Começar a Contribuir Agora

```bash
# Setup instantâneo (sem poluir seu sistema)
git clone https://github.com/SEU-USERNAME/metamodel.git
cd metamodel

# Testar sistema de desenvolvimento
./cndev.sh help
./cndev.sh init
./cndev.sh new decision "minha-primeira-contribuicao"

# Validar que tudo funciona
./test_e2e.sh

# Começar a explorar o código
# nano src/context_navigator/core/cn_global.py  # Editor de terminal
# code src/context_navigator/core/cn_global.py  # VS Code
# gedit src/context_navigator/core/cn_global.py # Editor gráfico
# ← O coração do sistema
```

**Bem-vindo ao desenvolvimento do futuro da documentação técnica!** 🎉

### **Próximos Passos Sugeridos:**

1. 📖 **Ler o código**: Começar por `cn_global.py` para entender o fluxo
2. 🧪 **Executar testes**: Rodar `./test_e2e.sh` para ver como tudo funciona
3. 🎯 **Escolher issue**: Pegar uma [good first issue](https://github.com/gen-ge/metamodel/labels/good%20first%20issue)
4. 💡 **Experimentar**: Criar pequenas mudanças e testar com `./cndev.sh`

---

📧 **Dúvidas sobre desenvolvimento?** Abra uma [Issue](https://github.com/gen-ge/metamodel/issues) ou [Discussion](https://github.com/gen-ge/metamodel/discussions) - estamos aqui para ajudar com a arquitetura!

📖 **Quer usar o Context Navigator?** Veja [README.md](README.md) para instruções de uso.
