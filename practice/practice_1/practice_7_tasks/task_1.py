total_buckwheat = 100
consumption_per_month = 4
for month in range(1, total_buckwheat // consumption_per_month + 1):
    total_buckwheat -= consumption_per_month
    print(f"Через {month} месяцев останется {total_buckwheat} кг гречки.")
