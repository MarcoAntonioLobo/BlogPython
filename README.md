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
├── app.py                 # Código principal da aplicação Flask
├── Dockerfile             # Imagem Docker da aplicação
├── k8s/
│   └── deployment.yaml    # Manifest único Kubernetes (ConfigMap, Secret, Deployments, Services)
├── requirements.txt       # Dependências Python
├── .env.example           # Exemplo de arquivo de variáveis de ambiente
├── .gitignore             # Arquivos ignorados pelo Git
├── README.md              # Documentação principal do projeto
├── templates/             # Templates HTML (layout e index)
│   ├── layout.html
│   └── index.html
└── static/                # Arquivos estáticos (CSS, imagens, JS)
    └── style.css
```

---

## Como Rodar Localmente com Kubernetes

### Pré-requisitos

- Docker instalado  
- Kubernetes instalado (minikube, kind ou outro)  
- kubectl configurado  
- Git  

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/marcoantoniolobo82/BlogPython.git
cd BlogPython
```

2. Crie o cluster Kubernetes (exemplo com kind):

```bash
kind create cluster --config kind-config.yaml
```

3. Aplique o manifesto Kubernetes único:

```bash
kubectl apply -f k8s/deployment.yaml
```

4. Verifique os pods, serviços e volumes:

```bash
kubectl get pods,svc,pvc
```

5. Acesse a aplicação no navegador:

```text
http://localhost:30000
```

---

## Como Funciona a Arquitetura

- O arquivo `deployment.yaml` contém **ConfigMap**, **Secret**, **Deployments** e **Services** juntos.  
- **Service db**: container PostgreSQL com PersistentVolumeClaim para persistência dos dados.  
- **Service web**: container Flask que depende do db, conecta via variáveis de ambiente do ConfigMap e Secret.  
- Rede interna Kubernetes facilita comunicação entre os containers pelo hostname `db`.  

---

## Variáveis de Ambiente

Gerenciadas via ConfigMap e Secret definidos no `deployment.yaml`:

| Variável         | Descrição                |
|------------------|--------------------------|
| APP_PORT         | Porta da aplicação Flask |
| APP_ENV          | Ambiente (development)   |
| POSTGRES_DB      | Nome do banco PostgreSQL |
| POSTGRES_USER    | Usuário do banco         |
| POSTGRES_PASSWORD| Senha do banco           |
| DB_HOST          | Host do banco (db)       |
| DB_PORT          | Porta do banco (5432)    |
| DB_NAME          | Nome do banco            |
| DB_USER          | Usuário do banco         |
| DB_PASSWORD      | Senha do banco           |

---

## Recursos Implementados

- CRUD básico de posts (criação e listagem)  
- Interface web simples com formulário para adicionar posts  
- Armazenamento dos posts no banco PostgreSQL  
- Visualização dos posts em ordem decrescente, com data/hora de criação  
- Variáveis de ambiente gerenciadas via ConfigMap e Secret no mesmo arquivo  
- Containerização com Docker e orquestração com Kubernetes  

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
