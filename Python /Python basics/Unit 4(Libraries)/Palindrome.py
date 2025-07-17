def is_palindrome(s):
    """
    Check if the input string s is a palindrome.
    A palindrome reads the same forward and backward.
    """
    # Remove spaces and convert to lowercase for uniform comparison
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse using conditionals
    if s == s[::-1]:
        return True
    else:
        return False

# Example usage
test_str = input("Enter a string to check if it's a palindrome: ")  
result = is_palindrome(test_str)
print(f'Is "{test_str}" a palindrome? {result}')