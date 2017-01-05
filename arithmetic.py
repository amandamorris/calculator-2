def add(number_list):
    """Return the sum of numbers"""
    #number = ()
    summation = 0
    for num in number_list:
        summation = summation + int(num)
    return summation

def subtract(number_list):
    """Return the difference of two numbers"""
    difference = int(number_list[0]) * 2
    for num in number_list:
        difference = difference - int(num)
    return difference

def multiply(num1, num2):
    """Return the product of two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return float(num1) / float(num2)

def square(num):
    """Return the square of a number"""
    return num ** 2

def cube(num):
    """Return the cube of a number"""
    return num ** 3

def power(num, exponent):
    """Return num raised to the power of exponent"""
    return num ** exponent

def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2
