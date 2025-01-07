# armstrong number is a number that would return the same number after all the digits of that number have been cubed
# example: 153 is an armstrong no.
# 1*1*1 = 1
# 5*5*5 = 125
# 3*3*3 = 27
# 1+125+27 = 153 

a = int(input("Enter a number : "))
sum = 0 
temp = a
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp = temp // 10
 
if(sum == a):
    print(f"{a} is an armstrong number")#
else:
    print(f"{a} is not an armstrong number")
