import requests
import json

# Получаем информацию о корабле
ship_url = "https://swapi.dev/api/starships/10/"
ship_response = requests.get(ship_url)
ship_data = ship_response.json()

ship_info = {
    "name": ship_data["name"],
    "max_speed": ship_data["max_atmosphering_speed"],
    "class": ship_data["starship_class"],
    "pilots": []
}

# Получаем информацию о пилотах
for pilot_url in ship_data["pilots"]:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()

    # Получаем информацию о родной планете пилота
    planet_response = requests.get(pilot_data["homeworld"])
    planet_data = planet_response.json()

    pilot_info = {
        "name": pilot_data["name"],
        "height": pilot_data["height"],
        "mass": pilot_data["mass"],
        "homeworld": planet_data["name"],
        "homeworld_link": pilot_data["homeworld"]
    }

    ship_info["pilots"].append(pilot_info)

# Выводим информацию на экран
print(json.dumps(ship_info, indent=4, ensure_ascii=False))

# Сохраняем информацию в JSON-файл
with open("millennium_falcon_pilots.json", "w", encoding='utf-8') as f:
    json.dump(ship_info, f, ensure_ascii=False, indent=4)
