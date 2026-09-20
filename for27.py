#for27
X = float(input('X: '))
N = int(input('N: '))
p = X
s = X
for i in range(1, N + 1):
    p *= X * X
    ch = 1
    zn = 1
    for j in range(1, i + 1):
        ch *= 2 * j - 1
        zn *= 2 * j
    s += ch * p / (zn * (2 * i + 1))
print('Значение = ', s)