#for6
price = float(input('Цена 1 кг: '))
for i in range(6, 11):
    kg = i / 5
    print(kg, 'кг = ', kg * price)