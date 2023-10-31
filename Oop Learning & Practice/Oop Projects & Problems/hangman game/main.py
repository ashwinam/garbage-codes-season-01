# Welcome to hangman @development
import random

class Hangman:
    def __init__(self, name):
        self.name = name
        self.word_list = ["Apple", "Bicycle", "Elephant", "Sunshine", "Guitar", "Rainbow",
                            "Butterfly", "Mountain", "Whisper", "Ocean", "Chocolate", "Universe", "Adventure", "Symphony", "Firefly", "Serendipity", "Harmony", "Tangerine", "Pillow", "Lighthouse"]
        self.__attempt = 6

    def select_random_word(self):
        random_word = random.choice(self.word_list)
        return random_word
    
    def __str__(self) -> str:
        return f"Hello {self.name}, Welcome to the Hangman!"


class Word:
    pass

if __name__ == '__main__':
    test = Hangman('ashwin')
    test.select_random_word()