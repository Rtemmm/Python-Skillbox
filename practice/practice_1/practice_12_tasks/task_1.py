def float_point(n):
    k = 0
    while n >= 10:
        n /= 10
        k += 1
    print(f'Формат плавающей точки: х = ', n, ' * 10 ** ', k)


def float_biggestThen10(n):
    k = 0
    while n < 1:
        n *= 10
        k -= 1
    print(f'Формат плавающей точки: х = ', round(n, 1), ' * 10 ** ', k)


n = float(input('Введите число: '))
if n >= 10:
    float_point(n)
elif n < 1:
    float_biggestThen10(n)
