import time


def delay_decorator(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Жду {seconds} секунд перед тем как запустить функцию.")
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@delay_decorator(5)
def test():
    print("Функция выполнилась")


test()
