from flask import request, render_template, session
#from app.models.AuthModel import authmodel
#from app.helpers.Utility import sendResponse
from models.usuario import Usuario
from models.plan import Plan

class UserController():

    def __init__(self):
        pass

    def index(self):
        return render_template('index.html')

    def register(self):
        planes = Plan.all()
        return render_template('registrar.html', planes=planes)

    def registeruser(self):
        #_firstname = request.form.get('firstname', '')
        #_lastname = request.form.get('lastname', '')
        #_email = request.form.get('email', '')
        #_password = request.form.get('password', '')
        #return sendResponse(authmodel.registerUser(_firstname,_lastname,_email,_password))
        usuario = Usuario.crear(request.form)
        print(usuario)
        return "<h1> REGISTRANDO USUARIO </h1> <br> " + str(request.form)
    
    def login(self):
        return render_template("login.html")
    
    def loginuser(self):
        session["usuario"] = request.form["email"]
        return self.index()
    
    def logout(self):
        session.pop("usuario", None)
        return self.index()
    
    def hello(self, name):
        saludo = "!Hola " + name + "!"
        return "<h1>" + saludo + "</h1>"
    
    def user_id(self, id):
        user = Usuario.encontrar_por_id(id)
        if user:
            return render_template("/usuarios/read.html", usuario = user)
        else:
            return "<h1> No existe ningun usuario con esa id</h1>"

usercontroller=UserController()

