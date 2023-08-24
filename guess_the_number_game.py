import random

def generate_random_number():
    """This function helps to generate a random four-digit number."""
    return random.randint(1000, 9999)

def get_user_guess():
    """ This helps to get the user's guess for the four-digit number."""
    guess = input("Enter your guess: ")
    while len(guess) != 4:  # Validate that the guess is four characters long
        print("Please enter a four-digit guess.")
        guess = input("Enter your guess: ")
    return guess

def get_number_of_correct_digits(guess, number):
    """Gets the number of correct digits in the user's guess."""
    correct_digits = 0
    for i in range(4):
        if guess[i] == str(number)[i]:
            correct_digits += 1
    return correct_digits

def get_number_of_correct_positions(guess, number):
    """Gets the number of correct positions in the user's guess."""
    correct_positions = 0
    for i in range(4):
        if guess[i] in str(number):
            correct_positions += 1
    return correct_positions

def play_game():
    """This function implements the main game loop where the user guesses the
    number and receives feedback on the correctness of their guess. The game
    continues until the user guesses correctly or decides to quit."""
    number = generate_random_number()
    attempts = 0
    while True:
        guess = get_user_guess()
        correct_digits = get_number_of_correct_digits(guess, number)
        correct_positions = get_number_of_correct_positions(guess, number)
        print(f"{correct_digits} correct digits, {correct_positions} correct positions.")
        attempts += 1
        if correct_digits == 4:
            print(f"You guessed the number in {attempts} attempts!")
            break
        if input("Do you want to quit? (y/n): ") == "y":
            break

def main():
    play_game()

if __name__ == "__main__":
    main()
