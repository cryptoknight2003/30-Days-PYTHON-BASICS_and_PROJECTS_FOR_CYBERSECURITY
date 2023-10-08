import random
import time

def choose_random_word():
    # List of words to choose from
    word_list = ["python", "hangman", "programming", "challenge", "coding"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6  # You can customize this to change the difficulty

    print("Welcome to Hangman!")

    while True:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            print("Incorrect!")
            incorrect_guesses += 1

        if incorrect_guesses == max_attempts:
            print("\nYou ran out of attempts! The word was:", word_to_guess)
            break

        if set(word_to_guess).issubset(guessed_letters):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break
time.sleep(1)

if __name__ == "__main__":
    hangman()

