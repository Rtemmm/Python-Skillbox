import math


def sqrt(number):
    try:
        if number < 0:
            raise ValueError("Число не может быть отрицательным")

        result = math.sqrt(number)
        return result

    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")


print(sqrt(9))
print(sqrt(-1))
