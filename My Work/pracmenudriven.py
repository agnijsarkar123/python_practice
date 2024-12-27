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
    
def time(c):
    time = c//60
    return time

print("Please enter1 a number to check wether even or odd") 
print("Please enter2 a number to check its factorial") 
print("Please enter3 a time in minutes to convert into hours")
menu = int(input("User please choose 1 or 2 or 3: "))

if menu == 1:
    
    print (oddoreven())
elif menu == 2:
    print (fact)
elif menu == 3:
    print(f"Time in hours is {time}")
else:
    print("Not valid choice,Please enter a valid choice.")
