first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(x) - len(y) for x,y in zip(first, second) if len(x) != len(y)]
print(first_result)

second_result = [True if len(first[x]) == len(second[x]) else False for x in range(len(first))]
print(second_result)