#!/usr/bin/python3
# Path to python interpreter

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating the final price
final_price = calculate_discount(original_price, discount_percentage)

# Displaying the result
if final_price != original_price:
    print("Final price after applying the discount:", final_price)
else:
    print("No discount applied. Final price is the original price:", original_price)
