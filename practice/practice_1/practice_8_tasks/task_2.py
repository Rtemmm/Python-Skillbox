str = input("Введите строку со *: ")
for symbol in str:
    if symbol == '*':
        print("Символ '*' стоит на позиции", str.index(symbol) + 1)
