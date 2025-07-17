def main():
    # Prompt user for camelCase input
    camel = input("camelCase: ")
    
    # Start with an empty snake_case result
    snake = ""

    # Loop over each character in the camelCase input
    for c in camel:
        if c.isupper():
            # If the character is uppercase, add an underscore and the lowercase version
            snake += "_" + c.lower()
        else:
            # If the character is lowercase, add it as is
            snake += c

    # Print the snake_case result
    print("snake_case:", snake)

