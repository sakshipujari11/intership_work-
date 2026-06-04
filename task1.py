import random
import os

# Word list with hints
word_list = {
    "python": "A popular programming language",
    "tiger": "A wild animal",
    "beach": "A sandy place near water",
    "apple": "A common fruit",
    "robot": "A machine that can perform tasks"
}

# Randomly choose word and hint
word, hint = random.choice(list(word_list.items()))

# Game setup
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

# Hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    --------
    """
]

# Welcome screen
print("🎮 =============================== 🎮")
print("        WELCOME TO HANGMAN         ")
print("🎮 =============================== 🎮")
print(f"💡 Hint: {hint}")

# Game loop
while attempts > 0 and "_" in guessed_word:
    print(hangman_stages[6 - attempts])
    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print("Attempts Left:", attempts)

    guess = input("👉 Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only ONE valid letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")

# Final result
if "_" not in guessed_word:
    print("\n🎉 CONGRATULATIONS! YOU WON!")
    print("🏆 The word was:", word)
else:
    print(hangman_stages[6])
    print("\n💀 GAME OVER!")
    print("❗ The word was:", word)