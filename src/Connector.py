#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
import os

from dotenv import load_dotenv
load_dotenv()
DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

DATABASE_URL = os.environ.get('DATABASE_URL')

class Connector:

    def __init__(self):
        self.con = psycopg2.connect(database=DATABASE,user=DATABASE_USERNAME,
            password=DATABASE_PASSWORD)
        # self.con = psycopg2.connect(DATABASE_URL)

    def pull(self,query,fetch_type="fetchall"):
        with self.con:
            cur = self.con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cur.execute(query)
            row = None
            if fetch_type == "fetchall":
                row = cur.fetchall()
            elif fetch_type == "fetchone":
                row = cur.fetchone()
            cur.close()

            return row

    def push(self,query,params=()):
        with self.con:
            cur = self.con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            try:
                if len(params) > 0:
                    cur.execute(query,params)
                else:
                    cur.execute(query)
                self.con.commit()
                return True
            except:
                return False
            finally:
                cur.close()

    def simple_query_builder(self,cols,table,conditions):
        query = "select {} from {}".format(",".join(cols),table)

        if len(conditions) > 0:
            query += " where {}".format(" and ".join(conditions))

        return query

    def compound_query_builder(self,entities,join_conditions,conditions=[],other=""):
        
        tables = []
        formated_cols = []
        for e in entities:
            tables.append("{} {}".format(e['table_name'],e['alias']))
            formated_cols += ["{}.{}".format(e['alias'],field) for field in e['fields']]

        query = "select {} from {} where {} and {} {}".format(
            ",".join(formated_cols),
            ",".join(tables),
            " and ".join(join_conditions),
            " and ".join(conditions),
            other
        )

        return query

    def insertion_builder(self,cols,table,other=""):
        query = "insert into {}({}) values({}) {}".format(
            table,",".join(cols),",".join(["%s"]*len(cols)),other)

        return query

    def update_builder(self,table,values,conditions):
        values_formated = ["{}={}".format(key,value) for key, value in values.items()]
        query = "update {} set {} where {}".format(table, 
            ",".join(values_formated),",".join(conditions))

        return query

    def delete_builder(self,table,conditions):
        return "delete from {} where {}".format(table," and ".join(conditions))
