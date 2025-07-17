def two_sum(numbers, target):
    # Dictionary to store numbers we've seen so far and their indices
    seen = {}
    
    # Iterate over the list with index and value
    for index, num in enumerate(numbers):
        # Calculate the complement number needed to reach the target sum
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in seen:
            # If yes, return the pair of indices: complement's index and current index
            return [seen[complement], index]
        
        # Otherwise, store the current number and its index in the dictionary
        seen[num] = index
    
    # If no such pair is found, return None
    return None

result = two_sum(numbers, target)
print("Indexes of numbers that sum to target:", result)