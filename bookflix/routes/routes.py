#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.UserController import usercontroller

@app.route("/", methods=["GET"])
def index():
	return usercontroller.index()

@app.route("/panel_de_control", methods=["GET"])
def panel_de_control():
	return usercontroller.panel_de_control()

@app.route("/register", methods=["GET"])
def register():
	return usercontroller.register()

@app.route("/register", methods=["POST"])
def registeruser():
	return usercontroller.registeruser()

@app.route("/login", methods=["GET"])
def login ():
	return usercontroller.login()

@app.route("/login", methods=["POST"])
def loginuser ():
   return usercontroller.loginuser()

@app.route("/logout", methods=["GET", "POST"])
def logout ():
	return usercontroller.logout()

#ruta para ver perfil
@app.route("/ver_perfil/<id>", methods=["GET", "POST"])
def ver_perfil (id):
	return usercontroller.ver_perfil(id)

#ruta ver perfiles 
@app.route("/ver_perfiles/<id>", methods=["GET", "POST"])
def ver_perfiles (id):
	return usercontroller.ver_perfiles(id)

#ruta crear un perfil
@app.route("/crear_perfil", methods=["GET", "POST"])
def crear_perfil ():
	return usercontroller.crear_perfil()

#ruta modificar un perfil
@app.route("/modificar_perfil", methods=["GET", "POST"])
def modificar_perfil ():
	return usercontroller.modificar_perfil()



# Borrar a futuro
@app.route("/hello/<name>")
def hello (name):
	return usercontroller.hello(name)

@app.route("/user/<id>")
def user_id (id):
	return usercontroller.user_id(id)

