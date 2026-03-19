import random

# List of words
words = [
    "python", "programming", "developer", "hangman",
    "computer", "science", "artificial", "intelligence",
    "machine", "learning"
]

# Hints for words
hints = {
    "python": "A popular programming language",
    "programming": "Writing code",
    "developer": "Person who writes software",
    "hangman": "This game!",
    "computer": "Electronic device",
    "science": "Systematic study",
    "artificial": "Not natural",
    "intelligence": "Ability to learn",
    "machine": "Mechanical device",
    "learning": "Gaining knowledge"
}

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("🎮 Welcome to Hangman Game!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("\nHint:", hints[word])

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            print("❌ Wrong guess!")
            attempts -= 1

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
