start = int(input("Начало отрезка: "))
end = int(input("Конец отрезка: "))
step = int(input("Шаг(отрицательный): "))
for x in range(end, start - 1, step):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print(f"Значение функции в точке {x} равно {y}")
