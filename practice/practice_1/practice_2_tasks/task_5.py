n = int(input("Введите количество минут: "))
hours = n // 60
otherMinutes = n % 60
print("В часах это:", hours)
print("Осталось столько", otherMinutes, "минут")
