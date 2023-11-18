message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
result = ""

char_list = [(alphabet[(alphabet.index(char) + offset) % 33] if char != " " else " ") for char in message]

for char in char_list:
    result += char

print(result)
