import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Conexão com o arquivo .db (no Termux)
db = sqlite3.connect('/data/data/com.termux/files/home/myslqenter.db', check_same_thread=False)
cursor = db.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    mensagem TEXT NOT NULL
)
""")
db.commit()

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
        sql = "INSERT INTO contatos (email, mensagem) VALUES (?, ?)"
        cursor.execute(sql, (email, mensagem))
        db.commit()
        return jsonify({'sucesso': True})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

