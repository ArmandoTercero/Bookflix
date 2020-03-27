from bookflix.db import get_db

class Usuario(object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def encontrar_por_id(cls, usuario_id):
		sql = "SELECT * FROM usuario WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (usuario_id))        
		return cursor.fetchone()