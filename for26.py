#for26
X = float(input('X: '))
N = int(input('N: '))
p = X
s = X
for i in range(1, N + 1):
    p *= X * X
    s += ((-1) ** i) * p / (2 * i + 1)
print('Значение = ', s)