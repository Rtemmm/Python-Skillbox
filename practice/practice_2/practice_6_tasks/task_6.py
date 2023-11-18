N = int(input("Введите количество заказов: "))
orders = {}

for i in range(N):
    order = input(f"{i + 1} заказ: ")
    customer, pizza, quantity = order.split()
    quantity = int(quantity)

    if customer in orders:
        if pizza in orders[customer]:
            orders[customer][pizza] += quantity
        else:
            orders[customer][pizza] = quantity
    else:
        orders[customer] = {pizza: quantity}

for customer in sorted(orders.keys()):
    print(f"{customer}:")

    for pizza in sorted(orders[customer].keys()):
        print(f"{pizza}: {orders[customer][pizza]}")
