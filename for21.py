#for21
N = int(input('N: '))
f = 1.0
s = 1.0
for i in range(1, N + 1):
    f *= i
    s += 1 / f
print('Сумма = ', s)