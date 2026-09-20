#for23
X = float(input('X: '))
N = int(input('N: '))
f = 1.0
p = X
s = X
for i in range(1, N + 1):
    f *= (2 * i) * (2 * i + 1)
    p *= X * X
    s += ((-1) ** i) * p / f
print('Значение = ', s)