num=int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by both 2 and 3.")
else:
    print(f"{num} is not divisible by both 2 and 3.")