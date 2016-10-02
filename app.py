from flask import Flask, redirect, render_template, request
from utils import account

import hashlib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/redirect/", methods = ['POST'])
def redir():
    try:
        if request.form['login'] == "Submit":
            return redirect("/authenticate/", code=307)
    except Exception:
        return redirect("/create/", code=307)
    
@app.route("/authenticate/", methods = ['POST'])
def auth():
    L = account.get_file()
    usr = hashlib.sha224(request.form['user']).hexdigest()
    i = account.is_user(usr, L)
    pwd = hashlib.sha224(request.form['pass']).hexdigest()
    resp = ""
    if i != -1:
        if account.is_pass(pwd, i, L):
            resp = "You have logged in successfully."
        else:
            resp = "Sorry, the password you submitted was incorrect."
            
    else:
        resp = "Sorry, the username you submitted does not exist."
    return render_template("response.html", response = resp)

@app.route("/create/", methods = ['POST'])
def create():
    L = account.get_file()
    usr = hashlib.sha224(request.form['user']).hexdigest()
    pwd = hashlib.sha224(request.form['pass']).hexdigest()
    if account.is_user(usr, L):
        return render_template("response.html", response = "Sorry, that username already exists.")
    account.add_usr_pwd(usr, pwd)
    return render_template("response.html", response = "Congratulations, your account has successfully been created!")

if __name__ == '__main__':
    app.debug = True
    app.run()
