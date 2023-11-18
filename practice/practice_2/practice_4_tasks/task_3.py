import random

first_team = [random.randint(5, 9) + round(random.random(), 2) for x in range(20)]
second_team = [random.randint(5, 9) + round(random.random(), 2) for x in range(20)]

winners = [first_team[x] if first_team[x] > second_team[x] else second_team[x] for x in range(20)]

print(f"Первая команда: {first_team}\nВторая команда: {second_team}\nПобедители тура: {winners}")
