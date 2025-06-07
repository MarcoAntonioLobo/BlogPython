# BlogPython

Blog simples em Flask com PostgreSQL.

## Como usar

1. Crie um banco PostgreSQL e configure o arquivo `.env` com suas credenciais:

DB_NAME=seubanco
DB_USER=seuusuario
DB_PASSWORD=suasenha
DB_HOST=localhost
DB_PORT=5432

javascript
Copiar
Editar

2. Instale as dependências:

bash
pip install -r requirements.txt

Rode o app:

bash
Copiar
Editar
python app.py
Acesse no navegador: http://localhost:8080