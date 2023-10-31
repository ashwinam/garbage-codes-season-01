# Welcome to hangman @development
import random


class Hangman:

    def __init__(self, name):
        self.name = name
        self.word_list = ["Apple", "Bicycle", "Elephant", "Sunshine", "Guitar", "Rainbow",
                            "Butterfly", "Mountain", "Whisper", "Ocean", "Chocolate", "Universe", "Adventure", "Symphony", "Firefly", "Serendipity", "Harmony", "Tangerine", "Pillow", "Lighthouse"]
        self.__attempt = 6 # limited number of attempts

    def __str__(self) -> str:
        return f"Hello {self.name}, Welcome to the Hangman!"
    
    def return_random_word(self): # selecting random word
        random_word = random.choice(self.word_list)
        return random_word
    
    def setup_game_board(self):
        word = self.return_random_word()
        word_len = len(word)
        underscores = '_ ' * word_len
        return underscores
    


class Word:
    pass

if __name__ == '__main__':
    test = Hangman('ashwin')
    print(test.return_random_word())
    print(test.setup_game_board())