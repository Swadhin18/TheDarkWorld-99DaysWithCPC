import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        
        if user_guess < number:
            print("Too low! Try again.")
        elif user_guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break

number_guessing_game()
