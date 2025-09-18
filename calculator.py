import math
   
def add(num1, num2):
    return num1 + num2 

def subtract(num1, num2):
    return num1 - num2 

def multiply(num1, num2):
    return num1 * num2 

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2
    

def power(num1, num2):
    return num1 ** num2

def square_root(num1):
    if num1 < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(num1)
