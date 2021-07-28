from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

app = Flask(__name__)

CORS(app)

try: 
    con = psycopg2.connect(database=DATABASE,user=DATABASE_USERNAME,
            password=DATABASE_PASSWORD)

    cur = con.cursor()

    @app.route("/")
    def hello_world():
        cur.execute('select * from examen')
        rows = cur.fetchall()
        
        return jsonify(rows)

except:
    print("There was an error while connecting to DB")

