import random

random.seed(42)
print("random():", round(random.random(), 3))
print("uniform(1, 18):", round(random.uniform(1, 18), 3))
print("randint(1, 6):", random.randint(1, 6))
print("randrange(6, 100, 5):", random.randrange(6, 100, 5))

print("\n-- Бросок двух кубиков, 5 раз --")
for i in range(5):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(f"Бросок {i+1}: {a} + {b} = {a+b}")

# *** TODO ***
N = 10_000
counts = [0] * 6
start = 1                     
random.seed(226)              

for _ in range(N):
    face = random.randint(start, 6)
    counts[face - start] += 1

print("\n-- Статистика 10000 бросков одного кубика --")
theoretical_prob = N / 6      

for face, cnt in enumerate(counts[start:], start=start):
    bar = "#" * int(cnt // 50)          
    deviation = abs((cnt - theoretical_prob) / theoretical_prob) * 100 
    
    print(
        f"{face}: {cnt:>5} ({cnt/N:.2f}%)\t"
        f"[Теория: {int(theoretical_prob)}, Откл.: ±{deviation:.2f}%]\t"
        f"{bar}"
    )