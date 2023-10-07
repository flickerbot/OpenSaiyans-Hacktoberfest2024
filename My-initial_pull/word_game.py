import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "dog", "elephant",
             "frog", "giraffe", "hamburger", "icecream", "jacket"]

# Function to choose a random word from the list


def choose_random_word():
    return random.choice(word_list)

# Function to play the word guessing game


def word_guessing_game():
    word_to_guess = choose_random_word()
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6  # Number of attempts allowed

    print("Welcome to the Word Guessing Game!")
    print(" ".join(guessed_word))  # Display the initial state of the word

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
            print(" ".join(guessed_word))
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")

        if "".join(guessed_word) == word_to_guess:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if "".join(guessed_word) != word_to_guess:
        print("You ran out of attempts. The word was:", word_to_guess)


# Start the game
word_guessing_game()
