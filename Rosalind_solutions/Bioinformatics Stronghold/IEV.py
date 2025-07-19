def expected_dominant_offspring(couples):
    # Probabilities that a child will show the dominant phenotype for each couple type
    dominant_probabilities = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    
    # Multiply each couple count by the corresponding probability
    expected = 0
    for count, prob in zip(couples, dominant_probabilities):
        expected += count * prob
    
    # Each couple has 2 children
    return 2 * expected

# Example input: number of couples with each genotype pairing
# Format: [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa]
input_couples = [1,0,0,1,0,1]

# Calculate and print the expected number of dominant phenotype offspring
result = expected_dominant_offspring(input_couples)
print(f"Expected number of dominant phenotype offspring: {result}")