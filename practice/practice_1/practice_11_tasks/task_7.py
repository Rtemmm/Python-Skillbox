import random


def rock_paper_scissors():
    comp = random.SystemRandom().choice(['камень', 'ножницы', 'бумага'])
    player = input('Введите камень, ножницы или бумага: ')

    if player == 'камень' and comp == 'ножницы':
        print(f'Компьютер выбрал: {comp}')
        print('Вы победили')

    elif player == 'камень' and comp == 'бумага':
        print(f'Компьютер выбрал: {comp}')
        print('Вы проиграли')

    elif player == 'ножницы' and comp == 'камень':
        print(f'Компьютер выбрал: {comp}')
        print('Вы проиграли')

    elif player == 'ножницы' and comp == ',бумага':
        print(f'Компьютер выбрал: {comp}')
        print('Вы победили')

    elif player == 'бумага' and comp == 'ножницы':
        print(f'Компьютер выбрал: {comp}')
        print('Вы проиграли')

    elif player == 'бумага' and comp == 'камень':
        print(f'Компьютер выбрал: {comp}')
        print('Вы победили')

    else:
        print(f'Компьютер выбрал: {comp}')
        print('Ничья')


def guess_the_number():
    comp = random.randint(1, 10)
    while True:
        player = int(input("Угадайте число, которое загадал компьютер(От 1 до 10): "))
        if player != comp:
            print("Вы не угадали, попробуйте еще раз.")
        else:
            print(f"Поздравляем! Вы назвали число {player}, а компьютер загадал число {comp}.")
            break


def mainMenu():
    choice = int(input('Выберите игру:\n1) Камень.Ножницы.Бумага.\n2) Угадай число.\nВаш выбор: '))
    if choice == 1:
        print()
        rock_paper_scissors()
    elif choice == 2:
        print()
        guess_the_number()
    else:
        print('Неправильный выбор. Выберите игру.')


mainMenu()
