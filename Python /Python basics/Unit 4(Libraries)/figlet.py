import sys
import pyfiglet
import random

def main():
    # Get available fonts
    fonts = pyfiglet.FigletFont.getFonts()

    # Handle command-line arguments
    if len(sys.argv) == 1:
        # Random font
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid font name.")
    else:
        sys.exit("Usage: python figlet.py [-f FONT]")

    # Prompt for input
    text = input("Input: ")

    # Render and print the text
    figlet = pyfiglet.Figlet(font=font)
    print("Output:\n")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()