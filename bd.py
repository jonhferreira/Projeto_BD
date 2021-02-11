from flask_app import db, lm
from flask_login import UserMixin


@lm.user_loader
def get_user(use_email):
    return Usuario.query.filter_by(email=use_email).first()
"""
@lm.user_loader
def get_user(use_email):
    return Ouvinte.query.filter_by(email=use_email).first()

@lm.user_loader
def get_user(use_email):
    return Artista.query.filter_by(email=use_email).first()
"""

class Usuario(db.Model, UserMixin):
    __tablename__ = "usuario"

    email = db.Column(db.String(45), primary_key = True)
    senha = db.Column(db.String(45), nullable = False)
    data_nasc = db.Column(db.Date) 


    def get_id(self):
        return self.email

    def __init__(self, email, senha, data_nasc):
        self.email = email
        self.senha = senha
        self.data_nasc = data_nasc

    def __repr__(self):
        
        return "<Usuario %r>" %self.email

class Artista(db.Model):
    __tablename__ = "artista"

    email = db.Column(db.String(45),db.ForeignKey('usuario.email'), primary_key = True)
    nome = db.Column(db.String(45), nullable = False)
    biografia = db.Column(db.Text(256))
    ano_form = db.Column(db.Integer)

    fk_usuario = db.relationship('Usuario',foreign_keys = email)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return self.email

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
        return "<Perfil %r>" %self.ide

class Ouvinte(db.Model, UserMixin):
     
    __tablename__ = "ouvinte"

    email = db.Column(db.String(45),db.ForeignKey('usuario.email'), primary_key = True)
    p_nome = db.Column(db.String(45),nullable = False)
    s_nome = db.Column(db.String(45),nullable = False)
    perfil = db.Column(db.Integer,db.ForeignKey('perfil.ide'))

    fk_usuario = db.relationship('Usuario',foreign_keys = email)
    fk_perfil = db.relationship('Perfil',foreign_keys = perfil)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return self.email

    def __init__(self,email,p_nome,s_nome,perfil):
        self.email = email
        self.p_nome = p_nome
        self.s_nome = s_nome
        self.perfil = perfil

    def __repr__(self):
        return "<Ouvinte %r>" %self.p_nome

# obrigacao de possuir uma chave primaria, mudar diagrama
class Telefone(db.Model):
    
    __tablename__ = "telefone"

    telefone = db.Column(db.String(20),primary_key = True)
    usuario = db.Column(db.String(45),db.ForeignKey('usuario.email'))

    fk_usuario = db.relationship("Usuario",foreign_keys = usuario)

class Playlist(db.Model):

    __tablename__ = "playlist"

    nome = db.Column(db.String(45),primary_key = True)
    status = db.Column(db.Enum('ativo','inativo'))

    def __init__(self,nome,status):
        self.nome = nome
        self.status = status

    def __repr__(self):
        return "<Playlist %r>" %self.nome

# obrigacao de possuir uma chave primaria, mudar diagrama
class Cria(db.Model):
     
    __tablename__ = "cria"

    usuario = db.Column(db.String(45),db.ForeignKey('usuario.email'),primary_key = True)
    playlist = db.Column(db.String(45),db.ForeignKey('playlist.nome'))
    data_cria = db.Column(db.Date, nullable = False)

    fk_usuario = db.relationship('Usuario',foreign_keys = usuario)
    fk_playlist = db.relationship('Playlist',foreign_keys = playlist)

    def __init__(self,usuario, playlist, data_cria):
        self.usuario = usuario
        self.playlist = playlist
        self.data_cria = data_cria
    
    def __repr__(self):
        return "<Playlist criada em %r>" %self.data_cria


class Evento(db.Model):

    __tablename__ = "evento"

    ide = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(45), nullable = False)
    usuario = db.Column(db.String(45),db.ForeignKey('usuario.email'), primary_key = True)

    fk_usuario = db.relationship("Usuario",foreign_keys = usuario)

    def __init__(self, ide,nome,usuario):
        self.ide = ide
        self.nome = nome
        self.usuario = usuario

    def __repr__(self):
        return "<Evento %r>" %self.ide


