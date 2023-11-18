import copy

def replace_product(data, product):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.replace('телефон', product)
            else:
                replace_product(value, product)
    return data

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

sites = []
products = []
num_sites = int(input("Сколько сайтов: "))
for _ in range(num_sites):
    product = input("Введите название продукта для нового сайта: ")
    new_site = replace_product(copy.deepcopy(site), product)
    sites.append(new_site)
    products.append(product)
    for i in range(len(sites)):
        print(f"Сайт для {products[i]}: ")
        print(sites[i])
