---
doc_type: "reference"
context_level: "c1_system"
context_type: "core"
module: "workspace-system"
priority: "high"
status: "active"
connections:
  references: ["ARCHITECTURE_2_0_OVERVIEW.md"]
  impacts: ["MANUAL_HUMANO.md", "MANUAL_IA.md"]
  depends_on: []
  blocks: []
  relates_to: ["INSTALACAO_GLOBAL.md"]
created_date: "2024-01-20"
last_updated: "2024-01-20"
owner: "Development Team"
---

# Como o Context Navigator Detecta e Usa Workspaces

## 🎯 Resumo

O Context Navigator funciona **como git** - busca automaticamente por workspaces na hierarquia de diretórios, permitindo usar comandos de qualquer subdiretório do projeto.

## 🔍 Algoritmo de Detecção

### **Busca Hierárquica**

```bash
# Exemplo: executando de src/components/api/
cn scan

# Busca em ordem:
# 1. ./                          (src/components/api/.cn_model/)
# 2. ../                         (src/components/.cn_model/)
# 3. ../../                      (src/.cn_model/)
# 4. ../../../                   (projeto/.cn_model/) ✅ ENCONTROU!
# 5. Para quando encontra ou chega na raiz do sistema
```

### **Arquivo de Workspace**

**Local**: `.cn_model/.cn_workspace`

**Formato**:

```yaml
workspace:
  created_at: "2025-07-16T11:47:28Z"
  id: projeto-e79eaf5c
  name: projeto
  root_path: .
  version: 2.0.0

configuration:
  auto_scan: true
  source_patterns:
    - "**/*.py"
    - "**/*.js"
    - "**/*.ts"
    - "**/*.md"
  ignore_patterns:
    - .cn_model
    - .git
    - node_modules
    - __pycache__
  output_dir: .cn_model
  templates_enabled: true

daemon:
  enabled: true
  auto_start: true
  log_level: INFO
  port: null
```

## 🏗️ Dois Sistemas de Registry

### **1. Sistema Global (Produção)**

**Quando**: Instalação via `cn init`  
**Registry**: `~/.local/share/context-navigator/workspaces-registry.yml`  
**Comando**: `cn`

```yaml
created_at: "2025-07-16T14:42:01Z"
version: 2.0.0
workspaces:
  projeto-e79eaf5c:
    name: projeto
    root_path: /home/user/projeto
    config_path: /home/user/projeto/.cn_model/.cn_workspace
    created_at: "2025-07-16T11:47:28Z"
```

### **2. Sistema de Desenvolvimento**

**Quando**: Desenvolvimento via `./cndev.sh`  
**Registry**: `src/context_navigator/workspaces-registry.yml`  
**Comando**: `./cndev.sh`

**Detecção automática:**

```python
def _get_global_installation_path(self) -> Path:
    # MODO DE DESENVOLVIMENTO: Se rodando do src/, usar fallback sempre
    current_path = Path(__file__).resolve()
    if "src/context_navigator" in str(current_path):
        print("🛠️ Modo de desenvolvimento detectado - usando registry local")
        return current_path.parent.parent
```

## 🔄 Fluxo de Detecção Completo

```mermaid
graph TD
    A[Comando cn/cndev.sh] --> B[WorkspaceManager.detect_current_workspace]
    B --> C[Path.cwd() - diretório atual]
    C --> D[Buscar .cn_model/.cn_workspace]
    D --> E{Encontrado?}
    E -->|Sim| F[Carregar configuração]
    E -->|Não| G[Subir um nível: dirname]
    G --> H{É raiz?}
    H -->|Não| D
    H -->|Sim| I[Workspace não encontrado]
    F --> J[Executar comando com workspace]
    I --> K[Erro: Execute cn init]
```

## ⚙️ Inicialização de Workspace

### **Comando**: `cn init` ou `./cndev.sh init`

**O que acontece:**

1. **Verifica se já existe**: Busca `.cn_model/` na hierarquia
2. **Cria estrutura**:
   ```
   .cn_model/
   ├── .cn_workspace      # Configuração
   └── docs/              # Documentação gerada
   ```
3. **Gera configuração**: Com padrões inteligentes baseados no projeto
4. **Registra globalmente**: Adiciona ao registry apropriado

### **Configuração Automática**

```python
def _generate_workspace_config(self, path: Path) -> Dict:
    return {
        'workspace': {
            'id': f"{path.name}-{uuid4().hex[:8]}",
            'name': path.name,
            'root_path': str(path.relative_to(path)),
            'version': '2.0.0',
            'created_at': datetime.utcnow().isoformat() + 'Z'
        },
        'configuration': {
            'auto_scan': True,
            'source_patterns': ['**/*.py', '**/*.js', '**/*.ts', '**/*.md'],
            'ignore_patterns': ['.cn_model', '.git', 'node_modules', '__pycache__'],
            'output_dir': '.cn_model',
            'templates_enabled': True
        }
    }
```

## 🎯 Comandos por Tipo

### **Comandos Globais** (não precisam workspace)

- `cn help`, `cn --version`
- `cn init`, `cn migrate`
- `cn list` (lista workspaces)

### **Comandos de Workspace** (precisam workspace)

- `cn scan`, `cn validate`, `cn demo`
- `cn component explore`, `cn component parse`
- `cn new decision/process/etc`

**Verificação automática:**

```python
def execute(self, args: List[str]) -> int:
    command = args[0]

    # Comandos que não precisam de workspace
    if command in ['init', 'migrate', 'list', 'help', '--help', '-h', '--version']:
        return self._handle_global_command(command, command_args)

    # Comandos que precisam de workspace
    current_workspace = self.workspace_manager.detect_current_workspace()
    if not current_workspace:
        print("❌ Context Navigator workspace não encontrado")
        print("💡 Execute 'cn init' para configurar este diretório")
        return 1
```

## 🚨 Problemas Comuns e Soluções

### **"Workspace não encontrado"**

**Causa**: Não há `.cn_model/.cn_workspace` na hierarquia  
**Solução**: `cn init` no diretório raiz do projeto

### **"Registry corrompido"**

**Desenvolvimento**: Deletar `src/context_navigator/workspaces-registry.yml`  
**Produção**: Deletar `~/.local/share/context-navigator/workspaces-registry.yml`

### **"Modo desenvolvimento vs produção"**

**Desenvolvimento**: Use `./cndev.sh` (registry local)  
**Produção**: Use `cn` (registry global)

**Não misture os dois sistemas no mesmo projeto!**

## 💡 Boas Práticas

1. **Um workspace por projeto**: Execute `cn init` na raiz do projeto
2. **Use de qualquer lugar**: Comandos funcionam de subdiretórios
3. **Desenvolvimento**: Sempre use `./cndev.sh` para mudanças no código
4. **Produção**: Use `cn` para uso normal
5. **Registry separado**: Desenvolvimento e produção não se misturam

---

**Este sistema garante que o Context Navigator seja tão conveniente quanto git para desenvolvedores, funcionando de qualquer lugar no projeto.**
