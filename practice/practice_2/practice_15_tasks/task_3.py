class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        if cls.is_date_valid(day, month, year):
            return cls(day, month, year)
        else:
            raise ValueError("Invalid date")

    @staticmethod
    def is_date_valid(day, month, year):
        if month < 1 or month > 12 or day < 1 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2 and day > 29:
            return False
        if month == 2 and day == 29 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
            return False
        return True

    def __str__(self):
        return f"День: {self.day}    Месяц: {self.month}    Год: {self.year}"


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid(10, 12, 2077))
print(Date.is_date_valid(40, 12, 2077))
