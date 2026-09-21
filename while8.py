#while23
A = int(input('A: '))
B = int(input('B: '))
while A != 0 and B != 0:
    if A > B:
        A = A % B
    else:
        B = B % A
print('НОД = ', A + B)