from flask import Flask, render_template
from forms import Formulare_Login, Formulare_addMusic


app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def entrar():
    return render_template('principal.html')

@app.route('/login', methods=["POST","GET"])
def login():
    formL = Formulare_Login() 
    if formL.validate_on_submit():
        entrar()
    return render_template('login.html',formL = formL)

@app.route('/addmusic', methods=["POST","GET"])
def addMusic():
    formA = Formulare_addMusic()
    return render_template("addMusic.html",formA = formA)

if __name__ == '__main__':
    app.run()