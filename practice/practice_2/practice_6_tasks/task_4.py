def print_dict(dictionary):
    for i in dictionary.items():
        print(f"{i[0]} : {i[1]}")


text = input("Введите текст: ")

freq_dict = {x: text.count(x) for x in text}
freq_dict = {a: freq_dict[a] for a in sorted(freq_dict)}

inverted_freq_dict = {count: [letter for letter in freq_dict.keys() if freq_dict[letter] == count] for count in
                      freq_dict.values()}

print("Оригинальный словарь частот:")
print_dict(freq_dict)

print("Инвертированный словарь частот:")
print_dict(inverted_freq_dict)
