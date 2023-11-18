class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Функция {self.func.__name__} была вызвана {self.count} раз")
        return self.func(*args, **kwargs)


@Counter
def test():
    print("Function executed")


test()
test()
