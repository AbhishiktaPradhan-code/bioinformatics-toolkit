# Prompt the user to input the arithmetic expression
expression = input("Enter an arithmetic expression: ")

# Split the input into components (x, operator, z)
try:
    x, operator, z = expression.split()

    # Convert x and z to integers and operator remains a string
    x = int(x)
    z = int(z)

    # Perform the operation based on the input operator and print the result formatted to one decimal place
    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        # Handle division by zero
        if z == 0:
            print("Error: Division by zero is not allowed.")
            exit()  # Exit if division by zero is attempted
        result = x / z
    else:
        print("Invalid operator")
        exit()  # Exit if the operator is invalid

    # Output the result, formatted to one decimal place
    print(f"{result:.1f}")

except ValueError:
    print("Invalid input format. Please enter in the form 'x operator z'.")