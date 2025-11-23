from flask import Flask, request, jsonify, render_template
import mysql.connector
import ssl

app = Flask(__name__)

# Conexão com MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA_AQUI",
    database="meubanco"
)
cursor = db.cursor()

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para salvar dados
@app.route('/salvar-dados', methods=['POST'])
def salvar_dados():
    data = request.get_json()
    email = data.get('email')
    mensagem = data.get('mensagem')

    if not email or not mensagem:
        return jsonify({'erro': 'Dados incompletos'}), 400

    try:
        # Prepared statement para segurança
        sql = "INSERT INTO contatos (email, mensagem) VALUES (%s, %s)"
        cursor.execute(sql, (email, mensagem))
        db.commit()
        return jsonify({'sucesso': True})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    # Para HTTPS local, gere certificados autoassinados
    context = ('certs/cert.pem', 'certs/key.pem')  # opcional
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)
    
