names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

print("Первый день: ", end="")
for i in range(0, len(names), 2):
    print(names[i], end=" ")