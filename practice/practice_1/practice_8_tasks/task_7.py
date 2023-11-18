encoded_message = input("Введите зашифрованное сообщение: ")
length = len(encoded_message)
decoded_message = [''] * length
index = 0
newStr1 = ''
newStr2 = ''
for i in range(1, length + 1, 2):
    decoded_message[index] = encoded_message[i - 1]
    newStr1 += decoded_message[index]
    index += 1
for i in range(2, length + 1, 2):
    decoded_message[index] = encoded_message[i - 1]
    newStr2 = decoded_message[index] + newStr2
    index += 1
print(f"Расшифрованное сообщение:{newStr1 + newStr2}")
