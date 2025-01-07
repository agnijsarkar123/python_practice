def oddoreven(a):
    if a%2==0:
        return True
    else:
        return False       

def fact(b):
    product = 1
    for i in range(1 , b + 1):
        product = product*i
        return product

def time_hours(c):
    time = c//60
    return time

print("Please enter1 a number to check wether even or odd") 
print("Please enter2 a number to check its factorial") 
print("Please enter3 a time in minutes to convert into hours")
menu = int(input("User please choose 1 or 2 or 3: "))

if(menu == 1):
    num = int(input("Enter a number: "))
    oddoreven(num)
   

elif(menu == 2):
    num = int(input("Enter a number: "))
    print(f"factorial is: {fact(num)}")

elif(menu == 3):
    time = int(input("Enter a time in seconds: "))
    print("time in hours: ",time_hours(time) )
    
else:
    print("Enter correct choice")
#The End 