class Property:

    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def get_tax(self):
        return

    def get_name(self):
        return


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth=worth)

    def get_tax(self):
        return 1 / 1000 * self.get_worth()

    def get_full_price(self):
        return self.get_tax() + self.get_worth()

    def get_name(self):
        return "Квартиру:D"


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth=worth)

    def get_tax(self):
        return 1 / 200 * self.get_worth()

    def get_full_price(self):
        return self.get_tax() + self.get_worth()

    def get_name(self):
        return "Машину xD"


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth=worth)

    def get_tax(self):
        return 1 / 500 * self.get_worth()

    def get_full_price(self):
        return self.get_tax() + self.get_worth()

    def get_name(self):
        return "Загородный дом :D"


def Print(money, property):
    print(
        f"Налог на {property.get_name()}: {property.get_tax()}. "
        f"{f'Не хватает {abs(money - property.get_full_price())} деняк' if not (money - property.get_full_price() > 0) else 'купить можно'}")


money = int(input("Сколько деняк: "))
propertyCost = int(input("Сколько стоит что-то: "))

car = Car(propertyCost)
aparts = Apartment(propertyCost)
house = CountryHouse(propertyCost)
a = (car, aparts, house)
for i in a:
    Print(money, i)
