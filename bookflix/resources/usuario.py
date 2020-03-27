from flask import render_template
from bookflix.models.usuario import Usuario

def hello(nombre):
	saludo = "¡Hola " + nombre + "!"
	return "<h1>" + saludo + "</h1>"

def id(id):
	usuario = Usuario.encontrar_por_id(id)
	if usuario:
		return render_template("/usuarios/read.html", usuario = usuario)
	else:
		return "<h1> No existe ningun usuario con esa id</h1>"