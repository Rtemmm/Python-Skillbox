N = int(input("Введите количество чисел: "))
maxk = 0
maxNumber = 0
for i in range(N):
    k = 0
    numb = int(input("Введите число:"))
    for i in str(numb):
        k += int(i)
    if k > maxk:
        maxk = k
        maxNumber = numb
print(f"Число с наибольшей суммой цифр: {maxNumber}")
print(f"Сумма его цифр: {maxk}")
