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
            print("token: "+token)
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


@app.route('/evaluaciones',methods=['GET'])
@token_auth_required
def evaluaciones(current_user):

    evaluations = get_user_evaluations(current_user)

    return json.dumps({'evaluaciones':evaluations})

@app.route('/evaluaciones/<evaluacion_id>',methods=['GET'])
def evaluacion(evaluacion_id):

    evaluation = get_evaluation_by_id(evaluacion_id)

    if evaluation:
        return jsonify({'evaluacion':evaluation})
    else:
        return jsonify({'message':'No se encontró la evaluación solicitada'}), 400


if __name__ == '__main__':
    app.run(debug=True)

