# Lab 7-3 The Dice Game
# Author:
# Date: 3/28/2024
# Description: This program simulates a dice game.

# add libraries needed
import random

# the main function
def main():
    print()

    # initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    # call to inputNames
    playerOne, playerTwo = inputName(playerOne, playerTwo)

    # while loop to run program again
    while endProgram == 'no':

        # populate variables
        winnersName = 'NO NAME'
        p1number = 0
        p2number = 0

        # call to rollDice
        winnersName = rollDice(p1number, p2number, playerOne, playerTwo, winnersName)

        # call to displayInfo
        displayInfo(winnersName)
        endProgram = input('Do you want to end program? (yes/no): ')

#this function gets the players names
def inputName(playerOne, playerTwo):
    playerOne = input("Enter player one's name: ")
    playerTwo = input("Enter player two's name: ")
    return playerOne, playerTwo

#this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnersName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    
    if p1number > p2number:
        winnersName = playerOne
    elif p2number > p1number:
        winnersName = playerTwo
    else: 
        winnersName = "TIE"
    return winnersName

#this function displays the winner
def displayInfo(winnersName):
    print(winnersName)

# calls main
main()

# i followed the word document but its not working how i want it too :<