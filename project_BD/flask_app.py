from flask import Flask, render_template, redirect, url_for
from flask_forms import Formulare_Login

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import bd

# configuracao
app = Flask(__name__)
app.config.from_object('flask_config')



db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@app.route('/', methods=["POST","GET"])
def login():
    formL = Formulare_Login()

    if formL.validate_on_submit():
        return redirect(url_for('home'))

    return render_template('login.html',formL = formL)

@app.route('/home',methods=["GET","POST"])
def home():
    return render_template('principal.html')

if __name__ == '__main__':
    manager.run()





