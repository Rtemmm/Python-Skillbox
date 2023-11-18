def find_key(data, key, max_depth=None, current_depth=0):
    if key in data:
        return data[key]
    
    elif max_depth is None or current_depth < max_depth:
        for value in data.values():
            if isinstance(value, dict):
                result = find_key(value, key, max_depth, current_depth + 1)
                if result is not None:
                    return result
    return None


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input("Введите искомый ключ: ")
max_depth_input = input("Хотите ввести максимальную глубину? Y/N: ")
max_depth = int(input("Введите максимальную глубину: ")) if max_depth_input.lower() == 'y' else None

print("Значение ключа:", find_key(site, key, max_depth))