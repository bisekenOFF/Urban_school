from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
time_end = datetime.now()
time_res = time_end - time_start
print(f"Время записи: {time_res}")

time_start1 = datetime.now()
file_5 = Thread(target=write_words, args=(10, "example5.txt"))
file_6 = Thread(target=write_words, args=(30, "example6.txt"))
file_7 = Thread(target=write_words, args=(200, "example7.txt"))
file_8 = Thread(target=write_words, args=(100, "example8.txt"))

file_5.start()
file_6.start()
file_7.start()
file_8.start()

file_5.join()
file_6.join()
file_7.join()
file_8.join()

time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(f"Время записи: {time_res1}")
