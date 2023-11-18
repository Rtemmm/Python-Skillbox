str = input("Введите строку: ").lower()
lengthHalf = len(str) // 2
reverseStr = ''
for i in str:
    reverseStr = i + reverseStr
if str == reverseStr:
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром!")
