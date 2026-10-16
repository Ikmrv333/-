import random

EVENTS = [
    ("Микрометеорит пробил обшивку", -15, 0.4),
    ("Солнечная вспышка: радиация", -10, 0.2),
    ("Удачная коррекция курса", 5, 0.2),
    ("Найдены запасы предыдущей миссии", 20, 0.1),
    ("Отказ системы охлаждения", -25, 0.1),
]

def random_event(seed=None):
    """Возвращает описание случайного события и изменение ресурса."""
    rnd = random.Random(seed)
    weights = [event[2] for event in EVENTS]
    description, delta, weight = rnd.choices(EVENTS, weights=weights, k=1)[0]
    return description, delta
