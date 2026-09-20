#for22
X = float(input('X: '))
N = int(input('N: '))
f = 1.0
p = 1.0
s = 1.0
for i in range(1, N + 1):
    f *= i
    p *= X
    s += p / f
print('Значение = ', s)