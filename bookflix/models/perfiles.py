from db import get_db


class Perfiles (object):

    @classmethod
    def database(cls):
        return get_db()

    @classmethod
    def encontrar_por_id(cls, perfiles_id):
        sql = "SELECT * FROM perfiles WHERE id = %s"
        cursor = cls.database().cursor()
        cursor.execute(sql, (perfiles_id))
        return cursor.fetchone()

    @classmethod
    def all(cls):
        sql = "SELECT * FROM perfiles"
        cursor = cls.database().cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def crear(cls, data):
        sql = """INSERT INTO perfiles
		(nombre, foto, id_usuario)
		VALUES (%s)"""
        parametros = str(list(data.values())).strip('[]')
        cursor = cls.database().cursor()
        cursor.execute(sql % parametros)
        cls.database().commit()
        return True

    @classmethod
    def eliminar(cls, id):
        sql = """ DELETE FROM perfiles WHERE id = %s"""
        cursor = cls.database().cursor()
        cursor.execute(sql, (str(id)))
        cls.database().commit()
        return True

    @classmethod
    def edit(cls, data):
        sql = """
			UPDATE perfiles
			SET nombre = %s, foto = %s
			WHERE perfiles.id = %s
		"""
        cursor = cls.database().cursor()
        print(list(data.values()))
        cursor.execute(sql, list(data.values()))
        cls.database().commit()
        return True
