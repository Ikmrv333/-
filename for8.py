#for8
A = int(input('A: '))
B = int(input('B: '))
p = 1
for i in range(A, B + 1):
    p *= i
print('Произведение = ', p)