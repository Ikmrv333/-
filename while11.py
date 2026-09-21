#while20
N = int(input('N: '))
found = False
while N > 0:
    if N % 10 == 2:
        found = True
    N //= 10
print(found)