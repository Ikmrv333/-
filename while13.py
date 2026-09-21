#while18
N = int(input('N: '))
K = 0
while N > 0:
    print(N % 10)
    N //= 10
    K += 1
print('Количество цифр = ', K)