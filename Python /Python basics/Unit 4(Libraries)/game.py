import random

# Function to repeatedly prompt for a positive integer
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass

# Get level
level = get_positive_int("Level: ")

# Generate random number between 1 and level
number = random.randint(1, level)

# Prompt guesses until correct
while True:
    guess = get_positive_int("Guess: ")
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break