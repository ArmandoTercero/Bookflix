from db import get_db
from models.libro import Libro

class Author (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def id(cls, autor_id):
		sql = "SELECT * FROM autor WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % autor_id)
		autor = cursor.fetchone()
		sql = "SELECT * FROM libro WHERE autor = %s"
		cursor.execute(sql % autor_id)
		autor["libros"] = cursor.fetchall()
		#autor["libros"] = [Libro.id(i["libro_id"]) for i in libros_id]
		#agregar a autor los libros relacionados
		return autor

	@classmethod
	def existe(cls, name):
		sql = "SELECT * FROM autor WHERE nombre = '%s'"
		cursor = cls.database().cursor()
		cursor.execute(sql % name)
		return (cursor.fetchone() is None)

	@classmethod
	def all(cls):
		sql = "SELECT * FROM autor"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def edit (cls, autor_id, name):
		sql = "UPDATE autor SET nombre = '%s' WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % (name, autor_id))
		cls.database().commit()
		return True

	@classmethod
	def crear(cls, name):
		sql = "INSERT INTO autor (nombre) VALUES ('%s')"
		cursor = cls.database().cursor()
		cursor.execute(sql % name)
		cls.database().commit()
		return True

