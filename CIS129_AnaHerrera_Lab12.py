# Module 10 Lab
# Author: Ana Herrera
# Date: 5/17/2024
# Description: This code will convert a previous "Create a Pet Class" code to Python.

class pet:
    def __init__(self, name='', type='', age=0):
        self.name = name
        self.type = type
        self.age = age
    
    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setAge(self, age):
        self.age = age
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getAge(self):
        return self.age

def main():
    inputName = ""
    inputType = ""
    inputAge = 0

    animal = pet()

    inputName = input("enter a pet type:")
    animal.setName(inputName)

    inputType = input("enter a pet type: ")
    animal.setType(inputType)

    inputAge = int(input("enter a pet age: "))
    animal.setAge(inputAge)

    print("the pet name is", animal.getName())
    print("the pet type is", animal.getType())
    print("the pet age is", animal.getAge())

if __name__ == "__main__":
    main()