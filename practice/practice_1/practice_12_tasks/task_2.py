def maximum_of_two(a, b):
    return a if a > b else b


def maximum_of_three(a, b, c):
    return maximum_of_two(a, maximum_of_two(b, c))


numb1 = int(input("Введите число: "))
numb2 = int(input("Введите число: "))
numb3 = int(input("Введите число: "))
print(f'Наибольшее число: {maximum_of_three(numb1, numb2, numb3)}')
