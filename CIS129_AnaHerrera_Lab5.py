# Module 5 Lab-5
# Author: Ana Herrera
# Date: 3/6/2024
# Description:

# Lab 5 The Bottle Return Program
# Declaring Variables
total_bottles = 0
total_payout = 0.0

# Loop to run the program again
while True:
    # Get user input for bottles returned
    bottles_returned = int(input("Enter the number of bottles returned: "))

    # Calculate total payout
    total_payout = bottles_returned * 0.10

    # Display results
    print("Total bottles returned:", bottles_returned)
    print(f"Total payout: ${total_payout:.2f}")

    # Ask if the user wants to enter data for another week
    user_input = input("Do you want to enter another week's worth of data? (Enter y or n): ")

    # End the loop if the user enters 'n'
    if user_input.lower() != 'y':
        break
