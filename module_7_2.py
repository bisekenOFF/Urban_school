from pprint import pprint

def custom_write(file_name, strings):
    name = file_name
    string_position = {}
    i = 1
    file = open(name, 'w', encoding='utf-8')
    for st in strings:
        tell = file.tell()
        kor = (i, tell)
        i += 1
        string_position[kor] = st
        file.write(f'{st}\n')
    file.close()

    file = open(name, 'r', encoding='utf-8')
    file.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('simple.txt', info)
for elem in result.items():
    print(elem)
