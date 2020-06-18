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
            # si el pdf lo hago de tipo file en el html no me puedo fijar si esta vacio
            print(formulario)
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

    def modificar(self, id):
        vista_previa = VistaPrevia.encontrar_por_id(id)
        if request.method == 'GET':
            return render_template('vistas_previas/edit.html', vista_previa=vista_previa)
        else:
            if request.method == 'POST':
                
                nombre = request.form['nombre']
                descripcion = request.form['descripcion']
                video = request.form['video']
                pdf = request.form['pdf']
                #imagen = request.form['imagen'] 
                fecha_de_publicacion = request.form['fecha_de_publicacion']
                activa = request.form['activa']
                

                VistaPrevia.edit(nombre, descripcion, video, pdf, fecha_de_publicacion, activa, id)
                return self.index()


vistaPreviaController = VistaPreviaController()
