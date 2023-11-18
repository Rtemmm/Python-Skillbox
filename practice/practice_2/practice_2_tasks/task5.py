n = int(input("Количество контейнеров: "))
listContainers = []

for i in range(n):
    weight = int(input("Введите вес контейнера: "))
    if weight > 200:
        continue

    listContainers.append(weight)

newContainer = int(input("Введите вес нового контейнера: "))
index = -1

for i in range(len(listContainers)):
    if newContainer > listContainers[i]:
        index = i + 1
        listContainers.insert(i, newContainer)
        break
