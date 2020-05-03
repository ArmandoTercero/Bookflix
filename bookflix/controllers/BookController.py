from flask import request, render_template, session
from flask import send_from_directory, url_for
#from app.models.AuthModel import authmodel
#from app.helpers.Utility import sendResponse
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
		return send_from_directory(config['UPLOAD_FOLDER'], libro["nombre"])

	def upload (self):
		return render_template ('libros/agregar.html')

	def upload_file(self):
		file = request.files['libro']
		filename = file.filename
		path = config['UPLOAD_FOLDER'] + filename
		file.save(path)
		Libro.crear(filename, path)
		return self.index()

bookController = BookController()

