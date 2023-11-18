from typing import List
from functools import reduce
import operator

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

new_floats = [round(x ** 3, 3) for x in floats]
new_names = [name for name in names if len(name) >= 5]
new_numbers = reduce(operator.mul, numbers)

print("Новый список floats:", new_floats)
print("Новый список names:", new_names)
print("Произведение всех чисел из списка numbers:", new_numbers)
