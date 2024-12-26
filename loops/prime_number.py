# wap to check prime number.

n = int(input("enter a prime number: "))

if n > 1:
    

    for i in range(2, (n//2)+1): # factors of a number always will go till half of a number
        if n % i == 0:
            print("not a prime number")
            break
        else:
            print(f"{n} is a prime number")
            break
else:
    print(f"{n} is not a prime number")

# 0 and 1 can't be prime no.s
# 