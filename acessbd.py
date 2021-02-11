from bd import *
import datetime
from flask_app import db

def add(entidade):
    db.session.add(entidade)
    db.session.commit()

# Usuario

def addUsuario(email,senha,data_nas = None):
    
    #if(not data_nas is None):
        #ano, mes, dia = data_nas
        #data = datetime.date(ano,mes,dia)

    usuario = Usuario(email,senha,data_nas)
    add(usuario)

def updateUsuario(usuario,email,senha,data_nas = None):
    if(not data_nas is None):
        ano, mes, dia = data_nas
        data = datetime.date(ano,mes,dia)
    
    usuario.email = email
    usuario.senha = senha
    usuario.data_nas = data_nas
    db.session.commit()

# pesquisa um usuario especifico
def searchUsuario(user_email):
    usuario = db.session.query(Usuario).filter_by(email = user_email)
    return usuario[0]

# Artista

def addArtista(email, nome, biografia = None, ano_form = None):
    
    artista = Artista(email, nome, biografia, ano_form)
    add(artista)

def updateArtista(artista,email, nome, biografia = None, ano_form = None):
    artista.email = email
    artista.nome = nome
    artista.biografia = biografia
    artista.ano_form = ano_form

# Ouvinte

def addOuvinte(email, p_nome, s_nome, perfil):
    
    ouvinte = Ouvinte(email, p_nome, s_nome, perfil=None)
    add(ouvinte)

def updateOuvinte(ouvinte,email, p_nome, s_nome, perfil):
    ouvinte.email = email
    ouvinte.p_nome = p_nome
    ouvinte.s_nome = s_nome
    ouvinte.perfil = perfil


# Perfil

def addPerfil(ide, info):
    perfil = Perfil(ide, info)
    add(perfil)

# Genero_favorito

def addGenero_favorito(genero, perfil):
    genero_favorito = Genero_favorito(genero, perfil)
    add(genero_favorito)

def generosFavoritos(perfil):
    favoritos = db.session.query(Genero_favorito).filter_by(perfil = perfil)
    return favoritos

# Artista_favorito

def addArtista_favorito(perfil, artista):
    artista_favorito = Artista_favorito(perfil, artista)
    add(artista_favorito)

def artistasFavoritos(perfil):
    favoritos = db.session.query(Artista_favorito).filter_by(perfil = perfil)
    return favoritos

# Musica

def addMusica(ide, nome, duracao = None):

    musica = Musica(ide, nome, duracao)
    add(musica)

def updateMusica(musica, ide, nome, duracao = None):
    musica.ide = ide
    musica.nome = nome
    musica.duracao = nome

def searchMusica(nome):
    musicas = db.session.query(Musica).filter(Musica.nome.like('%'+nome+'%'))
    return musicas

# Grava 

def addGrava(artista, musica):
    grava = Grava(grava,musica)
    add(grava)

def musicasGravadas(artista):
    gravadas = db.session.query(Grava).filter_by(artista = artista)
    return gravadas

# Mus_tem_gen

def addMus_tem_gen(musica, genero):
    mus_tem_gen = Mus_tem_gen(musica,genero)
    add(mus_tem_gen)

def musicasPorGenero(genero):
    musicas = db.session.query(Mus_tem_gen).filter_by(genero = genero)
    return musicas

# Album( ver a questão da anulidade de ano_lan)

def addAlbum(ide, titulo, ano_lan, artista):
    album = Album(ide,titulo, ano_lan, artista)
    add(album)

def updateAlbum(album,ide, titulo, ano_lan, artista):
    album.ide = ide
    album.titulo = titulo
    album.ano_lan = ano_lan
    album.artista = artista
    
    db.session.commit()

def albunsCriados(artista):
    criados = db.session.query(Album).filter_by(artista = artista)
    
    return criados

# Salva_album

def addSalva_Album(ouvinte, album):
    salva_album = Salva_album(ouvinte, album)
    add(salva_album)

def albunsSalvos(ouvinte):
    salvos = db.session.query(Salva_album).filter_by(ouvinte = ouvinte)

# Alb_tem_mus

def addAlb_tem_mus(album, musica):
    alb_tem_mus = Alb_tem_mus(album, musica)
    add(alb_tem_mus)

def musicasPorAlbum(album):
    musicas = db.session.query(Alb_tem_mus).filter_by(album = album)
    return musicas

# Segue

def addSegue(ouvinte, artista):
    segue = Segue(ouvinte, artista)
    add(seg)

def seguidos(ouvinte):
    seguidos = db.session.query(Segue).filter_by(ouvinte = ouvinte)
    return seguidos

# Curte - ver uma questão de pesquisa musicas curtidas

def addCurte(ouvinte, musica):

    curte = Curte(ouvinte, musica)
    add(curte)

def curtidas(ouvinte):
    curtidas = db.session.query(Curte).filter_by(ouvinte = ouvinte)
    return curtidas

# PlayList

def addPlayList(nome, status = None):

    play_list = Playlist(nome, status)
    add(play_list)

def updatePlayList(play_list, nome, status = None):
    play_list.nome = nome
    play_list.status = status

    db.session.commit()

def searchPlayList(nome):
    play_list = db.session.query(Playlist).filter(Playlist.nome.like('%'+nome+'%'))
    return play_list

# Genero -- provavelmente adicionados pelo programador somente

def addGenero(nome, estilo):
    genero = Genero(nome, estilo)
    add(genero)

def addArt_tem_gen(artista, genero):
    art_tem_gen = Art_tem_gen(artista,genero) 
    add(art_tem_gen)

# criar a cada addPlayList

def addCria(usuario, playlist, data_cria):

    ano, mes, dia = data_cria
    data = datetime.date(ano,mes,dia)

    cria = Cria(usuario, playlist, data)
    add(cria)

def criadas(artista):
    criadas = db.session.query(Cria).filter_by(artista = artista)
    return criadas

# Grava -- criar a cada addMusica

def addGrava(artista, musica):
    grava = Grava(artista, musica)
    add(musica)

def gravadas(artista):
    gravadas = db.session.query(Artista).filter_by(artista = artista)
    return gravadas

# retorna uma lista de objetos, cada um corresponde a uma linha da tabela
def listTable(tabela):
    lista = db.session.query(tabela).all()
    
    return lista.copy()

# função generica que remove qualquer registro
def remover(linha):
    db.session.delete(linha)
    db.session.commit()