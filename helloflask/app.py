# cd helloflask && export FLASK_APP=app.py && python3 -m flask run

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    if name:
        return render_template("hello.html", name=name)
    else:
        return "<h1>Hello, world!</h1>"

@app.route("/double/<number>")
def double(number = None):
    if number:
        return f"{float(number)*2}"
    else:
        return f"Enter a number"