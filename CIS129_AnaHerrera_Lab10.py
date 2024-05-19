# Module 10 Lab
# Author: Ana Herrera
# Date: 4/30/2024
# Description: This is exercise 8.1 on Deitel & Deitel

def protect_check_amount(amount):
    amount_str = str(amount)
    if len(amount_str) < 10:
        num_astericks = 10 - len(amount_str)
        protected_amount = '*' * num_astericks + amount_str
    else:
        protected_amount = amount_str
    return protected_amount

while True:
    amount_input = input("Enter the dollar amount (or 'quit' to exit): ")
    if amount_input.lower() == 'quit':
        print("Exiting")
        break
    
    try: 
        amount = float(amount_input)
        protected_amount = protect_check_amount(amount)
        print("This is the Protected amount:", protected_amount)
        continue
    except ValueError:
        print("Please enter a valid number.")