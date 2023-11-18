def merge_sorted_lists(first_list, second_list):
    first_list.extend(second_list)
    first_list.sort()
    new_list = list(set(first_list))
    return new_list


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
