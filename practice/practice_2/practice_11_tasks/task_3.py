class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.children = children

        for child in children:
            age_difference = age - child.age

            if age_difference < 16:
                self.age = age + (16 - age_difference)
            else:
                self.age = age

    def print_info(self):
        print(f'Меня зовут {self.name}.\n'
              f'Мне {self.age} лет.\n'
              f'У меня {len(self.children)} детей:')

        for child in self.children:
            print(child.name, end=' ')
        print()

    @staticmethod
    def calm(child):
        child.calmness = True
        print("Ребенок успокоился")

    @staticmethod
    def feed(child):
        child.hunger = False
        print("Ребенок накормлен")


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calmness = False
        self.hunger = True


children = [Child("Ваня", 4), Child("Алеша", 8)]
parent = Parent("Мама", 32, children)

parent.print_info()
parent.calm(children[0])
parent.feed(children[0])
