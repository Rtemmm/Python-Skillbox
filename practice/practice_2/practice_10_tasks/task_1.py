total_chars = 0

with open('people.txt', 'r') as file, open('errors.log', 'w') as error_log:
    for i, line in enumerate(file, start=1):
        name = line.strip()
        if len(name) < 3:
            error_log.write(f'Ошибка: менее трёх символов в строке {i}.\n')
        else:
            total_chars += len(name)

print(f'Общее количество символов: {total_chars}.')

