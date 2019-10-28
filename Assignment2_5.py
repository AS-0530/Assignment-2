# Write a program which accept one number for user and check whether number is prime or not.


def Prime(x):
    i=2
    j=0
    while i<x:
        if x%i==0:
            j=1
        i=i+1
    return j

x=(int(input("Enter the number")))
y=Prime(x)
if y==1:
    print("Number is not prime")
else:
    print("Number is prime")

Prime(x)