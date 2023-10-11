amount = 0
tickets = int(input("Введите количество билетов:\n"))
for age in range(tickets):
    age = int(input("Введите возраст:\n"))
    if age < 18:
        amount += 0
    elif age >= 18 and age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
if amount == 0:
    print("Проходите на конференцию бесплатно!")
else:
    print("Количество билетов:", tickets)

if tickets > 3:
    discount = amount / 100 * 10
    print("Скидка составляет:","%.2f" % discount)
    print("К оплате с учетом скидки:","%.2f" % discount)
