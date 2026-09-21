#while15
P = float(input('P: '))
S = 1000.0
K = 0
while S <= 1100:
    S += S * P / 100
    K += 1
print('K = ', K)
print('Вклад = ', S)