n = int(input("Количество человек: "))
dropout = int(input("Какое число в считалке? ")) - 1

print(f"Значит, выбывает каждый {dropout}-й человек")

circle = list(range(1, n + 1))
index = 0
first = True

while len(circle) > 1:
    print(f"\nТекущий круг людей: {circle}")
    index = (index + dropout) % len(circle)
    print(f"Выбывает человек под номером: {circle.pop(index)}")

print(f"\nОстался человек под номером {circle[0]}")
