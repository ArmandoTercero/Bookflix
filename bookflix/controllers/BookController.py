from flask import request, render_template, session, abort, redirect
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

	def leido (self, libro_id):
		if "perfil_id" in session:
			perfil_id = session["perfil_id"]
			Libro.update_leido (libro_id, perfil_id)
		return redirect (url_for("libro", libro_id=libro_id))

	def agregar_fav (self, libro_id):
		Libro.agregar_favorito (libro_id, session["perfil_id"])
		return redirect (url_for("libro", libro_id=libro_id))

	def eliminar_fav (self, libro_id):
		Libro.eliminar_favorito (libro_id, session["perfil_id"])
		return redirect (url_for("libro", libro_id=libro_id))

	def search (self):
		return render_template('libros/search.html')

	def catalogo (self, libros):
		if not session["admin"]:
			libros = [libro for libro in libros if libro["activo"] == 1]
		autores = Author.all()
		generos = Genero.all()
		editoriales = Editorial.all()
		return render_template('libros/catalogo.html', libros=libros, autores=autores, generos=generos, editoriales=editoriales)

	def search_book (self):
		criterios = {
			"autor": Libro.search_autor,
			"nombre": Libro.search_name,
			"editorial": Libro.search_editorial,
			"genero": Libro.search_genero
		}
		criterio = request.form.get('criterio', '')
		if criterio in criterios:
			texto = request.form.get('texto', '')
			libros = criterios[criterio](texto)
			return self.catalogo (libros)

	def leyendo (self):
		if not "perfil_id" in session:
			abort(403)
		perfil_id = session["perfil_id"]
		libros = Libro.all_leyendo (perfil_id)
		return self.catalogo (libros)

	def favorito (self):
		if not "perfil_id" in session:
			abort(403)
		perfil_id = session["perfil_id"]
		libros = Libro.all_favorito (perfil_id)
		return self.catalogo (libros)

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
		capitulos = Capitulo.libro(libro_id)
		if "perfil_id" in session and not session["admin"]:
			perfil_id = session["perfil_id"]
			leido = Libro.leido (libro_id, perfil_id)
			favorito = Libro.favorito (libro_id, perfil_id)
		else:
			leido = None
		return render_template(
			'libros/show.html',
			libro=libro,
			autor=autor,
			genero=genero,
			editorial=editorial,
			capitulos=capitulos,
			leido=leido,
			favorito=favorito
		)

	@AbstractController.validate
	def new(self, errores=[], old={}):
		editoriales = Editorial.all()
		generos = Genero.all()
		autores = Author.all()
		return render_template('libros/agregar.html', editoriales=editoriales, generos=generos, autores=autores, errores=errores, old=old)

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
			return self.new (errores, request.form)
		imgpath = self.gen_path('portada')
		Libro.crear(request.form, imgpath)
		return redirect (url_for("libro_index"))

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
		return redirect (url_for("libro_index"))

	def ver_catalogo(self):
		libros = Libro.all()
		return self.catalogo(libros)

	def habilitar(self, libro_id):
		Libro.habilitar(libro_id)
		return redirect (url_for("libro_index"))

	def deshabilitar(self, libro_id):
		Libro.deshabilitar(libro_id)
		return redirect (url_for("libro_index"))

bookController = BookController()
