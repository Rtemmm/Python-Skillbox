n = int(input("Количество роликов: "))
rollersSizes = []

for i in range(n):
    rollersSizes.append(int(input(f"Размер пары {i + 1}: ")))

print()
n = int(input("Количество людей: "))

humansSizes = []

for i in range(n):
    humansSizes.append(int(input(f"Размер пары {i + 1}: ")))

for i in range(len(rollersSizes)):
    if rollersSizes[i] in humansSizes:
        humansSizes[humansSizes.index(rollersSizes[i])], rollersSizes[i] = -1, -1

print("Наибольшее количество людей, которые могут взять ролики:", rollersSizes.count(-1))