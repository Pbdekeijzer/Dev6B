import sqlite3
import sys

def Execute_Query(query):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()