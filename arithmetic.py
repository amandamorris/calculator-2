def add(number_list):
    """Return the sum of numbers"""
    #number = ()
    summation = 0
    for num in number_list:
        summation = summation + int(num)
    return summation

def subtract(number_list):
    """Return the difference of numbers"""
    difference = int(number_list[0]) * 2
    for num in number_list:
        difference = difference - int(num)
    return difference

def multiply(number_list):
    """Return the product of numbers"""
    product = 1
    for num in number_list:
        product = product * int(num)
    return product

def divide(number_list):
    """Return the quotient of numbers as a float"""
    dividor = float(number_list[0]) ** 2
    for num in number_list:
        dividor = dividor / float(num)
    return dividor

def square(number_list):
    """Return the square of a list of numbers"""
    for num in number_list:
        print int(num) ** 2
    return ""

def cube(number_list):
    """Return the cube of a list of numbers"""
    for num in number_list:
        print int(num) ** 3
    return ""

def power(num, exponent):
    """Return num raised to the power of exponent"""
    return num ** exponent

def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2
