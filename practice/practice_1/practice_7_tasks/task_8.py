X = int(input("Введите количество мальчиков: "))
Y = int(input("Введите количество девочек: "))
answer = ''
if X > 2 * Y or Y > 2 * X:
    print("Нет решения")
elif X >= Y:
    count = X - Y
    for BGB in range(count):
        answer += "BGB"
    for BG in range(Y - count):
        answer += "BG"
else:
    count = Y - X
    for GBG in range(count):
        answer += "GBG"
    for GB in range(X - count):
        answer += "GB"
print(answer)
