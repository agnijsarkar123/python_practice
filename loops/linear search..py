
# function declaration  
# def keyword function_name (parameter(s))
def linear_search(a,b):
    for i in a:
        if(i == b):
            return True
        else:
            return False

def update_fruit_list(a,b):
    return a.append(b)


l1 = ["apple", "banana", "kiwi"]
value = input("Enter what you wish to search in a list of fruits: ")
print(linear_search(l1,value))


print("These are the fruits we have",l1)
no_of_fruits = int(input("How many fruits would you like to add:"))
for i in range(no_of_fruits):
    update_fruits = input("Enter name of fruit you'd like to add: ")
    update_fruit_list(l1,update_fruits)
    

for i in l1:
        print(i)



