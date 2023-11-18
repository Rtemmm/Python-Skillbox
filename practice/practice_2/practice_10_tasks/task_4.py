while True:
    print("1. Посмотреть текущий текст чата")
    print("2. Отправить сообщение")
    action = input("Выберите действие: ")
    if action == '1':
        with open('chat.txt', 'r') as file:
            print(file.read())
    elif action == '2':
        name = input("Введите ваше имя: ")
        message = input("Введите ваше сообщение: ")
        with open('chat.txt', 'a') as file:
            file.write(f'{name}: {message}\n')
    else:
        print("Неверный ввод, попробуйте еще раз.")
