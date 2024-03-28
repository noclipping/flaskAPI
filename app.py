from flask import Flask, request, jsonify
from db import get_db_connection
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email) VALUES (%s, %s)',
                (data['name'], data['email']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(data), 201

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE users SET name = %s, email = %s WHERE id = %s',
                (data['name'], data['email'], id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(data)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'User deleted successfully'}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
