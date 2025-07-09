# BlogPython - Blog em Flask com PostgreSQL Containerizado no Kubernetes

Projeto simples de blog feito em Flask com banco PostgreSQL, rodando em containers Docker orquestrados pelo Kubernetes.

---

## Tecnologias Utilizadas

- Python 3.10 + Flask  
- PostgreSQL 15  
- Docker  
- Kubernetes  
- psycopg2 para conexão com PostgreSQL  
- python-dotenv para variáveis de ambiente  

---

## Estrutura do Projeto

```plaintext
BlogPython/
│
├── app.py                     # Código principal da aplicação Flask
├── Dockerfile                 # Imagem Docker da aplicação
├── k8s/
│   ├── deployment-dev.yaml    # Manifest para ambiente de desenvolvimento (com probes configurados)
│   ├── deployment-prod.yaml   # Manifest para ambiente de produção (com probes configurados)
│   ├── quota-dev.yaml         # ResourceQuota para ambiente dev
│   ├── quota-prod.yaml        # ResourceQuota para ambiente prod
│   ├── kind-config.yaml       # Configuração do cluster Kind
│   └── k3d-config.yaml        # Configuração do cluster K3d
├── requirements.txt           # Dependências Python
├── .env.example               # Exemplo de arquivo de variáveis de ambiente
├── .gitignore                 # Arquivos ignorados pelo Git
├── README.md                  # Documentação principal do projeto
├── templates/                 # Templates HTML (layout e index)
│   ├── layout.html
│   └── index.html
└── static/                    # Arquivos estáticos (CSS, imagens, JS)
    └── style.css
```

---

## Como Rodar Localmente com Kubernetes

### Pré-requisitos

- Docker instalado  
- Kubernetes instalado (minikube, kind, k3d ou outro)  
- kubectl configurado  
- Git  

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/marcoantoniolobo82/BlogPython.git
cd BlogPython
```

2. Crie o cluster Kubernetes:

- Com Kind:

```bash
kind create cluster --config k8s/kind-config.yaml
```

- Com K3d:

```bash
k3d cluster create meu-cluster --config k8s/k3d-config.yaml
```

3. Faça o build da imagem Docker e envie para o Docker Hub (ou use imagem pública):

```bash
docker build -t marcoantoniolobo82/blogpython:v1 .
docker push marcoantoniolobo82/blogpython:v1
```

4. Para aplicar o ambiente de desenvolvimento (contém liveness, readiness e startup probes configurados):

```bash
kubectl apply -f k8s/deployment-dev.yaml
```

Ou para aplicar o ambiente de produção (também com probes configurados):

```bash
kubectl apply -f k8s/deployment-prod.yaml
```
Ou Aplique a ResourceQuota para limitar recursos por namespace:

Para ambiente de desenvolvimento:

```bash
kubectl apply -f k8s/quota-dev.yaml -n dev
```
Para ambiente de produção:

```bash
kubectl apply -f k8s/quota-prod.yaml -n prod
```
Aplique o ambiente de desenvolvimento (contém probes configurados e quotas aplicadas):

```bash
kubectl apply -f k8s/deployment-dev.yaml -n dev
```
Ou para o ambiente de produção:

```bash
kubectl apply -f k8s/deployment-prod.yaml -n prod
```

5. Verifique os pods, serviços e volumes:

```bash
kubectl get pods,svc,pvc -n dev
kubectl get pods,svc,pvc -n prod
```

6. Acesse a aplicação:

```text
http://localhost:30000
```

---

## Como Funciona a Arquitetura

- Os arquivos `deployment-dev.yaml` e `deployment-prod.yaml` contêm **ConfigMap**, **Secret**, **Deployments** e **Services** adequados para cada ambiente.  
- Nos Deployments `web`, estão configurados os **liveness probe**, **readiness probe** e **startup probe** para monitorar a saúde e disponibilidade da aplicação Flask.
- **ResourceQuota** nos namespaces `dev` e `prod` para garantir limites de CPU, memória e pods, evitando sobrecarga do cluster.  
- **Service db**: container PostgreSQL com PersistentVolumeClaim para persistência dos dados.  
- **Service web**: container Flask que depende do db, conecta via variáveis de ambiente do ConfigMap e Secret.  
- Rede interna Kubernetes facilita comunicação entre os containers pelo hostname `db`.  

---

## Variáveis de Ambiente

Gerenciadas via ConfigMap e Secret definidos nos manifests:

| Variável         | Descrição                  |
|------------------|----------------------------|
| APP_PORT         | Porta da aplicação Flask   |
| APP_ENV          | Ambiente (development ou production) |
| POSTGRES_DB      | Nome do banco PostgreSQL   |
| POSTGRES_USER    | Usuário do banco           |
| POSTGRES_PASSWORD| Senha do banco             |
| DB_HOST          | Host do banco (db)         |
| DB_PORT          | Porta do banco (5432)      |
| DB_NAME          | Nome do banco              |
| DB_USER          | Usuário do banco           |
| DB_PASSWORD      | Senha do banco             |

---

## Recursos Implementados

- CRUD básico de posts (criação e listagem)  
- Interface web simples com formulário para adicionar posts  
- Armazenamento dos posts no banco PostgreSQL  
- Visualização dos posts em ordem decrescente, com data/hora de criação  
- Variáveis de ambiente gerenciadas via ConfigMap e Secret no mesmo arquivo  
- Containerização com Docker e orquestração com Kubernetes  
- **Liveness probe, readiness probe e startup probe configurados** para garantir resiliência da aplicação  
- ResourceQuota para controlar uso de recursos no cluster e evitar consumo excessivo

---

## Próximos Passos / Melhorias Futuras

- Autenticação e autorização  
- Atualização e exclusão de posts (CRUD completo)  
- Testes automatizados  
- Pipeline CI/CD com GitHub Actions para build/test/deploy automático  
- Deploy em nuvem (AWS, GCP, Azure)  

---

## Contato

Criado por Marco Lobo  
https://github.com/marcoantoniolobo82
