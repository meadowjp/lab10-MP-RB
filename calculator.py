"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
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


#ANYTHING

