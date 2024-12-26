# perfect number --> a number whose factors will add up to that number

def perfect_num(n):
        
        factors = 0
        # dup_num = num
        for i in (1, n):
            if(i%2) == 0:
                factors+=i
                
        print(factors)
        return factors == n

# 28 = 1,2,4,7,14,28

num = int(input("Enter a number: "))

print(perfect_num(num))