from flask import Flask, render_template, request #new

app = Flask(__name__)

usr = "u"
pwd = "p"

@app.route("/")
@app.route("/login/") #can have multiple routes attached
def run():
    #print request.headers
    return render_template("main.html")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    #print request.form
    #print request.form['user']
    if request.form['user'] == usr and request.form['pass'] == pwd:
        resp = "!!! login successful"
    else:
        resp = "smh"
    return render_template("response.html", response = resp)
    
if __name__ == '__main__':
    app.debug = True
    app.run()
