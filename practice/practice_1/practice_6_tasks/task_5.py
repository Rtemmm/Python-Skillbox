a = int(input("Введите число: "))
b = int(input("Введите число: "))
summ = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        summ += i
        count += 1
if count > 0:
    print("Среднее арифметическое чисел, кратных 3, из отрезка [a; b]: ", summ / count)
else:
    print("В данном отрезке нет чисел, кратных 3.")
