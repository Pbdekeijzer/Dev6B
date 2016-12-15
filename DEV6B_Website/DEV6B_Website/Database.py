import sqlite3
import sys

def Execute_Query(query):
    try:
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute(query)
        ret = c.fetchall()
        conn.commit()
        conn.close()
        return ret
    except:
        print("Execute failed!")
        return 400