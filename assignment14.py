# Traverse and print elements of an array

arr =  [10, 20, 30, 40 ]
for element in arr:
    print(element)

# Insert an element at a specific position

arr.insert(2, 15)
print(arr)


# Delete an element from an array

arr.pop(2) # delete by index
print(arr)

arr.remove(40) # delete by value
print(arr)

# Find the missing number in an array

num = [1, 3, 4, 5, 6]
n = 6
total = n * (n + 1) // 2
array_sum = sum(arr)

missing = total - array_sum
print("Missing number: ", missing)

#  Find longest sunstring without repeating character

#Rotate array by k position

k = 2
k = k % len(num)
num = num[-k:] + num[:-k]
print(num)