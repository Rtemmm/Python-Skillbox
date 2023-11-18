n = int(input("Введите число: "))
if n < 0:
    n = -n
fac = 1
for i in range(1, n + 1):
    fac = fac * i
print(f"Факториал {n} равен {fac}")
