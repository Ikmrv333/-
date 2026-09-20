#for13
N = int(input('N: '))
s = 0
for i in range(1, N + 1):
    s += (1 + i / 10) * ((-1) ** (i + 1))
print('Значение = ', s)