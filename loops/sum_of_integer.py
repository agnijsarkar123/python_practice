# program for adding the integers in a number

a = 153
sum = 0
temp = a
while (temp>0):
    digit = temp % 10 #153 % 10 = 3, 15 % 10 = 5, 1  % 10 = 1
    sum += digit # 0 + 3 = 3, 3 + 5 = 8, 8 + 1 = 9
    temp //= 10 # 153 //  10 = 15, 15 // 10 = 1, 1 // 10 = 0

print(sum)