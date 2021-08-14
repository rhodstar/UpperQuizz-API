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


def get_user_evaluations(user):
    query = ("select e.examen_id,e.nombre, s.nombre, aciertos_totales, num_intento "
    "from evaluacion_alumno ev,status_evaluacion s, examen e "
    "where ev.examen_id = e.examen_id "
    "and ev.status_evaluacion_id = s.status_evaluacion_id "
    "and alumno_id = "+str(user['alumno_id']))

    cur.execute(query)

    rows = cur.fetchall()

    keys = ['examen_id',"nombre_examen","status","aciertos_totales","num_intento"] 

    evaluations = []
    
    #TODO:- Check null case
    for row in rows:
        evaluations.append(dict(zip(keys,row)))

    return evaluations

def get_evaluation_by_id(evaluacion_id):
    keys = ["pregunta_id","texto_pregunta","materia_id","opcion_id",
            "texto_opcion", "es_correcta"]
    query = '''
    select p.pregunta_id,p.texto_pregunta,p.materia_id,
    o.opcion_id,o.texto_opcion,o.es_correcta
    from pregunta p, opcion o
    where p.examen_id = (
      select examen_id from evaluacion_alumno 
      where evaluacion_id = {}
    )
    and p.pregunta_id = o.pregunta_id
    order by p.pregunta_id'''. format(evaluacion_id)

    cur.execute(query)

    rows = cur.fetchall()

    if not rows:
        return None
    
    questions = [dict(zip(keys,row)) for row in rows]

    questions_formated = []
    question_id_counter = questions[0]['pregunta_id']
    
    # Get max question id and max opcion id
    question_ids = [q['pregunta_id'] for q in questions]
    options_ids = [q['opcion_id'] for q in questions]
    question_id_max = max(question_ids)
    opcion_id_max = max(options_ids)

    options = []
    correct_option_id = -1
    for q in questions:
        if q['pregunta_id'] != question_id_counter:
            question['opciones'] = options
            question['opcion_correcta_id'] = correct_option_id
            questions_formated.append(question)
            options = []
            question_id_counter +=1

        question = {}
        question['pregunta_id'] = q['pregunta_id'] 
        question['texto_pregunta'] = q['texto_pregunta'] 
        question['materia_id'] = q['materia_id'] 
        options.append({'opcion_id': q['opcion_id'],'texto_opcion': q['texto_opcion']})

        if q['es_correcta']:
            correct_option_id = q['opcion_id']

        if q['pregunta_id'] == question_id_max and q['opcion_id'] == opcion_id_max:
            question['opciones'] = options
            question['opcion_correcta_id'] = correct_option_id
            questions_formated.append(question)
            options = []
            question_id_counter +=1

    return questions_formated

def save_student_answer(evaluation_id,question_id,selected_option_id):
    # Using UPSERT
    query = ("insert into respuestas_alumno(evaluacion_id,pregunta_id,opcion_id) "
    "values(%s,%s,%s) on conflict(evaluacion_id,pregunta_id) "
    "do update set opcion_id= EXCLUDED.opcion_id")

    try:
        cur.execute(query,(evaluation_id,question_id,selected_option_id))
        con.commit()
        return True
    except Exception:
        
        return False
