#for12
N = int(input('N: '))
p = 1
for i in range(1, N + 1):
    p *= 1 + i / 10
print('Произведение = ', p)