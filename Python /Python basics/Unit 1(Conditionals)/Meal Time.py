def main():
    # Prompt the user for input in HH:MM format
    time = input("Enter the time in 24-hour format (HH:MM): ")
    
    # Call convert() to get the time as a float (e.g., "7:30" → 7.5)
    hours = convert(time)

    # Check which meal time it is based on the float value
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")


def convert(time):
    # Split the string into hours and minutes
    hours, minutes = time.split(":")
    
    # Convert to float format: hours + (minutes/60)
    return float(hours) + float(minutes) / 60


# Ensures main() only runs when this file is executed directly
if __name__ == "__main__":
    main()

