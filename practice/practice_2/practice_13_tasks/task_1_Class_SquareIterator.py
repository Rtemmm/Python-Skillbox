class SquareIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.max_value:
            result = self.current_value ** 2
            self.current_value += 1
            return result
        else:
            raise StopIteration


N = int(input("Введите число N: "))

for number in SquareIterator(N):
    print(number)
