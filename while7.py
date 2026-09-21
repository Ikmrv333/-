#while24
N = int(input('N: '))
F1 = 1
F2 = 1
is_fib = False
while F2 <= N:
    if F2 == N or F1 == N:
        is_fib = True
    F = F1 + F2
    F1 = F2
    F2 = F
if N == 1:
    is_fib = True
print(is_fib)