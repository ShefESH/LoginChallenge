from flask import Flask
from flask import render_template, jsonify, make_response, redirect, request
from flask_bootstrap import Bootstrap
from base64 import b64encode, b64decode, urlsafe_b64decode

app = Flask(__name__)
Bootstrap(app)

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
        resp.set_cookie('status', b64encode(b"authorised"))
    else:
        resp.set_cookie('status', b64encode(b"unauthorised"))

    return resp

@app.route("/secret")
def view_secret():
    if request.cookies.get('status') is not None:
        testCookie=request.cookies.get('status')
        print(testCookie)
        cookieVal = b64decode(testCookie.encode('utf-8'), '-_')
        print(cookieVal)
        if cookieVal.decode('utf-8') == "authorised":
            #unset the cookie and reset the password for the next player
            #then return the page
            resp = make_response(render_template('secret.html'))
            resp.set_cookie('status', 'none', max_age=0)
            global password
            password = "SESH2021You'llNeverGuess!"
            return resp
        else:
            return redirect('/', code=302)
    else:
        return redirect('/', code=302)

@app.route("/reset-password", methods=["POST"])
def reset_password():
    global password
    if request.form.get('new_password') != "":
        password = request.form.get('new_password')

    security_answer = request.form.get('security_answer')

    if security_answer == "ChocolateCakeWithSprinkles":
        return jsonify({'correct':'true'})
    else:
        return jsonify({'correct':'false'})