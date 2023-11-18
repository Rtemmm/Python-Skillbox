grant = float(input("Введите стипендию: "))
expenses = float(input("Введите расходы на проживание в месяц: "))
total_expenses = 0
parents_money = 0
print(f"1. месяц траты  {expenses} не хватает {expenses - grant}")
for month in range(10):
    total_expenses += expenses
    if month != 0:
        expenses *= 1.03
        print(f"{month}. месяц {expenses}траты не хватает{expenses - grant}")
    if total_expenses > grant * (month + 1):
        parents_money += total_expenses - grant * (month + 1)
print("Сумма денег, которую необходимо получить у родителей: ", parents_money)
