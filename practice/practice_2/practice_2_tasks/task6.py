listNums = [1, 4, -3, 0, 10]
shift = int(input("Сдвиг: "))
nums = []

for i in range(len(listNums) - shift, len(listNums)):
    nums.append(listNums[i])

for i in range(len(listNums)-shift):
    nums.append(listNums[i])

print("Изначальный список: ", listNums)
print("Сдвинутый список: ", nums)
