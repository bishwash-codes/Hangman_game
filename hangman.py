import random

# List of words
words = ["machine", "computer", "programming", "pattern", "scientist"]

word = random.choice(words)

guessed_word = ["_"] * len(word)

attempts = 6
guessed_letters = []

print("===== HANGMAN GAME =====")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong guess!")
        attempts -= 1

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You won tough guy!")
    print("The word was:", word)
else:
    print("\nGame Over lil fella!")
    print("The word was:", word)
