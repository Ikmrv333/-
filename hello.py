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

'''#Begin13
R1 = float(input('R1: '))
R2 = float(input('R2: '))
pi = 3.14
S1 = pi * (R1 ** 2)
S2 = pi * (R2 ** 2)
S3 = S1 - S2
print(f'S1 = ', S1, 'S2 = ', S2, 'S3 = ', S3)'''

'''#Begin14
L = float(input('Длина окружности: '))
pi = 3.14
R = L / (2 * pi)
S = pi * (R ** 2)
print(f'Радиус = ', R, 'Площадь = ', S)'''

'''#Begin15
S = float(input('Площадь круга: '))
pi = 3.14
D = (4 * S / pi) ** 0.5
L = pi * D
print(f'Диаметр = ', D, 'Длина окружности = ', L)'''

'''#Begin16
x1 = float(input())
x2 = float(input())
print(f'Расстояние = ', abs(x2 - x1))'''

'''#Begin17
A = float(input())
B = float(input())
C = float(input())
AC = abs(C - A)
BC = abs(C - B)
print(f'AC = ', AC, 'BC = ', BC, 'Сумма = ', AC + BC)'''

'''#Begin18
A = float(input())
B = float(input())
C = float(input())
AC = abs(C - A)
BC = abs(C - B)
print(f'Произведение = ', AC * BC)'''

'''#Begin19
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
a = abs(x2 - x1)
b = abs(y2 - y1)
P = 2 * (a + b)
S = a * b
print(f'Периметр = ', P, 'Площадь = ', S)'''

'''#Begin20
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'Расстояние = ', dist)'''

'''#Begin21
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
P = a + b + c
p = P / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f'Периметр = ', P, 'Площадь = ', S)'''

'''#Begin22
A = float(input())
B = float(input())
A, B = B, A
print(f'A = ', A, 'B = ', B)'''

'''#Begin23
A = float(input())
B = float(input())
C = float(input())
A, B, C = B, C, A
print(f'A = ', A, 'B = ', B, 'C = ', C)'''

'''#Begin24
A = float(input())
B = float(input())
C = float(input())
A, B, C = C, A, B
print(f'A = ', A, 'B = ', B, 'C = ', C)'''

'''#Begin25
x = float(input())
y = 3 * (x ** 6) - 6 * (x ** 2) - 7
print(f'y = ', y)'''

'''#Begin26
x = float(input())
y = 4 * ((x - 3) ** 6) - 7 * ((x - 3) ** 3) + 2
print(f'y = ', y)'''

'''#Begin27
A = float(input())
A2 = A * A
A4 = A2 * A2
A8 = A4 * A4
print(f'A2 = ', A2, 'A4 = ', A4, 'A8 = ', A8)'''

'''#Begin28
A = float(input())
A2 = A * A
A3 = A2 * A
A5 = A3 * A2
A10 = A5 * A5
A15 = A10 * A5
print(f'A2 = ', A2, 'A3 = ', A3, 'A5 = ', A5, 'A10 = ', A10, 'A15 = ', A15)'''

'''#Begin29
a = float(input('Угол в градусах: '))
pi = 3.14
r = a * pi / 180
print(f'Угол в радианах = ', r)'''

'''#Begin30
a = float(input('Угол в радианах: '))
pi = 3.14
g = a * 180 / pi
print(f'Угол в градусах = ', g)'''

'''#Begin31
TF = float(input('Температура по Фаренгейту: '))
TC = (TF - 32) * 5 / 9
print(f'Температура по Цельсию = ', TC)'''

'''#Begin32
TC = float(input('Температура по Цельсию: '))
TF = TC * 9 / 5 + 32
print(f'Температура по Фаренгейту = ', TF)'''

'''#Begin33
X = float(input('Количество кг: '))
A = float(input('Стоимость: '))
p1 = A / X
Y = float(input('Сколько кг: '))
pY = p1 * Y
print(f'1 кг = ', p1, 'Y кг = ', pY)'''

'''#Begin34
X = float(input('Кг шоколадных: '))
A = float(input('Стоимость шоколадных: '))
Y = float(input('Кг ирисок: '))
B = float(input('Стоимость ирисок: '))
p_sh = A / X
p_ir = B / Y
d = p_sh / p_ir
print(f'1 кг шоколадных = ', p_sh, '1 кг ирисок = ', p_ir, 'Дороже в ', d, 'раз')'''

'''#Begin35
V = float(input('Скорость лодки: '))
U = float(input('Скорость течения: '))
T1 = float(input('Время по озеру: '))
T2 = float(input('Время против течения: '))
S = V * T1 + (V - U) * T2
print(f'Путь = ', S)'''

'''#Begin36
V1 = float(input())
V2 = float(input())
S = float(input())
T = float(input())
S_new = S + (V1 + V2) * T
print(f'Расстояние = ', S_new)'''

'''#Begin37
V1 = float(input())
V2 = float(input())
S = float(input())
T = float(input())
S_new = abs(S - (V1 + V2) * T)
print(f'Расстояние = ', S_new)'''

'''#Begin38
A = float(input())
B = float(input())
x = -B / A
print(f'x = ', x)'''

'''#Begin39
A = float(input())
B = float(input())
C = float(input())
D = B ** 2 - 4 * A * C
x1 = (-B - D ** 0.5) / (2 * A)
x2 = (-B + D ** 0.5) / (2 * A)
print(f'Меньший = ', x1, 'Больший = ', x2)'''

'''#Begin40
A1 = float(input())
B1 = float(input())
C1 = float(input())
A2 = float(input())
B2 = float(input())
C2 = float(input())
D = A1 * B2 - A2 * B1
x = (C1 * B2 - C2 * B1) / D
y = (A1 * C2 - A2 * C1) / D
print(f'x = ', x, 'y = ', y)'''

'''#Целые2
a = int(input("Введите число: "))
if (a % 2 == 0):
    print("Четное")
else:
    print("Нечет")'''