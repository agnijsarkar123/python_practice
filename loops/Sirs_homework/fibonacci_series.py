#0,1,1,2,3,5,8...........(unendingseries)
def fib(n):
    n = int(input("Enter a number:"))    
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
fib(10)  # sir wut to do about this i am unable to understand please help sir.
#it not considering the argument but it needs it .
#its taking input from user but it needs this

