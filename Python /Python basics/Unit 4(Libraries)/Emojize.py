import emoji

def main():
    # Prompt user for input string
    user_input = input("Input: ")

    # Convert codes or aliases to emoji using emoji.emojize
    # language="alias" tells it to recognize aliases like ":thumbsup:"
    output = emoji.emojize(user_input, language="alias")

    # Print the emojized string
    print(f"Output: {output}")

if __name__ == "__main__":
    main()