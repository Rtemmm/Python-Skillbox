n = int(input("Введите число: "))
res = []

for i in range(1, n + 1, 2):
    res.append(i)

print(f"Список из нечётных чисел от одного до N: {res}")
