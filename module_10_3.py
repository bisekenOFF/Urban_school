import threading
from threading import Thread, Lock
import random
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            num = random.randint(50, 500)
            self.balance = self.balance + num
            print(f"Пополнение: {num}. Баланс: {self.balance}\n")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):

        for i in range(100):
            num = random.randint(50, 500)
            print(f"Запрос на {num}")
            if num <= self.balance:
                self.balance = self.balance - num
                print(f"Снятие: {num}. Текущий Баланс: {self.balance}\n")
            else:
                print("Запрос отклонен. Недостаточно средств\n")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
