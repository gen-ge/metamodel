# 🎯 PRD: Context Navigator - Sistema de Documentação Context-Aware

## 🔍 Visão Geral

### **Problema**

Desenvolvedores solo e IAs perdem contexto durante desenvolvimento de projetos complexos. A pergunta "Como esta documentação se relaciona com o resto?" não tem resposta sistematizada, gerando retrabalho e perda de foco arquitetural.

### **Solução**

Context Navigator: Uma **metodologia de parceria humano-IA** que estrutura informações através de convenções rígidas, permitindo que sistemas automatizados leiam, agrupem e contextualizem documentação sem intervenção manual.

### **Diferencial Fundamental**

**Não é uma ferramenta para outros** - é uma **metodologia pessoal** que:

- Disciplina IA através de regras cristalinas em todos os prompts
- Padroniza interação humano-IA através de convenções imutáveis
- Permite automação completa de leitura documental
- Mantém contexto atualizado automaticamente durante desenvolvimento

### **Impacto Esperado**

- IA sempre contextualizada através de "lei sagrada" metodológica
- Documentação 10x mais rica e conectada
- Desenvolvimento solo mais eficiente e organizado
- Navegação contextual automática para projetos complexos

---

## 📋 Requisitos do Sistema

### **1. Componentes Metodológicos**

#### **1.1 Sistema de Configuração (.contextrc)**

- **Propósito**: Define convenções documentais absolutas
- **Função**: Estabelece "lei sagrada" para IA seguir religiosamente
- **Conteúdo**: Nomenclaturas fixas, tipos de documento, contextos extensíveis

#### **1.2 Context Scanner (Python)**

- **Propósito**: Lê pasta de documentos metodológicos (não projeto)
- **Função**: Detecta tipos, extrai metadados, mapeia conexões
- **Escopo**: Apenas pasta estruturada da metodologia
- **Resultado**: Contextualização automática sem falhas

#### **1.3 Sistema de Metadados Estruturados**

- **Propósito**: Templates impecáveis com cabeçalhos perfeitos
- **Função**: Mitiga edge cases através de padronização extrema
- **Estrutura**: Campos fixos que nunca mudam
- **Validação**: Scanner detecta inconsistências automaticamente

#### **1.4 Context Maps (.context-map/)**

- **Propósito**: Repositório central de contexto do projeto
- **Função**: Mapeia conexões, relacionamentos, conflitos
- **Atualização**: Automática via scanner
- **Escala**: Suporta crescimento orgânico do projeto

#### **1.5 AI Rule Engine (context.rule)**

- **Propósito**: "Lei sagrada" que orienta IA em todos os prompts
- **Função**: Instrução cristalina para disciplinar comportamento da IA
- **Aplicação**: Fixada como regra universal em todas as interações
- **Resultado**: IA sempre contextualizada e consistente

### **2. Metodologia de Templates Expandida**

#### **2.1 Context Engine Inteligente**

- **Propósito**: Decide automaticamente template baseado em doc_type
- **Função**: Elimina escolhas através de regras metodológicas
- **Extensibilidade**: Suporta novos templates conforme necessidade
- **Validação**: Verifica conformidade automaticamente

#### **2.2 Templates Metodológicos Completos**

**Template DECISÃO (Estimativa: 40% dos casos)**

- **Uso**: PRD, ADR, RFC, escolhas técnicas, arquitetura
- **Estrutura**: Problema → Análise → Opções → Decisão → Impactos

**Template PROCESSO (Estimativa: 20% dos casos)**

- **Uso**: Runbooks, playbooks, tutoriais, procedimentos
- **Estrutura**: Objetivo → Pré-requisitos → Passos → Validação → Troubleshooting

**Template REFERÊNCIA (Estimativa: 15% dos casos)**

- **Uso**: APIs, glossários, especificações, documentação técnica
- **Estrutura**: Overview → Referência → Exemplos → Recursos

**Template ARQUITETURA (Estimativa: 10% dos casos)**

