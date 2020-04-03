from flask import Flask,request
#from flaskext.mysql import MySQL
from config import config

app = Flask(__name__)

#mysql = MySQL()
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
#app.config['MYSQL_DATABASE_DB'] = 'bookflix'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)

from routes import routes

if __name__ == "__main__":
    app.run()
