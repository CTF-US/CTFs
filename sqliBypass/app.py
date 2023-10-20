from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/login',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         username = request.form['username']
         password = request.form['password']
         correct = False
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("select * from users where username = '" + username + "' and password = '" + password + "'")
            row = cur.fetchall()

            if len(row) > 0:
               correct = True
               msg = "flag{example}"
            else:
               msg = " Los datos introducidos no fueron correctos."
               return render_template('login.html')
      except Exception as e:
         con.rollback()
         print(e)
         msg = "error in login"
      finally:
        con.close()
        if correct:
           return render_template("result.html",msg = msg)
        else:
           return render_template('login.html',msg = msg)
   else:
      return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)