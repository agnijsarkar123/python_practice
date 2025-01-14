def isPalindrome(num):
    return num == num[::-1]

a = input("Enter a palindrome number")
boo = isPalindrome(a)
print(boo)


# str2 = ""
# for s in a[::-1]:
#     str2 += s
# if(a == str2):
#     print("palindrome number")
# else:
#     print("not")




