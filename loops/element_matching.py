l1 = [2,2,3,4,5,5]
n = len(l1)

for i in range(n):
    for j in range(i+1,n):
        if(l1[i] == l1[i+1]):
            print(True)