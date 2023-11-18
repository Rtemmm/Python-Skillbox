import datetime
import functools


def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f"Название функции: {func.__name__}")
            print(f"Документация: {func.__doc__}")
            return func(*args, **kwargs)
        except Exception as e:
            with open("function_errors.log", "a") as file:
                file.write(f"{datetime.datetime.now()}: Функция {func.__name__} получила ошибку: {str(e)}\n")
            print(f"Ошибка в функции {func.__name__}. Ошибка записана.")

    return wrapper


@logging_decorator
def test():
    print("Функция выполнилась")


@logging_decorator
def test2():
    raise Exception()


test()
