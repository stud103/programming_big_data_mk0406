import math

def show_menu():
    print '*****************************'
    print 'MENU:'
    print 'Press 1 to use addition'
    print 'Press 2 to use subtraction'
    print 'Press 3 to use multiplication'
    print 'Press 4 to use division'
    print 'Press 5 to use exponentiation'
    print 'Press 6 to use power'
    print 'Press 7 to use square_root'
    print 'Press 8 to use cube'
    print 'Press 9 to use logarithm'
    print 'Press 10 to use factorial'
    print 'Press Q to quit the program'
    print '*****************************'

def addition(x, y):
    add = x + y
    return add

def subtraction(x, y):
    subs = x - y
    return subs
    
def multiplication(x, y):
    mult = x * y
    return mult     

def division(x, y):
    if y == 0:
        return 'Error'      
    div = x / float(y)   
    return div
    
def exponentiation(x, y):
    expo = x ** y
    return expo   
    
def power(x, y):
    power = math.pow(x, y)
    return power
    
def square_root(x):
    sqrt_r = math.sqrt(x)
    return sqrt_r  

def cube(x):
    cube = x ** 3
    return cube

def logarithm(x):
    if x <= 0:
        return 'Error'       
    loga = round((math.log(x)), 2) 
    return loga  

def factorial(x):
    if x == 0:
        return 1
    if x < 0:
        return None
    else:
        fact = x * factorial(x - 1)
        return fact
       

while True:
    show_menu()
    s_inp = raw_input ('Please choose one option from the Menu:\n')
    if s_inp == 'Q':
        break
    try:
        choice = float (s_inp)
    except:
        print 'Invalid input. Please enter corret input'
        continue
    if choice <1 or choice >11:
        print'Invalid input. Please enter corret input'
        continue
        
    if choice >=1 and choice <=6:
        x = float(raw_input('Enter No 1 please\n'))
        y = float(raw_input('Enter No 2 please\n'))
        
    elif choice >=7 and choice <=10:    
        x = float(raw_input('Enter a number please\n'))
       
    else:    
        x = raw_input('Enter a decimal number please\n')   
        if x < 0:
            x = int(x)
        elif x >= 0:
            x = float(x)

# Calculation and output
    
    if choice == 1:
        add = addition(x, y)
        print add
        
    elif choice == 2:
        subs = subtraction(x, y)
        print subs  

    elif choice == 3:
        mult = multiplication(x, y)
        print mult

    elif choice == 4:
        div = division(x, y)
        print div 

    elif choice == 5:
        expo = exponentiation(x, y)
        print expo

    elif choice == 6:
        power = power(x, y)
        print power               
        
    elif choice == 7:
        sqrt_r = square_root(x)
        print sqrt_r
        
    elif choice == 8:
        cube = cube(x)
        print cube 

    elif choice == 9:
        loga = logarithm(x)
        print loga

    elif choice == 10:
        fact = factorial(x)
        print fact                
        
    else:
        print'Invalid input. Please enter corret input'
        continue
        
    if 'Q' == raw_input('Press Q to Quit / Enter to continue \n'):
        break
        
print'Thank you and Goodbye'   

        
