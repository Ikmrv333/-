import random

deck = [f"{value}{suit}" for suit in "♠♥♦♣" for value in "6789TJQKA"]
random.seed(7)
print("Всего карт в колоде:", len(deck))
print("Рука игрока (sample):", random.sample(deck, 5))
print("Карта дня (choice):", random.choice(deck))
weights = {"обычная": 70, "редкая": 25, "легендарная": 5}
loot = random.choices(list(weights), weights=list(weights.values()), k=5)
print("Лут (choices, 5 шт.):", loot)
random.shuffle(deck)
print("После shuffle:", deck[:6], "...")
print("\n--- Раздача 3 игрокам по 5 карт ---")
players = ["Алиса", "Борис", "Вера"]
pool = deck.copy()
for player in players:
    hand = random.sample(pool, 5)
    for card in hand:
        pool.remove(card)
    print(f"{player:6s}: {hand}")
