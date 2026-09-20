#for30
import math
N = int(input('N: '))
A = float(input('A: '))
B = float(input('B: '))
H = (B - A) / N
print('H = ', H)
for i in range(N + 1):
    x = A + i * H
    print(1 - math.sin(x))