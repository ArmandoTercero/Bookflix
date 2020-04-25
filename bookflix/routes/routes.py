#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.UserController import usercontroller

@app.route("/", methods=["GET"])
def index():
    return usercontroller.index()

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

@app.route("/hello/<name>")
def hello (name):
    return usercontroller.hello(name)

@app.route("/user/<id>")
def user_id (id):
    return usercontroller.user_id(id)

