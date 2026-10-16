import math

def word_count(text: str) -> int:
    return len(text.split())

def char_stats(text: str) -> dict:
    letters = [char for char in text if char.isalpha()]
    n = len(text)
    entropy = -sum(text.count(char) / n * math.log2(text.count(char) / n) for char in set(text)) if n else 0.0
    return {"всего": n, "букв": len(letters), "уникальных": len(set(char.lower() for char in letters)), "энтропия": round(entropy, 3)}
