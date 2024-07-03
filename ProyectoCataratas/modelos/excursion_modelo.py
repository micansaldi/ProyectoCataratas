from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from app import app, db   #,ma


# defino las tablas
class Excursion(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    titulo=db.Column(db.String(100))
    precio=db.Column(db.Float)
    duracion=db.Column(db.String(100))
    descripcion = db.Column(db.String(1000))
    imagen=db.Column(db.String(400))
    def __init__(self,titulo,precio,duracion,descripcion,imagen):   #crea el  constructor de la clase
        self.titulo=titulo   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio=precio
        self.duracion=duracion
        self.descripcion=descripcion
        self.imagen=imagen


with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
