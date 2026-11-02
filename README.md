# Hangman Game

A simple text-based Hangman game written in Python. The computer picks a secret word and the player guesses it one letter at a time.

Built for revision of python.

## Features

- Picks a random word from a list of 5 predefined words
- Player guesses one letter at a time
- Shows the word with blanks for letters not guessed yet (for example `p _ t h _ n`)
- Allows a maximum of 6 incorrect guesses
- Tells the player if they win or lose at the end
- Runs fully in the console, with no graphics or audio

## Built With

- Python 3
- Standard library only (`random` module), so nothing extra to install

## Concepts Used

- `random` module
- `while` loop
- `if-else` statements
- Strings
- Lists

## How the Game Works

1. The program randomly chooses one word from a list of 5 words.
2. The word is displayed as blanks, one for each letter.
3. The player types one letter per turn.
4. A correct guess reveals that letter everywhere it appears in the word.
5. A wrong guess uses up one of the 6 chances.
6. The game ends when the player guesses the whole word (win) or runs out of chances (lose).

## How to Run

1. Make sure Python 3 is installed:

   ```
   python --version
   ```

2. Clone the repository:

   ```
   git clone https://github.com/bishwash-codes/CodeAlpha_hangmangame.git
   cd hangman_game
   ```

3. Run the game:

   ```
   python hangman.py
   ```

## Example Gameplay

```
=== Hangman Game ===
_ _ _ _ _ _
Wrong guesses left: 6
Guess a letter: p
p _ _ _ _ _
Wrong guesses left: 6
Guess a letter: z
Wrong! You have 5 guesses left.
...
You won! The word was python.
```

## Project Structure

```
hangman_game/
├── hangman.py
├── README.md
```

## Limitations

- Uses only 5 predefined words
- Text-only, with no graphics

## Author

**Bishwash Poudel**
GitHub: [bishwash-codes](https://github.com/bishwash-codes)

