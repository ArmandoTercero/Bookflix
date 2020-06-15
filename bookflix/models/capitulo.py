from db import get_db

class Capitulo (object):

	@classmethod
	def leyendo(cls, libro_id, perfil_id):
		sql = "SELECT * FROM leyendo WHERE libro_id = %s AND perfil_id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % (libro_id, perfil_id))
		return cursor.fetchone()

	@classmethod
	def update_leyendo (cls, libro_id, capitulo_id, perfil_id):
		leyendo = cls.leyendo (libro_id, perfil_id)
		if (leyendo):
			sql = "UPDATE leyendo SET capitulo_id = %s WHERE id = %s"
			sql %= (capitulo_id, leyendo["id"])
		else:
			sql = "INSERT INTO leyendo (libro_id, capitulo_id, perfil_id) VALUES ('%s', '%s', '%s')"
			sql %= (libro_id, capitulo_id, perfil_id)
		cursor = cls.database().cursor()
		cursor.execute(sql)
		cls.database().commit()
		return True

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def id(cls, cap_id):
		sql = "SELECT * FROM capitulo WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % cap_id)
		cap = cursor.fetchone()
		sql = "SELECT * FROM libro WHERE id = %s"
		cursor.execute(sql % cap["libro_id"])
		cap["libro"] = cursor.fetchone()
		return cap

	@classmethod
	def libro (cls, libro_id):
		sql = "SELECT * FROM capitulo WHERE libro_id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % libro_id)
		return cursor.fetchall()

	@classmethod
	def all(cls):
		sql = "SELECT * FROM capitulo"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def crear(cls, libro_id, pdate, ruta):
		sql = "INSERT INTO capitulo (libro_id, fecha_publicacion, ruta) VALUES ('%s', '%s', '%s')"
		cursor = cls.database().cursor()
		cursor.execute(sql % (libro_id, pdate, ruta))
		cls.database().commit()
		return True

