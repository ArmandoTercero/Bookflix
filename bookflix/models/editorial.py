from db import get_db
from datetime import datetime

class Editorial (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def id(cls, editorial_id):
		sql = "SELECT * FROM editorial WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % editorial_id)
		return cursor.fetchone()

	@classmethod
	def all(cls):
		sql = "SELECT * FROM editorial"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

