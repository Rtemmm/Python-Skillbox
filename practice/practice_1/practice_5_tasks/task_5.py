tasks = 0
phoneCall = False
goToTheShop = False
print("Начался 8-часовой рабочий день")
hour = 1
while hour <= 8:
    print(hour, "час")
    taskss = int(input("Сколько задач решит Максим? "))
    tasks += taskss
    call = int(input("Звонит жена. Взять трубку? (1-да, 0-нет) "))
    if call == 1:
        phoneCall = True
        goToTheShop = True
    if phoneCall:
        print("Нужно зайти в магазин")
    hour += 1
print("Рабочий день закончился. Всего выполнено задач: ", tasks)
if goToTheShop:
    print("Нужно зайти в магазин")
