#44.Accept three numbers from the user and display the second largest number.
a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=int(input("enter 3rd number: "))
if a>b and a<c:
    print("second largest number is a= ",a)
elif b>a and b<c:
    print("second largest number is b= ",b)
elif c>b and c<a:
    print("second largest number is c= ",c)
else:
    print("all are equal")

    
