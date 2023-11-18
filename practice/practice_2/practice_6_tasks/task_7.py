array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# 1.1 в каждом списке без использования множеств
new_array = []
for i in array_1:
    if i in array_2 and i in array_3:
        new_array.append(i)
print(new_array)

# 1.2 в каждом списке с  использования множеств
set_1 = set(array_1)
set_2 = set(array_2)
set_3 = set(array_3)
new_array = list(set_1 & set_2 & set_3)
print(new_array)

# 2.1 найти элементы из первого списка, которых нет во втором и третьем списках. без использования множеств;
new_array = []
for i in array_1:
    if i not in array_2 and i not in array_3:
        new_array.append(i)
print(new_array)

# 2.2 найти элементы из первого списка, которых нет во втором и третьем списках. с использования множеств;
set_1 = set(array_1)
set_2 = set(array_2)
new_array = list(set_1 - set_2 - set_3)
print(new_array)
