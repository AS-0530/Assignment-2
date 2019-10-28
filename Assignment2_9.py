# Write a program which accept number from user and return number of digits in that number.


def Number():

    x=(int(input("Enter the number")))
    count=0
    while x>0:
        count=count+1
        x=x//10
    print("Number of digit=",count)

Number()