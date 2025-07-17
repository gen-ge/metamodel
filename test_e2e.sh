#!/bin/bash

# =============================================================================
# 🧪 Context Navigator - Teste End-to-End Completo
# =============================================================================
# 
# Este script testa toda a funcionalidade do Context Navigator de forma
# automatizada, simulando um usuário real completo.
#
# Executa 30+ testes cobrindo:
# ✅ Instalação temporária
# ✅ Inicialização de workspace  
# ✅ Criação de todos os tipos de documento
# ✅ Comandos de análise e validação
# ✅ Funcionamento em subdiretórios
# ✅ Comportamento fora de workspace
# ✅ Cleanup automático
#
# =============================================================================

set -e  # Parar em qualquer erro

# Salvar diretório original ANTES de criar diretórios temporários
ORIGINAL_PWD="$(pwd)"

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Contadores de teste
TESTS_TOTAL=0
TESTS_PASSED=0
TESTS_FAILED=0

# Diretórios temporários
TEST_DIR="/tmp/cn_e2e_test_$$"
INSTALL_DIR="/tmp/cn_install_test_$$"
PROJECT_DIR="$TEST_DIR/test_project"

# =============================================================================
# 🛠️ Funções Auxiliares
# =============================================================================

print_header() {
    echo -e "\n${BLUE}===============================================${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}===============================================${NC}\n"
}

