def min_len(list1, list2):
    return min(len(list1), len(list2))


def to_zip(string, tupl):
    temp = tupl[1:len(tupl) - 1].split(', ')
    generator = ((string[index], temp[index]) for index in range(min_len(string, temp)))

    print(generator)

    for i in generator:
        print(i)


string = input("Строка: ")
tupl = input("Кортеж (пример: (1, 2, 3, 4)): ")

to_zip(string, tupl)
