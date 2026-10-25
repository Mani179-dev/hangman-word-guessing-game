#import random

#with open("google-10000-english-no-swears.txt", "r") as file:
    #words = file.read().splitlines()

#secret_word = random.choice(words).lower()

#print("Welcome to Hangman!")
#print("The word has", len(secret_word), "letters.")
import random


# -------------------- CONSTANTS --------------------

WORD_FILE = "google-10000-english-no-swears.txt"
MAX_MISTAKES = 6

HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


# -------------------- WORD FUNCTIONS --------------------

def load_words(filename):
    """Load valid words from the provided word-list file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = [
                line.strip().upper()
                for line in file
                if line.strip().isalpha()
            ]
    except FileNotFoundError:
        print(f"Error: Could not find '{filename}'.")
        return []

    return words


def choose_word(words):
    """Select one random secret word."""
    return random.choice(words)


# -------------------- DISPLAY FUNCTIONS --------------------

def display_word(word, guessed_letters):
    """Return the current visible form of the secret word."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def display_gallows(mistakes):
    """Display the Hangman drawing for the current mistake count."""
    print(HANGMAN_STAGES[mistakes])


def show_status(word, guessed_letters, mistakes):
    """Display the current game information."""
    print("Word:", display_word(word, guessed_letters))

    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: None")

    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")


# -------------------- INPUT FUNCTION --------------------

def get_guess(guessed_letters):
    """Get and validate one new letter from the player."""

    guess = input("Enter a letter: ").strip().upper()

    if len(guess) != 1:
        print("Please enter exactly one letter.")
        return None

    if not guess.isalpha():
        print("Please enter an alphabetic letter.")
        return None

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'.")
        return None

    return guess


# -------------------- GAME LOGIC --------------------

def update_game(word, guess, guessed_letters):
    """
    Store the guess and return whether it is present
    in the secret word.
    """
    guessed_letters.add(guess)
    return guess in word


def is_word_complete(word, guessed_letters):
    """Check whether every letter in the word has been guessed."""
    return all(letter in guessed_letters for letter in word)


# -------------------- MAIN GAME --------------------

def play_game(word):
    """Run one complete Hangman game."""

    guessed_letters = set()
    mistakes = 0

    print("\n" + "=" * 40)
    print("        HANGMAN WORD GAME")
    print("=" * 40)

    while mistakes < MAX_MISTAKES:

        display_gallows(mistakes)
        show_status(word, guessed_letters, mistakes)

        guess = get_guess(guessed_letters)

        if guess is None:
            continue

        correct = update_game(
            word,
            guess,
            guessed_letters
        )

        if correct:
            print(f"✓ Good guess! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"✗ '{guess}' is not in the word.")

        if is_word_complete(word, guessed_letters):
            display_gallows(mistakes)
            print("\n🎉 Congratulations!")

            print(f"You guessed the word: {word}")

            return
        display_gallows(MAX_MISTAKES)

    print("\nGame Over!")
    print(f"The correct word was: {word}")


# -------------------- PROGRAM START --------------------

def main():
    """Load the word list and start the game."""

    words = load_words(WORD_FILE)

    if not words:
        print("No valid words were loaded.")
        print("Please check the word-list file.")
        return

    secret_word = choose_word(words)

    play_game(secret_word)


if __name__ == "__main__":
    main()
