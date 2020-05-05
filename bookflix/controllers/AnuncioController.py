from flask import request, render_template, session, abort
from flask import send_from_directory, url_for
from models.anuncio import Anuncio

class AnuncioController():

	def __init__(self):
		pass

	def index(self):
		anuncios = Anuncio.all()
		return render_template('anuncios/index.html', anuncios=anuncios)

	def new(self):
		if request.method == 'GET':
			return render_template ('anuncios/new.html')
		elif request.method == 'POST':
			Anuncio.crear(request.form)
			return self.index()

	def edit(self):
		if request.method == 'GET':
			anuncio = Anuncio.encontrar_por_id(request.args.get("anuncio_id"))
			return render_template ('anuncios/edit.html', anuncio=anuncio)
		elif request.method == 'POST':
			Anuncio.edit(request.form)
			return self.index()

anuncioController = AnuncioController()