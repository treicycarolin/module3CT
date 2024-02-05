# Get the amount charged for the food from the user
food_charge = float(input("Enter the amount charged for the food: $"))

# Calculate the tip and sales tax
tip_percentage = 18
sales_tax_percentage = 7

tip_amount = (tip_percentage / 100) * food_charge
sales_tax_amount = (sales_tax_percentage / 100) * food_charge

# Calculate total amount
total_amount = food_charge + tip_amount + sales_tax_amount

# Display the results
print("\n*****Invoice Summary*****")
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
print(f"Sales Tax ({sales_tax_percentage}%): ${sales_tax_amount:.2f}")
print("---------------------------")
print(f"Total Amount: ${total_amount:.2f}")