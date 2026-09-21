#for37
N = int(input('N: '))
s = 0.0
for i in range(1, N + 1):
    p = 1.0
    for j in range(i):
        p *= i
    s += p
print('Сумма = ', s)