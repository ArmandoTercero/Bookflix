from flask import request, render_template, session
from flask import send_from_directory, url_for
#from app.models.AuthModel import authmodel
#from app.helpers.Utility import sendResponse
from controllers.AbstractController import AbstractController
from models.libro import Libro
from config import config
import os

class BookController():

	def __init__(self):
		pass

	def index(self):
		libros = Libro.all()
		return render_template('libros/index.html', libros=libros)

	def libro(self, libro_id):
		libro = Libro.id (libro_id)
		path = libro["ruta"]
		dir, name = os.path.split(path)
		return send_from_directory(dir, name)

	def new (self):
		return render_template ('libros/agregar.html')

	def new_book(self):
		
		def gen_path (field):
			file = request.files[field]
			name = file.filename
			path =  config['UPLOAD_FOLDER'] + name
			file.save (path)
			return path
		
		pdfpath = gen_path ('libro')
		imgpath = gen_path ('portada')
		Libro.crear(request.form, pdfpath, imgpath)
		return self.index()

bookController = BookController()

