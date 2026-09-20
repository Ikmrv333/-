#for29
N = int(input('N: '))
A = float(input('A: '))
B = float(input('B: '))
H = (B - A) / N
print('H = ', H)
for i in range(N + 1):
    print(A + i * H)