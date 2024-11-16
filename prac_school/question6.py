import random

def roll_dice(target):
    count = 0
    random_no = random.randint(0,7)
    while (random_no != target):
        print(random_no)
        count += 1
    return count


target = int(input("Enter a target number of a dice: "))
c = roll_dice(target)
print("the number of turns it took to get the target: ", c)
print("This is ur result")
#Sir done

