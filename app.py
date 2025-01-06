from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jwt_secret_key'  # In production, use secure key

# Mock database of users
USERS = {
    'testuser': {
        'password': 'password123',
        'id': 1
    }
}

@app.route('/')
def home():
    return "Welcome to the Authentication API"

@app.route('/auth/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing credentials', 'status': 'failure'}), 400
        
    username = data['username']
    password = data['password']
    
    if username in USERS and USERS[username]['password'] == password:
        token = jwt.encode({
            'user_id': USERS[username]['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({
            'token': token,
            'status': 'success'
        }), 200
    
    return jsonify({'error': 'Invalid credentials', 'status': 'failure'}), 401

if __name__ == '__main__':
    app.run(debug=True)