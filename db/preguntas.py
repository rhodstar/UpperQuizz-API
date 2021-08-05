import psycopg2
import os
from dotenv import load_dotenv
from faker import Faker
from random import randint

load_dotenv()

DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

con = psycopg2.connect(database=DATABASE,user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD)

cur = con.cursor()

fake = Faker()

num_exams = 10
num_subjects = 10
num_questions = 5
num_options = 4
initial_preg_id = 549

queryPregunta = ("insert into pregunta(examen_id,materia_id,texto_pregunta)"
        "values(%s,%s,%s)")

queryOpcion = ("insert into opcion(texto_opcion,pregunta_id,es_correcta)"
        "values(%s,%s,%s)")

for examen_id  in range(1,num_exams+1):
    for nsubject in range(1,num_subjects+1):
        for npreg in range(initial_preg_id,initial_preg_id + num_questions):
            pregunta = fake.text()
            opciones = [ fake.sentence() for _ in range(0,num_options) ]
            
            try:
                cur.execute(queryPregunta,(examen_id,nsubject,pregunta))
                print(cur.statusmessage)

                rand_correct = randint(1,num_options)

                for i in range(0,len(opciones)):
                    if rand_correct == i+1:
                        cur.execute(queryOpcion,(opciones[i],npreg,True))
                    else:
                        cur.execute(queryOpcion,(opciones[i],npreg,False))
                    print(cur.statusmessage)

                con.commit()

            except Exception:
                print("No se pudo insertar el dato")
