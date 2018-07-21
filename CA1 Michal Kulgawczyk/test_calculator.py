import unittest

from calculator import *
from math import *

# test the calculator functionality (11 functions)

class TestCalculator (unittest.TestCase):  

# test the addition functionality
# 2 + 2 = 4
# 2 + 4 = 6
# 2 + (-2) = 0
# 2 + 0 = 4
    def testAddition(self):
        self.assertEqual(addition(2,2),4)
        self.assertEqual(addition(2,4),6)
        self.assertEqual(addition(2,-2),0)
        self.assertEqual(addition(2,0),2)
        
        
# test the subtraction functionality
# 2 - 2 = 0
# 2 - 4 = -2
# 2 - (-2) = 4
# 2 - 0 = 2        
    def testSubtraction(self):
        self.assertEqual(subtraction(2,2),0)
        self.assertEqual(subtraction(2,4),-2)
        self.assertEqual(subtraction(2,-2),4)
        self.assertEqual(subtraction(2,0),2)


# test the multiplication functionality
# 2 * 2 = 4
# 2 * 4 = 8
# 2 * (-2) = -4
# 2 * 0 = 0        
    def testMultiplication(self):
        self.assertEqual(multiplication(2,2),4)
        self.assertEqual(multiplication(2,4),8)
        self.assertEqual(multiplication(2,-2),-4)
        self.assertEqual(multiplication(2,0),0)

        
# test the division functionality
# 2 / 2 = 1
# 4 / 2 = 2
# 8 /(-2) = -4
# 2 / 0 = Error 
    def testDivision(self):
        self.assertEqual(division(2,2),1)
        self.assertEqual(division(4,2),2)
        self.assertEqual(division(8,-2),-4)
        self.assertEqual(division(2,0),'Error')
 
 
# test the exponentiation functionality
# 2 ** 2 = 4
# 2 ** 4 = 16
# 2 **(-2) = 0.25
# 2 ** 0 = 1          
    def testExponentiation(self):
        self.assertEqual(exponentiation(2,2),4)
        self.assertEqual(exponentiation(2,4),16)
        self.assertEqual(exponentiation(2,-2),0.25)
        self.assertEqual(exponentiation(2,0),1)

        
# test the power functionality
# 2 power 2 = 4
# 3 power 3 = 27
# 3 power 2 = 9
# 3 power 4 = 81            
    def testPower(self):
        self.assertEqual(power(2,2),4)
        self.assertEqual(power(3,3),27)
        self.assertEqual(power(3,2),9)
        self.assertEqual(power(3,4),81)        

        
# test the square_root functionality
# square_root 4 = 2
# square_root 9 = 3
# square_root 16 = 4
# square_root 25 = 5         
    def testSquare_root(self):
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(9),3)
        self.assertEqual(square_root(16),4)
        self.assertEqual(square_root(25),5)

        
# test the cube functionality
# 2 cube = 8
# 3 cube = 27
# 5 cube = 125
# 1 cube = 1         
    def testCube(self):
        self.assertEqual(cube(2),8)
        self.assertEqual(cube(3),27)
        self.assertEqual(cube(5),125)
        self.assertEqual(cube(1),1)

        
# test the logarithm functionality
# logarithm 1000 = 6.91
# logarithm 50 = 3.91
# logarithm -5 = Error
# logarithm 1 = 0         
    def testLogarithm(self):
        self.assertEqual(logarithm (1000), 6.91)
        self.assertEqual(logarithm (50),3.91)
        self.assertEqual(logarithm (-5),'Error')
        self.assertEqual(logarithm (1),0)

        
# test the factorial functionality
# 2 factorial = 2
# 3 factorial = 6
# 4 factorial = 24
# 3 factorialbe = 6                
    def testFactorial(self):
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(3),6)
        self.assertEqual(factorial(4),24)
        self.assertEqual(factorial(3),6)    

        
# test the cube_root functionality
# cube_root of 27 = 3
# cube_root of 8 = 2
# cube_root of 64 = 4
# cube_root of -125 = -5           
    def testCube_root(self):
        self.assertEqual(cube_root(27),3)
        self.assertEqual(cube_root(8),2)
        self.assertEqual(cube_root(64),4)
        self.assertEqual(cube_root(-125),-5)        
   
        
if __name__ == '__main__':
    unittest.main()            
