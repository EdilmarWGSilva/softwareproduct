from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'produtos_db'
}

# Rota para cadastro de produtos
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()

    # Conecta ao banco de dados
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insere o produto no banco de dados
    sql = "INSERT INTO produtos (nome, preco, descricao) VALUES (%s, %s, %s)"
    val = (data['name'], data['price'], data['description'])
    cursor.execute(sql, val)

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Produto cadastrado com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
