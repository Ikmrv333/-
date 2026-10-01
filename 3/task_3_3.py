import math

def compound_interest(principal, rate, years, n=12):
    """Сложный процент с капитализацией n раз в год."""
    return principal * (1 + rate / n) ** (n * years)

def continuous_compound(principal, rate, years):
    """Непрерывное начисление процентов."""
    return principal * math.exp(rate * years)

def loan_payment(principal, rate, years):
    """Аннуитетный платёж по кредиту."""
    monthly_rate = rate / 12
    n = years * 12
    return principal * monthly_rate * (1 + monthly_rate) ** n / ((1 + monthly_rate) ** n - 1)

P = 100000
r = 0.08
for years in [1, 5, 10, 20]:
    a = compound_interest(P, r, years)
    b = continuous_compound(P, r, years)
    print(f"{years:2d} лет: капитализация={a:10.2f} руб., непрерывно={b:10.2f} руб.")

print("\nПлатёж по кредиту 1 000 000 руб. на 10 лет под 12%:")
payment = loan_payment(1_000_000, 0.12, 10)
print(f"Ежемесячный платёж: {payment:.2f} руб.")
print(f"Общая выплата: {payment * 120:.2f} руб.")
print(f"Переплата: {payment * 120 - 1_000_000:.2f} руб.")