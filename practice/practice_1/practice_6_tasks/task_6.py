for number in range(10, 100):
    numb1 = number // 10
    numb2 = number % 10
    if number == 3 * numb1 * numb2:
        print(number)
