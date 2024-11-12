num = int(input("Enter a number: "))
flag = False
if num > 1:
    for i in range(2,num):
        flag = True
        break
if flag:
    print(num,"The number is not prime")
else:
    print(num,"The number is prime")