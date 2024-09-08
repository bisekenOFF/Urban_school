class House:
    # Атрибут класса для хранения истории созданных объектов
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Создание нового объекта
        instance = super(House, cls).__new__(cls)
        # Добавление названия объекта в историю
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, floors):
        # Атрибуты объекта
        self.name = name
        self.floors = floors

    def __del__(self):
        # Вывод сообщения при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# Удаление последнего объекта
del h1
