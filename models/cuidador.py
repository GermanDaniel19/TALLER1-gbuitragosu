from db import db
from sqlalchemy import text

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'
    ID = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(250), nullable = False)
    Telefono = db.Column(db.String(250), nullable = False)
	
	