from collections import Counter

message = input("Введите строку: ")


def count_unique_chars(s: str) -> int:
    s = s.lower()
    counter = Counter(s)
    return len(list(filter(lambda x: counter[x] == 1, counter)))


print('Количество уникальных символов в строке: ', count_unique_chars(message))
