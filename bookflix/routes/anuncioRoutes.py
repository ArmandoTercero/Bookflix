#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.AnuncioController import anuncioController

@app.route("/anuncio", methods=["GET"])
def anuncio_index():
	return anuncioController.index()

# @app.route("/anuncio/create", methods=["GET"])
# def anuncio_crear():
# 	return anuncioController.crear()

# @app.route("/anuncio/create", methods=["POST"])
# def anuncio_crear_post():
# 	return anuncioController.crear_anuncio()