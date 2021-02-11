from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager, login_user, logout_user

from flask_forms import*
from acessbd import*
# configuracao
app = Flask(__name__)
app.config.from_object('flask_config')



db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)

import bd


@lm.user_loader
def get_user(use_email):
    return Usuario.query.filter_by(email=use_email).first()

@app.route('/', methods=["POST","GET"])
def login():
	if request.method == 'POST':
		email = request.form['email']
		pwd = request.form['senha']
		user = Usuario.query.filter_by(email=email).first()
		try:
			if not user:
				return redirect(url_for('login'))
			if pwd != user.senha:
				return redirect(url_for('login'))
		except:
			return render_template('login.html')

		login_user(user)
		return redirect(url_for('home'))
	return render_template('login.html')


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/cadastro_ouvinte', methods=['GET', 'POST'])
def cadastro_ouvinte():
	formU = Formulare_cadastro_User()
	formO = Formulare_ouvinte()
	if formU.validate_on_submit() and formU.senha.data == formU.confirm.data:
		from acessbd import addOuvinte

		if formO.validate_on_submit():
			perfis = Perfil.query.all()
			ide = len(perfis) + 1
			addPerfil(ide, "info")
			p = Perfil.query.filter_by(ide=ide).first()

			try:
				addUsuario(formU.email.data, formU.senha.data, formU.data_nasc.data)
			except exc.SQLAlchemyError as e:
				print(e)
				return render_template('cadastro.html', formU=formU, formO=formO)

			try:
				addOuvinte(formU.email.data, formO.p_nome.data, 'sobrenome', p.ide)
			except exc.SQLAlchemyError as e:
				print(e)
				return render_template('cadastro.html', formU=formU, formO=formO)

			print("adicionei no banco")
				
			return redirect(url_for('login'))

	return render_template('cadastro.html', formU=formU, formO=formO)


@app.route('/escolha')
def escolha():
	return render_template('escolha.html')


@app.route("/cadastro_artista", methods=['GET', 'POST'])
def cadastro_artista():

	formA = Formulare_artista()
	formU = Formulare_cadastro_User()
	if formA.validate_on_submit() and formU.senha.data == formU.confirm.data:
		from acessbd import addUsuario, addArtista

		try:
			addUsuario(formU.email.data, formU.senha.data, formU.data_nasc.data)
		except exc.SQLAlchemyError as e:
			print(e)
			return render_template('cadastro_artista.html', formA=formA, formU=formU)

		try:
			addArtista(formU.email.data, formA.nome.data, formA.biografia.data, formA.ano_form.data)
		except exc.SQLAlchemyError as e:
			print(e)
			return render_template('cadastro_artista.html', formA=formA, formU=formU)

		return redirect(url_for('login'))

	return render_template('cadastro_artista.html', formA=formA, formU=formU)


def prox_id(table):
	return len(table.query.all()) + 1

@app.route('/cadastro_musica',methods=['GET', 'POST'])
def cadastro_musica():

	formM = Formulare_addMusic()
	
	if formM.validate_on_submit():
		ide = prox_id(Musica)
		addMusica(ide, formM.nome.data, formM.duracao.data)
		addMus_tem_gen(ide, formM.genero.data)	

	return render_template('cadastro_musica.html', formM = formM)


@app.route('/delete/<int:id>')
def delete(id):

	mus = Musica.query.get(id)
	remover(mus)
	return redirect(url_for('home'))


@app.route('/home', methods=['GET', 'POST'])
def home():
	ouv = Ouvinte.query.all()
	art = Artista.query.all()
	musicas = Musica.query.all()
	return render_template('principal.html', ouv=ouv, art=art, musicas=musicas)


if __name__ == '__main__':
    app.run()
