# Define the menu as a dictionary with items and their prices
def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.0  # Variable to keep track of the total cost

    # Loop to take multiple inputs until the user signals EOF (Ctrl-D)
    while True:
        try:
            # Prompt the user for an item and format it to match the menu keys
            item = input("Item: ").strip().title()

            # Check if the item exists in the menu
            if item in menu:
                # Add the item's price to the total
                total += menu[item]
                # Display the running total, formatted to two decimal places
                print(f"Total: ${total:.2f}")

            # If the item is not on the menu, ignore and continue
        except EOFError:
            # When the user inputs Ctrl-D, exit the loop
            print("\n")  # Print a newline for clean formatting
            break

# This ensures the main function runs only when the file is executed directly
if __name__ == "__main__":
    main()