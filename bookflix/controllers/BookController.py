from flask import request, render_template, session
from flask import send_from_directory, url_for
#from app.models.AuthModel import authmodel
#from app.helpers.Utility import sendResponse
from controllers.AbstractController import AbstractController
from models.libro import Libro
from models.editorial import Editorial
from models.genero import Genero
from models.autor import Author
from config import config
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
			data.append({"libro":libro, "autor":autor, "genero":genero})
		return render_template('libros/index.html', libros=data)

	def libro(self, libro_id):
		libro = Libro.id (libro_id)
		autor = Author.id (libro["autor"])
		genero = Genero.encontrar_por_id (libro["genero"])
		editorial = Editorial.id (libro["editorial"])
		return render_template('libros/show.html', libro=libro, autor=autor, genero=genero, editorial=editorial)
		#path = libro["ruta"]
		#dir, name = os.path.split(path)
		#return send_from_directory(dir, name)

	@AbstractController.validate
	def new (self, errores = []):
		editoriales = Editorial.all()
		generos = Genero.all()
		autores = Author.all()
		return render_template ('libros/agregar.html', editoriales=editoriales, generos=generos, autores=autores, errores=errores)

	def gen_path (self, field):
		file = request.files[field]
		name = file.filename
		path =  config['UPLOAD_FOLDER'][1:] + name
		file.save (path)
		return path

	def check_path (self, libro, field, default):
		if (request.files[field].filename != ''):
			return self.gen_path (field)
		else:
			return libro[default]

	@AbstractController.validate
	def new_book(self):
		isbn = request.form.get('isbn', '')
		if Libro.existe_isbn(isbn):
			return self.new(["ISBN Repetido"])
		pdfpath = self.gen_path ('libro')
		imgpath = self.gen_path ('portada')
		Libro.crear(request.form, pdfpath, imgpath)
		return self.index()

	@AbstractController.validate
	def edit (self, libro_id, errores = []):
		libro = Libro.id (libro_id)
		editoriales = Editorial.all()
		generos = Genero.all()
		autores = Author.all()
		return render_template ('libros/editar.html', libro=libro, editoriales=editoriales, generos=generos, autores=autores, errores=errores)

	@AbstractController.validate
	def edit_book (self, libro_id):
		libro = Libro.id (libro_id)
		isbn = request.form.get('isbn', '')
		if isbn != libro["isbn"] and Libro.existe_isbn(isbn):
			return self.edit(libro_id, ["ISBN Repetido"])
		pdfpath = self.check_path (libro, 'libro', 'ruta')
		imgpath = self.check_path (libro, 'portada', 'ruta_img')
		Libro.edit(request.form, pdfpath, imgpath, libro_id)
		return self.index()
		
		

bookController = BookController()

