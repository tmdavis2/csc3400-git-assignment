from calculator import add, subtract, power, multiply, divide, square_root

print("Which arithmetic function would you like to use?\n" \
    "\nEnter the coressponding number for the function\n" \
    "\n1 : Addition\n" \
    "2 : Subtraction\n" \
    "3 : Multiplication\n" \
    "4 : Division\n" \
    "5 : Power\n" \
    "6 : Square Root\n" \
    "7 : QUIT\n" \
    "8 : Function List")

def get_number():
    while True:
        try:
            user_input = input("\nEnter a number: ").strip()

            if not user_input:
                print("\nPlease enter a value. Try again")
                continue

            return float(user_input)
        except ValueError:
            print("\nPlease enter a numeric value")
        except KeyboardInterrupt:
            print("Exiting")
            return None
        

while True:
    
    function = int(input("Enter Function: "))
    print("")
    
    #additon
    if function == 1:
        num1 = get_number()
        num2 = get_number()
        answer = add(num1, num2)
        print("\nAnswer: ", answer, "\n")
    #subtraction
    elif function == 2:
        num1 = get_number()
        num2 = get_number()
        answer = subtract(num1, num2)
        print("\nAnswer: ", answer, "\n")
    #multiplication
    elif function == 3:
        num1 = get_number()
        num2 = get_number()
        answer = multiply(num1, num2)
        print("\nAnswer: ", answer, "\n")
    #division
    elif function == 4:
        num1 = get_number()
        while True:
            num2 = get_number()
            if num2 != 0:
                break
            else:
                print("Invalid input, try again\n")
        answer = divide(num1, num2)
        print("\nAnswer: ", answer, "\n")
    #power
    elif function == 5:
        num1 = get_number()
        num2 = get_number()
        answer = power(num1, num2)
        print("\nAnswer: ", answer, "\n")
    #sqaure root
    elif function == 6:
        while True:
            num1 = get_number()
            if num1 >= 0:
                break
            else:
                print("Invalid input, try again\n")
        answer = square_root(num1)
        print("\nAnswer: ", answer, "\n")
    #quit
    elif function == 7:
        break
    #operation list
    elif function == 8:
        print("\n1 : Addition\n" \
    "2 : Subtraction\n" \
    "3 : Multiplication\n" \
    "4 : Division\n" \
    "5 : Power\n" \
    "6 : Square Root\n" \
    "7 : QUIT\n" \
    "8 : Function List\n")
    else:
        print("Error\n")
    