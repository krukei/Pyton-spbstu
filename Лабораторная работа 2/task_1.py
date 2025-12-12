money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
n = 0
money = money_capital
pay = spend

while money >= 0:
    money += salary
    money -= pay
    if money > 0:
        n += 1
    else:
        break
    pay *= (1 + (increase))


print("Количество месяцев, которое можно протянуть без долгов:", n)
