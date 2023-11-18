violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

n = int(input("Сколько песен выбрать? "))
sum = 0

for i in range(1, n + 1):
    answer = input(f"Название {i} песни: ")

    for j in violator_songs:
        if j[0] == answer:
            sum += j[1]
            break

print("Общее время звучания песен — ", round(sum, 2))
