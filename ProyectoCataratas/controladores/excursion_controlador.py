from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request
from app import app, db,ma
from modelos.excursion_modelo import *


class ExcursionSchema(ma.Schema):
    class Meta:
        fields=('id','titulo','precio','duracion','descripcion','imagen')


excursion_schema=ExcursionSchema()            # El objeto producto_schema es para traer un producto
excursiones_schema=ExcursionSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto


# crea los endpoint o rutas (json)
@app.route('/excursiones',methods=['GET'])
def get_Excursiones():
    all_excursiones=Excursion.query.all()         # el metodo query.all() lo hereda de db.Model
    result=excursiones_schema.dump(all_excursiones)  # el metodo dump() lo hereda de ma.schema y
                                               # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla


@app.route('/excursiones/<id>',methods=['GET'])
def get_excursion(id):
    excursion=Excursion.query.get(id)
    return excursion_schema.jsonify(excursion)   # retorna el JSON de un producto recibido como parametro


@app.route('/excursiones/<id>',methods=['DELETE'])
def delete_excursion(id):
    excursion=Excursion.query.get(id)
    db.session.delete(excursion)
    db.session.commit()
    return excursion_schema.jsonify(excursion)   # me devuelve un json con el registro eliminado


@app.route('/excursiones', methods=['POST']) # crea ruta o endpoint
def create_excursion():
    #print(request.json)  # request.json contiene el json que envio el cliente
    titulo=request.json['titulo']
    precio=request.json['precio']
    duracion=request.json['duracion']
    descripcion=request.json['descripcion']
    imagen=request.json['imagen']
    new_excursion=Excursion(titulo,precio,duracion,descripcion,imagen)
    db.session.add(new_excursion)
    db.session.commit()
    return excursion_schema.jsonify(new_excursion)


@app.route('/excursiones/<id>' ,methods=['PUT'])
def update_excursion(id):
    excursion=Excursion.query.get(id)
 
    excursion.titulo=request.json['titulo']
    excursion.precio=request.json['precio']
    excursion.duracion=request.json['duracion']
    excursion.descripcion=request.json['descripcion']
    excursion.imagen=request.json['imagen']


    db.session.commit()
    return excursion_schema.jsonify(excursion)


@app.route('/')
def bienvenida():
    return "Bienvenidos al backend"   # retorna el JSON de un usuario recibido como parametro
