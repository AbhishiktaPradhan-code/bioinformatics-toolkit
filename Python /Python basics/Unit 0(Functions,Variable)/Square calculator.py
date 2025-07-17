def main():
    # Get user input
    number = int(input("Enter a number to calculate its square: "))
    print("The square of", number, "is", square(number))

def square(num):
    # Calculate the square of the number
    return num * num

main()