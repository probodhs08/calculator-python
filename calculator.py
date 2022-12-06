number= int(input("enter your number: "))
import math
print('''1.Add
      2.substract
      3.modulus
      4.square
      5.divide
      6.absolute
      7.squareroot''')
def Add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def modulus(a,b):
    return a%b
def square(a,b):
    return a**b
def divide(a,b):
    return a/b
def absolute(a,b):
    return a//b
def squareroot(a):
    return math.sqrt(a)
a = int(input("enter your value:"))
b = int(input("enter your value:"))
operation=int(input("enter your operation:"))
if operation == 1:
    print(Add(a,b))
elif operation == 2:
    print(substract(a,b))
elif operation == 3:
    print(modulus(a,b))
elif operation == 4:
    print(square(a,b))
elif operation == 5:
    print(divide(a,b))
elif operation == 6:
    print(absolute(a,b))
elif operation == 7:  
    print(squareroot(a))  
else:
    print(multiply(a,b))

