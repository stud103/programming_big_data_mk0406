import math

def addition(x, y):
    print x+y
    return x + y

def subtraction(x, y):
    print x - y
    return x - y
    
def multiplication(x, y):
    print x * y
    return x * y      

def division(x, y):
    if y == 0:
        print 'Error'
        return 'Error'      
    print  x / float(y)   
    return x / float(y)
    
def exponentiation(x, y):
    print x ** y
    return x ** y     
    
def power(x, y):
    print math.pow(x, y)
    return math.pow(x, y)     
   
def square_root(x):
    print math.sqrt(x)
    return math.sqrt(x)

def cube(x):
    print x ** 3
    return x ** 3

def logarithm(x):
    if x <= 0:
        print 'Error'
        return 'Error'       
    print round((math.log(x)), 2) 
    return round((math.log(x)), 2)   

def factorial(x):
    if x == 0:
        return 1
    if x < 0:
        return None
    else:
        return x * factorial(x - 1)
        
def cube_root(x):
    if 0<=x: 
        print int(round(x**(1./3.)))
        return int(round(x**(1./3.)))
    print int(round(-(-x)**(1./3.)))    
    return int(round(-(-x)**(1./3.)))        
