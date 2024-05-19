# Module 7 Lab
# Author:
# Date: 4/2/2024
# Description: This program displays different seatings and shows availability of some or not.

# Constants/Functions
sectionNames = ['A', 'B', 'C']
sectionPrices = {'A': 20, 'B': 15, 'C': 10}
sectionCapacities = {'A': 300, 'B': 500, 'C': 200}

# Displays welcome message
def displayWelcome():
    print("Welcome!")
    print("Section prices:")
    for section in sectionNames:
        print(f"Section {section}: ${sectionPrices[section]} per seat")
        print("")

# Gets the number of tickets sold for each section
def get_tickets_sold(section):
    while True:
        try:
            tickets = int(input(f"Enter the number of tickets sold for section {section}: "))
            if tickets < 0:
                print("Please enter a positive number.")
            elif tickets > sectionCapacities[section]:
                print(f"Sorry, there are only {sectionCapacities[section]} seats available in section {section}.")
            else:
                return tickets
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Calculates subtotal per section
def calculate_subtotal(section, tickets_sold):
    return tickets_sold * sectionPrices[section]

# Main function
def main():
    displayWelcome()
    total_income = 0
    section_sales = {section: 0 for section in sectionNames}

    for section in sectionNames:
        tickets_sold = get_tickets_sold(section)
        subtotal = calculate_subtotal(section, tickets_sold)
        total_income += subtotal
        section_sales[section] += subtotal

        print(f"Subtotal for section {section}: ${subtotal}")
        print(f"Total income: ${total_income}\n")

    print("Overall Summary:")
    for section in sectionNames:
        print(f"Section {section}: {sectionCapacities[section]} seats, subtotal: ${section_sales[section]}")
    print(f"Overall total income: ${total_income}")
main()