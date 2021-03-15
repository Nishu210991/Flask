import mysql.connector

import json

with open('config.json', 'r') as c:
    config=json.load(c)["params"]

def mysql_db():
    db = mysql.connector.connect(
        host=config['host'],
        user=config['database_user'],
        password="", database=config['database_name'])
    return db

def add_contact(sql, val):
    db = mysql_db()
    cur = db.cursor()
    cur.execute(sql, val)
    db.commit()

def get_contact():
    sql="Select * from contacts"
    db = mysql_db()
    cur = db.cursor()
    cur.execute(sql)
    return cur.fetchall()

def delete_contact(id):
    sql=f"DELETE FROM contacts WHERE sno = {id}"
    db = mysql_db()
    cur = db.cursor()
    cur.execute(sql)

