import math

print("Простые числа до 50:")
primes = [n for n in range(2, 51) if all(n % d != 0 for d in range(2, math.isqrt(n) + 1))]
print(primes)

print("\nНОД и НОК:")
pairs = [(12, 18), (48, 180), (7, 13), (100, 75)]
for a, b in pairs:
    print(f"  НОД({a},{b}) = {math.gcd(a, b)}, НОК({a},{b}) = {math.lcm(a, b)}")

print("\nКомбинаторика:")
print(f"  C(10,3) = {math.comb(10, 3)}")
print(f"  A(10,3) = {math.perm(10, 3)}")
print(f"  C(49,6) = {math.comb(49, 6)} (шанс угадать 6 из 49)")

print("\nФакториалы:")
for n in range(1, 11):
    print(f"  {n}! = {math.factorial(n)}")