workHours = int(input("Введите отработанные часы: "))
remainingCredit = int(input("Введите остаток по кредиту: "))
costOfEat = int(input("Введите траты на еду: "))
if workHours * 200 / 2 ** 3 + workHours >= remainingCredit + costOfEat:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать больше!")
