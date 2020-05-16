from flask import request, render_template, session
from flask import send_from_directory, url_for
# from app.models.AuthModel import authmodel
# from app.helpers.Utility import sendResponse
from controllers.AbstractController import AbstractController
from models.libro import Libro
from models.editorial import Editorial
from models.genero import Genero
from models.autor import Author
from models.capitulo import Capitulo
from config import config
from datetime import datetime
import os


class BookController(AbstractController):

	def __init__(self):
		pass

	def index(self):
		libros = Libro.all()
		data = []
		for libro in libros:
			autor = Author.id(libro["autor"])
			genero = Genero.encontrar_por_id(libro["genero"])
			data.append({"libro": libro, "autor": autor, "genero": genero})
		return render_template('libros/index.html', libros=data)

	def libro(self, libro_id):
		libro = Libro.id(libro_id)
		autor = Author.id(libro["autor"])
		genero = Genero.encontrar_por_id(libro["genero"])
		editorial = Editorial.id(libro["editorial"])
		return render_template('libros/show.html', libro=libro, autor=autor, genero=genero, editorial=editorial)

	@AbstractController.validate
	def new(self, errores=[]):
		editoriales = Editorial.all()
		generos = Genero.all()
		autores = Author.all()
		return render_template('libros/agregar.html', editoriales=editoriales, generos=generos, autores=autores, errores=errores)

	def gen_path(self, field):
		file = request.files[field]
		name = file.filename
		path = config['UPLOAD_FOLDER'][1:] + name
		dbpath = config['UPLOAD_FOLDER'] + name
		file.save(path)
		return dbpath

	def check_path(self, libro, field, default):
		if (request.files[field].filename != ''):
			return self.gen_path(field)
		else:
			return libro[default]

	@AbstractController.validate
	def new_book(self):
		isbn = request.form.get('isbn', '')
		pdate = datetime.strptime(request.form["fechaPublicacion"], "%Y-%m-%d")
		vdate = datetime.strptime(request.form["fechaVencimiento"], "%Y-%m-%d")
		errores = []
		if Libro.existe_isbn(isbn):
			errores.append("ISBN Repetido")
		if vdate <= pdate:
			errores.append("Fecha de vencimiento incorrecta")
		if (len(errores) != 0):
			return self.new (errores)
		imgpath = self.gen_path('portada')
		Libro.crear(request.form, imgpath)
		return self.index()

	@AbstractController.validate
	def edit(self, libro_id, errores=[]):
		libro = Libro.id(libro_id)
		editoriales = Editorial.all()
		generos = Genero.all()
		autores = Author.all()
		return render_template('libros/editar.html', libro=libro, editoriales=editoriales, generos=generos, autores=autores, errores=errores)

	@AbstractController.validate
	def edit_book(self, libro_id):
		libro = Libro.id(libro_id)
		isbn = request.form.get('isbn', '')
		pdate = datetime.strptime(request.form["fechaPublicacion"], "%Y-%m-%d")
		vdate = datetime.strptime(request.form["fechaVencimiento"], "%Y-%m-%d")
		errores = []
		if isbn != libro["isbn"] and Libro.existe_isbn(isbn):
			errores.append("ISBN Repetido")
		if vdate <= pdate:
			errores.append("Fecha de vencimiento incorrecta")
		if (len(errores) != 0):
			return self.edit (libro_id, errores)
		imgpath = self.check_path(libro, 'portada', 'ruta_img')
		Libro.edit(request.form, imgpath, libro_id)
		return self.index()

	def ver_catalogo(self, libro_id):
		libro = Libro.id(libro_id)
		autor = Author.id(libro["autor"])
		genero = Genero.encontrar_por_id(libro["genero"])
		editorial = Editorial.id(libro["editorial"])
		libros = Libro.all()
		print(libros)
		return render_template('libros/catalogo.html', libros=libros, autor=autor, genero=genero, editorial=editorial)


bookController = BookController()
