from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    return "Página inicial"


app.run()