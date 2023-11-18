n = int(input("Введите количество чисел в последовательности: "))
count = 0
for i in range(n):
    numb = int(input("Введите число: "))
    k = 0
    for i in range(2, numb // 2 + 1):
        if numb % i == 0:
            k = k + 1
    if k <= 0:
        count += 1
    else:
        count = count
print(f"Количество простых чисел в последовательности: {count}")