class Segue(db.Model):
    
    __tablename__  = "segue"

    ouvinte = db.Column(db.String(45),db.ForeignKey('ouvinte.email'), primary_key = True)
    artista = db.Column(db.String(45),db.ForeignKey('artista.email'),primary_key = True)

    fk_ouvinte = db.relationship("Ouvinte",foreign_keys = ouvinte)
    fk_artista = db.relationship("Artista",foreign_keys = artista)

    def __init__(self, ouvinte, artista):
        self.ouvinte = ouvinte
        self.artista = artista
    
    def __repr__(self):
        
        return "<%r segue %r>" %(self.ouvinte,self.artista)


class Album(db.Model):
    __tablename__ = "album"

    ide = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(45), nullable=False)
    ano_lancamento = db.Column(db.Integer)
    artista = db.Column(db.String(45),db.ForeignKey('artista.email'))

    fk_artista = db.relationship("Artista",foreign_keys = artista)
    
    def __init__(self, ide, titulo, ano_lancamento, artista):
        self.ide = ide
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
        self.artista = artista

    def __repr__(self):
         return f"Album de {self.artista}"


class Salva_album(db.Model):

    __tablename__ = "salva_album"

    ouvinte = db.Column(db.String(45), db.ForeignKey('ouvinte.email'), primary_key = True)
    album = db.Column(db.String(45), db.ForeignKey('album.ide'),primary_key = True)

    fk_ouvinte = db.relationship("Ouvinte", foreign_keys=ouvinte)
    fk_album = db.relationship('Album', foreign_keys=album)

    def __init__(self, ouvinte, album):
        self.ouvinte = ouvinte
        self.album = album

    def __repr__(self):
        return f"{self.ouvinte} salvou o album {self.album}"


class Musica(db.Model):

    __tablename__ = 'musica'
    ide = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    duracao = db.Column(db.Integer)

    def __init__(self, ide, nome, duracao):
        self.ide = ide
        self.nome = nome
        self.duracao = duracao

    def __repr__(self):
        return f"Música {self.nome}"



class Alb_tem_mus(db.Model):

    __tablename__ = "alb_tem_mus"

    album = db.Column(db.Integer, db.ForeignKey('album.ide'), primary_key = True)
    musica = db.Column(db.Integer, db.ForeignKey('musica.ide'),primary_key = True)

    fk_album = db.relationship("Album", foreign_keys=album)
    fk_musica = db.relationship('Musica', foreign_keys=musica)

    def __init__(self, album, musica):
        self.album = album
        self.musica = musica

class Local(db.Model):

    __tablename__ = "local"

    ide = db.Column(db.Integer,primary_key = True)
    cidade = db.Column(db.String(45), nullable = False)
    pais = db.Column(db.String(45), nullable = False)

    def __init__(self, ide, cidade, pais):
        self.ide = ide
        self.cidade = cidade
        self.pais = pais

    def __repr__(self):
        return "<Local %r>" %self.cidade

class Evento_ocorre(db.Model):
    __tablename__ = "evento_ocorre"

    evento = db.Column(db.Integer, db.ForeignKey('evento.ide'), primary_key = True)
    local = db.Column(db.Integer, db.ForeignKey('local.ide'), primary_key = True)
    artista = db.Column(db.String(45), db.ForeignKey('artista.email'), primary_key = True)
    data = db.Column(db.Date, nullable = False)

    fk_evento = db.relationship("Evento",foreign_keys = evento)
    fk_local = db.relationship("Local",foreign_keys = local)
    fk_artista = db.relationship("Artista",foreign_keys = artista)

    def __init__(self, evento, local, artista, data):
        
        self.evento = evento
        self.local = local
        self.artista = artista
        self.data = data

    def __repr__(self):
        return "<Evento marcado em %r>" %self.local

class Genero(db.Model):
    __tablename__ = "genero"

    nome = db.Column(db.String(45), primary_key = True)
    estilo = db.Column(db.Enum('blues', 'rock', 'mpb','samba','sertanejo','jazz','classica'), nullable = False)

    def __init__(self, nome, estilo):
        
        self.nome = nome
        self.estilo = estilo

    def __repr__(self):
        return "<Genero %r>" %self.nome

class Genero_favorito(db.Model):
    __tablename__ = "genero_favorito"

    genero = db.Column(db.String(45),db.ForeignKey('genero.nome'),primary_key = True)
    perfil = db.Column(db.Integer,db.ForeignKey('perfil.ide'), primary_key = True)

    fk_genero = db.relationship("Genero", foreign_keys = genero)
    fk_perfil = db.relationship("Perfil", foreign_keys = perfil)

    def __init__(self, genero, perfil):

        self.genero = genero
        self.perfil = perfil

    def __repr__(self):
        return "<Genero %r e favorito de %r >" %(self.genero,self.perfil)

