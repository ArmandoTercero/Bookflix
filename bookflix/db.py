import pymysql

from flask import g
import os

def get_db():
	if 'db' not in g:
		g.db = pymysql.connect(
			host = 'localhost',
			user = 'root',
			password = 'L8v4fbyDZAmDYSfYKDTQJEz2Wyvy68VF',
			db = 'bookflix',
			cursorclass = pymysql.cursors.DictCursor
		)

	return g.db


def close_db(e=None):
	db = g.pop('db', None)

	if db is not None:
		db.close()
