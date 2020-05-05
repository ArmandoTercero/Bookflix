from flask import request, render_template, session, abort
from flask import send_from_directory, url_for
#from app.models.AuthModel import authmodel
#from app.helpers.Utility import sendResponse

class AbstractController():

	def validate (func):
		def val (*args, **kwargs):
			if not "admin" in session:
				abort (401)
			else:
				return func (*args, **kwargs)
		return val


