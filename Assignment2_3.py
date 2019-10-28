# Write a program which accept one number from user and return its factorial.


def Factorial(x):
    i=1
    while x>0:
        i=i*x
        x=x-1

    return i

x=(int(input("Enter the number")))
print("Factorial is=",Factorial(x))