import random
def hello():
    print("""
                Всем привет!
            Это игра Анаграмы!
        ___________________________
                Hello everyone!
            This is Anagrama game!
        
        
        Сейчас вам будет выведена анаграма.
        Ваша задача угадать исходное слово.
        """)


def wordChoice():
    words = ["меч", "анаграма", "клей",
             "трактор", "яблоко", "такси",
             "магия", "программирование", "молния",
             "питон", "интернет", "шкаф"]
    word = random.choice(words)
    print(word)


def main():
    hello()
    wordChoice()
