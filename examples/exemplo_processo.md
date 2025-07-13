---
doc_type: "process"
context_level: "c2_module"
context_type: "infra"
module: "deployment"
priority: "high"
status: "active"
connections:
  references: ["kubernetes-architecture.md", "ci-cd-pipeline.md"]
  impacts: ["monitoring-setup.md", "rollback-process.md"]
  depends_on: ["docker-build-process.md"]
  blocks: []
  relates_to: ["security-scan-process.md", "database-migration-process.md"]
created_date: "2024-01-15"
last_updated: "2024-01-15"
owner: "DevOps Lead"
---

# Processo de Deployment em Produção

## Objetivo

### Propósito

Definir processo padronizado e seguro para deployment de aplicações em ambiente de produção, garantindo alta disponibilidade, rollback rápido e zero downtime.

### Escopo

Este processo cobre:

- Deployment de aplicações web (frontend/backend)
- Deployment de serviços de API
- Deployment de jobs/workers
- Deployment de updates de configuração
- Deployment de migrations de banco de dados

**Não cobre:**

- Deployment de infraestrutura (Terraform)
- Deployment de ferramentas internas
- Hotfixes emergenciais

### Resultados Esperados

- **Zero downtime** durante deployments normais
- **Rollback automático** em caso de falhas
- **Tempo de deployment** < 10 minutos
- **Validação completa** antes do go-live
- **Rastreabilidade** completa do processo

## Pré-requisitos

### Conhecimentos Necessários

- Kubernetes básico (pods, services, deployments)
- Docker e containerização
- Git e Git Flow
- Monitoramento com Prometheus/Grafana
- Conceitos de CI/CD

### Ferramentas Obrigatórias

- **kubectl** (versão 1.20+)
- **helm** (versão 3.0+)
- **git** (versão 2.30+)
- **jq** (para parsing JSON)
- **curl** (para testes de API)
- **VPN** conectada ao cluster

### Condições Necessárias

- **Acesso:** Permissões de deploy no cluster produção
- **Código:** Branch `main` com todos os testes passando
- **Imagem:** Docker image buildada e testada
- **Banco:** Migrations testadas em staging
- **Monitoring:** Dashboards funcionando normalmente

## Procedimento Principal

### Passo 1: Validação Pré-Deployment

#### **Comando:**

```bash
# Verificar status do cluster
kubectl cluster-info

# Verificar nodes saudáveis
kubectl get nodes

# Verificar recursos disponíveis
kubectl top nodes

# Verificar deployment atual
kubectl get deployment -n production
```

#### **Validação:**

- Cluster acessível e responsivo
- Todos os nodes em estado "Ready"
- CPU < 80% e Memory < 85% nos nodes
- Deployment atual rodando sem erros

#### **Resultado Esperado:**

```
NAME           STATUS   ROLES    AGE     VERSION
node-1         Ready    worker   45d     v1.20.0
node-2         Ready    worker   45d     v1.20.0
node-3         Ready    worker   45d     v1.20.0
```

### Passo 2: Backup e Preparação

#### **Comando:**

```bash
# Backup da configuração atual
kubectl get deployment app-backend -n production -o yaml > backup-deployment-$(date +%Y%m%d_%H%M%S).yaml

# Backup dos configmaps
kubectl get configmap -n production -o yaml > backup-configmap-$(date +%Y%m%d_%H%M%S).yaml

# Verificar última versão deployada
kubectl describe deployment app-backend -n production | grep Image
```

#### **Validação:**

- Arquivos de backup criados com sucesso
- Timestamps corretos nos backups
- Versão atual identificada

#### **Resultado Esperado:**

```
backup-deployment-20240115_143022.yaml created
backup-configmap-20240115_143022.yaml created
Image: app-backend:v1.2.3
```

### Passo 3: Atualização da Configuração

#### **Comando:**

```bash
# Atualizar valores do Helm chart
helm upgrade app-backend ./helm/app-backend \
  --namespace production \
  --set image.tag=v1.2.4 \
  --set replicaCount=3 \
  --dry-run --debug

# Se dry-run OK, executar deployment
helm upgrade app-backend ./helm/app-backend \
  --namespace production \
  --set image.tag=v1.2.4 \
  --set replicaCount=3 \
  --wait --timeout=600s
```

#### **Validação:**

- Dry-run executa sem erros
- Configuração renderizada corretamente
- Deployment iniciado com sucesso

