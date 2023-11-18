n = int(input('Введите число: '))
if n < 0:
    c = 1
    k = -1
else:
    c = 0
    k = 0
while n != 0:
    n = int(input('Введите число: '))
    if n >= 0:
        k += 1
    else:
        c += 1
print("Кол-во положительных чисел: ", k)
print("Кол-во отрицательных чисел: ", c)
