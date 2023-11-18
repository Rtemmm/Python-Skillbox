def reverse_number():
    while True:
        num = input("Введите число: ")
        if num == '0':
            print("Программа завершена!")
            break
        else:
            reversed_num = num[::-1].lstrip('0')
            if len(reversed_num) <= 1:
                while len(reversed_num) != len(num):
                    reversed_num = '0' + reversed_num
            print(f"Число наоборот: {reversed_num}")


reverse_number()
