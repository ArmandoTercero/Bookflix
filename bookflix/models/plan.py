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