#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

with open("00-ddl.sql", "r") as f:
    query = f.read()

    conn = psycopg2.connect(DATABASE_URL)
    with conn:
        with conn.cursor() as curs:
            curs.execute(query)

