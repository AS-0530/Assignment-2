# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user

import Arithmatics

x=(int(input("Enter the 1st number")))
y=(int(input("Enter the 2nd number")))

print("Addition is=",Arithmatics.Add(x,y))
print("Subtraction is=",Arithmatics.Sub(x,y))
print("Multiplication is=",Arithmatics.Mult(x,y))
print("Division is=",Arithmatics.Div(x,y))