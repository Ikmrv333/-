#for28
X = float(input('X: '))
N = int(input('N: '))
s = 1 + X / 2
p = X
for i in range(2, N + 1):
    p *= X
    ch = 1
    zn = 1
    for j in range(1, i):
        ch *= 2 * j - 1
        zn *= 2 * j
    s += ((-1) ** (i - 1)) * ch * p / zn
print('Значение = ', s)