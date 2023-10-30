## Hangman Game Problem Statement

You are tasked with developing a Hangman game in Python using object-oriented programming principles. The game should provide an interactive and enjoyable experience for players.

## Game Rules and Requirements:

1. The game randomly selects a word from a predefined list of words.
2. The player has a limited number of attempts (e.g., 6) to guess the word.
3. The word to guess is displayed as a series of underscores initially, with spaces representing word spaces (e.g., "_ _ _ _ _ _" for the word "hangman").
4. The player can guess one letter at a time. If the guessed letter is in the word, all occurrences of that letter are revealed.
5. If the guessed letter is not in the word, the player loses one attempt.
6. The player wins if they correctly guess the word within the allowed attempts or loses if they run out of attempts.
7. Display the current state of the word and the number of attempts left after each guess.
8. Allow the player to see the list of previously guessed letters.
9. Display a message at the end of the game, indicating whether the player won or lost and reveal the complete word.

## Object-Oriented Design:

1. Create a HangmanGame class to manage the game's state and logic.
2. Implement methods within the class for selecting a random word, displaying the current word state, handling guesses, tracking the number of attempts, and checking for a win or loss.
3. Use a separate class, such as Word, to represent the word to be guessed. This class can handle operations like revealing letters and checking for a win.

## User Interface:

- Implement a simple text-based user interface for the game that allows the player to input guesses and displays the game's current state.

## Additional Features (Optional):

You can add more features to enhance the game, such as:

- The ability to choose different categories of words (e.g., animals, fruits, movies).
- A scoring system to track the player's performance.
- Hints or difficulty levels.
- Visual representation of the hangman based on the number of incorrect guesses.

## Testing:

- Write unit tests for your classes and methods to ensure that the game functions correctly.

## Example Interaction:

```
Welcome to Hangman!

Word to guess: _ _ _ _ _
Attempts left: 6

Guess a letter: a

Word to guess: _ a _ _ _
Attempts left: 6

Guess a letter: t

Word to guess: _ a t _ _
Attempts left: 6

...

Guess a letter: g

Word to guess: _ a t g a n
Attempts left: 6

Congratulations! You've won. The word was "hangman."

```