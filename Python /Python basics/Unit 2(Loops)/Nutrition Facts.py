# Define a dictionary with fruit names and their corresponding calories per portion
fruit_calories = {
    'apple': 95,
    'banana': 105,
    'cherry': 50,
    'grape': 62,
    'kiwi': 42,
    'lemon': 17,
    'lime': 20,
    'mango': 150,
    'orange': 62,
    'peach': 59,
    'pear': 102,
    'plum': 46,
    'pineapple': 82,
    'strawberry': 4,
    'blueberry': 57,
    'watermelon': 30,
    'raspberry': 52,
    'blackberry': 43,
    'apricot': 48
}

def main():
    # Prompt the user to input a fruit name
    fruit = input("Enter a fruit name: ").strip().lower()

    # Check if the fruit exists in the dictionary
    if fruit in fruit_calories:
        print(f"The calories in one portion of {fruit.capitalize()} are {fruit_calories[fruit]} calories.")
    else:
        print("Sorry, that fruit is not recognized. Please enter a valid fruit from the list.")

if __name__ == "__main__":
    main()