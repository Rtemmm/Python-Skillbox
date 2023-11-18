n = int(input("Введите число: "))
for i in range(1, n + 1):
    s = ''
    for j in range(n, n - i, -1):
        s += str(j)
    print(s + '.' * (n * 2 - i * 2) + s[::-1])
