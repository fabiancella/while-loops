import random

# Function to run game again
def game_choice():
    choice = input("\nWould you like to play again (y/n): ")
    if choice.lower() == "n":
        print("\nHave a great day!")
        return False
    elif choice.lower() == "y":
        return True
    else:
        print("Invalid choice. Please enter 'y' or 'n'")
        return game_choice()

print("Welcome to the Guessing Game App")
running = True
while running:

    # Guess words
    word_1 = "baseball"
    word_2 = "banana"
    word_3 = "cat"

    # Input user guesses and create loop for game
    print("\nGuess an 8-letter word from the following category: Sports")
    guess_limit = 5
    while guess_limit > 0:
        guess_limit -= 1
        guess = input("Enter your guess: ")
        if guess == word_1:
            print("Correct")
            break
        elif guess_limit == 0:
            print("Ran out of guesses")

    # Asks user to play again (y/n)
    running = game_choice()
    if not running:
        break # exits the loop

    # Runs the game again with different guess word
    print("\nGuess a 6-letter word from the following category: Fruit")
    guess_limit = 5
    while guess_limit > 0:
            guess_limit -= 1
            guess = input("Enter your guess: ")
            if guess == word_2:
                print("Correct")
                break
            elif guess_limit == 0:
                print("Ran out of guesses")

    # Asks user to play again (y/n)
    running = game_choice()
    if not running:
        break

    # Runs the game with different guess word
    print("\nGuess a 3-letter word from the following category: House pet")
    guess_limit = 5
    while guess_limit > 0:
        guess_limit -= 1
        guess = input("Enter your guess: ")
        if guess == word_3:
            print("Correct")
            break
        elif guess_limit == 0:
            print("Ran out of guesses")

    # Asks user to play again (y/n)
    running = game_choice()
    if not running:
        break



