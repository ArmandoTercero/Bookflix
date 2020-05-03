from db import get_db

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
	def crear(cls, name, ruta):
		sql = "INSERT INTO libro (nombre, ruta) VALUES ('%s', '%s')"
		cursor = cls.database().cursor()
		cursor.execute(sql % (name, ruta))
		cls.database().commit()
		return True

