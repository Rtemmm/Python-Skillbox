string = input("Введите строку: ")
newString = ""
count = 1

for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        count += 1
    else:
        newString += string[i] + str(count)
        count = 1

newString += string[-1] + str(count)
print(f"Закодированная строка: {newString}")
