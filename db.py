from flask import current_app,g
import sqlite3
import click
import os

from Model.User import UserRead, User
from Model.Product import ProductRead, ProductTypeRead

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
        user=UserRead(id=row[0], firstname=row[1], lastname=row[2], email=row[3], password=row[4], is_admin=row[5], is_active=row[6])
        return user

def select_user_by_email(email):
    mydb=get_db()
    row=mydb.execute("""SELECT id, firstname, lastname, email, password, is_admin, is_active FROM User WHERE email = ?""",
                 (email,)).fetchone()
    if row:
        user=UserRead(id=row[0], firstname=row[1], lastname=row[2], email=row[3], password=row[4], is_admin=row[5], is_active=row[6])
        return user

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def create_product(name, description, stock, price, imageurl, created_by,
                   product_type, created_at):
    mydb=get_db()
    mydb.execute("""INSERT INTO Product(name, description, stock, price, imageurl, created_by, product_type, created_at) VALUES(?,?,?,?,?,?,?,?)""",
                 (name, description, stock, price, imageurl, created_by, product_type, created_at))
    mydb.commit()

def create_producttype(name, material, size):
    mydb=get_db()
    with mydb:
        cursor=mydb.cursor()
        cursor.execute("""INSERT INTO ProductType(name, material, size) VALUES(?,?,?)""",
                 (name, material, size))
        lastrowid=cursor.lastrowid
        if lastrowid:
            return lastrowid

def select_products():
    mydb=get_db()
    rows=mydb.execute("""SELECT id, name, description, stock, price, imageurl, created_by, product_type, created_at FROM Product""").fetchall()
    products=[ProductRead(id=row[0],
                          name=row[1],
                          description=row[2],
                          stock=row[3],
                          price=row[4],
                          imageurl=row[5],
                          created_by=row[6],
                          product_type=row[7],
                          created_at=row[8]).to_dict() for row in rows]
    return products

def select_product_by_name(productname):
    mydb=get_db()
    row=mydb.execute("""SELECT id, name, description, stock, price, imageurl, created_by, product_type, created_at FROM Product WHERE name = ?""",
                     (productname,)).fetchone()
    if row:
        product_type_id=row[7]#row 7 contains product type id
        #it fetches product type from database by calling select product type by id function
        #we assign product type object to product_typeobject
        product_typeobject=select_product_type_by_id(product_type_id)
        product=ProductRead(id=row[0],
                     name=row[1],
                     description=row[2],
                     stock=row[3],
                     price=row[4],
                     imageurl=row[5],
                     created_by=row[6],
                     product_type=product_typeobject,#assign product type object to Product's product_type field
                     created_at=row[8]).to_dict()
        return product

def select_product_type_by_id(id):
    mydb = get_db()
    row=mydb.execute("""select id, name, material, size FROM ProductType WHERE id = ?"""
                     ,(id,)).fetchone()
    if row:
        producttype=ProductTypeRead(id=row[0],
                                    name=row[1],
                                    material=row[2],
                                    size=row[3]).to_dict()
        return producttype

def select_products_types():
    mydb=get_db()
    rows=mydb.execute("""SELECT id, name, material, size FROM ProductType""").fetchall()
    producttypes=[ProductTypeRead(id=row[0],
                                  name=row[1],
                                  material=row[2],
                                  size=row[3],
                                  ).to_dict() for row in rows]
    return producttypes
def update_product_type(id, name, material, size):
    mydb = get_db()
    row=mydb.execute("""UPDATE ProductType SET name = ?, material = ?, size = ? WHERE id =?""",
                     (name, material, size, id))
    mydb.commit()

def update_product(id, name, description, stock, price, imageurl, producttypeid, producttypename, producttypematerial, producttypesize):
    try:
        update_product_type(producttypeid, producttypename, producttypematerial, producttypesize)
        mydb = get_db()
        row=mydb.execute("""UPDATE Product SET name = ?, description = ?, stock = ?, price = ?, imageurl = ? WHERE id=?""",
                         (name, description, stock, price, imageurl, id))
        mydb.commit()
        return True
    except Exception as e:
        print(e)
        return False

def delete_product_by_name(name):
    try:
        mydb = get_db()
        row=mydb.execute("""DELETE FROM Product WHERE name = ?""",(name,))
        mydb.commit()
        return True
    except Exception as e:
        print(e)
        return False
