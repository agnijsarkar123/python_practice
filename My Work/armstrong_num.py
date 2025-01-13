a= int(input("Enter a number: "))
sum = 0
temp = a #initialization

while (temp>0): #condition
    digits = temp%10
    sum = (digits**3)+sum
    temp = temp//10 #decrement

print(sum)
if sum == a:
    print("armstrong number")
else:
    print("Not armstrong")

