import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def say(text):
    print(f"[{time.strftime('%H:%M:%S')}] {text}")


start = time.time()
scheduler.enter(0.5, 1, say, ("Прошло 0.5 секунды",))
scheduler.enter(1, 1, say, ("Прошла 1 секунда",))
scheduler.enter(2, 0, say, ("Прошло 2 секунды (приоритет 0)",))
scheduler.enter(2, 1, say, ("Прошло 2 секунды (приоритет 1)",))
scheduler.enterabs(start + 3, 0, say, ("Абсолютное время t0 + 3 с",))

print("Старт. Отсчёт времени от t0 = 0")
print("Очередь до run():", len(scheduler.queue), "задач")
scheduler.run()
print("Готово. Пустая очередь?", scheduler.empty())
