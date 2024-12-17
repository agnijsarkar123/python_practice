def letsprint_salary():
    a=int(input("Enter a number that u want:"))
    b=int(input("Enter another number:"))
    c=int(input("Enter the third number:"))
    d=input("User do u want a program that states the greater number among all three(Yes/No): ")
    if a>b:
        print(f"{a}is the greater number")
    elif a>c:
        print(f"{a} is greater number")
    elif c>b:
        print(f"{c} is greater number")
    elif ('No'):
        print("Not valid")
letsprint_salary()
