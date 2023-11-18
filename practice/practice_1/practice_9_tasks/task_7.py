separator, numberInPyramid = ' ' * 3, -1
n = int(input("Введите количество уровней: "))
for i in range(1, n + 1):
    print(separator * (n - i),
          separator.join(f'{(numberInPyramid := numberInPyramid + 2):^{len(separator)}}' for _ in range(i)))
