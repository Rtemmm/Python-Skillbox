def sum(*args):
    total = 0
    for arg in args:
        if isinstance(arg, list):
            total += sum(*arg)
        else:
            total += arg
    return total


print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))
