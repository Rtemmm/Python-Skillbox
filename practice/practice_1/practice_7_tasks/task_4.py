a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))
c = int(input("Введите число, на которое должны делиться числа из отрезка: "))
sum = 0
count = 0
for i in range(a, b + 1):
    if i % c == 0:
        sum += i
        count += 1
if count > 0:
    print("Среднее арифметическое чисел из отрезка [a; b], кратных c: ", sum / count)
else:
    print("В данном отрезке нет чисел, кратных c.")
