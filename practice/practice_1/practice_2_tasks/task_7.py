number = int(input("Введите число: "))
digit1 = number // 1000
digit2 = number % 1000 // 100
digit3 = number // 10 % 10
digit4 = number % 10
print(digit1, digit2, digit3, digit4)
