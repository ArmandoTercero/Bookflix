from db import get_db

class Anuncio (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def all(cls):
		sql = "SELECT * FROM anuncio"

		cursor = cls.database().cursor()
		cursor.execute(sql)

		return cursor.fetchall()

	@classmethod
	def crear(cls, data):
		sql = """INSERT INTO anuncio
		(titulo, contenido)
		VALUES (%s)"""
		parametros = str(list(data.values())).strip('[]')
		cursor = cls.database().cursor()
		cursor.execute(sql % parametros)
		cls.database().commit()
		return True

	@classmethod
	def encontrar_por_id(cls, id):
		sql = "SELECT * FROM anuncio WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (id))
		return cursor.fetchone()

	@classmethod
	def edit(cls, data):
		sql = """
			UPDATE anuncio
			SET titulo = %s, contenido = %s
			WHERE anuncio.id = %s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, list(data.values()))
		cls.database().commit()
		return True
