from db import get_db
from datetime import datetime
from models.capitulo import Capitulo

class Libro (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def search (cls, sql):
		cursor = cls.database().cursor()
		cursor.execute(sql)
		libros = cursor.fetchall()
		return libros

	@classmethod
	def search_autor(cls, name):
		sql = "SELECT * FROM autor AS a, libro AS l WHERE a.nombre LIKE '%%%s%%' AND l.autor = a.id"
		return cls.search (sql % name)

	@classmethod
	def search_name(cls, name):
		sql = "SELECT * FROM libro WHERE nombre LIKE '%%%s%%'"
		return cls.search (sql % name)

	@classmethod
	def search_editorial(cls, name):
		sql = "SELECT * FROM editorial AS e, libro AS l WHERE e.nombre LIKE '%%%s%%' AND l.editorial = e.id"
		return cls.search (sql % name)

	@classmethod
	def search_genero(cls, name):
		sql = "SELECT * FROM genero AS g, libro AS l WHERE g.nombre LIKE '%%%s%%' AND l.genero = g.id"
		return cls.search (sql % name)

	@classmethod
	def id(cls, libro_id):
		sql = "SELECT * FROM libro WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % libro_id)
		libro = cursor.fetchone()
		libro["capitulos"] = Capitulo.libro(libro["id"])
		return libro

	@classmethod
	def isbn (cls, isbn):
		sql = "SELECT * FROM libro WHERE isbn = '%s'"
		cursor = cls.database().cursor()
		cursor.execute(sql % isbn)
		return cursor.fetchone()

	@classmethod
	def existe_isbn (cls, isbn):
		return not (cls.isbn(isbn) is None)

	@classmethod
	def all(cls):
		sql = "SELECT * FROM libro"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def commit (cls, form, sql, imgpath, extra = tuple()):
		name = form.get('nombre', '')
		isbn = form.get('isbn', '')
		pdate = datetime.strptime(form["fechaPublicacion"], "%Y-%m-%d")
		vdate = datetime.strptime(form["fechaVencimiento"], "%Y-%m-%d")
		sinopsis = form.get('sinopsis', '')
		editorial = form.get('editorial', '')
		genero = form.get('genero', '')
		autor = form.get('autor', '')
		cursor = cls.database().cursor()
		cursor.execute(sql % ((name, isbn, pdate, vdate, imgpath, sinopsis, editorial, genero, autor) + extra))
		cls.database().commit()

	@classmethod
	def crear(cls, form, imgpath):
		sql = """INSERT INTO
		libro (nombre, isbn, fecha_publicacion, fecha_vencimiento, ruta_img, sinopsis, editorial, genero, autor)
		VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""
		cls.commit (form, sql, imgpath)
		return True

	@classmethod
	def edit(cls, form, imgpath, libro_id):
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
		autor = '%s'
		WHERE id = '%s'
		"""
		cls.commit (form, sql, imgpath, (libro_id,))
		return True

	@classmethod
	def habilitar(cls, libro_id):
		sql = "UPDATE libro SET activo = 1 WHERE libro.id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (libro_id))
		cls.database().commit()
		return True

	@classmethod
	def deshabilitar(cls, libro_id):
		sql = "UPDATE libro SET activo = 0 WHERE libro.id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (libro_id))
		cls.database().commit()
		return True
