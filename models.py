import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

con = psycopg2.connect(database=DATABASE,user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD)

cur = con.cursor()


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

    cur.close()
    con.close()

    if row:
        res = dict(zip(column_names,row)) 
        return res
    else:
        return None

def save_user(user):
    query = ("insert into alumno(nombre,apellidos,correo,contrasena) "
        "values(%s, %s, %s, %s)")
    try:
        cur.execute(query,(user['nombre'],user['apellidos'],
            user['correo'],user['contrasena']))
        con.commit()
        return True
    except Exception:
        return False


