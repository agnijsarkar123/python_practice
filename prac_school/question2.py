# Define a function digi(n) which displays the largest and smallest digit 
# present in the number n. 

def digi(n):
    length = len(n)
    n.sort()
    print(n)
    print("the largest number is", l1[length-1])
    print("the smallest number is", l1[0])

num = input("enter a number: ")

l1 = []
for i in num:
    l1.append(i)

digi(l1)
