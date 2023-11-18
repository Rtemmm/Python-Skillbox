ghostNumber = int(input("Загадывайте число от 0 до 10: "))
guessNumber = int(input("Введите число: "))
count = 0
while ghostNumber != guessNumber:
    if guessNumber < ghostNumber:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    count += 1
    guessNumber = int(input("Введите число: "))
print("Вы угадали! Число попыток:  ", count)
