from flask import Flask,request,render_template,url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mail = request.form['mail']
        phone = request.form['phone']
        #de aca para abajo tengo que mejorarlo porque funciona pero es muy inseguro y no tiene muy buenas practicas
        if len(username) >= 3 and len(username) <= 20 and len(password)>= 5 and len(password)<= 20:
            with sqlite3.connect('Data.db') as conn:
                cursor = conn.cursor()
                #agregando los users y las contras a base de datos
                cursor.execute(f'''INSERT INTO Users (username,password,mail,phone) VALUES ("{username}","{password}","{mail}","{phone}")''')
        else:
            error = """El nombre de usuario debe tener entre 3 a 20 caracteres. \n
            La contraseña debe tener entre 5 y 20 caracteres"""
            return render_template('index.html', error = error)
    return render_template('index.html')