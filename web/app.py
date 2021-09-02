from flask import Flask
from flask import render_template, jsonify, make_response, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/verify-login", methods=["POST"])
def verify_login():
    resp = make_response(redirect('/secret', code=302))

    # print(request.form.get('password'))

    if request.form.get('password') == "SESH2021You'llNeverGuess!":
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
            resp = make_response(render_template('secret.html'))
            resp.set_cookie('status', 'none', max_age=0)
            return resp
        else:
            return redirect('/', code=302)
    else:
        return redirect('/', code=302)