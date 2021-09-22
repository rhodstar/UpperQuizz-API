# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras as extras

class CargaMasiva():
    
    con = ""
    
    def __init__(self, databaseURL):
        #self.con = psycopg2.connect(databaseURL)
        print()
    
    def close_conexion(self):
        #self.con.close()
        print()
            
    def carga_pregunta_bacth(self, tuples):
        min = 0; max,aux = len(tuples),len(tuples)
        query = "INSERT INTO pregunta(texto_pregunta,materia_id, examen_id) VALUES (%s, %s, %s)"        
        #cursor = self.con.cursor()
        while aux >=100:
            #extras.execute_batch(cursor, query, tuples[min:min+100], page_size=100)
            min = min +100
            aux = aux -100
            print(min)
        if aux <100:
            #extras.execute_batch(cursor, query, tuples[min:max], page_size=100)
            print(min, max)
        #cursor.close()
        #self.con.commit()

    def carga_option_bacth(self, tuples):
        min = 0; max,aux = len(tuples),len(tuples)
        print(aux)
        #cursor = self.con.cursor()
        query = "INSERT INTO opcion(texto_opcion,pregunta_id, es_correcta) VALUES (%s, %s, %s)"        
        while aux >=100:
            #extras.execute_batch(cursor, query, tuples[min:min+100], page_size=100)
            min = min +100
            aux = aux -100
            print(min)
        if aux <100:
            #extras.execute_batch(cursor, query, tuples[min:max], page_size=100)
            print(min, max)
        #cursor.close()
        #self.con.commit()