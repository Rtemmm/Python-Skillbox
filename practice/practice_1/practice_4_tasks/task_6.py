flatPrice = int(input('Введите стоимость квартиры(в млн): '))
flatSquare = int(input('Введите площадь квартиры: '))
if 10 >= flatPrice > 7 and flatSquare >= 10:
    print('Вам подходит квартира первый вариант')
elif flatPrice <= 7 and flatSquare >= 80:
    print('Вам подходит квартира второй вариант')
else:
    print('Вам не подходит ни один из вариантов')
