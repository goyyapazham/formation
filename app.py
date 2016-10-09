from flask import Flask, redirect, render_template, request, url_for, session
from utils import account

import hashlib

app = Flask(__name__)
app.secret_key = "nala_est_tres_cool"

@app.route("/")
def main():
    if 'user' in session.keys():
        return redirect(url_for('home'))
    return render_template("login.html", message = "")

@app.route("/home/")
def home():
    return render_template("home.html", username = session['user'])
    
@app.route("/auth/", methods = ['POST'])
def auth():
    sub = request.form['sub']
    usr = request.form['user']
    pwd = hashlib.sha224(request.form['pass']).hexdigest()
    if sub == "Login":
        x = account.login(usr, pwd)
    if sub == "Register":
        x = account.register(usr, pwd)
    if x == 1:
        session['user'] = usr
        return redirect(url_for('home'))
    return render_template("login.html", message = account.get_message(x))

@app.route("/logout/", methods = ['POST'])
def logout():
    session.pop('user')
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.debug = True
    app.run()
