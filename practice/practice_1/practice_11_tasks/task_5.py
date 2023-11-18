def count_letters(text, K, N):
    count_k = 0
    count_n = 0
    for letter in text:
        if letter == K:
            count_k += 1
        if letter == N:
            count_n += 1
    print(f"Количество цифр {K}: {count_k}")
    print(f"Количество букв {N}: {count_n}")


text = input("Введите текст: ")
K = input("Какую цифру ищем? ")
N = input("Какую букву ищём? ")
count_letters(text.lower(), K, N)
