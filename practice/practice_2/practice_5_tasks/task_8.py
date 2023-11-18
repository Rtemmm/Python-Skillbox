def GetShift(string1, string2):
    for i in range(len(string1)):
        # print(string2[0:i])
        print(f"{string2[i:len(string2)]}{string2[0:i]}")
        if f"{string2[i:len(string2)]}{string2[0:i]}" == string1:

            return abs(i)
    return -1


string1 = input("Первая строка: ")
string2 = input("Вторая строка: ")
shift = GetShift(string1, string2)

if shift >= 0:
    print(f"Первая строка получается из второй со сдвигом {shift}")
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
