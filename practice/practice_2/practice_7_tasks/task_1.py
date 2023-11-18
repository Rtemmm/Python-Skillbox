students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def GetLengthStudentsSurname(students):
    length = 0
    for i in students:
        length += len(students[i]["surname"])
    return length


def GetStudentsInterests(students):
    list_interests = []
    for i in students:
        list_interests += (students[i]['interests'])
    return set(list_interests)


def GetPairs(students, feature):
    return [(i, students[i][feature]) for i in students]


print(f"Список пар «ID студента — возраст»: {GetPairs(students, 'age')}")
print(f"Полный список интересов всех студентов: {GetStudentsInterests(students)}")
print(f"Общая длина всех фамилий студентов: {GetLengthStudentsSurname(students)}")
