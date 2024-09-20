import math


class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides: int):
        self.__sides = sides
        for c in color:
            if c < 0:
                print("цвет имеет отрицательное значение")
                exit()
        self.__color = list(color)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *in_sides):
        if len(in_sides) != len(self.__sides):
            return False
        for side in in_sides:
            if side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        p_figure = 0
        for side in self.__sides:
            p_figure += side
        return p_figure

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, [sides])
        self.__radius = sides

    def get_square(self):
        return 3.14 * (self.__radius[0] ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        p = 0.5 * (sum(self.__sides))
        s = math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, [sides] * 12)

    def get_volume(self):
        r = self.get_sides()[0]
        return r[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
