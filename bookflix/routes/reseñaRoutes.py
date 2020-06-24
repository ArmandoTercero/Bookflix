#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.ReseñaController import reseñaController
from controllers.BookController import bookController

# @app.route("/reseña", methods=["GET"])
# def reseña_index():
# 	return reseñaController.index()

# @app.route("/reseña/agregar", methods=["POST", "GET"])
# def reseña_new():
# 	return reseñaController.new()

# @app.route("/reseña/editar", methods=["POST", "GET"])
# def reseña_edit():
# 	return reseñaController.edit()

@app.route("/reseña/eliminar", methods=["POST", "GET"])
def reseña_eliminar():
	libro_id = (request.args.get('libro_id'))
	reseña_id = (request.args.get('reseña_id'))
	perfil_id = (request.args.get('perfil_id'))
	return reseñaController.delete(libro_id, reseña_id, perfil_id)
	
	# return bookController.libro(libro_id)