#### **Resultado Esperado:**

```
Release "app-backend" has been upgraded. Happy Helming!
NAME: app-backend
LAST DEPLOYED: Mon Jan 15 14:30:22 2024
NAMESPACE: production
STATUS: deployed
```

### Passo 4: Monitoramento do Deployment

#### **Comando:**

```bash
# Acompanhar status do deployment
kubectl rollout status deployment/app-backend -n production --timeout=600s

# Verificar pods em execução
kubectl get pods -n production -l app=app-backend

# Verificar logs dos novos pods
kubectl logs -n production -l app=app-backend --tail=50
```

#### **Validação:**

- Rollout completo com sucesso
- Todos os pods em estado "Running"
- Logs sem erros críticos
- Health checks passando

#### **Resultado Esperado:**

```
deployment "app-backend" successfully rolled out
NAME                           READY   STATUS    RESTARTS   AGE
app-backend-7d4f8b6d9c-abc123  1/1     Running   0          2m
app-backend-7d4f8b6d9c-def456  1/1     Running   0          2m
app-backend-7d4f8b6d9c-ghi789  1/1     Running   0          2m
```

### Passo 5: Testes de Funcionalidade

#### **Comando:**

```bash
# Teste de health check
curl -s https://api.production.com/health | jq '.'

# Teste de endpoint principal
curl -s https://api.production.com/api/v1/status | jq '.'

# Teste de autenticação
curl -s -H "Authorization: Bearer $TEST_TOKEN" https://api.production.com/api/v1/user/profile | jq '.'

# Verificar métricas
curl -s https://api.production.com/metrics | grep -E "(http_requests_total|response_time)"
```

#### **Validação:**

- Health check retorna status 200
- Endpoints principais funcionando
- Autenticação funcionando corretamente
- Métricas sendo coletadas

#### **Resultado Esperado:**

```json
{
  "status": "healthy",
  "version": "v1.2.4",
  "timestamp": "2024-01-15T14:35:00Z",
  "database": "connected",
  "redis": "connected"
}
```

### Passo 6: Validação de Performance

#### **Comando:**

```bash
# Verificar métricas de CPU/Memory
kubectl top pods -n production -l app=app-backend

# Verificar response time médio
curl -s "https://grafana.production.com/api/datasources/proxy/1/api/v1/query?query=histogram_quantile(0.95,rate(http_request_duration_seconds_bucket[5m]))"

# Verificar taxa de erro
curl -s "https://grafana.production.com/api/datasources/proxy/1/api/v1/query?query=rate(http_requests_total{status=~\"5..\"}[5m])"
```

#### **Validação:**

- CPU < 70% nos pods
- Memory < 80% nos pods
- Response time p95 < 200ms
- Taxa de erro < 0.1%

#### **Resultado Esperado:**

```
NAME                           CPU(cores)   MEMORY(bytes)
app-backend-7d4f8b6d9c-abc123  45m          128Mi
app-backend-7d4f8b6d9c-def456  50m          135Mi
app-backend-7d4f8b6d9c-ghi789  48m          142Mi
```

## Validação e Testes

### Critérios de Sucesso

#### **Funcionalidade**

- [ ] Todas as APIs respondem corretamente
- [ ] Autenticação funcionando
- [ ] Integração com banco de dados OK
- [ ] Integração com Redis OK
- [ ] Logs sendo gerados corretamente

#### **Performance**

- [ ] Response time p95 < 200ms
- [ ] CPU usage < 70%
- [ ] Memory usage < 80%
- [ ] Zero memory leaks
- [ ] Throughput mantido ou melhorado

#### **Segurança**

- [ ] Certificados SSL válidos
- [ ] Headers de segurança presentes
- [ ] Autenticação obrigatória funcionando
- [ ] Rate limiting ativo
- [ ] Logs de auditoria funcionando

### Testes de Validação

#### **Teste de Carga**

```bash
# Executar teste de carga por 5 minutos
ab -n 10000 -c 50 -t 300 https://api.production.com/api/v1/status

# Verificar se sistema aguenta carga
kubectl top pods -n production -l app=app-backend
```

#### **Teste de Integração**

```bash
# Testar fluxo completo de usuário
curl -X POST https://api.production.com/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass"}'

# Usar token para acessar recurso protegido
curl -H "Authorization: Bearer $TOKEN" https://api.production.com/api/v1/dashboard
```

### Métricas de Qualidade

