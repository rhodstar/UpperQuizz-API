from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2
import os
import jwt
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

load_dotenv()

DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

app.config['SECRET_KEY'] = 'regteamdevelopment'
app.config['DEBUG'] = True

CORS(app)

ENDPOINT_BASE = 'upper-quizz/v1/'

con = psycopg2.connect(database=DATABASE,user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD)

cur = con.cursor()

##############################################################################
##########                      Query Builders                      ##########
##############################################################################

def get_user_by_id(id):
    column_names = ['alumno_id','nombre','apellidos','correo','contrasena']
    query = 'select {}, {}, {}, {}, {} from alumno where alumno_id = {}'.format(
            *column_names,id)
    cur.execute(query)
    row = cur.fetchone()

    if row:
        res = dict(zip(column_names,row)) 
        return res
    else:
        return None


def get_user_by_email(email):
    column_names = ['alumno_id','nombre','apellidos','correo','contrasena']
    query = "select {}, {}, {}, {}, {} from alumno where correo='{}'".format(
            *column_names,email)

    cur.execute(query)
    row = cur.fetchone()

    if row:
        res = dict(zip(column_names,row)) 
        return res
    else:
        return None

def save_user(user):
    query = "insert into alumno(nombre,apellidos,correo,contrasena) values(%s, %s, %s, %s)"
    try:
        cur.execute(query,(user['nombre'],user['apellidos'],user['correo'],user['contrasena']))
        con.commit()
        return True
    except Exception:
        return False



##############################################################################
##########              Token function decorator                    ##########
##############################################################################

def token_auth_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user = get_user_by_id(data['id'])
        except:
            return jsonify({'message': 'Token is missing'}), 401

        return f(current_user,**args,**kwargs)

    return decorated

##############################################################################
##########                      Endpoints                           ##########
##############################################################################

@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()

    if not data['correo'] or  not data['contrasena']:
        return make_response('No se pudo verificar',404,
                {'WWW-Authenticate': 'Basic realm="Login required"'})

    user = get_user_by_email(data['correo'])

    if not user:
        return make_response('No se pudo verificar',404,
                {'WWW-Authenticate': 'Basic realm="Login required"'})

    #TODO:- Update using hash password
    if data['contrasena'] == user['contrasena']:
        token = jwt.encode({'alumno_id':user['alumno_id'], 
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
            app.config['SECRET_KEY'])

        return jsonify({'token': token})

    return make_response('No se pudo verificar',404,
            {'WWW-Authenticate': 'Basic realm="Login required"'})


@app.route('/register',methods=['POST'])
def register():

    print(request)
    data = request.get_json()

    if 'nombre' not in data or 'apellidos' not in data or 'correo' not in data or 'contrasena' not in data:
        return make_response('Falta algun campo',404,
                {'WWW-Authenticate': 'Basic realm="Fallo el registro"'})

    # Check if email isnt in DB
    hashed_password = generate_password_hash(data['contrasena'],method='sha256')

    user = data
    user['contrasena'] = hashed_password

    # Perform insert
    if save_user(user) :
        return jsonify({'message': 'Usuario insertado correctamente'}), 200
    else:
        return jsonify({'message': 'Algo salio mal'}), 403

if __name__ == '__main__':
    app.run(debug=True)

