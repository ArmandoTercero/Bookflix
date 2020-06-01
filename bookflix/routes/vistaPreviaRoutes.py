#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.VistaPreviaController import vistaPreviaController

@app.route("/vista_previa", methods=["GET"])
def vista_previa_index():
	return vistaPreviaController.index()