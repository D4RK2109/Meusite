import sqlite3
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

DB_PATH = '/data/data/com.termux/files/home/downloads/myslqenter.db'

# Função para criar conexão por requisição
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

# Criar a tabela caso não exista
if not os.path.exists(DB_PATH):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        mensagem TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salvar-dados', methods=['POST'])
def salvar_dados():
    data = request.get_json()
    email = data.get('email')
    mensagem = data.get('mensagem')

    if not email or not mensagem:
        return jsonify({'erro': 'Dados incompletos'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contatos (email, mensagem) VALUES (?, ?)", (email, mensagem))
        conn.commit()
        conn.close()
        return jsonify({'sucesso': True})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    # Executa no Termux (localhost:5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
    
