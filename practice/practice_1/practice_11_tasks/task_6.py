def finedMaxDel(numb1, numb2):
    if numb2 == 0:
        return numb1
    else:
        return finedMaxDel(numb2, numb1 % numb2)


numb1 = int(input("Введите первое число: "))
numb2 = int(input("Введите второе число: "))
print(f"Наибольший общий делитель чисел это: {finedMaxDel(numb1, numb2)}")
