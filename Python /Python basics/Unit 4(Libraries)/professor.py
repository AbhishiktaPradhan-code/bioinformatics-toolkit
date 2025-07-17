import random

def main():
    level = get_level()  # Get the level (1, 2, or 3)
    score = 0  # Initialize score

    # Generate and ask 10 math problems
    for _ in range(10):
        x = generate_integer(level)  # Generate X (first number)
        y = generate_integer(level)  # Generate Y (second number)
        correct_answer = x + y  # Calculate the correct answer

        attempts = 0
        while attempts < 3:
            try:
                # Ask the user for an answer
                answer = int(input(f"{x} + {y} = "))
                
                if answer == correct_answer:
                    score += 1  # Increase score if answer is correct
                    break  # Move to the next question
                else:
                    print("EEE")  # Incorrect answer
                    attempts += 1
            except ValueError:
                print("EEE")  # Invalid input (not an integer)
                attempts += 1
        
        if attempts == 3:
            # After 3 incorrect answers, show the correct answer
            print(f"The correct answer was {correct_answer}")

    # Output the final score
    print(f"Your final score is {score} out of 10")

def get_level():
    # Prompt the user to input a valid level
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level  # Return the level if valid
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    # Generate a random integer with 'level' digits
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()