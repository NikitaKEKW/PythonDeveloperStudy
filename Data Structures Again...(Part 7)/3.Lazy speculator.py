rates = {'Sberbank': 55.8, 'VTB24': 53.91, 'Tinkoff': 56.21, 'Kaspi': 49.99}
min_rates = min(rates.values())
bank = ""
for key, value in rates.items():
    if value == min_rates:
        bank = key
        break
print("Наиболее привлекательный курс доллара в банке - ", bank)
