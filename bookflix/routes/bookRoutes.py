#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, json
from flask import render_template
from app import app
from controllers.BookController import bookController


@app.route("/libro", methods=["GET"])
def libro_index():
    return bookController.index()


@app.route("/libro/new", methods=["GET"])
def libro_upload():
    return bookController.new()


@app.route("/libro/new", methods=["POST"])
def libro_upload_file():
    return bookController.new_book()


@app.route("/libro/search", methods=["GET"])
def libro_search():
    return bookController.search()


@app.route("/libro/search", methods=["POST"])
def libro_search_text():
    return bookController.search_book()


@app.route("/libro/<libro_id>", methods=["GET"])
def libro(libro_id):
    return bookController.libro(libro_id)


@app.route("/libro/edit/<libro_id>", methods=["GET"])
def libro_edit(libro_id):
    return bookController.edit(libro_id)


@app.route("/libro/edit/<libro_id>", methods=["POST"])
def libro_edit_file(libro_id):
    return bookController.edit_book(libro_id)


@app.route("/ver_catalogo", methods=["GET", "POST"])
def ver_catalogo():
    return bookController.ver_catalogo()
