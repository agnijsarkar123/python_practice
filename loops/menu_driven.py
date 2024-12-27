def odd_or_even(a):
    if(a%2 == 0):
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
    

def factorial(a): 
    product = 1
    for i in range(1,a+1):
        product = product*i
    return product

def time_conversion(time):
    hours = time // 3600 
    return hours


print("Enter 1 for wanting to check if a number is odd or even")
print("Enter 2 for wanting to calculate the factorial of a number")
print("Enter 3 for wanting to see time in seconds and then convert in hours")
menu = int(input("Enter your choice: "))

if(menu == 1):
    num = int(input("Enter a number: "))
    odd_or_even(num)
   

elif(menu == 2):
    num = int(input("Enter a number: "))
    print(f"factorial is: {factorial(num)}")

elif(menu == 3):
    time = int(input("Enter a time in seconds: "))
    print("time in hours: ",time_conversion(time) )
    
else:
    print("Enter correct choice")