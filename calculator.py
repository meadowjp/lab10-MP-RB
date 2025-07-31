#https://github.com/meadowjp/lab10-MP-RB
# Partner 1: Meadow Parks
# Partner 2: Richard Bennett

import math
# First example
def add(a, b): 
    return a+b
    
def sub(a, b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a, b):
    try:
        b/a
    except ZeroDivisionError:
        return "Division error"
    return b/a
    
def log(a,b):
    try:
        math.log(a,b)
    except ValueError:
        return "Value error"
    return math.log(a,b)
    
def exp(a,b):
    return math.exp(a*b)



