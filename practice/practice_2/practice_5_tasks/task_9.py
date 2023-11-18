def count_uppercase_lowercase(string):
    upper = 0
    lower = 0
    for i in string:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    return upper, lower


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)

print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
