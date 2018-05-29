from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    author = "Prashant Bhosale"
    name = "Prashant Bhosale"
    return render_template('index.html', author=author, name=name)
