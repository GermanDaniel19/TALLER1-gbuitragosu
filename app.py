from flask import Flask,render_template,Blueprint, request,flash
from flask_login import LoginManager, UserMixin, login_user, login_required
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from db import db, init_db
from models.cuidador import Cuidador
from models.perro import Perro
from controllers.cuidador_controller import cuidador_blueprint
from models.usuarios import Usuarios
import os


app = Flask(__name__,template_folder="views")
secret_key = os.urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@127.0.0.1:3306/tablas'
app.config["SQLALCHEMY_TRACK_MODIFICATIOS"] = False
app.config["SECRET_KEY"] = secret_key
app.secret_key = 'mi_clave_secreta'

login_manager = LoginManager(app)


db.init_app(app)
init_db(app)

# db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.buscar_usuario(user_id)

@app.route('/')
def index():

    usuario1 = Usuarios(username = "user1" , password = "123", is_admin = True)
    usuario2 = Usuarios(username = "user2" , password = "456", is_admin = False)
    usuario3 = Usuarios(username = "user3" , password = "789", is_admin = False)

    db.session.add(usuario1)
    db.session.add(usuario2)
    db.session.add(usuario3)
    db.session.commit()

    perros = Perro.query.all()
    cuidadores = Cuidador.query.all()
    return render_template('index.html', cuidadores=cuidadores,  perros=perros)

@app.route("/perros")
def perros():
    perros = Perro.query.all()
    cuidadores = Cuidador.query.all()
    return render_template("perros.html" , cuidadores=cuidadores,  perros=perros)

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form["user"]
        password = request.form["password"]
        usuarios = Usuarios()
        print(user ,password)

        es_logueo = usuarios.existe_usuario(user=user, password=password)
        if isinstance(es_logueo, int):
            # login_user(es_logueo)
            if es_logueo == 1:
                perros = Perro.query.all()
                cuidadores = Cuidador.query.all()
                return render_template("perros.html" , cuidadores=cuidadores,  perros=perros)
            else:
                return(f"Hola mundo {user}")

        else: 
            print("pAILAS")
            flash("Usuario no encontrado")
        return render_template('login.html')

app.register_blueprint(cuidador_blueprint)

#Esto nos corre con el play, si no se tiene toca con el comando Flask run
if __name__ == '__main__':
    #with app.app_context():
    #    db.drop_all()
    #    db.create_all()
    app.run(debug=True)
