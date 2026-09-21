#while22
N = int(input('N: '))
i = 2
is_prime = N > 1
while i * i <= N:
    if N % i == 0:
        is_prime = False
    i += 1
print(is_prime)