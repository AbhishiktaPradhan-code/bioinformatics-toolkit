import inflect

# Create inflect engine
p = inflect.engine()

# Empty list to store names
names = []

# Prompt user for names until EOF (Ctrl+D)
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    print()  # Move cursor to new line

# Generate the formatted list of names
formatted_names = p.join(names)

# Print the farewell message
print(f"Adieu, adieu, to {formatted_names}")