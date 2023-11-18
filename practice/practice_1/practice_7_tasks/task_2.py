num_debtors = int(input("Введите количество должников: "))
total_debt = 0
for i in range(num_debtors):
    if i % 5 == 0:
        debt = int(input(f"Должник с номером {i}, сколько должны: "))
        total_debt += debt
print("Общая сумма долгов: ", total_debt)
