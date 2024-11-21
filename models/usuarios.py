from db import db
# from flask_login import UserMixin

class Usuarios(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(60), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    is_admin = db.Column(db.Boolean, nullable = True)

    def buscar_usuario(self, id_usuario):
        usuario = Usuarios.query.filter_by(id = id_usuario).first()
        return usuario
    
    def existe_usuario(self, user, password):
        usuario  = Usuarios.query.filter_by(username = user, password = password).first()

        if isinstance(usuario, Usuarios):
            if usuario.is_admin == True:
                return 1
            else: 
                return 2
        else: -1