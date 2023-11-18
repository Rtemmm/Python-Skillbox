films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
    'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

favFilms = []

filmsToAdd = int(input("Сколько фильмов хотите добавить? "))

for i in range(filmsToAdd):
    film = input("Введите название фильма: ")

    if film in films:
        favFilms.append(film)
    else:
        print(f"Ошибка: фильма {film} у нас нет :(")

print(f"Ваш список любимых фильмов: {favFilms}")

