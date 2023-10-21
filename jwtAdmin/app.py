from flask import Flask, request, jsonify, make_response, render_template
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
    resp = make_response(render_template('menu.html'))
    resp.set_cookie('token', token)
    return resp

@app.route('/secrets', methods=['GET'])
def secrets():
    resp = make_response(render_template('secret.html'))
    return resp
# Admin panel route

@app.route('/admin')
def admin():
    token = request.cookies.get('token')
    payload = verify_jwt(token)
    if payload and payload['id'] == 1:
        return make_response(render_template('result.html'))
    else:
        msg = "Acceso denegado, usted no es un administrador"
        angry = "../static/resources/synthia_angry.png"
        return make_response(render_template('menu.html', msg = msg, angry = angry)), 401
if __name__ == '__main__':
    app.run(debug=True)
