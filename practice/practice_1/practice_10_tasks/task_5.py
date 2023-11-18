import math

planet_radius_km = float(input("Введите радиус планеты в километрах: "))
earth_volume = 1.08321 * 10 ** 12
planet_volume = 4 / 3 * math.pi * planet_radius_km ** 3
ratio = round(earth_volume / planet_volume, 3)
if ratio > 0:
    print(f"Планета Земля больше теоретически возможной планеты по объёму в {ratio} раз.")
else:
    print(f"Планета Земля меньше теоретически возможной планеты по объёму в {ratio} раз.")
