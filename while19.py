#while12
N = int(input('N: '))
K = 0
s = 0
while s + K + 1 <= N:
    K += 1
    s += K
print('K = ', K)
print('Сумма = ', s)