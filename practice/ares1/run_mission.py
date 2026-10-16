import argparse
import csv
import sched
import time
from pathlib import Path
from mission import delta_v, flight_time, fuel_needed, random_event

def build_parser():
    parser = argparse.ArgumentParser(description="Симулятор межпланетной миссии АРЕС-1")
    parser.add_argument("--days", type=int, default=5, help="длительность миссии, сутки")
    parser.add_argument("--seed", type=int, default=None, help="зерно генератора случайных чисел")
    parser.add_argument("--speed", type=float, default=0.2, help="секунд на одни условные сутки")
    parser.add_argument("--csv", type=str, default=None, help="путь для сохранения хроники в CSV")
    return parser

def main():
    args = build_parser().parse_args()
    if args.days < 1:
        raise SystemExit("Параметр --days должен быть не меньше 1")
    if args.speed < 0:
        raise SystemExit("Параметр --speed не может быть отрицательным")
    resource = 100
    history = []
    scheduler = sched.scheduler(time.monotonic, time.sleep)
    start = time.monotonic()
    print("=" * 62)
    print("МИССИЯ «АРЕС-1»: Марс")
    print("=" * 62)
    print(f"Характеристическая скорость (Циолковский): {delta_v(45000, 20000):.1f} м/с")
    print(f"Топлива для dv = 4000 м/с при сухой массе 20 т: {fuel_needed(20000, 4000):,.0f} кг")
    hours = flight_time(78_340_000, 0.003)
    print(f"Время перелёта 78,340 тыс. км при a = 0.003 м/с^2: {hours:,.0f} ч = {hours / 24:,.0f} сут")
    print("-" * 62)

    def day_report(day):
        nonlocal resource
        event_seed = args.seed + day if args.seed is not None else None
        description, change = random_event(event_seed)
        resource = max(0, min(100, resource + change))
        print(f"Сутки {day:>2} | {description:<38s} {change:+3d} | ресурс {resource:3d}% {'#' * (resource // 5)}")
        history.append({"day": day, "event": description, "change": change, "resource": resource})
        if resource == 0:
            for event in list(scheduler.queue):
                scheduler.cancel(event)
            return
        if day < args.days:
            scheduler.enter(args.speed, 1, day_report, (day + 1,))

    scheduler.enter(args.speed, 1, day_report, (1,))
    scheduler.run()
    elapsed = time.monotonic() - start
    print("-" * 62)
    status = "Миссия завершена" if resource > 0 and len(history) == args.days else "Миссия аварийно прервана"
    print(f"{status}. Итоговый ресурс: {resource}%. Реальное время симуляции: {elapsed:.2f} с")
    if args.csv:
        output = Path(args.csv)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=["day", "event", "change", "resource"])
            writer.writeheader()
            writer.writerows(history)
        print("Хроника сохранена:", output.resolve())

if __name__ == "__main__":
    main()
