def reverse_and_add(n, k):
    n_reversed = int(str(n)[::-1])
    k_reversed = int(str(k)[::-1])

    print(f"Первое число наоборот: {n_reversed}")
    print(f"Второе число наоборот: {k_reversed}")

    sum_reversed = n_reversed + k_reversed
    print(f"Сумма: {sum_reversed}")

    sum_final = int(str(sum_reversed)[::-1])
    print(f"Сумма наоборот: {sum_final}")


n = int(input("Введите первое число: "))
k = int(input("Введите второе число: "))
reverse_and_add(n, k)
