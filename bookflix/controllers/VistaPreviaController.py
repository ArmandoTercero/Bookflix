from datetime import datetime

from flask import request, render_template, session, abort
from flask import send_from_directory, url_for, redirect
from models.vistaPrevia import VistaPrevia
from config import config


class VistaPreviaController():

    def __init__(self):
        pass

    def index(self):
        vistas_previas = VistaPrevia.all()
        return render_template('vistas_previas/index.html', vistas_previas=vistas_previas)

    def new(self):
        errores = []
        fecha_de_hoy = datetime.date(datetime.now())
        if request.method == 'GET':
            
            return render_template('vistas_previas/new.html', fecha_de_hoy=fecha_de_hoy)
        elif request.method == 'POST':
            formulario = request.form
            print(formulario)   #si el pdf lo hago de tipo file en el html no me puedo fijar si esta vacio
            if formulario['video'] == '' and formulario['pdf'] == '':
                errores.append("Es obligatorio agregar un pdf o un video")
                return render_template('vistas_previas/new.html', errores=errores, fecha_de_hoy=fecha_de_hoy)
            else:
                VistaPrevia.crear(formulario)
                return self.index()

    def delete(self, id):
        vistas_previas = VistaPrevia.all()
        vista = VistaPrevia.eliminar(id)
        return render_template('vistas_previas/index.html', vistas_previas=vistas_previas)
    
    def modificar(self, id): #example arreglar construir esto bien empezando por el html!!!
        vista_previa = VistaPrevia.encontrar_por_id(id)
        print(vista_previa)
        return render_template('vistas_previas/edit.html', vista_previa=vista_previa)


vistaPreviaController = VistaPreviaController()
