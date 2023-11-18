letters: list[str] = ['a', 'b', 'c', 'd', 'e']
numbers: list[int] = [1, 2, 3, 4, 5]
results = [(letters[i], numbers[i]) for i in range(len(letters))]
print(results)
