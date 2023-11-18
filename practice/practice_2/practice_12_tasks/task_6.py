import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self, *args):
        pass


class Circle(Shape):
    @staticmethod
    def area(radius: int):
        return math.pi * radius ** 2


class Square(Shape):
    @staticmethod
    def area(a: int, b: int):
        return a * b


class Triangle(Shape):
    @staticmethod
    def area(a: int, b: int, c: int):
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


print(Circle.area(34))
print(Square.area(2, 3))
print(Triangle.area(3, 4, 5))