| Métrica       | Alvo   | Atual  | Status |
| ------------- | ------ | ------ | ------ |
| Uptime        | 99.9%  | 99.95% | ✅     |
| Response Time | <200ms | 150ms  | ✅     |
| Error Rate    | <0.1%  | 0.05%  | ✅     |
| CPU Usage     | <70%   | 50%    | ✅     |
| Memory Usage  | <80%   | 65%    | ✅     |

## Troubleshooting

### Problema Comum 1: Pods não inicializam

#### **Sintomas:**

- Pods ficam em estado "Pending" ou "ImagePullBackOff"
- Deployment não progride
- Timeout no rollout

#### **Causa:**

- Imagem não encontrada no registry
- Recursos insuficientes no cluster
- Configuração incorreta

#### **Solução:**

```bash
# Verificar eventos do pod
kubectl describe pod <pod-name> -n production

# Verificar se imagem existe
docker pull <image-name>

# Verificar recursos
kubectl describe nodes

# Corrigir configuração
kubectl edit deployment app-backend -n production
```

### Problema Comum 2: Health check falhando

#### **Sintomas:**

- Pods reiniciam constantemente
- LoadBalancer não direciona tráfego
- Readiness probe falha

#### **Causa:**

- Aplicação não está pronta para receber tráfego
- Health check endpoint com problema
- Configuração incorreta de probe

#### **Solução:**

```bash
# Verificar logs da aplicação
kubectl logs -n production -l app=app-backend --tail=100

# Testar health check manualmente
kubectl exec -it <pod-name> -n production -- curl localhost:8080/health

# Ajustar configuração de probe
kubectl patch deployment app-backend -n production -p '{"spec":{"template":{"spec":{"containers":[{"name":"app","readinessProbe":{"initialDelaySeconds":30}}]}}}}'
```

### Problema Comum 3: Performance degradada

#### **Sintomas:**

- Response time aumentado
- CPU/Memory usage alto
- Timeouts frequentes

#### **Causa:**

- Bottleneck no banco de dados
- Memory leak na aplicação
- Configuração inadequada de recursos

#### **Solução:**

```bash
# Verificar métricas detalhadas
kubectl top pods -n production -l app=app-backend

# Verificar logs de performance
kubectl logs -n production -l app=app-backend | grep -i "slow\|timeout\|error"

# Aumentar recursos temporariamente
kubectl patch deployment app-backend -n production -p '{"spec":{"template":{"spec":{"containers":[{"name":"app","resources":{"limits":{"cpu":"1000m","memory":"1Gi"}}}]}}}}'
```

### Problema Comum 4: Rollback necessário

#### **Sintomas:**

- Erro crítico detectado
- Funcionalidade principal não funciona
- Decisão de reverter deployment

#### **Causa:**

- Bug introduzido na nova versão
- Configuração incompatível
- Dependência quebrada

#### **Solução:**

```bash
# Verificar histórico de deployments
kubectl rollout history deployment/app-backend -n production

# Executar rollback para versão anterior
kubectl rollout undo deployment/app-backend -n production

# Verificar status do rollback
kubectl rollout status deployment/app-backend -n production

# Confirmar que versão anterior está funcionando
curl -s https://api.production.com/health | jq '.version'
```

## Checklist de Deployment

### Pré-deployment

- [ ] Código na branch `main` com testes passando
- [ ] Docker image buildada e testada
- [ ] Staging environment validado
- [ ] Migrations testadas
- [ ] Plano de rollback definido

### Durante deployment

- [ ] Backup da configuração atual
- [ ] Dry-run executado com sucesso
- [ ] Deployment executado
- [ ] Rollout status monitorado
- [ ] Testes funcionais executados

### Pós-deployment

- [ ] Health checks passando
- [ ] Métricas dentro do esperado
- [ ] Logs sem erros críticos
- [ ] Testes de integração OK
- [ ] Documentação atualizada

## Plano de Contingência

### Rollback Automático

- Configurado para reverter se health check falhar por 5 minutos
- Trigger automático se error rate > 1%
- Notificação imediata via Slack/PagerDuty

### Rollback Manual

- Comando de rollback disponível a qualquer momento
- Backup da configuração sempre disponível
- Processo documentado e testado

### Comunicação

- Notificação automática no #deployments
- Status page atualizada automaticamente
- Escalação para tech lead se necessário

---

**Processo validado e testado. Deployment realizado com sucesso em produção.**
