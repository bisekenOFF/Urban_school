
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = "root", b = 33, c = False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'строка', True]
print_params(*values_list)

values_dict = {'a': 20,
               'b': 'Имя',
               'c': 'Фамилия'}
print_params(**values_dict)

values_list2 = [54.32, 'string']
print_params(*values_list2,42)