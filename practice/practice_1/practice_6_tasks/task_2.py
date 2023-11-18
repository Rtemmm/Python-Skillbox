summ = 0
for i in range(12):
    salary = int(input(f"Введите зарплату за {i + 1} месяц: "))
    summ += salary
print(summ / 12)
