#!/bin/bash

# =============================================================================
# 🧪 Context Navigator - Teste de Instalação REAL
# =============================================================================
# 
# Este script testa se a instalação REALMENTE funciona
# (não usa hacks de desenvolvimento como ./cndev.sh)
#
# =============================================================================

set -e  # Parar em qualquer erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Contadores
TESTS_TOTAL=0
TESTS_PASSED=0

print_header() {
    echo -e "\n${BLUE}=== $1 ===${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

run_test() {
    local test_name="$1"
    local test_command="$2"
    
    TESTS_TOTAL=$((TESTS_TOTAL + 1))
    echo -e "\n${BLUE}Teste $TESTS_TOTAL: $test_name${NC}"
    
    if eval "$test_command" >/dev/null 2>&1; then
        print_success "PASSOU: $test_name"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        print_error "FALHOU: $test_name"
        return 1
    fi
}

# Limpeza automática
cleanup() {
    print_header "LIMPEZA"
    rm -rf /tmp/test_real_install_$$
    rm -rf /tmp/test_project_$$
    echo "Arquivos temporários removidos"
}
trap cleanup EXIT

print_header "CONTEXT NAVIGATOR - TESTE DE INSTALAÇÃO REAL"

# Diretórios temporários únicos
INSTALL_DIR="/tmp/test_real_install_$$"
PROJECT_DIR="/tmp/test_project_$$"

print_header "FASE 1: INSTALAÇÃO"

echo "📦 Instalando Context Navigator..."
python3 src/context_navigator/installer/install.py --path "$INSTALL_DIR"

print_header "FASE 2: TESTE DO LAUNCHER"

# Verificar estrutura instalada
run_test "Diretório de instalação criado" "[ -d \"$INSTALL_DIR\" ]"
run_test "Arquivo cn_global.py existe" "[ -f \"$INSTALL_DIR/core/cn_global.py\" ]"
run_test "Launcher criado" "[ -f \"/home/\$USER/.local/bin/cn\" ]"

print_header "FASE 3: TESTE DOS COMANDOS"

# Testar comando global
run_test "cn --version funciona" "cn --version"
run_test "cn help funciona" "cn help"

print_header "FASE 4: TESTE DE WORKSPACE"

# Criar projeto de teste
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# Testar comandos de workspace
run_test "cn init cria workspace" "cn init"
run_test "Estrutura .cn_model criada" "[ -d \".cn_model\" ]"
run_test "cn info funciona" "cn info"
run_test "cn templates funciona" "cn templates"

print_header "FASE 5: TESTE DE CRIAÇÃO DE DOCUMENTOS"

# Testar criação de documentos
run_test "cn new decision funciona" "cn new decision \"teste-instalacao\""
run_test "Arquivo de decisão criado" "[ -f \".cn_model/docs/decisions/teste-instalacao.md\" ]"
run_test "cn new process funciona" "cn new process \"processo-teste\""
run_test "Arquivo de processo criado" "[ -f \".cn_model/docs/processes/processo-teste.md\" ]"

print_header "FASE 6: TESTE DE SUBDIRETÓRIOS"

# Testar funcionamento em subdiretórios
mkdir -p src/components
cd src/components

run_test "cn info em subdiretório" "cn info"
run_test "cn new em subdiretório" "cn new reference \"api-teste\""
run_test "Arquivo criado no local correto" "[ -f \"../../.cn_model/docs/references/api-teste.md\" ]"

print_header "RESULTADOS FINAIS"

echo -e "${BLUE}📊 Estatísticas:${NC}"
echo -e "   Total de testes: $TESTS_TOTAL"
echo -e "   Testes passaram: $TESTS_PASSED"

if [ $TESTS_PASSED -eq $TESTS_TOTAL ]; then
    echo -e "\n${GREEN}🎉 SUCESSO: Instalação funciona perfeitamente!${NC}"
    echo -e "${GREEN}✅ Sistema REAL está pronto para uso${NC}"
    exit 0
else
    FAILED=$((TESTS_TOTAL - TESTS_PASSED))
    echo -e "\n${RED}💥 FALHOU: $FAILED de $TESTS_TOTAL testes falharam${NC}"
    echo -e "${RED}❌ Sistema ainda tem problemas${NC}"
    exit 1
fi 