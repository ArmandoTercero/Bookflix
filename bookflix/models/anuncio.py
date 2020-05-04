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