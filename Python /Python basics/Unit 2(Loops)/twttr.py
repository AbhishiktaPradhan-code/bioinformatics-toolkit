# Prompt the user to enter a string
text = input("Input: ")

# String of vowels to remove (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Initialize an empty string to build the result
result = ""

# Loop through each character in the input text
for c in text:
    # If the character is not a vowel, add it to the result string
    if c not in vowels:
        result += c

# Print the final string without vowels
print(f"Output: {result}")