Height=float(input("Enter your height in m: " ))
Weight=float(input("Enter your weight in kg: "))
# Calculate BMI
BMI = Weight / (Height ** 2)
# Print the BMI
print(f"Your BMI is: {BMI:.2f}")
# Determine the BMI category
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("You have a normal weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")
elif 30 <= BMI < 34.9:
    print("You have obesity (Class 1).")
elif 35 <= BMI < 39.9:
    print("You have obesity (Class 2).")
elif BMI >= 40:
    print("You have obesity (Class 3).")
# The code calculates the Body Mass Index (BMI) based on user input for height and weight, and categorizes the BMI into different weight classes.