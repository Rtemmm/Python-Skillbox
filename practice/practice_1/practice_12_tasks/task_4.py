def count_numbers(n):
    num_count = 0
    temp = n
    while temp > 0:
        num_count += 1
        temp = temp // 10
    return num_count


def change_number(n, num_count):
    last_digit = n % 10
    first_digit = n // 10 ** (num_count - 1)
    between_digits = n % 10 ** (num_count - 1) // 10
    n = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    return n


def main():
    first_n = int(input("Введите первое число: "))
    first_num_count = count_numbers(first_n)
    if first_num_count < 3:
        print("В первом числе меньше трёх цифр.")
    else:
        first_n = change_number(first_n, first_num_count)
        print('Изменённое первое число:', first_n)

        second_n = int(input("\nВведите второе число: "))
        second_num_count = count_numbers(second_n)
        if second_num_count < 4:
            print("Во втором числе меньше четырёх цифр.")
        else:
            second_n = change_number(second_n, second_num_count)
            print('Изменённое второе число:', second_n)

            print('\nСумма чисел:', first_n + second_n)


main()
