import random

first_num = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = random.choice(first_num)
result = []
for i in range(n):
    for j in range(n):
        if i != 0 and j != 0 and i != j:
            if n % (i+j) == 0:
                result.append([i,j])
        else:
            continue

for a,b in result:
    for c,d in result:
        if a == d and b == c:
            result.remove([c,d])
        else:
            continue

print(f'Первое число: {n}')
print("Второе число: ", end = '')
for i,j in result:
    print(i, end = '')
    print(j, end = '')

