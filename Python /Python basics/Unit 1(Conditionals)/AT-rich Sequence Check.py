Sequence=input("Enter a sequence of DNA bases (A, T, C, G): ").strip().upper()
# Initialize a dictionary to count occurrences of each base
AT_count = Sequence.count("A")+Sequence.count("T")
Total_count = len(Sequence)
# Calculate the AT content percentage
AT_content = (AT_count / Total_count) * 100
# Print the AT content percentage
print(f"AT content: {AT_content:.2f}%")
if AT_content > 60 :
    print("The sequence is AT-rich more than 60% AT content")
else:
    print("The sequence is not AT-rich")
# The code calculates the AT content of a DNA sequence and checks if it is AT-rich (more than 60% AT content).
