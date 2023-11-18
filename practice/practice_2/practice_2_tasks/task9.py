listed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in listed:
    if i % 2 == 0:
        listed.remove(i)

for i in range(len(listed)):
    for j in range(i, len(listed)):
        if listed[i] < listed[j]:
            listed[i], listed[j] = listed[j], listed[i]

print(listed)
