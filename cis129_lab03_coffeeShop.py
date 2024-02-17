// Author: Ana Herrera
// Date: 2-16-2024

def calculate_total(num_coffees, num_muffins):
    
    Calculates the total cost including tax for the given number of coffees and muffins.

    Parameters:
    - num_coffees (int): Number of coffees purchased
    - num_muffins (int): Number of muffins purchased

    Returns:
    - float: Total cost including tax
    
    coffee_price = 5
    muffin_price = 4
    tax_rate = 0.06

  // Calculate subtotal
    subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price)

  // Calculate tax
    tax = subtotal * tax_rate

  // Calculate total
    total = subtotal + tax

    return total

def main():
    
    Main function to execute the program.
    
  // Display welcome message
    print("***************************************")
    print("My Coffee and Muffin Shop")

  // Prompt user for input
    num_coffees = int(input("Number of coffees bought? "))
    num_muffins = int(input("Number of muffins bought? "))

  // Calculate total cost
    total_cost = calculate_total(num_coffees, num_muffins)

  // Display receipt
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{num_coffees} Coffee at $5 each: ${num_coffees * 5:.2f}")
    print(f"{num_muffins} Muffins at $4 each: ${num_muffins * 4:.2f}")
    print(f"6% tax: ${total_cost - (num_coffees * 5 + num_muffins * 4):.2f}")
    print("---------")
    print(f"Total: ${total_cost:.2f}")
    print("***************************************")

if __name__ == "__main__":
    main()
