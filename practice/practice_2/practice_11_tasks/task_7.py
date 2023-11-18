class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            self.data = data

    def __str__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.data])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы разных размеров не могут быть сложены")
        return Matrix(self.rows, self.cols,
                      [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы разных размеров не могут быть вычтены")
        return Matrix(self.rows, self.cols,
                      [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        return Matrix(self.rows, other.cols,
                      [[sum(a*b for a, b in zip(self_row, other_col)) for other_col in zip(*other.data)] for self_row in self.data])

    def transpose(self):
        return Matrix(self.cols, self.rows, [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)])


# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())