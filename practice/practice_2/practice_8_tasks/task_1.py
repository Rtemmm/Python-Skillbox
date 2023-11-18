def result(start, end):
    if start > end:
        return

    print(start)
    start += 1

    result(start, end)


num = int(input("Введите num: "))
result(1, num)
