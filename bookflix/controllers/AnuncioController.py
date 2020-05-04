from flask import request, render_template, session, abort
from flask import send_from_directory, url_for
from models.anuncio import Anuncio

class AnuncioController():

	def __init__(self):
		pass

	def index(self):
		anuncios = Anuncio.all()
		return render_template('anuncios/index.html', anuncios=anuncios)

	# def crear(self):
	# 	return render_template ('anuncios/agregar.html')

	# def crear_anuncio(self):
	# 	# OBTENER LOS DATOS DEL FORMULARIO
	# 	# Anuncio.crear(request.form)
	# 	return self.index()

anuncioController = AnuncioController()