import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I have chosen a number between 1 and 100.")
    print("Can you guess what it is?")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Take user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Start the game yes sorry for t
if __name__ == "__main__":
    guess_the_number()
