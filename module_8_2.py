def personal_sum(numbers):
    sum = 0
    incorrect_data = 0
    for number in numbers:
        try:
            sum += number
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы -{number}")
            incorrect_data += 1
    result = (sum, incorrect_data)
    return result


def calculate_average(numbers):
    numbers_len = 0
    try:
        for number in numbers:
            if type(number) == int:
                numbers_len += 1
    except TypeError:
        print("В numbers записан неккоректный тип данных")
        return None

    try:
        return personal_sum(numbers)[0] / numbers_len
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать