import random

# Step 1: Predefined word list
words = ["apple", "tiger", "chair", "robot", "plant",]

# Step 2: Choose a random word
word = random.choice(words)

# Step 3: Create empty display ( _ _ _ )
guessed_word = ["_"] * len(word)

# Step 4: Initialize variables
attempts = 6
guessed_letters = []

print("Welcome to Hangman Game!")

# Step 5: Game loop
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Step 6: Check correct or wrong guess
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

# Step 7: Result
if "_" not in guessed_word:
    print("\n You won! The word is:", word)
else:
    print("\n You lost! The word was:", word)