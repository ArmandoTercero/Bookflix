from flask import request, render_template, session, abort
from flask import send_from_directory, url_for
from models.reseña import Reseña
from controllers.BookController import BookController

class ReseñaController():

	def __init__(self):
		pass

	# Llama al indice de bookRoutes
	def index(self, id_libro):
		BookController.libro(id_libro)

	def new(self):
		if request.method == 'GET':
			return render_template ('reseñas/new.html')
		elif request.method == 'POST':
			Reseña.new(request.form["id_perfil"], request.form["id_libro"], request.form["calificacion"], request.form["comentario"])
			return self.index(request.form["id_libro"])

	def edit(self):
		if request.method == 'GET':
			reseña = Reseña.encontrar_por_id(request.args.get("reseña_id"))
			return render_template ('reseñas/edit.html', reseña=reseña)
		elif request.method == 'POST':
			Reseña.edit(request.form["id_reseña"], request.form["id_perfil"], request.form["id_libro"], request.form["calificacion"], request.form["comentario"])
			return self.index(request.form["id_libro"])

	def delete(self):
		Reseña.eliminar(request.form["id_reseña"])
		return self.index(request.form["id_libro"])

reseñaController = ReseñaController()