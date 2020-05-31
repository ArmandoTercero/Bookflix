from db import get_db

class Usuario (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def encontrar_por_id(cls, usuario_id):
		sql = "SELECT * FROM usuario WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (usuario_id))		
		return cursor.fetchone()

	@classmethod
	def crear(cls, data):
		sql = """INSERT INTO usuario
		(nombre, apellido, email, contraseña, fecha_de_nacimiento, tarjetaNumero, tarjetaPin, tarjetaFechaDeExpiracion, plan_id)
		VALUES (%s)"""
		parametros = str(list(data.values())).strip('[]')
		cursor = cls.database().cursor()
		cursor.execute(sql % parametros)
		cls.database().commit()
		return True

	# Esta función devuelve TRUE o FALSE:
	# - True: Si es que existe un usuario con el email pasado como parametro.
	# - False: Caso contrario.
	@classmethod
	def existe_usuario_con_email(cls, email):
		sql = """
		SELECT *
		FROM usuario u
		WHERE u.email = %s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (email))

		return cursor.rowcount > 0

	# Esta función devuelve el resultado de una consulta a la BBDD que busca a ...
	# ... un usuario por el campo de email.
	@classmethod
	def encontrar_por_email(cls, email):
		sql = "SELECT * FROM usuario WHERE email = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (email))
		return cursor.fetchone()

	# Esta función devuelve la cantidad de perfiles creados que tiene un usuario
	@classmethod
	def cantidad_de_perfiles_creados_por_el_usuario_con_id(cls, id):
		sql = "SELECT COUNT(*) FROM perfiles AS p WHERE p.id_usuario=%s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (id))
		return cursor.fetchone()['COUNT(*)']

	@classmethod
	def modificar_plan_id(cls, id, plan_id):
		sql = """
			UPDATE usuario
			SET plan_id = %s
			WHERE usuario.id = %s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (plan_id, id))
		cls.database().commit()
		return True