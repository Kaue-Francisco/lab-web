################################################################################
# Importa as bibliotecas necessárias
from flask import jsonify
import sqlite3

################################################################################
class UserView:
    """ Classe para fazer a conexão com o banco de dados e realizar operações de CRUD """

    def create_user(self, data):
        """ Método para criar um usuário no banco de dados """

        name = data['name']
        age = data['age']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
            conn.commit()
            conn.close()
            return jsonify({'message': 'User created successfully'}), 201
        except:
            return jsonify({'message': 'An error occurred while trying to create the user'}), 500
    
    ################################################################################
    def get_users(self):
        """ Método para retornar todos os usuários do banco de dados """

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            conn.close()

            if users:
                users = [{'name': user[1], 'age': user[2]} for user in users]
                return jsonify(users)

            return jsonify({'message': 'No users found'}), 404
        except:
            return jsonify({'message': 'An error occurred while trying to get users'}), 500

    ################################################################################
    def get_user(self, id):
        """ Método para retornar um usuário específico do banco de dados """

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
            user = cursor.fetchone()
            conn.close()

            if user:
                return list(user)[1:]
    
            return jsonify({'message': 'User not found'}), 404
        except:
            return jsonify({'message': 'An error occurred while trying to get the user'}), 500

    ################################################################################
    def update_user(self, id, data):
        """ Método para atualizar um usuário no banco de dados """

        name = data['name']
        age = data['age']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, id))
            conn.commit()
            conn.close()
            return jsonify({'message': 'User updated successfully'}), 200
        except:
            return jsonify({'message': 'An error occurred while trying to update the user'}), 500

    ################################################################################
    def delete_user(self, id):
        """ Método para deletar um usuário do banco de dados """

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('DELETE FROM users WHERE id = ?', (id,))
            conn.commit()
            conn.close()
            return jsonify({'message': 'User deleted successfully'}), 200
        except:
            return jsonify({'message': 'An error occurred while trying to delete the user'}), 500