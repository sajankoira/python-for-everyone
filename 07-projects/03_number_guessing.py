"""
PROJECT 3: Number Guessing Game
"""
import random

def guessing_game():
    print("🎯 Number Guessing Game")
    print("I'm thinking a number between 1 and 100")
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts+1}/{max_attempts} - Your guess: "))
        except ValueError:
            print("Enter valid number!")
            continue

        attempts += 1

        if guess == secret:
            print(f"🎉 Correct! You guessed in {attempts} attempts!")
            return
        elif guess < secret:
            print("Too low! 📉")
        else:
            print("Too high! 📈")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Hints: {remaining} attempts left, secret is {'even' if secret%2==0 else 'odd'}")

    print(f"\nGame Over! Secret was {secret}")

if __name__ == "__main__":
    guessing_game()
