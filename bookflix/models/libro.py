from db import get_db
from datetime import datetime

class Libro (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def id(cls, libro_id):
		sql = "SELECT * FROM libro WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % libro_id)
		return cursor.fetchone()

	@classmethod
	def all(cls):
		sql = "SELECT * FROM libro"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def crear(cls, form, pdfpath, imgpath):
		sql = """INSERT INTO
		libro (nombre, isbn, fecha_publicacion, fecha_vencimiento, ruta_img, sinopsis, editorial, ruta)
		VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""
		name = form.get('nombre', '')
		isbn = form.get('isbn', '')
		pdate = datetime.strptime(form["fechaPublicacion"], "%Y-%m-%d")
		vdate = datetime.strptime(form["fechaVencimiento"], "%Y-%m-%d")
		sinopsis = form.get('sinopsis', '')
		editorial = form.get('editorial', '')
		cursor = cls.database().cursor()
		cursor.execute(sql % (name, isbn, pdate, vdate, imgpath, sinopsis, editorial, pdfpath))
		cls.database().commit()
		return True

