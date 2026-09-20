#for24
X = float(input('X: '))
N = int(input('N: '))
f = 1.0
p = 1.0
s = 1.0
for i in range(1, N + 1):
    f *= (2 * i - 1) * (2 * i)
    p *= X * X
    s += ((-1) ** i) * p / f
print('Значение = ', s)