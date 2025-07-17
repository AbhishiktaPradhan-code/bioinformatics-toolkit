# dna_analysis.py

import sys

# 1. Sample DNA sequences
sequences = [
    "ATCGTACGATCG",
    "GGGCCCATAAAA",
    "TTTTGGGCGCGC",
    "ACTGACTGACTG",
    "CGATCGATTTGC"
]

# 2. Function to calculate GC content
def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

# 3. Function to compute reverse complement using dictionary
def reverse_complement(seq):
    # Dictionary mapping each nucleotide to its complement
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # Reverse the input sequence (e.g., 'ATGC' becomes 'CGTA')
    rev_seq = reversed(seq)
    
    # Initialize an empty string to store the reverse complement
    rev_comp = ''
    
    # Loop through each base in the reversed sequence
    for base in rev_seq:
        # Add the complement of each base to the new string
        rev_comp += complement[base]
    
    # Return the final reverse complement string
    return rev_comp

# 4. Function to process a list of DNA sequences
def analyze_sequences(seq_list):
    # Loop over each sequence in the list with an index starting from 1
    for i, seq in enumerate(seq_list, 1):
        # Calculate GC content using a separate function (assumes gc_content(seq) is already defined)
        gc = gc_content(seq)
        
        # Get the reverse complement using the reverse_complement function
        rev_comp = reverse_complement(seq)
        
        # Print the sequence number and the original sequence
        print(f"\nSequence {i}: {seq}")
        
        # Print the length of the sequence
        print(f"Length: {len(seq)}")
        
        # Print the GC content percentage, formatted to 2 decimal places
        print(f"GC Content: {gc:.2f}%")
        
        # Print the reverse complement of the sequence
        print(f"Reverse Complement: {rev_comp}")


import sys

# Check if more than one argument is passed (i.e., the script + at least one sequence)
if len(sys.argv) > 1:
    # Take the first command-line argument (after the script name) and convert to uppercase
    input_seq = sys.argv[1].upper()
    
    # Notify the user that a command-line input was detected
    print("\n⏩ Command-line input detected!")
    
    # Display the input sequence
    print(f"Input Sequence: {input_seq}")
    
    # Print the GC content of the input sequence
    print(f"GC Content: {gc_content(input_seq):.2f}%")
    
    # Print the reverse complement of the input sequence
    print(f"Reverse Complement: {reverse_complement(input_seq)}")

else:
    # 6. If no command-line input is provided, analyze a predefined list of sequences
    analyze_sequences(sequences)
