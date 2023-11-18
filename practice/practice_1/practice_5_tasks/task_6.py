X = float(input("Введите начальный вклад: "))
Y = float(input("Введите желаемую сумму: "))
P = float(input("Введите процент: "))
years = 0
while X < Y:
    X += X * P / 100
    X = int(X * 100) / 100
    years += 1
print(f"Вклад достигнет желаемой суммы через {years} лет.")
