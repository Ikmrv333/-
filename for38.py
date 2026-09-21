#for38
N = int(input('N: '))
s = 0.0
for i in range(1, N + 1):
    p = 1.0
    for j in range(N - i + 1):
        p *= i
    s += p
print('Сумма = ', s)