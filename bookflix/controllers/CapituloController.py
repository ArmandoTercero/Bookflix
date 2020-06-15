from flask import request, render_template, session
from flask import send_file, send_from_directory, url_for
# from app.models.AuthModel import authmodel
# from app.helpers.Utility import sendResponse
from controllers.AbstractController import AbstractController
from models.libro import Libro
from models.capitulo import Capitulo
from controllers.BookController import bookController
from config import config
from datetime import datetime
import os


class CapituloController(AbstractController):

	def capitulo (self, capitulo_id):
		capitulo = Capitulo.id(capitulo_id)
		libro_id = capitulo["libro_id"]
		#perfil_id = session["perfil_id"]
		perfil_id = 1#placeholder
		Libro.update_leyendo (libro_id, capitulo_id, perfil_id)
		return send_file(capitulo["ruta"][3:])

	@AbstractController.validate
	def new(self, libro_id, errores=[]):
		return render_template('capitulos/agregar.html', errores=errores)

	def gen_path(self, field):
		file = request.files[field]
		name = file.filename
		path = config['UPLOAD_FOLDER'][1:] + name
		dbpath = config['UPLOAD_FOLDER'] + name
		file.save(path)
		return dbpath

	@AbstractController.validate
	def new_capitulo(self, libro_id):
		libro = Libro.id (libro_id)
		pdate = datetime.strptime(request.form["fechaPublicacion"], "%Y-%m-%d")
		errores = []
		if pdate.date() < libro["fecha_publicacion"]:
			errores.append("Fecha de publicacion incorrecta")
		if (len(errores) != 0):
			return self.new (libro_id, errores)
		pdfpath = self.gen_path('archivo')
		Capitulo.crear(libro_id, pdate, pdfpath)
		return bookController.libro(libro_id)

capituloController = CapituloController()
