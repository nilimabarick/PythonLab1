# create a list and print elememt
list = ["chips", "chocolate", "water melon", "litchi"]
print(list)

# Find maximum and minimum of the list

numbers = [32,43,11,42,56,74,9]
minimum = numbers[0]
maximum =numbers[0]

for i in range(len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
    elif numbers[i] < minimum:
        minimum = numbers[i]
    
print("minimum: ",minimum)
print("maximum: ",maximum)

# find odd and even of the list
odd = []
even = []

for i in numbers:
    if i % 2 == 0:
       even.append(i)
    else:
       odd.append(i)

print("even: ", even)
print("odd: ", odd)

# remove duplicates element from a list

list2 = [ 2,6,9,6,2,6,6,3,1,4]
dup = [] 
uniq = []
for i in list2:
    if i not in uniq:
        uniq.append(i)
    else:
        dup.append(i)

print("duplicates value: ", dup)
print("unique value: ", uniq)

# find the second largest number of the list

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print("the second largest number is:", numbers[1])

'''
    ROTATE A LIST BY K POSITION 

    IT'S BASICALLY MEAN MOVE THE ELEMENTS FROM K TO EITHER LEFT OR RIGHT, IN THE 
    BELOW EXAMPLE THE LAST 3 ELEMENTS MOVED TO FIRST BECAUSE K = 2 (FROM INDEX 2) AND IT IS TO THE LEFT


    lst = [1,2,3,4,5]
    k = 2

    rotated = lst[k:] + lst[:k]
    print(rotated)

    IF K = 2 BUT TO THE RIGHT THEN THE ELEMENTS AFTER INDEX 2 (LAST 2 ELEMENTS) MOVED TO 
    THE FIRST 

    lst = [1,2,3,4,5]
    k = 2

    rotated = lst[-k:] + lst[:-k]
    print(rotated)


    REMARKS :
    ASSIGNMENT CHECKED 
    SCORE 7 / 10



'''

