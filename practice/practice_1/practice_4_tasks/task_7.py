time = int(input("Введите время в часах: "))
if 8 <= time < 10 or 12 < time < 14 or 15 < time < 18 or 20 < time <= 22:
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")
