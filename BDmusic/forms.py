from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TimeField
from wtforms.validators import DataRequired

class Formulare_Login(FlaskForm):
    usuario = StringField("Usuário",validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])

class Formulare_addMusic(FlaskForm):
    nome = StringField("Nome",validators=[DataRequired()])
    cantor = StringField("Cantor",validators=[DataRequired()])
    duracao =TimeField("Duração",validators=[DataRequired()])
    descricao = StringField("Descrição",validators=[DataRequired()])