- **Uso**: Diagramas, modelagem, estrutura, componentes
- **Estrutura**: Contexto → Componentes → Fluxos → Decisões → Evolução

**Template ANÁLISE (Estimativa: 10% dos casos)**

- **Uso**: Performance, bugs, retrospectivas, investigações
- **Estrutura**: Situação → Análise → Descobertas → Ações → Acompanhamento

**Template PLANEJAMENTO (Estimativa: 5% dos casos)**

- **Uso**: Roadmaps, sprints, releases, marcos
- **Estrutura**: Objetivos → Escopo → Cronograma → Riscos → Métricas

_Nota: Percentuais baseados em análise de padrões de desenvolvimento solo_

### **3. Sistema de Contextos Extensível**

#### **3.1 Contextos Hierárquicos**

```yaml
contexts:
  # Contextos principais (baseado em DDD)
  c1_root: "Contexto raiz do projeto (ex: pasta 'Gen')"
  c2_module: "Contexto módulo (ex: 'front', 'back', 'shared')"
  c3_component: "Contexto componente (ex: arquivos específicos)"

  # Contextos especializados (extensíveis)
  infra: "Contexto de infraestrutura e deploy"
  shared: "Contexto de componentes compartilhados"
  core: "Contexto de lógica de negócio central"
  api: "Contexto de interfaces e contratos"
  data: "Contexto de persistência e dados"
  ui: "Contexto de interface de usuário"
```

#### **3.2 Detecção Automática de Contexto**

```python
# Detecção baseada em estrutura de pastas
CONTEXT_DETECTION = {
    "c1_root": ["Gen/", "project_root/"],
    "c2_module": ["front/", "back/", "shared/", "api/"],
    "c3_component": ["specific_files", "components/"],
    "infra": ["deploy/", "infrastructure/", "docker/"],
    "shared": ["common/", "utils/", "lib/"],
    "core": ["domain/", "business/", "core/"],
    "api": ["endpoints/", "controllers/", "routes/"],
    "data": ["models/", "repositories/", "database/"],
    "ui": ["views/", "components/", "pages/"]
}
```

### **4. Estrutura Metodológica Robusta**

```
📁 context-navigator/                # Pasta da metodologia (não do projeto)
├── 📄 .contextrc                   # Configuração metodológica
├── 📄 context.rule                 # "Lei sagrada" para IA
├── 📁 .context-map/                # Mapas gerados automaticamente
│   ├── 📄 index.yml                # Índice geral
│   ├── 📄 architecture.yml         # Visão arquitetural
│   ├── 📄 connections.yml          # Conexões e relacionamentos
│   ├── 📄 conflicts.yml            # Conflitos detectados
│   └── 📁 contexts/                # Contexto por módulo
├── 📁 scripts/
│   ├── 📄 context_scanner.py       # Scanner robusto
│   ├── 📄 context_engine.py        # Engine metodológica
│   ├── 📄 template_validator.py    # Validador de templates
│   └── 📄 conflict_detector.py     # Detector de conflitos
├── 📁 templates/
│   ├── 📄 decisao.md              # Template decisão
│   ├── 📄 processo.md             # Template processo
│   ├── 📄 referencia.md           # Template referência
│   ├── 📄 arquitetura.md          # Template arquitetura
│   ├── 📄 analise.md              # Template análise
│   └── 📄 planejamento.md         # Template planejamento
├── 📁 docs/
│   ├── 📄 MANUAL_HUMANO.md        # Manual para operador humano
│   ├── 📄 MANUAL_IA.md            # Manual para IA
│   └── 📄 CONVENTIONS.md          # Convenções imutáveis
└── 📁 examples/
    ├── 📄 exemplo_decisao.md
    ├── 📄 exemplo_processo.md
    └── 📄 exemplo_arquitetura.md
```

---

## 🔧 Especificações Metodológicas

### **Nomenclatura Imutável e Extensível**

