# Welcome to hangman @development
import random


class Hangman:

    def __init__(self, name):
        self.name = name
        self.word_list = ["Apple", "Bicycle", "Elephant", "Sunshine", "Guitar", "Rainbow",
                            "Butterfly", "Mountain", "Whisper", "Ocean", "Chocolate", "Universe", "Adventure", "Symphony", "Firefly", "Serendipity", "Harmony", "Tangerine", "Pillow", "Lighthouse"]
        self.__attempt = 6 # limited number of attempts
        self.word = random.choice(self.word_list)

    def __str__(self) -> str:
        return f"Hello {self.name}, Welcome to the Hangman!"
    
    def return_random_word(self): # selecting random word
        return self.word
    
    def setup_game_board(self):
        word_len = len(self.word)
        underscores = '_ ' * word_len
        return underscores
    
    @property
    def attempt(self):
        return self.__attempt
    


class Word:
    pass

if __name__ == '__main__':
    test = Hangman('ashwin')
    print(f'word to guess: ', test.setup_game_board())
    print(f'Attempts left: ', test.attempt)