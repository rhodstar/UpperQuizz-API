#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Connector import Connector

db = Connector()

def get_user_by_id(id):
    cols = ['alumno_id','nombre','apellidos','correo','contrasena']
    query = db.simple_query_builder(cols,"alumno",["alumno_id={}".format(id)])

    return db.pull(query,"fetchone")

def get_user_by_email(email):
    cols = ['alumno_id','nombre','apellidos','correo','contrasena']

    query = db.simple_query_builder(cols,"alumno",["correo='{}'".format(email)])

    return db.pull(query,"fetchone")

def save_user(user):
    cols = ["nombre","apellidos","correo","contrasena"]
    query = db.insertion_builder(cols,"alumno")

    params = tuple([ user[col] for col in cols ])

    return db.push(query,params)

def get_user_evaluations(user):
    examen = {
        "table_name": "examen", 
        "alias": "e",
        "fields": ["examen_id","nombre"]
    }
    status_evaluacion = {
        "table_name": "status_evaluacion", 
        "alias": "se",
        "fields": ["nombre"]
    }
    evaluacion_alumno = {
        "table_name": "evaluacion_alumno", 
        "alias": "ea",
        "fields": ["aciertos_totales","num_intento"]
    }

    entities = [examen,status_evaluacion,evaluacion_alumno]
    join_conditions = ["e.examen_id=ea.examen_id",
        "ea.status_evaluacion_id=se.status_evaluacion_id"]
    conditions = ["ea.alumno_id={}".format(user['alumno_id'])]

    query = db.compound_query_builder(entities,join_conditions,conditions)

    res = db.pull(query)

    if res:
        res_dict = []
        for r in res:
            item_dict = {}
            item_dict['examen_id'] = r['examen_id']  
            item_dict['status'] = r['nombre']
            item_dict['aciertos_totales'] = r['aciertos_totales']
            item_dict['num_intento'] = r['num_intento']
            res_dict.append(item_dict)
        return res_dict
    else:
        return []


def get_evaluation_by_id(evaluation_id):
    pregunta = {
        "table_name":"pregunta",
        "alias": "p",
        "fields": ["pregunta_id","texto_pregunta","materia_id"]
    }
    opcion = {
        "table_name":"opcion",
        "alias": "o",
        "fields": ["opcion_id","texto_opcion","es_correcta"]
    }
    entities = [pregunta,opcion]
    join_conditions = ["p.pregunta_id=o.pregunta_id"]
    conditions = ["p.examen_id=({})".format(db.simple_query_builder(
        ["examen_id"],"evaluacion_alumno",
        ["evaluacion_id={}".format(evaluation_id)]
    ))]

    other="order by p.pregunta_id"

    query = db.compound_query_builder(entities,join_conditions,conditions,other)
    questions = db.pull(query)

    if not questions:
        return []

    questions_formated = []
    question_id_counter = questions[0]['pregunta_id']
    
    # Get max question id and max opcion id
    question_id_max = max([q['pregunta_id'] for q in questions])
    opcion_id_max = max([q['opcion_id'] for q in questions])

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

    cols = ["evaluacion_id","pregunta_id","opcion_id"]
    # Using UPSERT
    other = ("on conflict(evaluacion_id,pregunta_id) do update "
    "set opcion_id=EXCLUDED.opcion_id")
    query = db.insertion_builder(cols,"respuestas_alumno",other)

    return db.push(query,(evaluation_id,question_id,selected_option_id))

def save_student_scores(evaluation_id,scores):
    total_score = scores['aciertos_totales']
    aplication_date = scores['fecha_aplicacion']
    subject_scores = scores['puntaje_materia']

    values = {
        "aciertos_totales": total_score,
        "fecha_aplicacion": "'{}'".format(aplication_date),
        "status_evaluacion_id": 2,
        "num_intento": "num_intento+1"
    }

    query = db.update_builder("evaluacion_alumno",values,
        ["evaluacion_id={}".format(evaluation_id)])

    if db.push(query):
        cols = ["evaluacion_id","materia_id","puntaje"]
        query_scores = db.simple_query_builder(cols,"puntaje_materia")
        
        for subject in subject_scores:
            params = (evaluation_id,subject["materia_id"],subject["puntaje"])
            if not db.push(query_scores,params):
                return False

        return True
    else:
        return False

def get_evaluation_history(student_id):
    evaluacion_alumno = {
        "table_name":"evaluacion_alumno",
        "alias": "ea",
        "fields": ["evaluacion_id","aciertos_totales","fecha_aplicacion"]
    }

    examen = {
        "table_name":"examen",
        "alias": "e",
        "fields": ["nombre"]
    }

    entities = [evaluacion_alumno,examen]
    join_conditions = ["e.examen_id=ea.examen_id"]
    conditions = ["alumno_id={}".format(student_id),"status_evaluacion_id=2"]
    query = db.compound_query_builder(entities,join_conditions,conditions)

    res = db.pull(query)
    if res:
        res_dict = []
        for r in res:
            item_dict = {}
            item_dict['evaluacion_id'] = r['evaluacion_id']  
            item_dict['nombre_examen'] = r['nombre']
            item_dict['aciertos_totales'] = r['aciertos_totales']
            item_dict['fecha_aplicacion'] = r['fecha_aplicacion']
            res_dict.append(item_dict)
        return res_dict
    else:
        return []


def get_evaluation_history_by_id(student_id,evaluation_id):

    evaluacion_alumno = {
        "table_name": "evaluacion_alumno",
        "alias": "ea",
        "fields": ["aciertos_totales","fecha_aplicacion","num_intento"]
    }

    puntaje_materia = {
        "table_name": "puntaje_materia",
        "alias": "pm",
        "fields": ["materia_id","puntaje"]
    }
    materia = {
        "table_name": "materia",
        "alias": "m",
        "fields": ["nombre"]
    }

    entities = [evaluacion_alumno,puntaje_materia,materia]
    join_conditions = ["ea.evaluacion_id=pm.evaluacion_id","m.materia_id=pm.materia_id"]
    conditions = ["ea.evaluacion_id={}".format(evaluation_id)]

    query = db.compound_query_builder(entities,join_conditions,conditions)
    res = db.pull(query)

    if not res:
        return {}

    history = []
    for r in res:
        item_dict = {}
        item_dict['aciertos_totales'] = r['aciertos_totales']  
        item_dict['fecha_aplicacion'] = r['fecha_aplicacion']
        item_dict['num_intento'] = r['num_intento']
        item_dict['materia_id'] = r['materia_id']
        item_dict['puntaje'] = r['puntaje']
        item_dict['nombre_materia'] = r['nombre']
        history.append(item_dict)

    aciertos_totales = history[0]['aciertos_totales']
    fecha_aplicacion = history[0]['fecha_aplicacion']
    num_intento = history[0]['num_intento']

    puntaje_materia = [{
        "materia_id":row["materia_id"],
        "nombre_materia":row["nombre_materia"],
        "puntaje":row["puntaje"]
    } for row in history]

    history_formated = {
        "evaluacion_id": evaluation_id,
        "aciertos_totales":aciertos_totales,
        "num_intento":num_intento,
        "puntaje_materia":puntaje_materia
    }

    return history_formated
