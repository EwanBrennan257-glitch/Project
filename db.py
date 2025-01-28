from flask import current_app,g
import sqlite3
import click
import os

from Model.User import User
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE=os.path.join(BASE_DIR, 'Ecommerce.db')

@click.command("initdb")
def initdb():
    #to intialise database run flask initdb
    with current_app.open_resource('database.sql') as f:
        get_db().executescript(f.read().decode("utf-8"))
    click.echo("Initializing")

def insert_user(firstname, lastname, email, password, is_admin, is_active):
    mydb=get_db()
    mydb.execute("""INSERT INTO User(firstname, lastname, email, password, is_admin, is_active) VALUES (?,?,?,?,?,?)""",
                 (firstname, lastname, email, password, is_admin, is_active))
    mydb.commit()

def select_user(email, password):
    mydb=get_db()
    row=mydb.execute("""SELECT id, firstname, lastname, email, password, is_admin, is_active FROM User WHERE email = ?""",
                 (email,)).fetchone()
    if row:
        user=User(id=row[0], firstname=row[1], lastname=row[2], email=row[3], password=row[4], is_admin=row[5], is_active=row[6])
        return user

def select_user_by_email(email):
    mydb=get_db()
    row=mydb.execute("""SELECT id, firstname, lastname, email, password, is_admin, is_active FROM User WHERE email = ?""",
                 (email,)).fetchone()
    if row:
        user=User(id=row[0], firstname=row[1], lastname=row[2], email=row[3], password=row[4], is_admin=row[5], is_active=row[6])
        return user

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db