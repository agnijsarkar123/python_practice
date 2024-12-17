def fib(n):      
    a = 0
    b = 1
    if n == 1:
       return a
    else:
        print(a)
        print(b)
        for i in range(2,n): 
            c = a + b
            a = b
            b = c
            print(c)

            
n = int(input("Enter a number:"))
fib(n) 




#0,1,1,2,3,5,8,13........(Unending loop)called the fibonacci series
