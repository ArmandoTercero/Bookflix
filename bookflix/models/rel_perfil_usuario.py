from db import get_db

class RelacionPerUser (object):
    
    @classmethod
    def database(cls):
        return get_db()
        
    @classmethod
    def all(cls):
        sql = "SELECT * FROM rel_perfil_usuario"
        cursor = cls.database().cursor()
        cursor.execute(sql)
        return cursor.fetchall()