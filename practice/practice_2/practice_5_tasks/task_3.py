file = input("Название файла: ")

errorsStart = ("@", "№", "$", "%", "^", "&", "*", "()")
errorsEnd = (".txt", ".docx")

if file.startswith(errorsStart):
    print("Ошибка: название начинается недопустимым символом.")
elif not file.endswith(errorsEnd):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("Файл назван верно")
