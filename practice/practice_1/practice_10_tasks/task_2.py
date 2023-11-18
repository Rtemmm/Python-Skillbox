import math

n = int(input("Введите кол-во чисел: "))
for i in range(n):
    result = 0
    x = float(input("Введите число: "))
    if x > 0:
        result = math.log(math.ceil(x))
        print(f"x = {math.ceil(x)}log(x) = {result}")
    else:
        result = math.exp(math.floor(x))
        print(f"x = {math.floor(x)}exp(x) = {result}")
