# a = int(input("Enter a number to find its factorial: "))
# fact = a
# product = 1
# while (fact!=1):
#     product = product * fact
#     fact = fact - 1
# print(product)


a = int(input("Enter a number : "))
sum = 0
digit = 0
temp = a
while temp > 0:
    digit = temp % 10
    sum = sum + digit**3
    temp = temp//10

if sum==a:
    print("This is your number-_-.")
else:
    print("This number is not valid,please try again")