```yaml
nomenclature:
  document_types:
    decision: "Documentos de decisão técnica"
    process: "Documentos de processo/procedimento"
    reference: "Documentos de referência"
    architecture: "Documentos de arquitetura"
    analysis: "Documentos de análise"
    planning: "Documentos de planejamento"

  metadata_fields:
    # Campos obrigatórios (imutáveis)
    doc_type: "Tipo do documento"
    context_level: "Nível de contexto"
    context_type: "Tipo de contexto (c1/c2/c3/infra/shared/core/api/data/ui)"
    connections: "Conexões com outros documentos"

    # Campos opcionais (extensíveis)
    priority: "Prioridade do documento"
    status: "Status atual"
    owner: "Responsável"
    last_updated: "Última atualização"

  connection_types:
    references: "Documentos referenciados"
    impacts: "Documentos impactados"
    depends_on: "Dependências"
    blocks: "Documentos bloqueados"
    relates_to: "Documentos relacionados"
```

### **Sistema de Metadados Robusto**

```yaml
# Front matter obrigatório (template perfeito)
---
doc_type: "decision"
context_level: "c2"
context_type: "core"
module: "authentication"
priority: "high"
status: "active"
connections:
  references: ["UserService", "AuthPolicy"]
  impacts: ["LoginFlow", "SessionManagement"]
  depends_on: ["SecurityFramework"]
  blocks: ["SSOIntegration"]
created_date: "2024-01-15"
last_updated: "2024-01-15"
---

# Metadados inline para detecção avançada
<!-- CONTEXT_META
responsibility: "Define authentication flow"
architectural_impact: "high"
stakeholders: ["backend-team", "security-team"]
complexity: "medium"
maintenance_notes: "Review quarterly"
-->
```

### **Detecção de Conflitos e Relacionamentos**

```python
# Sistema de detecção automática
CONFLICT_DETECTION = {
    "duplicate_references": "Mesmo componente referenciado diferentemente",
    "circular_dependencies": "Dependências circulares detectadas",
    "orphaned_documents": "Documentos sem conexões",
    "broken_connections": "Conexões para documentos inexistentes",
    "inconsistent_context": "Contexto inconsistente entre documentos"
}

RELATIONSHIP_MAPPING = {
    "strong_coupling": "Documentos fortemente acoplados",
    "weak_coupling": "Documentos fracamente acoplados",
    "hierarchy": "Relação hierárquica detectada",
    "peer_relationship": "Relação entre pares",
    "cross_context": "Relação entre contextos diferentes"
}
```

---

## 📚 Manual para Parceria Humano-IA

### **Protocolo de Interação**

#### **1. Regra Sagrada para IA**

```
SEMPRE antes de qualquer ação:
1. Carregar context.rule
2. Ler .context-map/index.yml
3. Verificar contexto atual
4. Aplicar template apropriado
5. Atualizar conexões se necessário
```

#### **2. Fluxo de Trabalho Humano**

```
1. Criar documento seguindo template exato
2. Preencher metadados obrigatórios
3. Executar scanner para validação
4. Corrigir inconsistências detectadas
5. Atualizar context maps
```

#### **3. Validação Automática**

```python
# Validação executada pelo scanner
VALIDATION_RULES = {
    "required_metadata": "Todos os campos obrigatórios preenchidos",
    "valid_connections": "Conexões apontam para documentos existentes",
    "consistent_context": "Contexto consistente com localização",
    "template_compliance": "Documento segue template correto",
    "no_conflicts": "Nenhum conflito detectado"
}
```

### **Casos de Uso Específicos**

#### **Caso 1: Desenvolvimento de Feature**

```
1. Criar ADR seguindo template DECISÃO
2. Scanner detecta contexto automaticamente
3. IA gera documentação baseada em contexto
4. Atualização automática de conexões
```

#### **Caso 2: Refatoração de Código**

```
1. Criar documento de análise
2. Scanner identifica impactos
3. IA sugere documentos a atualizar
4. Validação de consistência
```

#### **Caso 3: Documentação de API**

