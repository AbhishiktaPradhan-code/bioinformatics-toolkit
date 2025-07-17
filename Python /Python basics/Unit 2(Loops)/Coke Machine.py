# Total amount that needs to be paid
amount_due = 50

# Keep asking the user for coins until the amount due is 0 or less
while amount_due > 0:
    # Prompt user to insert a coin
    coin = int(input("Insert coin (5, 10, or 25): "))
    
    # Check if coin is valid
    if coin in [5, 10, 25]:
        # Subtract valid coin from amount due
        amount_due -= coin
    else:
        # Ignore invalid coins
        print("Invalid coin.")

    # If more money is still needed, print how much is due
    if amount_due > 0:
        print(f"Amount due: {amount_due}")
        
# Once enough has been paid (amount_due ≤ 0), calculate and show change
print(f"Change owed: {abs(amount_due)}")    
