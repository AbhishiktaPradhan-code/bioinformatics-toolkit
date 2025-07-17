# This is the main function that runs the overall program
def main():
    # Call get_number() to get a positive integer from the user
    number = get_number()
    # Call meow() to print "meow" that many times
    meow(number)


# Function to repeatedly ask the user for a number until it's positive
def get_number():
    while True:
        # Ask user to input an integer
        n = int(input("What's n? "))
        # If it's a positive number, break the loop
        if n > 0:
            break
    # Return the valid positive number
    return n


# Function to print "meow" n times
def meow(n):
    for _ in range(n):
        print("meow")


# Call main() to start the program
main()