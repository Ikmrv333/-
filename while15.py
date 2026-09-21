#while16
P = float(input('P: '))
S = 1000.0
K = 0
while S <= 2000:
    S += S * P / 100
    K += 1
print('K = ', K)
print('Вклад = ', S)