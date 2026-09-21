#for36
N = int(input('N: '))
K = int(input('K: '))
s = 0.0
for i in range(1, N + 1):
    p = 1.0
    for j in range(K):
        p *= i
    s += p
print('Сумма = ', s)