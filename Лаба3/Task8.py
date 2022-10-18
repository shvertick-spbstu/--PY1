money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True:
    money_capital = money_capital + salary - spend
    month += 1
    spend *= (1 + increase)
    if money_capital < spend:
        break
print(month)
