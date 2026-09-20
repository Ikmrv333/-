#for18
A = float(input('A: '))
N = int(input('N: '))
s = 1
p = 1
for i in range(1, N + 1):
    p *= -A
    s += p
print('Значение = ', s)