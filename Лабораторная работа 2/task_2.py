from calendar import month

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

n = 1
pay = spend
sum = 0

while n <= months:
    sum += pay
    pay *= 1 + increase
    n += 1

money_capital = sum - salary * months

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
