# BlogPython - Blog em Flask com PostgreSQL Containerizado

Projeto simples de blog feito em Flask com banco PostgreSQL, todo rodando em containers Docker orquestrados pelo Docker Compose.

---

## Tecnologias Utilizadas

- Python 3.10 + Flask
- PostgreSQL 15
- Docker & Docker Compose
- psycopg2 para conexão com PostgreSQL
- python-dotenv para variáveis de ambiente

---

## Estrutura do Projeto

BlogPython/
│
├── app.py # Código principal da aplicação Flask
├── Dockerfile # Imagem Docker da aplicação
├── docker-compose.yml # Orquestração dos containers (app + banco)
├── requirements.txt # Dependências Python
├── .env.example # Exemplo de arquivo de variáveis de ambiente
├── .gitignore # Arquivos ignorados pelo Git
├── README.md # Documentação do projeto
└── templates/ # Templates HTML (layout e index)
├── layout.html
└── index.html

## Como Rodar Localmente

### Pré-requisitos

- Docker instalado
- Docker Compose instalado
- Git

### Passos

1. Clone o repositório:

git clone https://github.com/marcoantoniolobo82/BlogPython.git

2. Crie um arquivo .env baseado no .env.example com suas credenciais:

env

DB_NAME=blogdb
DB_USER=malobo
DB_PASSWORD=233234
DB_HOST=db
DB_PORT=5432

3. Construa e rode os containers com Docker Compose:

docker-compose up -d

4. Acesse no navegador:

http://localhost:8080

## Como Funciona a Arquitetura
Service db: container PostgreSQL com volume para persistência dos dados.

Service web: container Flask que depende do db e se conecta usando variáveis de ambiente.

Rede Docker interna facilita comunicação entre os containers pelo hostname db.

## Recursos Implementados
CRUD básico de posts (apenas criação e listagem)

Interface web simples com formulário para adicionar posts

Armazenamento dos posts no banco PostgreSQL

Visualização dos posts em ordem decrescente, com data/hora de criação

Variáveis de ambiente gerenciadas via .env

Containerização completa com Docker e Docker Compose

### Próximos Passos / Melhorias Futuras

Autenticação e autorização

Atualização e exclusão de posts (CRUD completo)

Testes automatizados

Pipeline CI/CD com GitHub Actions para build/test/deploy automático

Deploy em nuvem (AWS, GCP, Azure) ou Kubernetes

Contato
Criado por Marco Lobo
