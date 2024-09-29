def add_everything_up(a, b):
    try:
        c = a + b
        c_r = round(c, 3)
        return c_r
    except TypeError as ext:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
