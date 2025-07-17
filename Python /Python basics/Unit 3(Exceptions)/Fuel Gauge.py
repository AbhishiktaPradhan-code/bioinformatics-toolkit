while True:
    try:
        # Ask the user to input fuel in the format X/Y (e.g., 3/4)
        fraction = input("Fraction: ")
        
        # Split the input string by '/' to separate numerator and denominator
        X, Y = fraction.split("/")
        
        # Convert both parts to integers
        X = int(X)
        Y = int(Y)

        # Make sure denominator is not zero and X is not greater than Y
        if Y == 0 or X > Y:
            continue  # Invalid input, restart the loop

        # Calculate the percentage of fuel
        percent = round((X / Y) * 100)

        # If 1% or less fuel remains, print "E" (Empty)
        if percent <= 1:
            print("E")

        # If 99% or more fuel remains, print "F" (Full)
        elif percent >= 99:
            print("F")

        # Otherwise, print the percentage followed by %
        else:
            print(f"{percent}%")

        break  # Exit the loop after a valid input is processed

    except (ValueError, ZeroDivisionError):
        # If input is not properly formatted or causes division by zero,
        # catch the error and prompt the user again
        continue