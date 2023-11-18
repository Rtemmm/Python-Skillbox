text = input("Введите текст: ")
k = 0
maxLength = 0
for str in text:
    if str != ' ':
        k += 1
        maxLength = max(k, maxLength);
    else:
        k = 1
print(f'Самое длинное слово: {maxLength} букв')
