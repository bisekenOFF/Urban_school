# 1st program
print((9**0.5)*5)

# 2nd program
if 9.99 > 9.98 and 1000 != 1000.1:
    print (True)
else:
    print (False)

# 3rd program
a = 1234
b = 5678
a1 = (a//10) % 100;
b1 = (b//10) % 100;
print (a1+b1)

# 4th program
c = 13.42
d = 42.13
c1 = round((c % 1) * 100)
d1 = round((d % 1) * 100)

if (int(c)) == (d1) or (int(d)) == (c1):
    print (True)
else: print(False)

# есть проблема: код будет корректно работать только с числами "c" и "d" у которых два знака после точки.
# Пример: если число с = 13.421, то с1 будет все равно равняться 42.