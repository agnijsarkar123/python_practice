a = 153
sum=0
temp=a
while(temp>0):

 digit = temp%10
 sum+=digit
 temp//=10

print(sum)