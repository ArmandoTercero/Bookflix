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
        (nombre, apellido, email, contraseña, tarjetaNumero, tarjetaPin, tarjetatarjetaFechaDeExpiracion, fecha_de_nacimiento, plan)
        VALUES (%s)"""
        parametros = str(list(data.values())).strip('[]')
        print(sql % parametros)
        # cursor = cls.database().cursor()
        # cursor.execute(sql, (usuario_id))
        # return cursor.fetchone()