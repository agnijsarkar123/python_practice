def calculate(num1,num2):
    product = num1*num2
    if product<=1000:
        return product
    else:
        return num1+num2
    
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
result= calculate(num1,num2)
print(f"result is: {result}")