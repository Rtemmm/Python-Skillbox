N = int(input("Введите число N: "))

for number in (value ** 2 for value in range(1, N + 1)):
    print(number)
