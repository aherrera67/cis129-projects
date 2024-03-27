# Module 6 Lab-6
# Author: Ana Herrera
# Date: 3/26/2024
# Description: This code demonstrates the attempt in calculation of the number of packages of hot dogs and the number of hot dog buns needed for a cookout. 
               
def main():
   # constant variables
   dogs = 10
   buns = 8

   # local variable
   total = getTotalHotDogs()

   # calculate the number of left over hot dogs
   dogsLeft = (dogs - total % dogs) % dogs

   # calculate the minimum number 
   minDogs = total // dogs + (1 if dogsLeft > 0 else 0)

   # calculate the number of left over hot dog buns
   bunsLeft = (buns - total % buns) % buns 

   # calculate the minimum number of packages
   minBuns = total // buns + (1 if bunsLeft > 0 else 0) 

   # display the result
   showResults(dogsLeft, minDogs, bunsLeft, minBuns)

def getTotalHotDogs():
   # get the number of people attending the cookout
   people = int(input("Enter the number of people attending the cookout:"))

   # get the number of hot dogs each person will be given
   hotDogs = int(input("Enter the number of hot dogs for each person: "))

   # calculate the total number of hot dogs needed.
   total = people * hotDogs
   return total

def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
   # display the minimum packages of hot dogs needed
   print("Minimum packages of hot dogs needed:", minDogs)

   # display the minimum packages of buns needed
   print("Minimum packages of hot buns needed:", minBuns)

   # display the number of hot dogs left over
   print("Hot dog buns left over:", dogsLeft)

   # display the number of hot dog buns left over.
   print("Hot dog buns left over:", bunsLeft)