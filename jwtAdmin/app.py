from flask import Flask, request, jsonify, make_response
import random
import string
import jwt
app = Flask(__name__)
# Generate a random name
def generate_name():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
# Generate a JWT
def generate_jwt(name, id):
    payload = {
        'name': name,
        'id': id
    }
    return jwt.encode(payload, 'secret', algorithm='HS256')
# Verify a JWT
def verify_jwt(token):
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256','None'])
        return payload
    except:
        return None
# Login route
@app.route('/', methods=['GET'])
def login():
    name = generate_name()
    id = random.randint(2, 100)
    token = generate_jwt(name, id)
    resp = make_response("Se ha asignado un jwt al usuario actual")
    resp.set_cookie('token', token)
    return resp
# Admin panel route
@app.route('/admin')
def admin():
    token = request.cookies.get('token')
    payload = verify_jwt(token)
    if payload and payload['id'] == 1:
        return '<h1>Bienvenido al panel de administrador</h1>'
    else:
        return '<h1>No tienes permiso para acceder a esta página</h1>', 401
if __name__ == '__main__':
    app.run(debug=True)
