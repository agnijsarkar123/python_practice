def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num
print(is_armstrong(153))  
 

#Sir done

# swap program
num1 = int(input())
num2 = int(input())

if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp
    print(f"Number 1 : {num1} Number 2: {num2}")
else:
    print(f"Number 1 : {num1} Number 2: {num2}")
