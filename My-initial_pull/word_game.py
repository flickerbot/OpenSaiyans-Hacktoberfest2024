import random

class WordGuessingGame:
    def __init__(self):
        self.word_list = ["apple", "banana", "cherry", "dog", "elephant",
                          "frog", "giraffe", "hamburger", "icecream", "jacket"]
        self.hints = {
            "apple": ["A fruit that is often red or green.", "Keeps the doctor away."],
            "banana": ["A long, yellow fruit.", "Monkeys love it."],
            "cherry": ["A small, round fruit that is often red.", "Often found on top of desserts."],
            "dog": ["A common domestic animal.", "Man's best friend."],
            "elephant": ["The largest land animal.", "Has a trunk."],
            "frog": ["An amphibian known for its jumping abilities.", "Often found near water."],
            "giraffe": ["The tallest land animal with a long neck.", "Has spots."],
            "hamburger": ["A popular fast food item.", "Often served with fries."],
            "icecream": ["A cold dessert that comes in many flavors.", "Melts quickly."],
            "jacket": ["A piece of clothing worn on the upper body.", "Keeps you warm."]
        }
        self.score = 0
        self.games_played = 0

    def choose_random_word(self):
        return random.choice(self.word_list)

    def provide_hint(self, word, hint_index):
        return self.hints.get(word, ["No hint available."])[hint_index]

    def play(self):
        play_again = True

        while play_again:
            self.games_played += 1
            word_to_guess = self.choose_random_word()
            guessed_word = ["_"] * len(word_to_guess)
            attempts = 6
            guessed_letters = set()
            hint_index = 0

            print("\nWelcome to the Advanced Word Guessing Game!")
            print(" ".join(guessed_word))
            print("Hint:", self.provide_hint(word_to_guess, hint_index))

            while attempts > 0 and "_" in guessed_word:
                guess = input("Guess a letter: ").lower()

                if len(guess) != 1 or not guess.isalpha():
                    print("Invalid input. Please enter a single letter.")
                    continue

                if guess in guessed_letters:
                    print("You already guessed that letter. Try again.")
                    continue

                guessed_letters.add(guess)

                if guess in word_to_guess:
                    for idx, letter in enumerate(word_to_guess):
                        if letter == guess:
                            guessed_word[idx] = guess
                    print("Good guess!")
                else:
                    attempts -= 1
                    hint_index = min(hint_index + 1, len(self.hints[word_to_guess]) - 1)
                    print(f"Wrong guess. You have {attempts} attempts left.")
                    print("Hint:", self.provide_hint(word_to_guess, hint_index))

                print(" ".join(guessed_word))

            if "_" not in guessed_word:
                self.score += 1
                print("Congratulations! You've guessed the word correctly.")
            else:
                print(f"Game over. The word was '{word_to_guess}'.")

            play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"

        print(f"\nThanks for playing! You played {self.games_played} games and scored {self.score} points.")

if __name__ == "__main__":
    game = WordGuessingGame()
    game.play()