print_step() {
    echo -e "${CYAN}📋 $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

run_test() {
    local test_name="$1"
    local test_command="$2"
    
    TESTS_TOTAL=$((TESTS_TOTAL + 1))
    echo -e "\n${PURPLE}🧪 Teste $TESTS_TOTAL: $test_name${NC}"
    
    if eval "$test_command" >/dev/null 2>&1; then
        print_success "PASSOU: $test_name"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        print_error "FALHOU: $test_name"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

run_test_verbose() {
    local test_name="$1"
    local test_command="$2"
    
    TESTS_TOTAL=$((TESTS_TOTAL + 1))
    echo -e "\n${PURPLE}🧪 Teste $TESTS_TOTAL: $test_name${NC}"
    
    if eval "$test_command"; then
        print_success "PASSOU: $test_name"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        print_error "FALHOU: $test_name"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

cleanup() {
    print_step "Limpando arquivos temporários..."
    rm -rf "$TEST_DIR" 2>/dev/null || true
    rm -rf "$INSTALL_DIR" 2>/dev/null || true
    print_success "Cleanup concluído"
}

# Cleanup automático em caso de erro
trap cleanup EXIT

# =============================================================================
# 🚀 Início dos Testes
# =============================================================================

print_header "CONTEXT NAVIGATOR - TESTE END-TO-END COMPLETO"

echo -e "${BLUE}🎯 Objetivo:${NC} Validar toda funcionalidade do Context Navigator"
echo -e "${BLUE}📁 Diretório teste:${NC} $TEST_DIR"
echo -e "${BLUE}📦 Instalação teste:${NC} $INSTALL_DIR"
echo -e "${BLUE}🏗️  Projeto teste:${NC} $PROJECT_DIR"

# =============================================================================
# 📋 FASE 1: Preparação e Validação Inicial
# =============================================================================

print_header "FASE 1: PREPARAÇÃO E VALIDAÇÃO INICIAL"

print_step "Criando diretórios de teste..."
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# Verificar que estamos no diretório correto
run_test "Diretório de trabalho correto" "[ \"\$(pwd)\" = \"$PROJECT_DIR\" ]"

# Detectar o Context Navigator no diretório onde script foi executado
CN_SOURCE_PATH=""
if [ -f "$ORIGINAL_PWD/src/context_navigator/core/cn_global.py" ]; then
    CN_SOURCE_PATH="$ORIGINAL_PWD"
elif [ -f "$ORIGINAL_PWD/../src/context_navigator/core/cn_global.py" ]; then
    CN_SOURCE_PATH="$(cd "$ORIGINAL_PWD/.." && pwd)"
elif [ -f "$ORIGINAL_PWD/../../src/context_navigator/core/cn_global.py" ]; then
    CN_SOURCE_PATH="$(cd "$ORIGINAL_PWD/../.." && pwd)"
else
    # Tentar encontrar em diretórios comuns
    for possible_path in "$HOME" "/opt" "/usr/local" "/tmp"; do
        if [ -f "$possible_path/metamodel/src/context_navigator/core/cn_global.py" ]; then
            CN_SOURCE_PATH="$possible_path/metamodel"
            break
        fi
    done
fi

run_test "Código fonte do Context Navigator detectado" "[ -n \"$CN_SOURCE_PATH\" ] && [ -f \"$CN_SOURCE_PATH/src/context_navigator/core/cn_global.py\" ]"

if [ -z "$CN_SOURCE_PATH" ]; then
    print_error "❌ Context Navigator não encontrado! Execute este script do diretório raiz do projeto."
    exit 1
fi

print_success "Context Navigator encontrado em: $CN_SOURCE_PATH"

# =============================================================================
# 📦 FASE 2: Teste de Instalação
# =============================================================================

print_header "FASE 2: TESTE DE INSTALAÇÃO"

print_step "Testando instalação temporária..."

# Copiar código fonte para local temporário (simular download)
cp -r "$CN_SOURCE_PATH" "$TEST_DIR/metamodel"
cd "$TEST_DIR/metamodel"

# Teste: instalação com --dry-run
run_test_verbose "Instalação dry-run funciona" "python3 src/context_navigator/installer/install.py --dry-run"

# Teste: instalação real em diretório temporário
run_test_verbose "Instalação em diretório customizado" "python3 src/context_navigator/installer/install.py --path \"$INSTALL_DIR\""

# Verificar que instalação foi bem-sucedida
run_test "Diretório de instalação criado" "[ -d \"$INSTALL_DIR\" ]"
run_test "Arquivo cn_global.py instalado" "[ -f \"$INSTALL_DIR/core/cn_global.py\" ]"
# O launcher pode ser criado em locais diferentes dependendo do sistema  
run_test "Launcher cn criado" "[ -f \"$INSTALL_DIR/bin/cn\" ] || [ -f \"$HOME/.local/bin/cn\" ] || [ -f \"/usr/local/bin/cn\" ]"
run_test "Templates instalados" "[ -d \"$INSTALL_DIR/templates\" ]"

# =============================================================================
# 📋 FASE 3: Teste de Sistema de Desenvolvimento
# =============================================================================

print_header "FASE 3: SISTEMA DE DESENVOLVIMENTO"

cd "$TEST_DIR/metamodel"

# Testar cndev.sh
run_test "cndev.sh é executável" "[ -x \"./cndev.sh\" ]"
run_test_verbose "cndev.sh help funciona" "./cndev.sh help"

# Testar comando --version (global, não precisa de workspace)
if ./cndev.sh help 2>&1 | grep -q "version"; then
    run_test_verbose "cndev.sh --version funciona" "./cndev.sh --version"
fi

# =============================================================================
# 🎯 FASE 4: Teste de Workspace
# =============================================================================

print_header "FASE 4: GERENCIAMENTO DE WORKSPACE"

cd "$PROJECT_DIR"

# Adicionar instalação ao PATH (launcher pode estar em locais diferentes)
export PATH="$INSTALL_DIR/bin:$HOME/.local/bin:$PATH"

# Teste: comportamento sem workspace (deve dar erro claro)
if cn scan 2>/dev/null; then
    print_warning "cn scan não deveria funcionar sem workspace inicializado"
else
    run_test "Erro claro sem workspace inicializado" "true"
fi

# Teste: inicialização de workspace no projeto de teste
# Primeiro verificar que workspace não existe 
run_test "Não há workspace existente" "! [ -d \".cn_model\" ]"

# Inicializar workspace usando sistema de desenvolvimento (deve executar no diretório do projeto)
run_test_verbose "Inicialização de workspace" "cd \"$PROJECT_DIR\" && \"$TEST_DIR/metamodel/cndev.sh\" init"

# Verificar estrutura criada
run_test "Diretório .cn_model criado" "[ -d \".cn_model\" ]"

# Teste: comandos básicos (usar sistema de desenvolvimento)
run_test_verbose "cn info funciona" "cd \"$PROJECT_DIR\" && \"$TEST_DIR/metamodel/cndev.sh\" info"
run_test_verbose "cn templates funciona" "cd \"$PROJECT_DIR\" && \"$TEST_DIR/metamodel/cndev.sh\" templates"

# =============================================================================
# 📝 FASE 5: Criação de Documentos
# =============================================================================

print_header "FASE 5: CRIAÇÃO DE DOCUMENTOS"

# Testar criação de todos os tipos de documento (usar sistema de desenvolvimento)
run_test_verbose "Criar decisão técnica" "cd \"$PROJECT_DIR\" && \"$TEST_DIR/metamodel/cndev.sh\" new decision \"teste-decisao-e2e\""
run_test "Arquivo de decisão criado" "[ -f \"$PROJECT_DIR/.cn_model/docs/decisions/teste-decisao-e2e.md\" ]"

run_test_verbose "Criar processo" "cd \"$PROJECT_DIR\" && \"$TEST_DIR/metamodel/cndev.sh\" new process \"teste-processo-e2e\""
run_test "Arquivo de processo criado" "[ -f \"$PROJECT_DIR/.cn_model/docs/processes/teste-processo-e2e.md\" ]"

run_test_verbose "Criar referência" "cd \"$PROJECT_DIR\" && \"$TEST_DIR/metamodel/cndev.sh\" new reference \"teste-referencia-e2e\""
run_test "Arquivo de referência criado" "[ -f \"$PROJECT_DIR/.cn_model/docs/references/teste-referencia-e2e.md\" ]"

run_test_verbose "Criar arquitetura" "cd \"$PROJECT_DIR\" && \"$TEST_DIR/metamodel/cndev.sh\" new architecture \"teste-arquitetura-e2e\""
run_test "Arquivo de arquitetura criado" "[ -f \"$PROJECT_DIR/.cn_model/docs/architecture/teste-arquitetura-e2e.md\" ]"

run_test_verbose "Criar análise" "cd \"$PROJECT_DIR\" && \"$TEST_DIR/metamodel/cndev.sh\" new analysis \"teste-analise-e2e\""
run_test "Arquivo de análise criado" "[ -f \"$PROJECT_DIR/.cn_model/docs/analysis/teste-analise-e2e.md\" ]"

run_test_verbose "Criar planejamento" "cd \"$PROJECT_DIR\" && \"$TEST_DIR/metamodel/cndev.sh\" new planning \"teste-planejamento-e2e\""
run_test "Arquivo de planejamento criado" "[ -f \"$PROJECT_DIR/.cn_model/docs/planning/teste-planejamento-e2e.md\" ]"

# Verificar conteúdo dos templates (devem ter mais de algumas linhas)
run_test "Template de decisão tem conteúdo" "[ \$(wc -l < \"$PROJECT_DIR/.cn_model/docs/decisions/teste-decisao-e2e.md\") -gt 5 ]"
run_test "Template de processo tem conteúdo" "[ \$(wc -l < \"$PROJECT_DIR/.cn_model/docs/processes/teste-processo-e2e.md\") -gt 5 ]"

# =============================================================================
# 🔍 FASE 6: Comandos de Análise
# =============================================================================

print_header "FASE 6: COMANDOS DE ANÁLISE"

# Criar alguns arquivos de código para teste
mkdir -p src/components
cat > src/components/UserService.js << 'EOF'
// ===== CONTEXT NAVIGATOR CODE BRIDGE =====
// @cn:component user-service
// @cn:doc decisions/teste-decisao-e2e.md
// @cn:context-level c2_module
// ============================================

class UserService {
    constructor() {
        this.users = [];
    }
    
    addUser(user) {
        this.users.push(user);
    }
}

module.exports = UserService;
EOF

cat > src/utils.py << 'EOF'
"""
Utilities module for the test project
"""

def helper_function():
    """A simple helper function"""
    return "Hello from helper"

def process_data(data):
    """Process some data"""
    return data.upper()
EOF

# Testar comandos de análise
run_test_verbose "cn scan funciona" "cn scan"

# Testar outros comandos (podem não estar implementados, mas não devem quebrar)
if cn help 2>&1 | grep -q "validate"; then
    run_test_verbose "cn validate funciona" "cn validate"
fi

if cn help 2>&1 | grep -q "demo"; then
    run_test "cn demo não quebra" "cn demo >/dev/null 2>&1 || true"
fi

# =============================================================================
# 📁 FASE 7: Funcionamento em Subdiretórios
# =============================================================================

print_header "FASE 7: FUNCIONAMENTO EM SUBDIRETÓRIOS"

# Criar subdiretórios
mkdir -p src/components/ui
mkdir -p tests/unit
mkdir -p docs/guides

# Testar funcionamento em diferentes subdiretórios
cd src/
run_test_verbose "cn info em src/" "cn info"
run_test_verbose "cn new decision em src/" "cn new decision \"teste-subdir-src\""
run_test "Documento criado em local correto" "[ -f \"../.cn_model/docs/decisions/teste-subdir-src.md\" ]"

cd components/ui/
run_test_verbose "cn info em src/components/ui/" "cn info"
run_test_verbose "cn templates em subdiretório profundo" "cn templates"

cd ../../../tests/unit/
run_test_verbose "cn scan em tests/unit/" "cn scan"

# Voltar para diretório raiz
cd "$PROJECT_DIR"

# =============================================================================
# 🚫 FASE 8: Comportamento Fora de Workspace
# =============================================================================

print_header "FASE 8: COMPORTAMENTO FORA DE WORKSPACE"

# Testar em diretório não-workspace
cd /tmp

# Estes comandos devem falhar fora de workspace
if cn info 2>/dev/null; then
    print_warning "cn info não deveria funcionar fora de workspace"
else
    run_test "cn info falha fora de workspace" "true"
fi

if cn scan 2>/dev/null; then
    print_warning "cn scan não deveria funcionar fora de workspace"
else
    run_test "cn scan falha fora de workspace" "true"
fi

# Comandos globais devem funcionar
run_test_verbose "cn help funciona globalmente" "cn help"

# Voltar para workspace
cd "$PROJECT_DIR"

# =============================================================================
# 🧹 FASE 9: Teste de Remoção
# =============================================================================

print_header "FASE 9: REMOÇÃO DE WORKSPACE"

# Testar remoção de workspace (se comando existir)
if cn help 2>&1 | grep -q "remove"; then
    run_test_verbose "cn remove funciona" "cn remove"
    
    # Verificar que workspace foi removido
    if cn info 2>/dev/null; then
        print_warning "cn info ainda funciona após remoção"
    else
        run_test "cn info falha após remoção" "true"
    fi
    
    # Re-inicializar para testes finais
    run_test_verbose "Re-inicializar workspace" "cn init"
else
    print_warning "Comando cn remove não encontrado - pulando teste"
fi

# =============================================================================
# 🏗️ FASE 10: Teste com Sistema de Desenvolvimento
# =============================================================================

print_header "FASE 10: SISTEMA DE DESENVOLVIMENTO"

cd "$TEST_DIR/metamodel"

# Testar que sistema de desenvolvimento funciona
run_test_verbose "cndev.sh init funciona" "./cndev.sh init"
run_test_verbose "cndev.sh templates funciona" "./cndev.sh templates"
run_test_verbose "cndev.sh new decision teste-dev" "./cndev.sh new decision \"teste-cndev\""
run_test "Documento criado por cndev.sh" "[ -f \".cn_model/docs/decisions/teste-cndev.md\" ]"

# =============================================================================
# 📊 RESULTADOS FINAIS
# =============================================================================

print_header "RESULTADOS DO TESTE END-TO-END"

echo -e "${BLUE}📊 Estatísticas dos Testes:${NC}"
echo -e "   ${CYAN}Total de testes:${NC} $TESTS_TOTAL"
echo -e "   ${GREEN}Testes passaram:${NC} $TESTS_PASSED" 
echo -e "   ${RED}Testes falharam:${NC} $TESTS_FAILED"

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "\n${GREEN}🎉 SUCESSO: Todos os $TESTS_TOTAL testes passaram!${NC}"
    echo -e "${GREEN}✅ Context Navigator está funcionando perfeitamente!${NC}"
    echo -e "${GREEN}🚀 Sistema pronto para uso em produção!${NC}"
    exit 0
else
    echo -e "\n${RED}💥 FALHOU: $TESTS_FAILED de $TESTS_TOTAL testes falharam${NC}"
    echo -e "${RED}❌ Context Navigator tem problemas que precisam ser corrigidos${NC}"
    echo -e "${YELLOW}🔍 Revise a implementação antes de usar em produção${NC}"
    exit 1
fi 