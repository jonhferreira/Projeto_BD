from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TimeField, BooleanField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired 


# formulario de login
class Formulare_Login(FlaskForm):
    usuario = StringField("Usuário",validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])



class Formulare_cadastro_User(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	data_nasc = DateField('Data de nascimento', format='%d/%m/%Y',validators=[DataRequired()])
	senha = PasswordField('Senha', validators=[DataRequired()])
	confirm = PasswordField('Repita a senha', validators=[DataRequired()])



class Formulare_ouvinte(FlaskForm):
	p_nome = StringField('Primeiro nome', validators=[DataRequired()])
	s_nome = StringField('Sobrenome')
	

class Formulare_artista(FlaskForm):
	nome = StringField("None", validators=[DataRequired()])
	biografia = StringField('Bio')
	ano_form = IntegerField('Ano formação')


# formulario para adicao de musica -> precisa implementar

class Formulare_addMusic(FlaskForm):
	from acessbd import listTable
	from bd import Genero
	nome = StringField("Nome",validators=[DataRequired()])
	duracao =IntegerField("Duração")
	
	generos = []

	for gen in listTable(Genero):
		generos.append((gen,gen.nome))

	genero = SelectField("Genero", choices = generos)

# formulario para pesquisar musica -> precisa implementar
class Formulare_searcMusic(FlaskForm):
    termo = StringField("Termo")
