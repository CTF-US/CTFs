from flask import Flask, request
app = Flask(__name__)

def getIP(request):
  if 'X-Forwarded-For' in request.headers:
      return request.headers['X-Forwarded-For']
  return request.remote_addr

@app.route('/admin')
def admin():
    if getIP(request) == '127.0.0.1':
        return '<h1>Bienvenido a la página de administración</h1>'
    else:
        return '<h1>No tienes permiso para acceder a esta página</h1>', 401
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
