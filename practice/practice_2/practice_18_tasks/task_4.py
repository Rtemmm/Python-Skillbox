import re

numbers = ['9999999999', '999999-999', '99999x9999']

for i, number in enumerate(numbers, start=1):
    if len(number) != 10:
        print(f"{i} номер: не подходит")
        continue

    if not re.match(r'^[89]', number):
        print(f"{i} номер: не подходит")
        continue

    if not re.match(r'^\d{10}$', number):
        print(f"{i} номер: не подходит")
        continue

    print(f"{i} номер: всё в порядке")
