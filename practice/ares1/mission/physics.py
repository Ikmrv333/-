import math

G0 = 9.80665

def delta_v(m0, m1, isp=300):
    """Характеристическая скорость по формуле Циолковского, м/с."""
    if m1 <= 0 or m0 < m1 or isp <= 0:
        raise ValueError("Требуется m0 >= m1 > 0 и isp > 0")
    return isp * G0 * math.log(m0 / m1)

def flight_time(distance_km, accel):
    """Время перелёта в часах при разгоне на половине пути и торможении."""
    if distance_km <= 0 or accel <= 0:
        raise ValueError("Расстояние и ускорение должны быть положительными")
    distance_m = distance_km * 1000
    return 2 * math.sqrt((distance_m / 2) / accel) / 3600

def fuel_needed(m_dry, target_dv, isp=300):
    """Масса топлива для заданной характеристической скорости, кг."""
    if m_dry <= 0 or target_dv < 0 or isp <= 0:
        raise ValueError("Сухая масса и удельный импульс должны быть положительными, target_dv неотрицательна")
    exponent = target_dv / (isp * G0)
    try:
        return m_dry * math.expm1(exponent)
    except OverflowError as exc:
        raise ValueError("Требуемая скорость слишком велика для расчёта") from exc
