word = input("Введите слово: ")
indexFirst = word.index("h")
rindexSecond = word.rindex("h")

print(f"Развёрнутая последовательность между первым и последним h:\n{word[rindexSecond-1:indexFirst:-1]}")