from flask_app import db

class Usuario(db.Model):
    __tablename__ = "usuario"

    email = db.Column(db.String(45), primary_key = True)
    senha = db.Column(db.String(45), nullable = False)
    data_nasc = db.Column(db.Date) 

    def __init__(self, email, senha, data_nasc):
        self.email = email
        self.senha = senha
        self.data_nasc = data_nasc

    def __repr__(self):
        
        return "<Usuario %r>" %self.email

class  Artista(db.Model):
    __tablename__ = "artista"

    email = db.Column(db.String(45),db.ForeignKey('usuario.email'), primary_key = True)
    nome = db.Column(db.String(45), nullable = False)
    biografia = db.Column(db.Text(256))
    ano_form = db.Column(db.Integer)

    fk_art = db.relationship('Usuario',foreign_keys = email)

    def __init__(self, email, nome, biografia, ano_form):
        self.email = email
        self.nome = nome
        self.biografia = biografia
        self.ano_form = ano_form

    def __repr__(self):
        return "<Artista %r>" %self.nome 

class Perfil(db.Model):
    __tablename__ = "perfil"

    ide = db.Column(db.Integer, primary_key = True)
    info = db.Column(db.Text(256))
    
    def __init__(self, ide, info):
        self.ide = ide
        self.info = info

    def __repr__(self):
        return "<perfil %r>" %self.ide

class Ouvinte(db.Model):

    email = db.Column(db.String(45),db.ForeignKey('usuario.email'), primary_key = True)
    p_nome = db.Column(db.String(45),nullable = False)
    s_nome = db.Column(db.String(45),nullable = False)
    perfil = db.Column(db.Integer,db.ForeignKey('perfil.ide'))

    fk_ouv = db.relationship('Perfil',foreign_keys = perfil)

