from flask import Flask
from flask import render_template, jsonify, make_response, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

# global password
password = "SESH2021You'llNeverGuess!"

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/verify-login", methods=["POST"])
def verify_login():
    #redirect to secret
    #they can see the path in the redirects if looking carefully
    resp = make_response(redirect('/secret', code=302))

    #set cookie with basic encoding
    #they must guess they need to modify it
    if request.form.get('password') == password:
        print("Correct!")
        resp.set_cookie('status', "authorised".translate(rot13))
    else:
        resp.set_cookie('status', "unauthorised".translate(rot13))

    return resp

@app.route("/secret")
def view_secret():
    if request.cookies.get('status') is not None:
        if request.cookies.get('status').translate(rot13) == "authorised":
            #unset the cookie for the next player
            #then return the page
            resp = make_response(render_template('secret.html'))
            resp.set_cookie('status', 'none', max_age=0)
            return resp
        else:
            return redirect('/', code=302)
    else:
        return redirect('/', code=302)

@app.route("/reset-password", methods=["POST"])
def reset_password():
    global password
    password = request.form.get('new_password')

    security_answer = request.form.get('security_answer')

    if security_answer == "ChocolateCakeWithSprinkles":
        return jsonify({'correct':'true'})
    else:
        return jsonify({'correct':'false'})