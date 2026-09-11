'''#Begin1
a = float(input('Сторона квадрата: '))
P = 4 * a
print('Периметр = ', P)'''

'''#Begin2
a = float(input('Сторона квадрата: '))
S = a ** 2
print('Площадь = ', S)'''

'''#Begin3
a = float(input())
b = float(input())
S = a * b
P = 2 * (a+b)
print(f'Площадь = ', {S}, 'Периметр = ', {P})'''

'''#Begin4
d = float(input())
pi = 3.14
L = pi * d
print('Длина = ', L)'''

'''#Begin5
a = float(input())
V = a ** 3
S = 6 * (a ** 2)
print(f'Объём = ', V, 'площадь = ',)'''

'''#Begin6
a = int(input("Введите сторону а: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print(f"Обьем: {V}, Площадь: {S}")'''

'''#Beging7
R = int(input("Введите радиус: "))
L = 2 * 3.14 * R
S = 3.14 * R**2
print(f"Длина: {L}, Площадь: {S}")'''

'''#beginig8
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
ab = (a + b)/2'''

'''#beginig9
a = float(input("Введите неотрицательное число a: "))
b = float(input("Введите неотрицательное число b: "))
a >= 0 and b >= 0
ab = (a * b) ** 0.5'''

'''#Begin10
a = float(input())
b = float(input())
a != 0 and b != 0
c = a ** 2 + b ** 2
d = a ** 2 - b ** 2
e = (a ** 2) * (b ** 2)
f = (a ** 2) / (b ** 2)
print(f'Сумма квадратов = ', c, 'разность квадратов = ', d, 'произведение квадратов = ', e, 'частное квадратов = ', f,)'''

'''#Begin11
a = float(input())
b = float(input())
a != 0 and b != 0
c = a ** 2 + b ** 2
d = a ** 2 - b ** 2
e = (a ** 2) * (b ** 2)
f = ((a ** 2) ** 0.5) / ((b ** 2) ** 0.5)
print(f'Сумма квадратов = ', c, 'разность квадратов = ', d, 'произведение квадратов = ', e, 'частное модулей = ', f,)'''

'''#Begin12
a = float(input('Первый катет: '))
b = float(input('Второй катет: '))
c = (a ** 2 + b ** 2) ** 0.5
P = a + b + c
print('Гипотенуза = ', c)
print('Периметр = ', P)'''

#Целые2
a = int(input("Введите число: "))
if (a % 2 == 0):
    print("Четное")
else:
    print("Нечет")