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
        if request.method == 'GET':
            return render_template('vistas_previas/new.html')
        elif request.method == 'POST':
            VistaPrevia.crear(request.form)
            return self.index()

    def delete(self, id):
        vistas_previas = VistaPrevia.all()
        vista = VistaPrevia.eliminar(id)
        return render_template('vistas_previas/index.html', vistas_previas=vistas_previas)


vistaPreviaController = VistaPreviaController()