class Art_tem_gen(db.Model):
    __tablename__ = "art_tem_gen"

    artista = db.Column(db.String(45),db.ForeignKey('artista.email'), primary_key = True)
    genero = db.Column(db.String(45),db.ForeignKey('genero.nome'),primary_key = True)
    
    fk_artista= db.relationship("Artista", foreign_keys = artista)
    fk_genero = db.relationship("Genero", foreign_keys = genero)
    

    def __init__(self,artista, genero):

        self.artista = artista
        self.genero = genero

    def __repr__(self):
        return "<Artista %r pertence ao genero %r >" %(self.artista,self.genero)


class Mus_tem_gen(db.Model):
    __tablename__ = "mus_tem_gen"

    musica = db.Column(db.Integer,db.ForeignKey('musica.ide'), primary_key = True)
    genero = db.Column(db.String(45),db.ForeignKey('genero.nome'),primary_key = True)
    

    fk_genero = db.relationship("Genero", foreign_keys = genero)
    fk_musica= db.relationship("Musica", foreign_keys = musica)

    def __init__(self,musica, genero):

        self.musica = musica
        self.genero = genero

    def __repr__(self):
        return "<Musica %r pertence ao genero %r >" %(self.musica,self.genero)

class Grava(db.Model):

    __tablename__ = 'grava'

    artista = db.Column(db.String(45), db.ForeignKey('artista.email'), primary_key=True)
    musica= db.Column(db.Integer, db.ForeignKey('musica.ide'), primary_key=True)

    fk_artista = db.relationship("Artista", foreign_keys=artista)
    fk_musica= db.relationship("Musica", foreign_keys=musica)

    def __init__(self, artista, musica):
        
        self.artista = artista
        self.musica = musica

    def __repr__(self):
        return f"<Foi salvo a música {self.musica}>"


class Artista_favorito(db.Model):

    __tablename__ = 'artista_favorito'

    perfil = db.Column(db.Integer, db.ForeignKey('perfil.ide'), primary_key=True)
    artista = db.Column(db.String(45), db.ForeignKey('artista.email'), primary_key=True)

    fk_perfil = db.relationship("Perfil", foreign_keys=perfil)
    fk_artista = db.relationship("Artista", foreign_keys=artista)

    def __init__(self, perfil, artista):
        self.perfil = perfil
        self.artista = artista

    def __repr__(self):
        return f"<favorito {self.artista}>"


class Curte(db.Model):

    __tablename__ = 'curte'

    ouvinte = db.Column(db.String(45), db.ForeignKey('ouvinte.email'), primary_key = True)
    musica = db.Column(db.Integer, db.ForeignKey('musica.ide'), primary_key=True)

    fk_ouvinte = db.relationship("Ouvinte", foreign_keys=ouvinte)
    fk_musica= db.relationship("Musica", foreign_keys=musica)

    def __init__(self, ouvinte, musica):
        self.ouvinte = ouvinte
        self.musica= musica

    def __repr__(self):
        return f"<{self.ouvinte} curtiu {musica}>"


class Salva_playlist(db.Model):

    __tablename__ = 'salva_playlist'

    playlist= db.Column(db.String(45), db.ForeignKey('playlist.nome'), primary_key = True)
    ouvinte = db.Column(db.String(45), db.ForeignKey('ouvinte.email'), primary_key = True)

    fk_ouvinte = db.relationship("Ouvinte", foreign_keys=ouvinte)
    fk_playlist = db.relationship('Playlist', foreign_keys=playlist)


    def __init__(self, playlist, ouvinte):
        self.playlist = playlist
        self.ouvinte = ouvinte

    def __repr__(self):
        return f"<salvo {self.playlist}>"


class Play_tem_mus(db.Model):

    __tablename__ = 'play_tem_mus'

    musica = db.Column(db.Integer, db.ForeignKey('musica.ide'), primary_key=True)
    playlist = db.Column(db.String(45), db.ForeignKey('playlist.nome'), primary_key = True)

    fk_musica = db.relationship("Musica", foreign_keys=musica)
    fk_playlist= db.relationship('Playlist', foreign_keys=playlist)

    def __init__(self, playlist, musica):
        self.playlist = playlist
        self.musica = musica

    def __repr__(self):
        return f"<{musica} está {playlist}>"        


db.create_all()


