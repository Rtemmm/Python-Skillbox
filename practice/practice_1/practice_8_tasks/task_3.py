row = int(input("Введите кол-во рядов: "))
places = int(input("Введите количество мест: "))
distance = int(input("Введите расстояние между местами: "))
strCinema = ''
for rows in range(row):
    print("=" * places, "*" * distance, "=" * places)
