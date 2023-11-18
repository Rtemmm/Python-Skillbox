def addingNumbers(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    print("Сумма цифр числа: ", sum)


def finedMaxOfNumbers(number):
    max_numb = 0
    for numb in str(number):
        if int(numb) > max_numb:
            max_numb = int(numb)
    print(f"Самая большая цифра числа это {max_numb}")


def finedMinOfNumbers(number):
    min_numb = 10

    for numb in str(number):
        if int(numb) < min_numb:
            min_numb = int(numb)
    print(f"Самая маленькая цифра числа это {min_numb}")


N = int(input("Введите число (0 - Это выход): "))
while N != 0:
    action = int(input("Введите номер действия:\n1) Сумма цифр\n2) Максимальная из цифр\n3) Минимальная из цифр\n"))
    if action == 1:
        addingNumbers(N)
    elif action == 2:
        finedMaxOfNumbers(N)
    elif action == 3:
        finedMinOfNumbers(N)
    else:
        print("Неверное действие")
    N = int(input("Введите число (0 - Это выход): "))
