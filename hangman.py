import random

# List of words for the game
word_list = ["python", "hangman", "programming", "computer", "gaming", "coding", "challenge"]

# Select a random word from the list
chosen_word = random.choice(word_list)

# Convert the chosen word to lowercase
chosen_word = chosen_word.lower()

# Initialize variables
word_length = len(chosen_word)
guessed_word = ['_'] * word_length
attempts = 6
used_letters = []

# Function to display the current state of the game
def display_game():
    print(" ".join(guessed_word))
    print(f"Attempts left: {attempts}")
    print(f"Used letters: {' '.join(used_letters)}")

# Main game loop
while attempts > 0:
    display_game()
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in used_letters:
        print("You've already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
        if ''.join(guessed_word) == chosen_word:
            print("Congratulations! You've won. The word was:", chosen_word)
            break
    else:
        print("Incorrect guess.")
        attempts -= 1

if attempts == 0:
    print("Sorry, you're out of attempts. The word was:", chosen_word)
