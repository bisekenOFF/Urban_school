import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Users (
               id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER,
               balance INTEGER NOT NULL
               )
               ''')

cursor.execute(" CREATE INDEX IF NOT EXISTS username_index ON Users (username) ")

#Добавление юзеров
#for i in range(10):
#    cursor.execute('''INSERT INTO Users (username, email, age, balance)
#                    VALUES (?, ?, ?, ?)''', (f"user{i+1}", f"example{i+1}@gamil.com", f"{(i+1)*10}", "1000"))

#Обновление кажого 2го юзера начиная с 1го на 500
#for i in range(10):
#    if i % 2 != 0:
#        cursor.execute('''UPDATE Users SET balance = ? WHERE username = ?''', (500, f"user{i}"))

#Удаление каждгого треьего
#for i in range(1,10,3):
#    cursor.execute('''DELETE FROM Users WHERE username = ?''', (f"user{i}",))

#Получение всех юзеров у когорых возраст не 60
#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
#users = cursor.fetchall()
#for user in users:
#    print(user)

#Удаление юзера с ИД=6
#cursor.execute('''DELETE FROM Users WHERE id = ?''', (6,))

#Сколбко всего записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_u = cursor.fetchone()[0]
print(total_u)

#Сумма всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
total_b = cursor.fetchone()[0]
print(total_b)

#Средний баланс всех юзеров
avg_balance = total_b / total_u
print(avg_balance)




connection.commit()
connection.close()