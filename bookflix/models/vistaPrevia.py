from db import get_db


class VistaPrevia (object):

    @classmethod
    def database(cls):
        return get_db()

    @classmethod
    def all(cls):
        sql = "SELECT * FROM vista_previa"

        cursor = cls.database().cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def crear(cls, data):
        sql = """INSERT INTO
		vista_previa (nombre, descripcion, video, pdf, imagen, fecha_de_publicacion, activa)
		VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"""

        nombre = data.get('nombre', '')
        descripcion = data.get('descripcion', '')
        video = data.get('video', '')
        pdf = data.get('pdf', '')
        imagen = data.get('imagen', '')
        fecha_de_publicacion = data.get('fecha_de_publicacion', '')
        activa = data.get('activa', '')

        cursor = cls.database().cursor()
        cursor.execute(
            sql % (nombre, descripcion, video, pdf, imagen, fecha_de_publicacion, activa))
        cls.database().commit()
        return True

    @classmethod
    def encontrar_por_id(cls, id):
        sql = "SELECT * FROM vista_previa WHERE id = %s"
        cursor = cls.database().cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()

    @classmethod
    def eliminar(cls, id):  
        sql = """ DELETE FROM vista_previa WHERE id = %s"""
        cursor = cls.database().cursor()
        cursor.execute(sql, (str(id)))
        cls.database().commit()
        return True
#falta implementar el modificar vista previa