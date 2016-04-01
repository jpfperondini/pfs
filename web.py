from flask import Flask, render_template

def init():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template("index.html", statement=[("01/01/2016", "Teste", 56.21)])

    return app;
