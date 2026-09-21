#while28
eps = float(input('eps: '))
A1 = 2.0
A2 = 2 + 1 / A1
K = 2
while abs(A2 - A1) >= eps:
    A1 = A2
    A2 = 2 + 1 / A1
    K += 1
print('K = ', K)
print('A(K-1) = ', A1)
print('A(K) = ', A2)