class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
            self.data[username] = password

class User:
    """
    Класс пользователя содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

def contains_num(string): #проверка на наличие числа
    return any(char.isdigit() for char in string)

def contains_uppercase(string): #проверка на наличие большой буквы
    return any(char.isupper() for char in string)

if __name__ == '__main__' :
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход \n2 - Регистрация \n"))
        if choice == 1:
            login = input("Введите логин")
            password = input("Введите пароль")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен, {login}!")
                    break
                else:
                    print("Неверный пароль!")
            else:
                print("Пользователь не найден!")

        if choice == 2:
            user = User(input("Введите логин: "), password1 := input("Введите пароль: "), password2 := input("Повторите пароль: "))
            if password1 != password2:
                print("пароли не совпадают")
                continue
            elif len(password1) < 8:
                print("пароль меньше 8 знаков")
                continue
            elif contains_num(password1) == False:
                print("пароль содержит цифр")
                continue
            elif contains_uppercase(password1) == False:
                print("пароль содержит больших букв")
                continue
            database.add_user(user.username, user.password)

        #print(database.data)