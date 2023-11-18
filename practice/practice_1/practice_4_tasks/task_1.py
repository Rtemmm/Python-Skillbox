point = int(input("Введите количество опыта: "))
if point < 1000:
    print("Ваш уровень: 1")
elif point < 2500:
    level = point // 1000
    print("Ваш уровень: ", level)
elif point < 5000:
    level = point // 1000
    print("Ваш уровень: ", level)
else:
    print("Ваш уровень: 4")
