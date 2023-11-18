low = 1
height = 100
N = (height + low) // 2
print("Твое число больше, меньше или равно числу ", N, "?")
while True:
    answer = int(input("1 - равно, 2 - больше, 3 - меньше: "))
    if answer == 1:
        print("Я угадал")
        break
    if answer == 2:
        low = N + 1
        N = (height + low) // 2
        print("Твое число больше, меньше или равно числу ", N, "?")
        continue
    if answer == 3:
        height = N
        N = (height + 1) // 2
        print("Твое число больше, меньше или равно числу ", N, "?")
        continue
