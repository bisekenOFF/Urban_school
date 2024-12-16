import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()

#инициализация таблиц
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

initiate_db()

#добавление товара
def add_product(title,description,price):
    check_product = cursor.execute("SELECT * FROM products WHERE title = ?",(title,))
    if check_product.fetchone() is None:
        cursor.execute('''
           INSERT INTO products(title,description,price)
           VALUES(?,?,?)
           ''', (title, description, price))
    connection.commit()

#вывод всех товаров
def get_all_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

#Добавление пользователя
def add_user(username, email, age, balance):
    if is_included(username).fetchone() is None:
        cursor.execute('''
                INSERT INTO users(username,email,age,balance)
                VALUES(?,?,?,?)
                ''', (username, email, age, balance))
    connection.commit()

#проверка существования пользователя
def is_included(username):
    user = cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return user

add_user('user1','user1@gmail.com',20,1000)

connection.commit()
