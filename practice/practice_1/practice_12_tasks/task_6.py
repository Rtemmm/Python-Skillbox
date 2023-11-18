def calculateSafeLevel(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10


def calculateSafeDepth(danger_lvl):
    min_depth = 0
    max_depth = 4
    result = (min_depth + max_depth) / 2
    while abs(calculateSafeLevel(result)) >= danger_lvl:
        if abs(calculateSafeLevel(min_depth)) < abs(calculateSafeLevel(max_depth)):
            max_depth = result
        else:
            min_depth = result

        result = (min_depth + max_depth) / 2
    return result


accept_danger_lvl = float(input('Введите максимально допустимый уровень опасности: '))
print(f'Приблизительная глубина безопасной кладки: {calculateSafeDepth(accept_danger_lvl)}m')
