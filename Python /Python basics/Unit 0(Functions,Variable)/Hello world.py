# to take input for name from user remove space and capitalize the first letter of each word
name=input("what is your name? ").strip().title()

# to remove the whitespace and capitalize user's name
# name = name.strip().title()

# to Capitalize user's name (only the first letter)
# name = name.capitalize()

# to make title based capitalization
#>name= name.title()

# Split the user's name into first and last name
First , last  = name.split(" ")

# to print the name
print("Hello, ", First)




