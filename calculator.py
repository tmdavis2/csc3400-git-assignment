import math


def add(a, b):
    num1 = int(input("Please enter a number:"))
    num2 = int(input("Please enter another number:"))
    return num1 + num2 

def subtract(c, d):
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

print("Which arithmetic function would you like to use?\n" \
    "\nEnter the coressponding number for the function\n" \
    "\n1 : Addition\n" \
    "2 : Subtraction\n" \
    "3 : Multiplication\n" \
    "4 : Division\n"
    "5 : Power\n"
    "6 : Square Root\n" \
    "7 : QUIT\n" \
    "8 : Function List")

while True:
    
    function = int(input("Enter Function: "))
    print("")
    
    #additon
    if function == 1:
        answer = add(num1, num2)
        print("\nAnswer: ", answer, "\n")
    #subtraction
    elif function == 2:
        answer = subtract(num1, num2)
        print("\nAnswer: ", answer, "\n")
    #multiplication
    elif function == 3:
        answer = multiply()
        print("\nAnswer: ", answer, "\n")
    #division
    elif function == 4:
        answer = divide()
        print("\nAnswer: ", answer, "\n")
    #power
    elif function == 5:
        answer = power()
        print("\nAnswer: ", answer, "\n")
    #sqaure root
    elif function == 6:
        answer = square_root()
        print("\nAnswer: ", answer, "\n")
    #quit
    elif function == 7:
        break
    #operation list
    elif function == 8:
        print("\n1 : Addition\n" \
    "2 : Subtraction\n" \
    "3 : Multiplication\n" \
    "4 : Division\n"
    "5 : Power\n"
    "6 : Square Root\n" \
    "7 : QUIT\n" \
    "8 : Function List\n")
    else:
        print("Error\n")
    