from db import db
from sqlalchemy import text

class Perro(db.Model):
    __tablename__ = 'Perros'
    ID = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(250), nullable = False)
    Raza = db.Column(db.String(50), nullable = False)
    Edad = db.Column(db.Integer, nullable = False)
    Peso = db.Column(db.Float, nullable = False)
    ID_CUIDADOR = db.Column(db.Integer, nullable = False)