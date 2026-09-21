#while30
A = float(input('A: '))
B = float(input('B: '))
C = float(input('C: '))
K = 0
while A >= C and B >= C:
    A -= C
    B -= C
    K += 1
print('Количество квадратов = ', K)