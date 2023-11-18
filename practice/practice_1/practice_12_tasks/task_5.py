def pendulum_swing():
    initial_amplitude = float(input("Введите начальную амплитуду: "))
    final_amplitude = float(input("Введите амплитуду остановки: "))

    if initial_amplitude <= 0 or final_amplitude <= 0:
        print("Амплитуда должна быть положительной.")
        return

    swing_count = 0
    while initial_amplitude > final_amplitude:
        initial_amplitude *= 0.916
        swing_count += 1

    print(f"Маятник считается остановившимся через {swing_count} колебаний")


pendulum_swing()
