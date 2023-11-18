x1, y1 = float(input('Введите местоположение коня: \n')), float(input())
x2, y2 = float(input('Введите местоположение точки на доске: \n')), float(input())
horse_x = int(x1 * 10)
horse_y = int(y1 * 10)
point_x = int(x2 * 10)
point_y = int(y2 * 10)

print(f'Конь в клетке ({horse_x}, {horse_y}). Точка в клетке ({point_x}, {point_y}).')
if (int(10 * x1) - int(10 * x2)) * (int(10 * y1) - int(10 * y2)) in [-2, 2]:
    print('Да, конь может ходить в эту клетку')
else:
    print('Нет, конь не может ходить в эту клетку')
