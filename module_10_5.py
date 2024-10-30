from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    alldata = []
    with open(name) as f:
        for line in f:
            alldata.append(line.strip())


def leaner(list_files):
    time_start = datetime.now()
    for file in list_files:
        read_info(file)
    time_end = datetime.now()
    time_result = time_end - time_start
    print(f'{time_result} - Линейный')


def multi(list_files):
    time_start1 = datetime.now()
    with Pool() as pool:
            pool.map(read_info, list_files)
    time_end1 = datetime.now()
    time_result1 = time_end1 - time_start1
    print(f'{time_result1} - Многопоточный')


if __name__ == '__main__':
    list_files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
    leaner(list_files)
    multi(list_files)
