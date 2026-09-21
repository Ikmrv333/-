#while14
A = float(input('A: '))
K = 0
s = 0.0
while s + 1 / (K + 1) <= A:
    K += 1
    s += 1 / K
print('K = ', K)
print('Сумма = ', s)