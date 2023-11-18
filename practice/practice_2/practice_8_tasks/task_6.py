def partition(lst):
    pivot = lst[-1]
    less = [x for x in lst[:-1] if x < pivot]
    equal = [x for x in lst if x == pivot]
    greater = [x for x in lst[:-1] if x > pivot]
    return less, equal, greater


def quicksort(lst):
    if len(lst) <= 1:
        return lst
    less, equal, greater = partition(lst)
    return quicksort(less) + equal + quicksort(greater)


numbers = [5, 8, 9, 4, 2, 9, 1, 8]
numbers = [1, 23, 634, 3422, 43, 44, 6, 9, 5, 0, 5, 8, 9, 4, 2, 9, 1, 8]
print(quicksort(numbers))
