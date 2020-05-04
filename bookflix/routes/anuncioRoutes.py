#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.AnuncioController import anuncioController

@app.route("/anuncio", methods=["GET"])
def anuncio_index():
	return anuncioController.index()

@app.route("/anuncio/agregar", methods=["POST", "GET"])
def anuncio_new():
	return anuncioController.new()