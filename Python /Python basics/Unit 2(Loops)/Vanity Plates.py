def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: All characters must be alphanumeric (no spaces, punctuation, etc.)
    if not s.isalnum():
        return False

    # Rule 3: The first two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Rule 4: Numbers must come at the end and not start with '0'
    number_started = False
    for c in s:
        if c.isdigit():
            if not number_started:
                # First digit should not be 0
                if c == '0':
                    return False
                number_started = True
        else:
            if number_started:
                # Letter after number is not allowed
                return False

    # Passed all checks
    return True


main()