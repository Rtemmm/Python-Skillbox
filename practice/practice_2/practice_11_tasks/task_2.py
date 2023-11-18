class Student:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def print_info(self):
        print(f'{self.full_name} {self.group_number}', end='  ')
        self.print_grades()

    def print_grades(self):
        for grade in self.grades:
            print(grade, end=' ')

        print('\n')


students = [
    Student('Валерьянкин Егор', '1321', [3, 4, 2, 2, 5]),
    Student('Петушков Иван', '1421', [5, 4, 2, 3, 3]),
    Student('Гып Алексей', '1231', [2, 4, 3, 5, 2]),
    Student('Ебак Емеля', '4235', [2, 2, 2, 5, 4]),
    Student('Черт Петр', '8442', [5, 5, 5, 5, 5]),
    Student('Агык Алина', '1463', [2, 2, 2, 2, 2])
]

students.sort(key=Student.get_average_grade)

for student in students:
    student.print_info()
