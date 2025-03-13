################################################################################
# Importando as bibliotecas necessárias

from flask import Flask, request, jsonify, render_template
from view.user_view import UserView
import sqlite3

################################################################################
app = Flask(__name__)
user_view = UserView()

################################################################################
def init_db():
    """ Método para criar a tabela no banco de dados """

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

################################################################################
@app.route('/create-user', methods=['POST'])
def create_user():
    """ Método para criar um usuário no banco de dados """

    data = request.get_json()
    response = user_view.create_user(data)
    
    return response

################################################################################
@app.route('/users', methods=['GET'])
def get_users():
    """ Método para retornar todos os usuários do banco de dados """

    response = user_view.get_users()

    return response

################################################################################
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """ Método para retornar um usuário específico do banco de dados """

    response = user_view.get_user(id)

    return response

################################################################################
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """ Método para atualizar um usuário no banco de dados """

    data = request.get_json()
    response = user_view.update_user(id, data)

    return response

################################################################################
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """ Método para deletar um usuário do banco de dados """
    
    response = user_view.delete_user(id)

    return response

################################################################################
@app.route('/')
def home():
    return render_template('index.html')  

################################################################################
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)