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

CORS(app)

ENDPOINT_BASE = 'upper-quizz/v1/'

try: 
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

        res = dict(zip(column_names,row)) 

        return res
    
    def get_user_by_email(email):
        column_names = ['alumno_id','nombre','apellidos','correo','contrasena']
        query = "select {}, {}, {}, {}, {} from alumno where correo='{}'".format(
                *column_names,email)

        print(query)

        cur.execute(query)

        row = cur.fetchone()

        # Check if mail doesnt exist

        res = dict(zip(column_names,row)) 

        return res
    

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

        print(data)

        if not data['correo'] or  not data['contrasena']:
            return make_response('No se pudo verificar',404,
                    {'WWW-Authenticate': 'Basic realm="Login required"'})

        user = get_user_by_email(data['correo'])

        if not user:
            return make_response('No se pudo verificar',404,
                    {'WWW-Authenticate': 'Basic realm="Login required"'})

        if data['contrasena'] == user['contrasena']:
            token = jwt.encode({'alumno_id':user['alumno_id'], 
                'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
                app.config['SECRET_KEY'])

            return jsonify({'token': token})

        return make_response('No se pudo verificar',404,
                {'WWW-Authenticate': 'Basic realm="Login required"'})

except:
    print("There was an error while connecting to DB")

