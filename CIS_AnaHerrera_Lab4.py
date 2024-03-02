# Module 4 Lab-4
# Author: Ana Herrera
# Date: 2/29/2024
# Description: This program calculates store and employee bonuses based on monthly sales and sales increase percentage.

# declare local variables 
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
employeeAmount = 0 # employee bonus amount 
salesIncrease = 0 # percent of sales increase
prompt = 'enter monthly sales:' # prompt will be a string literal

# this code gets the monthly sales
monthlySales = float(input(prompt))

# this code determines the store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# this code gets the percent of increase in sales
salesIncrease = float(input("Enter the percent of increase in sales: "))
salesIncrease = salesIncrease / 100

# this code determines the employee bonus
if salesIncrease >= 0.05:
    employeeAmount = 75
elif salesIncrease >= 0.04:
    employeeAmount = 50
elif salesIncrease >= 0.03:
    employeeAmount = 40
else:
    employeeAmount = 0

# this code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", employeeAmount)
if storeAmount == 6000 and employeeAmount == 75:
    print('Congrats! You have reached the highest bonus amounts possible!')