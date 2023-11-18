N = int(input("Введите количество учеников: "))
excellent = 0
good = 0
satisfactory = 0
for i in range(1, N):
    grade = int(input("Введите отметку: "))
    if grade == 5:
        excellent += 1
    elif grade == 4:
        good += 1
    elif grade == 3:
        satisfactory += 1
if excellent > good and excellent > satisfactory:
    print("Сегодня больше всего отличников")
elif good > excellent and good > satisfactory:
    print("Сегодня больше всего хорошистов")
else:
    print("Сегодня больше всего троечников")
