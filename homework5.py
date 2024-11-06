#This looks hard but i will try
a=int(input("Enter a number: "))
if a % 2 != 0:
    print("Weird")
elif a % 2 == 0 and 2<=a<=5:
    print("Not Weird")
elif a % 2 == 0 and 6<=a<=20:
    print("Weird")
elif a % 2 == 0 and a > 20:
    print("Not Weird")    
