def magic_number(n):
    factors = 0
    for i in range(1,n):
        if (i%2) == 0 and i!=0:
            factors=factors+i
        print(factors)
        return factors==n
    n = int(input("Enter a number: "))
    print(magic_number(n))
