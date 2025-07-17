def main():
    # Dictionary to keep track of item counts
    grocery_list = {}

    # Use Ctrl-D (Unix/Linux/Mac) or Ctrl-Z (Windows) to signal EOF
    while True:
        try:
            item = input().strip().lower()  # Normalize to lowercase for consistency
            if item:
                # If item is already in the list, increment the count
                if item in grocery_list:
                    grocery_list[item] += 1
                else:
                    grocery_list[item] = 1
        except EOFError:
            print()  # For clean formatting before output
            break

    # Sort the items alphabetically
    for item in sorted(grocery_list):
        count = grocery_list[item]
        print(f"{count} {item.upper()}")  # Print count and item in uppercase


if __name__ == "__main__":
    main()