import sys
import os

def is_venv():
    return sys.prefix != sys.base_prefix

def venv_path():
    if is_venv():
        return sys.prefix
    return None

def site_packages():
    import site
    return site.getsitepackages()

print("В виртуальном окружении?", is_venv())
print("Путь к окружению:", venv_path())
print("site-packages:", site_packages())
print("Python:", sys.version.split()[0])
print("Executable:", sys.executable)

if is_venv():
    print("\nРекомендация: окружение активно, можно устанавливать пакеты.")
else:
    print("\nВнимание: вы в глобальном Python. Создайте venv!")