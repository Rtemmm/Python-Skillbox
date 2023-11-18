from random import randint


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def punch(self, enemy):
        if not enemy.health:
            return

        enemy.health -= 20
        print(f'Warrior {self.name} punched {enemy.name}. {enemy.name} has {enemy.health} HP')


warrior_1 = Warrior(input('First warrior name: '))
warrior_2 = Warrior(input('Second warrior name: '))

print()

while warrior_1.health and warrior_2.health:
    if randint(0, 1):
        warrior_1.punch(warrior_2)
    else:
        warrior_2.punch(warrior_1)

if warrior_1.health:
    print(f'\n{warrior_1.name} has won!')
else:
    print(f'\n{warrior_2.name} has won!')
