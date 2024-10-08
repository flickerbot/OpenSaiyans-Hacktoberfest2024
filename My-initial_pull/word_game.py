import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "dog", "elephant",
             "frog", "giraffe", "hamburger", "icecream", "jacket"]

# Function to choose a random word from the list
def choose_random_word():
    return random.choice(word_list)

# Function to provide hints for the chosen word
def provide_hint(word):
    hints = {
        "apple": "A fruit that is often red or green.",
        "banana": "A long, yellow fruit.",
        "cherry": "A small, round fruit that is often red.",
        "dog": "A common domestic animal.",
        "elephant": "The largest land animal.",
        "frog": "An amphibian known for its jumping abilities.",
        "giraffe": "The tallest land animal with a long neck.",
        "hamburger": "A popular fast food item.",
        "icecream": "A cold dessert that comes in many flavors.",
        "jacket": "A piece of clothing worn on the upper body."
    }
    return hints.get(word, "No hint available.")

# Function to play the word guessing game
def word_guessing_game():
    score = 0  # Initialize score
    play_again = True  # Flag for playing multiple rounds

    while play_again:
        word_to_guess = choose_random_word()
        guessed_word = ["_"] * len(word_to_guess)
        attempts = 6  # Number of attempts allowed

        print("Welcome to the Word Guessing Game!")
        print(" ".join(guessed_word))  # Display the initial state of the word
        print("Hint:", provide_hint(word_to_guess))  # Provide a hint

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
                score += 1  # Increase score for a correct guess
                break

        if "".join(guessed_word) != word_to_guess:
            print("You ran out of attempts. The word was:", word_to_guess)

        print("Your current score:", score)

        # Ask the player if they want to play again
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False

# Start the game
word_guessing_game()