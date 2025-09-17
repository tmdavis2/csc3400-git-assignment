import math


def add():
    num1 = int(input("Please enter a number:"))
    num2 = int(input("Please enter another number:"))
    return num1 + num2 

def subtract():
    num1 = int(input("Please enter a number:"))
    num2 = int(input("Please enter another number:"))
    return num1 - num2 

def multiply():
    num1 = int(input("Please enter a number:"))
    num2 = int(input("Please enter another number:"))
    return num1 * num2 

def divide():
    while True:
        num1 = int(input("Please enter a number:"))
        num2 = int(input("Please enter another number:"))
        if num2 != 0:
            break
        else:
            print("Invalid input, try again\n")

    return num1 / num2
    

def power():
    num1 = int(input("Please enter a number:"))
    num2 = int(input("Please enter another number:"))
    
    return num1 ** num2

def square_root():
    while True:
        num1 = int(input("Please enter a number:"))
        if num1 >= 0:
            break
        else:
            print("Invalid input, try again\n")

    return math.sqrt(num1)

