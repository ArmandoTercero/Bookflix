from datetime import datetime

from flask import request, render_template, session, redirect, url_for, flash
# from app.models.AuthModel import authmodel
# from app.helpers.Utility import sendResponse
from models.usuario import Usuario
from models.plan import Plan
from models.perfiles import Perfiles
from models.libro import Libro
from models.editorial import Editorial
from models.genero import Genero
from models.autor import Author
from models.anuncio import Anuncio


class UserController():

    def __init__(self):
        pass

    def index(self):
        libros = Libro.all()
        editoriales = Editorial.all()
        generos = Genero.all()
        autores = Author.all()
        cant = 0
        mostrar = []
        for libro in libros:
            if cant < 6:
                mostrar.append(libro)
            cant = cant + 1

        return render_template('index.html', libros=mostrar, editoriales=editoriales, generos=generos, autores=autores)

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

        contraseña = request.form["password"]
        # https://kite.com/python/answers/how-to-check-if-a-string-contains-letters-in-python
        tiene_letras = contraseña.lower().islower()
        # https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters
        tiene_numeros = '0' in contraseña or '1' in contraseña or '2' in contraseña or '3' in contraseña or '4' in contraseña or '5' in contraseña or '6' in contraseña or '7' in contraseña or '8' in contraseña or '9' in contraseña
        tiene_simbolos = "'" in contraseña or '¿' in contraseña or '?' in contraseña or '¡' in contraseña or '!' in contraseña or '#' in contraseña or '@' in contraseña or '.' in contraseña or '-' in contraseña or '_' in contraseña
        longitud_de_caracteres_valido = (contraseña.__len__() >= 8)
        contraseña_valida = tiene_letras and tiene_numeros and tiene_simbolos and longitud_de_caracteres_valido

        if not contraseña_valida:
            errores.append(
                'Contraseña inválida.')

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
        if usuario:
            # Luego de saber que el usuario buscado existe, pregunto si la contraseña es correcta
            if (usuario["contraseña"] != request.form["password"]):
                errores.append("Los datos ingresados son incorrectos.")
                return render_template("login.html", errores=errores)

            session["id"] = usuario["id"]

            # session["perfil_id"] = request.form["perfil_id"] TODAVÍA NO HICIMOS NADA ACERCA DE LOS PERFILES
            session["admin"] = (usuario["email"] == "admin@gmail.com")
            # se conecta a perfiles

            if session["admin"]:
                return render_template('panel_de_control.html')
            else:
                return render_template("/usuarios/perfiles.html", perfiles=perfiles, usuario=usuario)
        else:
            errores.append("No existe ninguna cuenta con el email ingresado.")
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
        user = Usuario.encontrar_por_id(id)
        perfiles = Perfiles.all()

        return render_template("/usuarios/perfiles.html", perfiles=perfiles, usuario=user)

    # crear un perfil
    def crear_perfil(self, id):
        errores = []
        user = Usuario.encontrar_por_id(id)
        perfiles = Perfiles.all()
        planes = Plan.all()
        print(planes[0])
        contador = 0
        print('el id', id)
        if user['plan_id'] == 2:
            for perfil in perfiles:
                if perfil['id_usuario'] == user['id']:
                    contador = contador + 1
            print("contador", contador)
            if contador < 4:
                if request.method == 'POST':
                    if Perfiles.existe_perfil_con_nombre(request.form["nombre"]):
                        errores.append("Ya existe un perfil con el nombre especificado.")
                        print("Ya existe un perfil con el nombre especificado.")                        
                    else:
                        foto = request.form['foto']
                        nombre = request.form['nombre']
                        Perfiles.crear(dict
                                       ([('nombre', nombre), ('foto', foto), ('id_usuario', id)]))
            else:
                print("Ya no puede agregar mas contactos!!!!!")
                flash('Ya no puede agregar mas contactos!!!!!')
            return render_template("/usuarios/crearPerfil.html", perfiles=perfiles, usuario=user, errores=errores)
        else:
            if user['plan_id'] == 1:
                for perfil in perfiles:
                    if perfil['id_usuario'] == user['id']:
                        contador = contador + 1
            print("contador", contador)
            if contador < 2:
                if request.method == 'POST':
                    if Perfiles.existe_perfil_con_nombre(request.form["nombre"]):
                        errores.append("Ya existe un perfil con el nombre especificado.")
                        print("Ya existe un perfil con el nombre especificado.")                        
                    else:
                        foto = request.form['foto']
                        nombre = request.form['nombre']
                        Perfiles.crear(dict
                                       ([('nombre', nombre), ('foto', foto), ('id_usuario', id)]))
            else:
                print("Ya no puede agregar mas contactos!!!!!")
                flash('Ya no puede agregar mas contactos!!!!!')

            return render_template("/usuarios/crearPerfil.html", perfiles=perfiles, usuario=user, errores=errores)

    # modificar un perfil
    def modificar_perfil(self, id_perfil):
        errores = []
        perfiles = Perfiles.encontrar_por_id(id_perfil)
        user = Usuario.encontrar_por_id(perfiles['id_usuario'])
        if request.method == 'POST':
            if Perfiles.existe_perfil_con_nombre(request.form["nombre"]):
                errores.append("Ya existe un perfil con el nombre especificado.")
                print("Ya existe un perfil con el nombre especificado.")
                
            else:
                foto = request.form['foto']
                nombre = request.form['nombre']
                Perfiles.edit(dict
                          ([('nombre', nombre), ('foto', foto), ('id_perfil', id_perfil)]))

        return render_template("/usuarios/modificarPerfil.html", perfil=perfiles, usuario=user, errores=errores)

    # eliminar perfil
    def eliminar_perfil(self, id_perfil):
        perfiles = Perfiles.encontrar_por_id(id_perfil)

        user = Usuario.encontrar_por_id(perfiles['id_usuario'])
        Perfiles.eliminar(id_perfil)
        return redirect(url_for('ver_perfiles', id=user['id']))

    def ver_anuncio(self):
        anuncios = Anuncio.all()
        return render_template("usuarios/anuncios.html", anuncios=anuncios)

    # ver perfil de usuario sus datos
    def ver_perfiles_con_sesion(self):
        return redirect(url_for('ver_perfiles', id=session['id']))


usercontroller = UserController()
