x, y = 8, 10

while True:
    print(f"Марсоход находится на позиции {x}, {y}, введите команду:")
    command = input()

    if command == 'W' and y < 20:
        y += 1
    elif command == 'S' and y > 0:
        y -= 1
    elif command == 'A' and x > 0:
        x -= 1
    elif command == 'D' and x < 15:
        x += 1
