from .stats import char_stats, word_count

def main():
    text = "Привет, мир! Это мой первый пакет."
    print("Слов:", word_count(text), "| Статистика:", char_stats(text))

if __name__ == "__main__":
    main()
