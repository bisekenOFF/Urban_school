def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        div = 0
        for i in range(2, num):
            if num % i == 0:
                div += 1
        if div == 0:
            print("Простое число")
        else:
            print("Составное число")
        return num

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
