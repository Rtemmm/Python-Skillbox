numb = int(input("Введите число: "))
if numb < 0:
    numb = -numb
i = 1
while numb // 10 != 0:
    i += 1
    numb = numb // 10
print(i)
