
def add(a, b):
    return a + b

def subtract(c, d):
    return c - d

def multiply(x, y):
    return x * z

def divide(y, z):
    return y / z

print("Which arithmetic function would you like to use?\n" \
    "\nEnter the coressponding number for the function\n" \
    "\n1 : Addition\n" \
    "2 : Subtraction\n" \
    "3 : Multiplication\n" \
    "4 : Division\n" \
    "5 : QUIT\n" \
    "6 : Function List")

while True:
    
    function = int(input("Enter Function: "))

    if function == 1:
        print("")
        num1 = int(input("You have chosen Addition, Please enter the first number:"))
        num2 = int(input("Enter the second:"))

        answer = num1 + num2

        print("\nAnswer: ", answer, "\n\n")

    elif function == 2:
        print("")
        num1 = int(input("You have chosen Subtraction, Please enter the first number:"))
        num2 = int(input("Enter the second:"))

        answer = num1 - num2

        print("\nAnswer: ", answer, "\n\n")
    elif function == 3:
        print("")
        num1 = int(input("You have chosen Multiplication, Please enter the first number:"))
        num2 = int(input("Enter the second:"))

        answer = num1 * num2

        print("\nAnswer: ", answer, "\n\n")
    elif function == 4:
        print("")
        num1 = int(input("You have chosen Division, Please enter the first number:"))
        num2 = int(input("Enter the second:"))

        answer = num1 / num2

        print("\nAnswer: ", answer, "\n\n")
    elif function == 5:
        break
    elif function == 6:
        print("\n1 : Addition\n" \
    "2 : Subtraction\n" \
    "3 : Multiplication\n" \
    "4 : Division\n" \
    "5 : QUIT\n" \
    "6 : Function List\n")
    else:
        print("Error\n")
    