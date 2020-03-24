from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
	# return "Hello World"

if __name__ == "__main__":
	app.run()

# Rutas de la página:

# Ruta de inicio de sesion
@app.route("/login")
def login():
	return render_template("login.html")
