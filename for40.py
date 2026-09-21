#for40
A = int(input('A: '))
B = int(input('B: '))
for i in range(A, B + 1):
    for j in range(i - A + 1):
        print(i)