import sys
import math
import random

print("Версия Python:", sys.version.split()[0])
print("Интерпретатор:", sys.executable)
print("Количество путей поиска:", len(sys.path))
print("Первые 4 пути поиска:")
for path in sys.path[:4]:
    print("    ", path)
print("math.pi =", math.pi)
print("random.random() =", random.random())
print("Всего загружено модулей:", len(sys.modules))
print("Первые 5 модулей:", sorted(sys.modules)[:5])
public_names = [name for name in dir(math) if not name.startswith("_")]
print("Публичных имён в math:", len(public_names))
print("Мой __name__ =", __name__)
