from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/contatoTeste")
def contatoTeste():
    return """
    Site para contato <br>
    
    Qualquer dúvida entre em contato <br><br>

    ijuniorao@gmail.com
    """


@app.route("/nexustech")
def teste():
    return render_template("nexustech.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/contato")
def contato():
    return render_template("contatos.html")


@app.route("/faleconosco")
def faleConosco():
    return render_template("faleconosco.html")


if __name__ == "__main__":
    app.run(debug=True)
