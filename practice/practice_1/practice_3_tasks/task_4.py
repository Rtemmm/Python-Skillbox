price1 = int(input("Цена первого товара: "))
price2 = int(input("Цена второго товара: "))
price3 = int(input("Цена третьего товара: "))
check = price1 + price2 + price3
if check > 10000:
    check = check - (check * 10 / 100)
print("Сумма чека: ", check)
