#for32
N = int(input('N: '))
A = 1.0
for i in range(1, N + 1):
    A = (A + 1) / i
    print(A)