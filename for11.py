#for11
N = int(input('N: '))
s = 0
for i in range(N, 2 * N + 1):
    s += i ** 2
print('Сумма = ', s)