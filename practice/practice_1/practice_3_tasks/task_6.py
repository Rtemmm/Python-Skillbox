cub1 = int(input("Кубик Кости: "))
cub2 = int(input("Кубик владельца: "))
sum = cub1 + cub2
if cub1 >= cub2:
    print("Игрок платит", sum)
else:
    print("Владелец платит", sum)
print("Игра окончена")
