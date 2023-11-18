guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
question1 = input("Гость пришел или ушел? ")

while question1 != "пора спать":
    name = input("Имя гостя: ")

    if question1 == "пришел" and len(guests) < 6:
        guests.append(name)
        print(f"Привет, {name}!")
    elif question1 == "пришел" and len(guests) == 6:
        print(f"Прости, {name}, но мест нет.")
    elif question1 == "ушел" and name in guests:
        guests.remove(name)
        print(f"Пока, {name}!")

    print()

    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    question1 = input("Гость пришел или ушел? ")

print("Вечеринка закончилась, все легли спать.")
