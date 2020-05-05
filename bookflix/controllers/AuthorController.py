from flask import request, render_template, session, abort
from flask import send_from_directory, url_for
#from app.models.AuthModel import authmodel
#from app.helpers.Utility import sendResponse
from controllers.AbstractController import AbstractController
from models.autor import Author
from models.libro import Libro
from config import config

class AuthorController(AbstractController):

	def __init__(self):
		pass

	def index(self):
		autores = Author.all()
		return render_template('autores/index.html', autores=autores)

	def autor (self, autor_id):
		autor = Author.id (autor_id)
		return render_template('autores/show.html', autor=autor)

	@AbstractController.validate
	def create (self):#formulario
		return render_template ('autores/agregar.html')

	@AbstractController.validate
	def create_author (self):
		name = request.form.get('nombre', '')
		if Author.existe (name):#chequear que no existe
			return render_template ('autores/error.html')
		else:
			Author.crear (name)
			return self.index()

	@AbstractController.validate
	def edit (self, autor_id):#formulario
		return render_template('autores/editar.html')

	@AbstractController.validate
	def edit_author (self, autor_id):
		name = request.form.get('nombre', '')
		if Author.existe (name):#chequear que no existe
			return render_template ('autores/error.html')
		else:
			Author.edit (autor_id, name)
			return self.index()

authorController = AuthorController()

