# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras as extras

class CargaMasiva():
    
    con = ""
    debug = False
    def __init__(self, databaseURL, debug=False):
        self.con = psycopg2.connect(databaseURL)
        self.debug = debug
        print("Connected!")
    
    def close_conexion(self):
        self.con.close()
        print("Close Connection!")
            
    def charge_question_batch(self, tuples):
        min = 0; max,aux = len(tuples),len(tuples)
        query = "INSERT INTO pregunta(pregunta_id,texto_pregunta,materia_id, examen_id) VALUES (%s,%s, %s, %s)"        
        cursor = self.con.cursor()
        print("Charge Question!")
        while aux >=100:
            extras.execute_batch(cursor, query, tuples[min:min+100], page_size=100)
            min = min +100
            aux = aux -100
            print(min)
        if aux <100:
            extras.execute_batch(cursor, query, tuples[min:max], page_size=100)
            print(min, max)
        cursor.close()
        self.con.commit()

    def charge_option_batch(self, tuples):
        min = 0; max,aux = len(tuples),len(tuples)
        cursor = self.con.cursor()
        query = "INSERT INTO opcion(pregunta_id,texto_opcion, es_correcta) VALUES (%s, %s, %s)"        
        print("Charge Option!")
        while aux >=100:
            extras.execute_batch(cursor, query, tuples[min:min+100], page_size=100)
            min = min +100
            aux = aux -100
            print(min)
        if aux <100:
            extras.execute_batch(cursor, query, tuples[min:max], page_size=100)
            print(min, max)
        cursor.close()
        self.con.commit()
        
    def delete(self,question = True, option=True):
        queryOpcion = "DELETE FROM opcion"
        queryQuestion = "DELETE FROM pregunta"
        cursor = self.con.cursor()
        if question == True:
            cursor.execute(queryOpcion)
            print("Delete from opcion")
        if question == True:
            cursor.execute(queryQuestion)
            print("Delete from pregunta")
        cursor.close()
        self.con.commit()        
        