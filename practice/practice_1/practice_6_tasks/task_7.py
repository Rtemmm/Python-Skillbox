N = int(input("Введите количество карточек: "))
total_sum = 0
for i in range(N + 1):
    total_sum += i
cards_sum = 0
for numberCard in range(1, N):
    card = int(input("Введите номер оставшейся карточки: "))
    cards_sum += card
print("Номер потерянной карточки: ", total_sum - cards_sum)
