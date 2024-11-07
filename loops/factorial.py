# ex- factorial of 4 = 4*3*2*1=24 

num = int(input("Enter  a number for factorial: "))
product = 1

for i in range(1,num+1): # 1 2 3 4
    product = product*i # 1*1 = 1, 1*2=2 , 2*3 = 6, 6*4 = 24,
    # print(product) # 1 2 6 24

print(product)