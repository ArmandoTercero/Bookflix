#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.BookController import bookController

@app.route("/libro", methods=["GET"])
def libro_index():
	return bookController.index()

@app.route("/libro/upload", methods=["GET"])
def libro_upload():
	return bookController.upload()

@app.route("/libro/upload", methods=["POST"])
def libro_upload_file():
	return bookController.upload_file()

@app.route("/libro/<libro_id>", methods=["GET"])
def libro (libro_id):
	return bookController.libro(libro_id)

