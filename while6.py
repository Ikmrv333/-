#while25
N = int(input('N: '))
F1 = 1
F2 = 1
while F2 <= N:
    F = F1 + F2
    F1 = F2
    F2 = F
print('Следующее число Фибоначчи = ', F2)