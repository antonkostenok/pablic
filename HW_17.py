per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму депозита: '))
deposit = []
for key in per_cent: deposit.append(round(per_cent[key] * money / 100, 2))
max_deposit = max(deposit)
print(deposit)
print(max_deposit)
