Hangman Word Guessing Game

Project Overview

This project is a Python-based Hangman word guessing game. The player attempts to guess a randomly selected English word one letter at a time.

The game uses a provided English word list as its source of secret words and displays an ASCII Hangman figure as incorrect guesses increase.

Features

- Random word selection from the provided English word list
- Hidden word display using underscores
- Single-letter input validation
- Tracking of previously guessed letters
- Detection of repeated guesses
- Maximum of 6 incorrect guesses
- ASCII Hangman stages
- Win and game-over conditions
- Clear console-based game interface

Technologies Used

- Python
- Python Standard Library
- "random"
- Text-file handling

How the Game Works

1. The program loads words from the provided ".txt" file.
2. A random word is selected.
3. The selected word is hidden using underscores.
4. The player enters one letter at a time.
5. Correct letters are revealed.
6. Incorrect guesses increase the mistake count.
7. The Hangman drawing changes after each incorrect guess.
8. The player wins when all letters are revealed.
9. The game ends after 6 incorrect guesses.

Project Files

hangman-word-guessing-game/
│
├── hangman.py
├── google-10000-english-no-swears.txt
└── README.md

How to Run

Make sure Python is installed.

Open the project folder in a terminal and run:

python hangman.py

The word-list file must remain in the same folder as "hangman.py".

Learning Objectives

This project demonstrates the use of:

- Functions
- Loops
- Conditional statements
- Sets
- Lists
- Strings
- File handling
- Random selection
- Input validation
- Modular program design

Author

Manikanta Vykuntam
