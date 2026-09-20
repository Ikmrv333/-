#for9
A = int(input('A: '))
B = int(input('B: '))
s = 0
for i in range(A, B + 1):
    s += i ** 2
print('Сумма квадратов = ', s)