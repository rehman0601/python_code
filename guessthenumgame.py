import random

target = random.randint(1, 10)
guess = None

while guess != target:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")

print(f"Congratulations! You've guessed the number {target}.")
