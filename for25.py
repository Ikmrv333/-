#for25
X = float(input('X: '))
N = int(input('N: '))
p = X
s = X
for i in range(2, N + 1):
    p *= X
    s += ((-1) ** (i - 1)) * p / i
print('Значение = ', s)