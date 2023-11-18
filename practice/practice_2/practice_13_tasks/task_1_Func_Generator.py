def square_generator(max_value):
    current_value = 0
    while current_value < max_value:
        yield current_value ** 2
        current_value += 1


N = int(input("Введите число N: "))

for number in square_generator(N):
    print(number)
