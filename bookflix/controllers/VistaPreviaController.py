from flask import request, render_template, session, abort
from flask import send_from_directory, url_for
# from models.vistaPrevia import VistaPrevia

class VistaPreviaController():

	def __init__(self):
		pass

	def index(self):
		# vistas_previas = VistaPrevia.all()
		vistas_previas = []
		return render_template('vistas_previas/index.html', vistas_previas=vistas_previas)

vistaPreviaController = VistaPreviaController()