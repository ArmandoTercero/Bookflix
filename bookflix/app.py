from flask import Flask,request
#from flaskext.mysql import MySQL
from config import config

app = Flask(__name__, static_folder='static')

#mysql = MySQL()
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
#app.config['MYSQL_DATABASE_DB'] = 'bookflix'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)

app.secret_key = "12345"

from routes import routes
from routes import bookRoutes
from routes import authorRoutes

if __name__ == "__main__":
	app.run()
