import math

def projectile_range(v0, angle_deg, g=9.81):
    """Дальность полёта снаряда."""
    angle_rad = math.radians(angle_deg)
    return (v0 ** 2 * math.sin(2 * angle_rad)) / g

def max_height(v0, angle_deg, g=9.81):
    """Максимальная высота подъёма."""
    angle_rad = math.radians(angle_deg)
    return (v0 ** 2 * math.sin(angle_rad) ** 2) / (2 * g)

def flight_time(v0, angle_deg, g=9.81):
    """Время полёта."""
    angle_rad = math.radians(angle_deg)
    return (2 * v0 * math.sin(angle_rad)) / g

v0 = 100
for angle in [15, 30, 45, 60, 75]:
    r = projectile_range(v0, angle)
    h = max_height(v0, angle)
    t = flight_time(v0, angle)
    print(f"Угол {angle:2d}°: дальность={r:7.2f} м, высота={h:6.2f} м, время={t:5.2f} с")