from flask import Flask, jsonify, request, make_response
import json
from flask_cors import CORS
import jwt
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

from models import *
import traceback

app = Flask(__name__)

app.config['SECRET_KEY'] = 'regteamdevelopment'
app.config['DEBUG'] = True

CORS(app)

ENDPOINT_BASE = '/v1/'


def token_auth_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'],algorithms="HS256")
            current_user = get_user_by_id(data['alumno_id'])
        except:
            traceback.print_exc()
            return jsonify({'message': 'Token is missing, carefull'}), 401

        return f(current_user,*args,**kwargs)

    return decorated

##############################################################################
##########                      Endpoints                           ##########
##############################################################################

@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()

    if 'correo' not in data or  'contrasena' not in data:
        return make_response('No se pudo verificar',404,
                {'WWW-Authenticate': 'Basic realm="Login required"'})

    user = get_user_by_email(data['correo'])

    if not user:
        return make_response('No se pudo verificar',404,
                {'WWW-Authenticate': 'Basic realm="Login required"'})

    if check_password_hash(user['contrasena'],data['contrasena']):
        token = jwt.encode({'alumno_id':user['alumno_id'], 
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
            app.config['SECRET_KEY'],algorithm="HS256")
        return jsonify({'token': token})

    return make_response('No se pudo verificar',404,
            {'WWW-Authenticate': 'Basic realm="Login required"'})


@app.route('/register',methods=['POST'])
def register():

    print(request)
    data = request.get_json()

    if ('nombre' not in data or 'apellidos' not in data or 'correo' not in 
            data or 'contrasena' not in data):
        return make_response('Falta algun campo',404,
                {'WWW-Authenticate': 'Basic realm="Fallo el registro"'})

    hashed_password = generate_password_hash(data['contrasena'],method='sha256')

    user = data
    user['contrasena'] = hashed_password

    # Perform insert
    if save_user(user) :
        return jsonify({'message': 'Usuario insertado correctamente'}), 200
    else:
        return jsonify({'message': 'Algo salio mal'}), 403


@app.route('/evaluacion',methods=['GET'])
@token_auth_required
def evaluaciones(current_user):

    evaluations = get_user_evaluations(current_user)

    return json.dumps({'evaluaciones':evaluations})

@app.route('/evaluacion/<evaluacion_id>',methods=['GET'])
def evaluacion(evaluacion_id):

    evaluation = get_evaluation_by_id(evaluacion_id)

    if evaluation:
        return jsonify({'evaluacion':evaluation})
    else:
        return jsonify({'message':'No se encontró la evaluación solicitada'}), 400


@app.route('/evaluacion/<evaluacion_id>/pregunta/<pregunta_id>',methods=['POST'])
@token_auth_required
def guardar_evaluacion_pregunta(current_user,evaluacion_id,pregunta_id):

    data = request.get_json()

    if 'opcion_seleccionada_id' not in data:
        return jsonify({'message':'No se mandó la opcion seleccionada'}), 400

    opcion_seleccionada_id = data['opcion_seleccionada_id']

    if save_student_answer(evaluacion_id,pregunta_id,opcion_seleccionada_id):
        return jsonify({'message':'Respuesta guardada exitosamente'})
    else:
        return jsonify({'message':'Error al guardar la respuesta'}), 400


@app.route('/evaluacion/<evaluacion_id>/calificar',methods=['POST'])
@token_auth_required
def guardar_calificacion_evaluacion(current_user,evaluacion_id):

    data = request.get_json()
    if ('aciertos_totales' not in data or 'fecha_aplicacion' not in data
    or 'puntaje_materia' not in data):
        return jsonify({'message':'Faltan campos en el cuerpo de la evaluacion'}), 400

    if type(data['puntaje_materia']) != list:
        return jsonify({'message':'Los puntajes no tienen el formato adecuado'}), 400

    puntaje_materia = data['puntaje_materia']

    original_subject_ids = [1,2,3,4,5,6,7,8,9,10] # Most be ordered
    if len(puntaje_materia) != len(original_subject_ids):
        return jsonify({'message':'Faltan los puntajes de algunas materias'}), 400

    for puntaje in puntaje_materia:
        if type(puntaje) != dict:
            return jsonify({'message':'Los puntajes no se reconocen adecuadamente'}), 400
        if 'materia_id' not in puntaje or 'puntaje' not in puntaje:
            return jsonify({'message':'Formatea los puntajes adecuadamente'}), 400

    subject_ids = [puntaje['materia_id'] for puntaje in puntaje_materia]
    subject_ids.sort()


    for i in range(len(original_subject_ids)):
        if subject_ids[i] - original_subject_ids[i] != 0:
            return jsonify({'message':'Fallo en los id''s de las materias'}), 400

    # Save exam
    if save_student_scores(evaluacion_id,data):
        return jsonify({'message':'Evaluación guardada correctamente'})
    else:
        return jsonify({'message':'Algo salió mal a la hora de guardar el examen'}), 400

@app.route('/historial',methods=['GET'])
@token_auth_required
def historial(current_user):
    history = get_evaluation_history(current_user['alumno_id'])

    if history:
        return jsonify({'historial':history})
    else:
        return jsonify({'historial':{}})

@app.route('/historial/<historial_id>',methods=['GET'])
@token_auth_required
def historial_by_id(current_user,historial_id):
    history = get_evaluation_history_by_id(current_user['alumno_id'],historial_id)

    if history:
        return jsonify({'historial':history})
    else:
        return jsonify({'historial':{}})

if __name__ == '__main__':
    app.run(debug=True)
