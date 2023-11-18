stalls = input("Введите строку из десяти символов a и b: ")
milk_per_stall = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
total_milk = 0
for i in range(len(stalls)):
    if stalls[i] == 'b':
        total_milk += milk_per_stall[i]
    else:
        total_milk = total_milk
print(f"Всего будет произведено молока за день: {total_milk} литров")
