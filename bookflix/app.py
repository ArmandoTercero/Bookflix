from flask import Flask, render_template, request, session, escape
from bookflix.resources import usuario

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
	# return "Hello World"

if __name__ == "__main__":
	app.run()

app.secret_key = "12345"

# Rutas de la página:

# Ruta de inicio de sesion
@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session["usuario"] = request.form["usuario"]
		return render_template('index.html')

	return render_template("login.html")

# Ruta para cerrar la sesión
@app.route("/logout")
def logout():
	session.pop("usuario", None)
	return render_template('index.html')

# Ruta para registrarse
@app.route("/registrar", methods=["POST", "GET"])
def registrar():
	if request.method == "POST":
		return "<h1> REGISTRANDO USUARIO </h1> <br> " + str(request.form)
	else:
		return render_template('registrar.html')

# Rutas de usuario
app.add_url_rule('/hello/<nombre>', 'usuario_hello', usuario.hello)
app.add_url_rule('/usuario/<id>', 'usuario_id', usuario.id)