listed = [1, 4, -3, 0, 10]

for i in range(len(listed)):
    for j in range(i, len(listed)):
        if listed[i] > listed[j]:
            listed[i], listed[j] = listed[j], listed[i]

print(listed)
