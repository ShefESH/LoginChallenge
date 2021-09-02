from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template('login.html')