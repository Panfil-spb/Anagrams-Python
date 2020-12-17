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
    return word

def anagrams(word):
    anagram = ""
    while word != "":
        choise = random.randrange(0, len(word))
        anagram += word[choise]
        word = word[:choise] + word[(choise + 1):]
    return anagram

def game(word, anagram):
    answer = ""
    while answer != word:
        print("Ваша анаграма: " + anagram)
        answer = input("Введите ваше слово:")
        if answer != word:
            print("Ответ не верный!\n"
                  "Попробуйте еще раз.")
    print("Поздравляю вас!"
          "Анаграмма " + anagram + " - это " + answer)

def main():
    hello()
    word = wordChoice()
    anagram = anagrams(word)
    game(word, anagram)


main()