text = input("Введите текст: ")
vowels = "уеыаоэяиюУЕЫАОЭЯИЮ"

answer = set([x for x in text if x in vowels])

print(answer, len(answer))
