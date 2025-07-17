# Main function that calculates the tip based on user input
def main():
    # Ask the user for the meal cost, convert it to float using dollars_to_float()
    dollars = dollars_to_float(input("How much was the meal? "))
    
    # Ask the user for the tip percentage, convert it to float using percent_to_float()
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip by multiplying cost with percentage
    tip = dollars * percent
    
    # Print the tip amount rounded to 2 decimal places
    print(f"Leave ${tip:.2f}")

# Function to convert dollar string (e.g. "$50") to float (e.g. 50.0)
def dollars_to_float(d):
    d = d.replace("$", "")  # Remove the dollar sign
    return float(d)         # Convert the remaining string to float

# Function to convert percent string (e.g. "15%") to float (e.g. 0.15)
def percent_to_float(p):
    p = p.replace("%", "")  # Remove the percent sign
    return float(p) / 100   # Convert to float and divide by 100 to get decimal

# Call the main function to run the program
main()