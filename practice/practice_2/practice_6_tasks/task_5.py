word_num = int(input("Введите количество пар слов: "))
syn_dict = dict()

for i in range(word_num):
    pair = input(f"{i + 1} пара: ").lower().split('-')

    if pair[0] != pair[1] and pair[0] not in syn_dict.keys() and pair[1] not in syn_dict.keys():
        syn_dict[pair[0]] = pair[1]
        syn_dict[pair[1]] = pair[0]
    else:
        print("Такая пара уже существует")

while True:
    word = input("Введите слово: ")

    if word == "q":
        break

    if word in syn_dict.keys():
        print(f"Синоним: {syn_dict[word]}")
    else:
        print("Такого слова в словаре нет.")
