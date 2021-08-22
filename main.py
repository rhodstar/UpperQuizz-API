#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, make_response
import json
from flask_cors import CORS
import jwt
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import traceback

from models import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'regteamdevelopment'
app.config['DEBUG'] = True

CORS(app)

ENDPOINT_BASE = '/v1'

def token_auth_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'No sé envío el token del usuario'}), 400

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'],algorithms="HS256")
            current_user = get_user_by_id(data['alumno_id'])
        except Exception as e:
            print(e)
            return jsonify({'message': 'Token inválido'}), 400

        return f(current_user,*args,**kwargs)

    return decorated

@app.after_request
def apply_caching(response):
    response.headers["Content-Type"] = "application/json"
    return response

##############################################################################
##########                      Endpoints                           ##########
##############################################################################

@app.route(ENDPOINT_BASE+'/login',methods=['POST'])
def login():
    data = request.get_json()
    http_header = {'WWW-Authenticate': 'Basic realm="Login required"'}

    if 'correo' not in data or  'contrasena' not in data:
        message = {"message": "Faltan datos para autentificar"}
        response = make_response(message,400,http_header)
        return response

    user = get_user_by_email(data['correo'])

    if not user:
        message = {"message": "El usuario o la contrasena son incorrectos"}
        response = make_response(message,400,http_header)
        return response

    if not check_password_hash(user['contrasena'],data['contrasena']):
        message = {"message": "Contraseña incorrecta"}
        response = make_response(message,400, http_header)
        return response
    else:
        exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        encode_data = {'alumno_id':user['alumno_id'], 'exp':exp_time}
        token = jwt.encode(encode_data, app.config['SECRET_KEY'],algorithm="HS256")

        return make_response(jsonify({'token': token}))


@app.route(ENDPOINT_BASE+'/register',methods=['POST'])
def register():

    data = request.get_json()
    http_header = {'WWW-Authenticate': 'Basic realm="Fallo el registro"'}

    if ('nombre' not in data or 'apellidos' not in data or 
    'correo' not in data or 'contrasena' not in data):
        message = {"message":"Falta algun campo"}
        return make_response(message,400,http_header)

    hashed_password = generate_password_hash(data['contrasena'],method='sha256')

    user = data
    user['contrasena'] = hashed_password

    if save_user(user) :
        message = {"message": "Usuario insertado correctamente"}
        return make_response(jsonify(message))
    else:
        message = {'message': 'Algo salio mal a la hora de guardar'}
        return make_response(jsonify(message),500)


@app.route(ENDPOINT_BASE+'/evaluacion',methods=['GET'])
@token_auth_required
def evaluaciones(current_user):

    evaluations = get_user_evaluations(current_user)
    return json.dumps({'evaluaciones':evaluations})


@app.route(ENDPOINT_BASE+'/evaluacion/<evaluacion_id>',methods=['GET'])
def evaluacion(evaluacion_id):

    evaluation = get_evaluation_by_id(evaluacion_id)

    if evaluation:
        return make_response(jsonify({'evaluacion':evaluation}))
    else:
        message = {'message':'No se encontró la evaluación solicitada'}
        return make_response(jsonify(message), 400)


@app.route(ENDPOINT_BASE+'/evaluacion/<evaluacion_id>/pregunta/<pregunta_id>',methods=['POST'])
@token_auth_required
def guardar_evaluacion_pregunta(current_user,evaluacion_id,pregunta_id):

    data = request.get_json()

    if 'opcion_seleccionada_id' not in data:
        message = {'message':'No se mandó la opcion seleccionada'}
        return make_response(jsonify(message), 400)

    #TODO:- Future version should make sure that the selected option is valid
    opcion_seleccionada_id = data['opcion_seleccionada_id']

    if save_student_answer(evaluacion_id,pregunta_id,opcion_seleccionada_id):
        message = {'message':'Respuesta guardada exitosamente'}
        return make_response(jsonify(message))
    else:
        message = {'message':'Error al guardar la respuesta'}
        return make_response(jsonify(message), 500)


@app.route(ENDPOINT_BASE+'/evaluacion/<evaluacion_id>/calificar',methods=['POST'])
@token_auth_required
def guardar_calificacion_evaluacion(current_user,evaluacion_id):

    data = request.get_json()
    # Check if request has the minimum attributes
    if ('aciertos_totales' not in data or 'fecha_aplicacion' not in data
    or 'puntaje_materia' not in data):
        message = {'message':'Faltan campos en el cuerpo del request'}
        return make_response(jsonify(message), 400)

    if type(data['puntaje_materia']) != list:
        message = {'message':'Los puntajes no tienen el formato adecuado'}
        return make_response(jsonify(message), 400)

    puntaje_materia = data['puntaje_materia']

    original_subject_ids = [1,2,3,4,5,6,7,8,9,10] # Most be ordered
    if len(puntaje_materia) != len(original_subject_ids):
        message = {'message':'Faltan los puntajes de algunas materias'}
        return make_response(jsonify(message), 400)

    # Checking if "puntaje_materia" has the appropiate format
    for puntaje in puntaje_materia:
        if type(puntaje) != dict:
            message = {'message':'Los puntajes no se reconocen adecuadamente'}
            return make_response(jsonify(message), 400)

        if 'materia_id' not in puntaje or 'puntaje' not in puntaje:
            message = {'message':'Faltan atributos: materia_id o puntaje'}
            return make_response(jsonify(message), 400)

    subject_ids = [puntaje['materia_id'] for puntaje in puntaje_materia]
    subject_ids.sort()

    # Checking for any missing materia_id 
    for i in range(len(original_subject_ids)):
        if subject_ids[i] - original_subject_ids[i] != 0:
            message = {'message':'Fallo en los id''s de las materias'}
            return make_response(jsonify(message), 400)

    # Save student answers data
    if save_student_scores(evaluacion_id,data):
        message = {'message':'Evaluación guardada correctamente'}
        return make_response(jsonify(message))
    else:
        message = {'message':'Algo salió mal a la hora de guardar el examen'}
        return make_response(jsonify(message), 500)


@app.route(ENDPOINT_BASE+'/historial',methods=['GET'])
@token_auth_required
def historial(current_user):
    history = get_evaluation_history(current_user['alumno_id'])
    message = {'historial':history}
    return make_response(jsonify(message))


@app.route(ENDPOINT_BASE+'/historial/<historial_id>',methods=['GET'])
@token_auth_required
def historial_by_id(current_user,historial_id):
    history = get_evaluation_history_by_id(current_user['alumno_id'],historial_id)
    if history:
        return make_response(jsonify({'historial':history}))
    else:
        message = {"message":"No existe la evaluación solicitada"}
        return make_response(jsonify(message),400)
