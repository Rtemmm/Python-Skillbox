from random import randint


class House:
    def __init__(self):
        self.food = 50
        self.money = 0


class Human:
    def __init__(self, name, house):
        self.name = name
        self.hunger = 50
        self.house = house

    def eat(self):
        self.hunger += 10
        self.house.food -= 10

    def work(self):
        self.house.money += 50
        self.hunger -= 10

    def play(self):
        self.hunger -= 10

    def shopping(self):
        self.house.money -= 50
        self.house.food += 50

    def live_one_day(self):
        dice = randint(1, 6)

        if self.hunger < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()

        return self.hunger <= 0


def experiment():
    house = House()
    human1 = Human('Артём', house)
    human2 = Human('Василий', house)

    for day in range(365):
        if human1.live_one_day() or human2.live_one_day():
            print('Один из людей умер.')
            return

    print('Оба человека успешно прожили год.')


experiment()
