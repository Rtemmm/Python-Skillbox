import random

total = 0
with open('out_file.txt', 'w') as file:
    while total < 777:
        try:
            if random.randint(1, 13) == 13:
                raise Exception('Вас постигла неудача!')
            num = int(input('Введите число: '))
            total += num
            file.write(f'{num}\n')
        except Exception as e:
            print(str(e))
            break

if total >= 777:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')

