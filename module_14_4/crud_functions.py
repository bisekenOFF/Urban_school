import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY,
title TEXT,
description TEXT,
price INTEGER NOT NULL
);
''')

def initiate_db(id_product, title,description,price):
    check_product = cursor.execute("SELECT * FROM products WHERE id = ?",(id_product,))
    if check_product.fetchone() is None:
        cursor.execute('''
        INSERT INTO products(id,title,description,price)
        VALUES(?,?,?,?)
        ''',(id_product,title,description,price))
    connection.commit()

def get_all_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()


connection.commit()
