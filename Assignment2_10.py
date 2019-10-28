# Write a program which accept number from user and return addition of digits in that number.


def Number(x):
    j=0
    while x>0:
        j=j+(x%10)
        x=x//10
    return j

x=(int(input("Enter the number")))
y=Number(x)
print("Number of digit=",y)

Number(x)