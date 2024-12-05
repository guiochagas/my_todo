from flask import Flask

app = Flask(__name__)


@site.route("/")
def homepage():
    return "Página inicial"


app.run()