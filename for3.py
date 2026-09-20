#for3
A = int(input('A: '))
B = int(input('B: '))
N = 0
for i in range(B - 1, A, -1):
    print(i)
    N += 1
print('Количество = ', N)