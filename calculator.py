#https://github.com/meadowjp/lab10-MP-RB
# Partner 1: Meadow Parks
# Partner 2: Richard Bennett

import math
# First example
def add(a, b): 
    return a+b
    
def subtract(a, b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a, b):
    try:
        b/a
    except ZeroDivisionError:
        return "Division error"
    return b/a
    
def logarithm(a,b):
    try:
        math.log(a,b)
    except ValueError:
        return "Value error"
    return math.log(a,b)
    
def exp(a,b):
    return math.exp(a*b)

def hypotenuse(a,b):
    sum = math.pow(a,2) + math.pow(b,2)
    result = math.sqrt(sum)
    return result

def square_root(a):
    try:
        result = math.sqrt(a)
    except ValueError:
        return "Value Error"
    return result


