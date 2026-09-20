#for20
N = int(input('N: '))
f = 1.0
s = 0.0
for i in range(1, N + 1):
    f *= i
    s += f
print('Сумма = ', s)