#for16
A = float(input('A: '))
N = int(input('N: '))
p = 1
for i in range(1, N + 1):
    p *= A
    print(p)