contacts = {}

while True:
    answer = int(input("Введите номер действия: \n\t1. Добавить Контакт\n\t2. Найти человека\n\t3. Выйти(q)\n"))

    if answer == 1:
        name = tuple(input("Введите имя и фамилию нового контакта (через пробел): ").split())

        if name in contacts:
            print("Такой человек уже есть в контактах")
        else:
            tel = input("Введите телефон: ")
            contacts[name] = tel

        print(f"Текущий словарь контактов: {contacts}")
    elif answer == 2:
        name = tuple(input("Введите имя и фамилию человека: ").split())

        if name in contacts:
            unpacked_name = ' '.join(name)
            print(unpacked_name, contacts[name])
    else:
        break
