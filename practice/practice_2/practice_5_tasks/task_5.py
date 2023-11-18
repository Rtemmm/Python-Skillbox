error = "Пароль ненадёжный. Попробуйте ещё раз."

while True:
    password = input("Придумайте пароль: ")

    if len(password) < 8 or not any(char.isupper() for char in password) or sum(char.isdigit() for char in password) < 3:
        print(error)
        continue

    print("Это надёжный пароль.")
    break
