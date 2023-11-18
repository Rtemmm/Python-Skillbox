import random

original = [random.randint(0, 100) for x in range(10)]
pairs = []

for i in range(0, len(original) - 1, 2):
    pairs.append((original[i], original[i + 1]))

print(pairs)

pairs = []
pairs = [(original[x], original[x + 1]) for x in range(0, len(original) - 1, 2)]

print(pairs)

pairs = []

for index, item in enumerate(original):
    if index == len(original) - 3:
        break
    pairs.append((original[index + 2], original[index + 3]))

print(pairs)
