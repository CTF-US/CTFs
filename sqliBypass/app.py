from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/robots.txt')
def getHint():
   return "User-agent: * <br>Disallowed: /wordpress/defaultCreds"

@app.route('/login',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         username = request.form['username']
         password = request.form['password']
         correctDefaultCred = False
         correctSqlinyection = False
         
         with sql.connect("database.db") as con:
            if username =='username' and password == 'password':
               correctDefaultCred=True
               msg ="flag{pRi_meRa__FlAg_deL_Reto_fAltaOtRa}"
            else:
               cur = con.cursor()
               cur.execute("select * from users where username = '" + username + "' and password = '" + password + "'")
               row = cur.fetchall()
               if len(row) > 0:
                  correctSqlinyection = True
                  msg = "flag{seG_unDa__FlAg_deL_Reto_fAltaOtRa}"
               else:
                  msg = " Los datos introducidos no fueron correctos."
                  return render_template('login.html')

      except Exception as e:
         con.rollback()
         print(e)
         msg = "error in login"
      finally:
        con.close()
        if correctSqlinyection:
           return render_template("resultInyection.html",msg = msg)
        elif correctDefaultCred:
           return render_template("resultDefaultCred.html", msg = msg)
        else:
           return render_template('login.html',msg = msg)
   else:
      return render_template('login.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

