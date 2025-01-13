n = int(input("Enter a number: "))

if n>1:
    for n in range(1,(n//2+1)):
        if n%2==0:
            print("not a prime number")
            break
    else:
        print(f"{n} is a prime number")
else:
    print(f"{n} is a not a prime number")

    