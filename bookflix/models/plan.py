from db import get_db

class Plan (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def all(cls):
		sql = "SELECT * FROM plan"

		cursor = cls.database().cursor()
		cursor.execute(sql)

		return cursor.fetchall()

	@classmethod
	def encontrar_por_id(cls, plan_id):
		sql = "SELECT * FROM plan WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (plan_id))		
		return cursor.fetchone()
