def summa_n(n):
    summ = 0
    for x in range(n + 1):
        summ += x
    return summ


N = int(input("Введите число: "))
print(f"Я знаю, что сумма чисел от 1 до {N} равна {summa_n(N)}")
