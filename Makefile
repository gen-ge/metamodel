# 🛠️ Context Navigator - Development Makefile
.PHONY: help dev build test install clean

# Default target
help: ## Mostrar ajuda dos comandos disponíveis
	@echo "🛠️ Context Navigator - Development Commands"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "📖 Para mais detalhes, veja: CONTRIBUTING.md"

dev: ## Rodar em modo desenvolvimento
	@./cndev.sh help

dev-scan: ## Rodar scan em modo desenvolvimento
	@./cndev.sh scan

dev-validate: ## Rodar validação em modo desenvolvimento
	@./cndev.sh validate

dev-demo: ## Rodar demo em modo desenvolvimento
	@./cndev.sh demo

build: ## Criar build para distribuição
	@echo "🏗️ Criando build..."
	@python3 build.py --version dev-$(shell date +%Y%m%d-%H%M)

build-release: ## Criar build de release (precisa de VERSION)
	@if [ -z "$(VERSION)" ]; then echo "❌ Use: make build-release VERSION=2.0.8"; exit 1; fi
	@echo "🏗️ Criando build release $(VERSION)..."
	@python3 build.py --version $(VERSION)

test: ## Testar build em ambiente limpo
	@echo "🧪 Testando build..."
	@cd dist && \
	latest_tar=$$(ls -t context-navigator-*.tar.gz | head -1) && \
	echo "📦 Testando: $$latest_tar" && \
	tar -xzf "$$latest_tar" && \
	cd context-navigator-* && \
	python3 install.py

install: ## Instalar versão de desenvolvimento globalmente
	@echo "⚙️ Instalando versão de desenvolvimento..."
	@python3 src/context_navigator/installer/install.py --global

clean: ## Limpar arquivos de build
	@echo "🧹 Limpando arquivos de build..."
	@python3 build.py --clean
	@rm -f cndev.sh.bak

setup: ## Setup inicial para novos desenvolvedores
	@echo "🚀 Setup inicial para desenvolvimento..."
	@chmod +x cndev.sh
	@echo "✅ cndev.sh configurado"
	@./cndev.sh version
	@echo ""
	@echo "🎯 Próximos passos:"
	@echo "  make dev-scan    # Testar scan"
	@echo "  make dev-demo    # Ver demonstração"
	@echo "  make build       # Criar build"
	@echo ""
	@echo "💡 NOTA: ./cndev.sh usa registry LOCAL (desenvolvimento)"
	@echo "💡       cn usa registry GLOBAL (produção)"

# Comandos para CI/CD (futuro)
ci-test: ## Testes para CI/CD
	@echo "🤖 Executando testes CI..."
	@./cndev.sh validate
	@python3 build.py --version ci-test
	@echo "✅ Testes CI passaram"

# Comandos para documentação
docs: ## Gerar documentação
	@echo "📚 Gerando documentação..."
	@./cndev.sh demo --docs

# Comando para verificar estilo
lint: ## Verificar estilo de código (futuro)
	@echo "🔍 Verificando estilo de código..."
	@echo "ℹ️ Linter não implementado ainda"

# Release workflow
release-check: ## Verificar se está pronto para release
	@echo "🔍 Verificando se está pronto para release..."
	@./cndev.sh validate
	@python3 build.py --version release-check
	@echo "✅ Pronto para release!"

release-tag: ## Criar tag de release (use: make release-tag VERSION=2.0.8)
	@if [ -z "$(VERSION)" ]; then echo "❌ Use: make release-tag VERSION=2.0.8"; exit 1; fi
	@echo "🏷️ Criando tag de release v$(VERSION)..."
	@git tag -a v$(VERSION) -m "Context Navigator v$(VERSION)"
	@git push origin v$(VERSION)
	@echo "✅ Tag v$(VERSION) criada! GitHub Actions criará release automaticamente."
	@echo "🔗 Acompanhe em: https://github.com/gen-ge/metamodel/actions"

release-local: ## Criar release local para teste (use: make release-local VERSION=2.0.8)
	@if [ -z "$(VERSION)" ]; then echo "❌ Use: make release-local VERSION=2.0.8"; exit 1; fi
	@echo "📦 Criando release local v$(VERSION)..."
	@python3 build.py --version $(VERSION)
	@echo "✅ Release local criado em dist/" 