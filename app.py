
from flask import Flask

app = Flask("hello")


@app.route("/")
def hello():
    return "Hello World"

@app.route("/contato")
def contato():
    return """
                <html>
                    <head>
                        <title> Contatos </title>
                    </head>
                    <body>
                        <h1>Andre Guedes</h1>
                        <h2>dreh@email.com</h2>
                        <h3>4432423-434234</h3>
                    </body>
                </html>"""

