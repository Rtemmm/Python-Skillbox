import time
from datetime import datetime


def log_methods(date_format):
    def decorator(cls):
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                def wrapper(*args, **kwargs):
                    start_time = time.time()
                    print(
                        f"Запускается '{cls.__name__}.{attr_name}'. Дата и время запуска: {datetime.now().strftime(date_format)}")
                    result = attr_value(*args, **kwargs)
                    end_time = time.time()
                    print(f"Завершение '{cls.__name__}.{attr_name}', время работы = {end_time - start_time} s.")
                    return result

                setattr(cls, attr_name, wrapper)
        return cls

    return decorator


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y — H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
