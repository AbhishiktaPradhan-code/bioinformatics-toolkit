
x = input("Greetings! ").strip().lower()

# If the greeting starts with "hello", respond with $0
if x.startswith("hello"):
    print("$0")
# If the greeting starts with "h" but not "hello", respond with $20
elif x.startswith("h"):
    print("$20")
# For any other greeting, respond with $100
else:
    print("$100")