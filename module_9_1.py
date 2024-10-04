def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        res = function(int_list)
        result[function.__name__] = res
    return result


print(apply_all_func([6, 20, 15, 9], min, max))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
