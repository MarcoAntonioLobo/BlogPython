from flask import Flask, render_template, request, redirect
import psycopg2
from dotenv import load_dotenv
import os
import time

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("POSTGRES_PORT")
    )
    return conn

def create_database_and_table():
    print("Tentando conectar ao banco de dados...")
    while True:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            );
            """)
            conn.commit()
            conn.close()
            print("Tabela 'posts' criada ou já existe.")
            break
        except psycopg2.OperationalError:
            print("Banco ainda não está pronto. Aguardando 2 segundos...")
            time.sleep(2)
        except Exception as e:
            print("Erro inesperado:", e)
            time.sleep(2)

create_database_and_table()

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM posts ORDER BY id DESC")
    posts = cursor.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
