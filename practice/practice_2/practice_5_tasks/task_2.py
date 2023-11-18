string_array = input("Введите строку: ").split(" ")
maxim = max(string_array, key=len)

print(f"Самое длинное слово: «{maxim}»\nДлина этого слова: {len(maxim)}")