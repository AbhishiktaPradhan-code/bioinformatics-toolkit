Sequence=input("Enter a sequence of DNA bases (A, T, C, G): ").strip().upper()
# Initialize a dictionary to count occurrences of each base
GC_count = Sequence.count("G")+Sequence.count("C")
Total_count = len(Sequence)
# Calculate the GC content percentage
GC_content = (GC_count / Total_count) * 100
# Print the GC content percentage
print(f"GC content: {GC_content:.2f}%")