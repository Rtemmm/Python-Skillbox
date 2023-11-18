with open('registrations.txt', 'r') as file, \
        open('registrations_good.log', 'w') as good, \
        open('registrations_bad.log', 'w') as bad:
    for i, line in enumerate(file, start=1):
        try:
            name, email, age = line.strip().split()
            if not name.isalpha():
                raise NameError
            if '@' not in email or '.' not in email:
                raise SyntaxError
            if not (10 <= int(age) <= 99):
                raise ValueError

            good.write(line)

        except IndexError:
            bad.write(f'{line.strip()}    НЕ присутствуют все три поля\n')
        except NameError:
            bad.write(f'{line.strip()}    Поле «Имя» содержит НЕ только буквы\n')
        except SyntaxError:
            bad.write(f'{line.strip()}    Поле «Имейл» НЕ содержит @ и точку\n')
        except ValueError:
            bad.write(f'{line.strip()}    Поле «Возраст» НЕ представляет число от 10 до 99\n')
