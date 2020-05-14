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
	def existe_isbn (cls, isbn):
		sql = "SELECT * FROM libro WHERE isbn = '%s'"
		cursor = cls.database().cursor()
		cursor.execute(sql % isbn)
		return not (cursor.fetchone() is None)

	@classmethod
	def all(cls):
		sql = "SELECT * FROM libro"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def crear(cls, form, pdfpath, imgpath):
		sql = """INSERT INTO
		libro (nombre, isbn, fecha_publicacion, fecha_vencimiento, ruta_img, sinopsis, editorial, genero, autor, ruta)
		VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""
		name = form.get('nombre', '')
		isbn = form.get('isbn', '')
		pdate = datetime.strptime(form["fechaPublicacion"], "%Y-%m-%d")
		vdate = datetime.strptime(form["fechaVencimiento"], "%Y-%m-%d")
		sinopsis = form.get('sinopsis', '')
		editorial = form.get('editorial', '')
		genero = form.get('genero', '')
		autor = form.get('autor', '')
		cursor = cls.database().cursor()
		cursor.execute(sql % (name, isbn, pdate, vdate, imgpath, sinopsis, editorial, genero, autor, pdfpath))
		cls.database().commit()
		return True

	@classmethod
	def edit(cls, form, pdfpath, imgpath, libro_id):
		sql = """
		UPDATE libro SET
		nombre = '%s',
		isbn = '%s',
		fecha_publicacion = '%s',
		fecha_vencimiento = '%s',
		ruta_img = '%s',
		sinopsis = '%s',
		editorial = '%s',
		genero = '%s',
		autor = '%s',
		ruta = '%s'
		WHERE id = '%s'
		"""
		name = form.get('nombre', '')
		isbn = form.get('isbn', '')
		pdate = datetime.strptime(form["fechaPublicacion"], "%Y-%m-%d")
		vdate = datetime.strptime(form["fechaVencimiento"], "%Y-%m-%d")
		sinopsis = form.get('sinopsis', '')
		editorial = form.get('editorial', '')
		genero = form.get('genero', '')
		autor = form.get('autor', '')
		cursor = cls.database().cursor()
		cursor.execute(sql % (name, isbn, pdate, vdate, imgpath, sinopsis, editorial, genero, autor, pdfpath, libro_id))
		cls.database().commit()
		return True

