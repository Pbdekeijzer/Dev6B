import sqlite3
import sys

def open_conn():    
    try:
        conn = sqlite3.connect('db.sqlite3')
        print("connected")
    except:
        print("tried")

def close_conn():
    conn.close()
    print('closed connection')

def create_user():
    print("Creating new user")
