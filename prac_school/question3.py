import math

def cal_hypotenuse(a,b):
    hypo = math.sqrt(math.pow(a,2)+math.pow(b,2))
    return hypo

num1 = float(input("Enter the base of the triangle: "))
num2 = float(input("Enter the perpendicular of the triangle: "))
hypotenuse = cal_hypotenuse(num1,num2)
print("the hypotenuse is ",hypotenuse)
