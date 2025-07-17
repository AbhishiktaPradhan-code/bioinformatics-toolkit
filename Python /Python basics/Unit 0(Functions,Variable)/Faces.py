#defines the main() function, which is the starting point of your program’s logic.
def main():
    user_input=input("what is your emoji?")

    result=convert(user_input)
    """This line calls the convert function, giving it the user’s input as an argument.
	•	It saves whatever convert() returns into a variable named result.
    """
    print(result)
    """	•	This line prints the final converted text (with emojis) to the screen so the user can see it.
	•	Without this line, the result would be calculated but never shown."""

def convert(emoji):
   
    emoji=emoji.replace(":)","😀")
    emoji=emoji.replace(":(","😢")
    
    return emoji
"""	This gives the modified string back to the place where convert() was called (in main())"""
main()
#	•	This calls the main() function, which kicks off the whole program.