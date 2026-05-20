import random

lowest = 1
highest = 100
target = random.randint(lowest, highest)

# print(target)
guesses = 0

is_running = True
while is_running:
    guess = int(input(f"Guess a number between {lowest} and {highest}: "))
    guesses += 1

    if guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {target} in {guesses} guesses!")
        is_running = False