```
1. Usar template REFERÊNCIA
2. Scanner mapeia endpoints
3. IA gera documentação completa
4. Conexões com outros módulos
```

---

## 📊 Métricas de Sucesso

### **Métricas Principais**

- **Consistência IA**: 95%+ prompts seguem context.rule
- **Cobertura Documental**: 90%+ documentos com metadados completos
- **Detecção Automática**: 95%+ contextos detectados corretamente
- **Resolução de Conflitos**: 90%+ conflitos detectados automaticamente
- **Eficiência**: 80% redução em retrabalho documental

### **Métricas de Desenvolvimento**

- **Tempo de Context Switch**: <2 minutos para recuperar contexto
- **Precisão de Conexões**: 95%+ conexões corretas
- **Completude de Templates**: 100% casos cobertos por templates
- **Manutenibilidade**: 0 intervenção manual regular

---

## 🚀 Roadmap de Implementação

### **Fase 1: Fundação (2 semanas)**

- [ ] Definir .contextrc com todos os contextos
- [ ] Criar 6 templates robustos com metadados perfeitos
- [ ] Desenvolver scanner básico para pasta metodológica
- [ ] Estabelecer "lei sagrada" para IA (context.rule)

### **Fase 2: Automação (2 semanas)**

- [ ] Scanner avançado com detecção de conflitos
- [ ] Validador automático de templates
- [ ] Detector de relacionamentos complexos
- [ ] Geração automática de context maps

### **Fase 3: Inteligência (2 semanas)**

- [ ] Sistema de sugestões baseado em contexto
- [ ] Análise de impacto automática
- [ ] Detecção de padrões e anomalias
- [ ] Otimização baseada em uso real

### **Fase 4: Refinamento (1 mês)**

- [ ] Ajuste de templates baseado em casos reais
- [ ] Expansão de contextos conforme necessidade
- [ ] Melhoria na precisão de detecção
- [ ] Documentação completa para parceria humano-IA

---

## 💡 Diferenciais Únicos

1. **Parceria Humano-IA**: Metodologia para trabalho colaborativo
2. **Lei Sagrada**: Regras cristalinas que disciplinam IA
3. **Detecção Automática**: Scanner focado em pasta metodológica
4. **Templates Robustos**: Cabeçalhos perfeitos mitigam edge cases
5. **Contextos Extensíveis**: Sistema cresce com projeto
6. **Resolução de Conflitos**: Detecta inconsistências automaticamente

---

## 🎯 Esclarecimentos Críticos

### **Foco Principal**

- **Desenvolvimento Solo**: Metodologia para um desenvolvedor + IA
- **Pasta Metodológica**: Scanner opera apenas na pasta estruturada
- **Disciplina da IA**: Regras cristalinas em todos os prompts
- **Evolução Contínua**: Sistema melhora conforme uso

### **Não É**

- Ferramenta para equipes grandes
- Scanner de código-fonte
- Metodologia para outros desenvolvedores
- Sistema que funciona sem disciplina

### **Problema Resolvido**

- Perda de contexto em projetos complexos
- Retrabalho por falta de documentação
- IA descontextualizada
- Desenvolvimento solo ineficiente

---

## 📝 Próximos Passos Críticos

### **Validação Necessária**

1. **Templates Suficientes**: 6 templates cobrem todos os casos?
2. **Contextos Adequados**: Sistema de contextos funciona?
3. **Regras Claras**: Context.rule disciplina IA adequadamente?
4. **Scanner Robusto**: Detecção automática é confiável?

### **Desenvolvimento Prioritário**

1. **Primeiro**: Templates perfeitos + .contextrc
2. **Segundo**: Scanner robusto + validação
3. **Terceiro**: Context.rule + manual para IA
4. **Quarto**: Testes em projeto real

---

_"Context Navigator: Uma parceria humano-IA para desenvolvimento solo eficiente."_

🚀 **Próxima Ação**: Definir templates detalhados e começar implementação do scanner básico para validar metodologia em projeto real.
