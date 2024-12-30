# Q3. Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
print("this is a program to find out different kinds of triangle")
a = int(input("Enter a number for the first side of a triangle: "))
b = int(input("Enter a number for the second side of a triangle: "))
c = int(input("Enter a number for the third side of a triangle: "))
if (a==b and b==c and c==a):
    print("It is an equilateral triangle")
elif((a==b and b!=c and c!=a) or (a!=b and b!=c and c==a) or (a!=b and b==c and c!=a)):
    print("It is a isosceles triangle")
elif(a!=b and b!=c and c!=a):
    print("It is a scalene triangle")
    #ok lets start programming 
    #first of ll we will take a look at alm the problems which we can face while
    #tell me the reason y he got bitten by a Wolf 
    tell