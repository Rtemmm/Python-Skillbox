import re

numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

# Используем регулярные выражения для поиска номеров частных автомобилей и номеров такси
private_car_pattern = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
taxi_pattern = r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'

private_car_numbers = re.findall(private_car_pattern, numbers)
taxi_numbers = re.findall(taxi_pattern, numbers)

print("Список номеров частных автомобилей:", private_car_numbers)
print("Список номеров такси:", taxi_numbers)
