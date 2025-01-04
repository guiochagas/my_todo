from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__": #Se o código for executado diretamente, irá rodar o 'app.run'... mas se o 'site.py' for importado, o código não será executado.
    app.run(debug=True)