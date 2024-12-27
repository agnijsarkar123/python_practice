def twoSum(arr, target):#arr for array , target is given by me aaccording the question.
  
    arr.sort()

    left, right = 0, len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return True
        elif sum < target: 
            left += 1 
        else:
            right -= 1 
    return False

arr = [2,7,11,15]
target = 9
if twoSum(arr, target):
    print("true")
else:
    print("false")