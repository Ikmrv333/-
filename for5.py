#for5
price = float(input('Цена 1 кг: '))
for i in range(1, 11):
    kg = i / 10
    print(kg, 'кг = ', kg * price)