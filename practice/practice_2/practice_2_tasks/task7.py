word = input("Введите слово: ")
flag = True

for i in range(len(word)):
    if word[i] != word[len(word) - 1 - i]:
        flag = False
        break

if flag:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")