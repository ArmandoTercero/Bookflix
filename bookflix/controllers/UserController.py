from datetime import datetime

from flask import request, render_template, session, redirect, url_for, flash
# from app.models.AuthModel import authmodel
# from app.helpers.Utility import sendResponse
from models.usuario import Usuario
from models.plan import Plan
from models.perfiles import Perfiles


class UserController():

    def __init__(self):
        pass

    def index(self):
        return render_template('index.html')

    def panel_de_control(self):
        return render_template('panel_de_control.html')

    def register(self):
        planes = Plan.all()
        return render_template('registrar.html', planes=planes)

    def registeruser(self):
        # _firstname = request.form.get('firstname', '')
        # _lastname = request.form.get('lastname', '')
        # _email = request.form.get('email', '')
        # _password = request.form.get('password', '')
        # return sendResponse(authmodel.registerUser(_firstname,_lastname,_email,_password))

        errores = []

        email = request.form["email"]
        if Usuario.existe_usuario_con_email(email):
            errores.append(
                'El email ya esta en uso, por favor seleccione otro.')

        # El número de la tarjeta tiene que ser de 16 digitos
        # El pin de la tiene que ser de 3 digitos
        tarjetaNumero_valido = (request.form["tarjetaNumero"].__len__() != 16)
        tarjetaPin_valido = (request.form["tarjetaPin"].__len__() != 3)

        # https://learnandlearn.com/python-programming/python-reference/python-get-current-date
        # Pregunto si la fecha de expiración ingresada para la tarjeta es mayor al día de hoy ...
        # ... con esto compruebo si es válida o no.
        feha_de_hoy = datetime.today()
        tarjetaFechaDeExpiracion = datetime.strptime(
            request.form["tarjetaFechaDeExpiracion"], "%Y-%m-%d")
        if (feha_de_hoy >= tarjetaFechaDeExpiracion) or tarjetaNumero_valido or tarjetaPin_valido:
            errores.append(
                'Los datos proporcionados acerca la tarjeta de crédito no son válidos.')

        if errores:
            # Solo entra aca si el arreglo tiene elementos, osea que hay errores.
            planes = Plan.all()
            return render_template('registrar.html', planes=planes, errores=errores)
        else:
            # Solo entra aca si el arreglo esta vacio, esto significa que no hay ...
            # ... errores y el registro se realiza de forma exitosa.
            usuario = Usuario.crear(request.form)
            return self.index()

    # Login GET
    def login(self):
        return render_template("login.html")

    # Login POST
    def loginuser(self):
        errores = []

        # Me fijo si existe el usuario ingresado y luego pregunto si la contraseña ingresada es correcta
        usuario = Usuario.encontrar_por_email(request.form["email"])
        perfiles = Perfiles.all()
        if usuario and (usuario["contraseña"] == request.form["password"]):
            session["id"] = usuario["id"]

            # session["perfil_id"] = request.form["perfil_id"] TODAVÍA NO HICIMOS NADA ACERCA DE LOS PERFILES
            session["admin"] = (usuario["email"] == "admin")
            # se conecta a perfiles
            return render_template("/usuarios/perfiles.html", perfiles=perfiles, usuario=usuario)

            # return self.index()
        else:
            errores.append("Los datos ingresados son incorrectos.")
            return render_template("login.html", errores=errores)

    def logout(self):
        session.pop("id", None)
        session.pop("admin", None)
        return self.index()

    def hello(self, name):
        saludo = "!Hola " + name + "!"
        return "<h1>" + saludo + "</h1>"

    def user_id(self, id):
        user = Usuario.encontrar_por_id(id)
        if user:
            return render_template("/usuarios/read.html", usuario=user)
        else:
            return "<h1> No existe ningun usuario con esa id</h1>"

    # ver perfil de usuario sus datos
    def ver_perfil(self, id):
        user = Usuario.encontrar_por_id(id)
        if user:
            return render_template("/usuarios/perfil.html", usuario=user)
        else:
            return "<h1> No existe ningun usuario con esa id</h1>"

    # ver perfiles de usuario
    def ver_perfiles(self, id):
        # print(id)
        user = Usuario.encontrar_por_id(id)
        perfiles = Perfiles.all()

        return render_template("/usuarios/perfiles.html", perfiles=perfiles, usuario=user)

    # crear un perfil
    def crear_perfil(self, id):
        user = Usuario.encontrar_por_id(id)
        perfiles = Perfiles.all()
        if request.method == 'POST':
            foto = request.form['foto']
            nombre = request.form['nombre']
            Perfiles.crear(dict
                           ([('nombre', nombre), ('foto', foto), ('id_usuario', id)]))

        return render_template("/usuarios/crearPerfil.html", perfiles=perfiles, usuario=user)

    # modificar un perfil
    def modificar_perfil(self, id_perfil):
        perfiles = Perfiles.encontrar_por_id(id_perfil)
        user = Usuario.encontrar_por_id(perfiles['id_usuario'])
        if request.method == 'POST':
            foto = request.form['foto']
            nombre = request.form['nombre']
            Perfiles.edit(request.form)

        return render_template("/usuarios/modificarPerfil.html", perfil=perfiles, usuario=user)

    # eliminar perfil
    def eliminar_perfil(self, id_perfil):
        perfiles = Perfiles.encontrar_por_id(
            id_perfil)  # el perfil completo con ese id
        # todos los datos del usuario dueño de ese perfil
        user = Usuario.encontrar_por_id(perfiles['id_usuario'])
        # print(user['id'])
        # print(perfiles)
        # print(user)
        Perfiles.eliminar(id_perfil)
        return redirect(url_for('ver_perfiles', id=user['id']))


usercontroller = UserController()
