k = 22  # AA
m = 30  # Aa
n = 21 # aa
total = k + m + n
pairs = total * (total - 1)

# Probabilities for dominant offspring
prob_dom = 0

# AA x AA
prob_dom += (k * (k - 1)) * 1

# AA x Aa
prob_dom += (k * m * 2) * 1
#Why * 2? Because (AA, Aa) and (Aa, AA) are both possible (ordered pairs) 

# AA x aa
prob_dom += (k * n * 2) * 1

# Aa x Aa
prob_dom += (m * (m - 1)) * 0.75

# Aa x aa
prob_dom += (m * n * 2) * 0.5

# aa x aa → 0 contribution

prob_dom = prob_dom / pairs
print(f"Probability of dominant phenotype: {prob_dom:.5f}")