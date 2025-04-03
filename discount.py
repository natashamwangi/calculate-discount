def calculate_discount(price, discount_percent):
    #Calculates the final price after applying dicount
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: (Enter from 1 to 100): "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the final result
if discount_percentage >= 20:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price remains: {original_price:.2f}")