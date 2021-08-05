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

queryOpcion = (
    "insert into "
    "evaluacion_alumno(num_intento,status_evaluacion_id,alumno_id,examen_id) "
    "values(%s,%s,%s,%s)"
)


# exam_ids = [randint(1,10) for _ in range(3)]
exam_ids = [1,3,5]

for i in exam_ids:
    cur.execute(queryOpcion,(0,3,1,i))
    print(cur.statusmessage)
    con.commit();
