from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.power = power
        self.name = name

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        day = 0
        while enemies > 0:
            sleep(1)
            enemies -= self.power
            day += 1
            print(f"{self.name}, сражается {day} день(дня)..., осталось {enemies} войнов!\n")

        print(f"{self.name}, одержал победу за {day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")