from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    return "Página inicial"

@app.route("/outra_page")
def outra_page():
    return "Another page created"

if __name__ == "__main__": #Se o código for executado diretamente, irá rodar o 'app.run'... mas se o 'site.py' for importado, o código não será executado.
    app.run(debug=True)