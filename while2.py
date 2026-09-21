#while29
eps = float(input('eps: '))
A1 = 1.0
A2 = 2.0
K = 3
A = (A1 + 2 * A2) / 3
while abs(A - A2) >= eps:
    A1 = A2
    A2 = A
    A = (A1 + 2 * A2) / 3
    K += 1
print('K = ', K)
print('A(K-1) = ', A2)
print('A(K) = ', A)