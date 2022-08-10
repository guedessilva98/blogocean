
from flask import Flask, render_template

app = Flask("hello")
nomeAula = "Aula Python para web"


@app.route("/usuario")
def usuario():
    usuario = [1, "Andre Guedes", "Professor"]
    alunos = ["Andre Guedes", "Lucas Santos", "Alicia Duarte", "Raiane Caroline"]
    return render_template("index.html", alunos = alunos, usuario = usuario)

@app.route("/contato")
def contato():
    return render_template("index.html", usuario = usuario, nome = nomeAula)
@app.route("/teste")
def teste():
    return "teste"
