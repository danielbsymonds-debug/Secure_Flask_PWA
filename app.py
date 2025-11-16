from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    connection = sqlite3.connect('LoginData.db') 
    cursor = connection.cursor()

    user = cursor.execute("SELECT * FROM  USERS WHERE email=? AND password=?", (email,password)).fetchall()
    if len(user) > 0:
        return 'Welcome'
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)