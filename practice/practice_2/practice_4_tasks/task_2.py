n = int(input("Введите длину списка: "))

answer = [1 if x % 2 == 0 else x % 5 for x in range(n)]

print(f"Результат: {answer}")
