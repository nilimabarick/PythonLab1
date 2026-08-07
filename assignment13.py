# find the complexity single loop

# n = 5
# for i in range(n):
#     print(i)
    # loop runs 5 times O(n)

# compare time complexity of two algorithms

def liner_search(arr, key):
    for i in arr:
        if i == key:
            return True
    return False

# base case 0(1) element in first search & worst case 0(n)

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False
# base case 0(1) & worst case 0(log n)

# program demonstrating O(n) and 0(n2)

# numbers = [10,20,30,40,50]
# for num in numbers:
#     print(num)

# #time complexity 0(n)
# numbers = [1,2,3]
# for i in numbers:
#     for j in numbers:
#         print(i, j)
# time complexity O(n2)

# optimize a given inefficent algorithm

arr = [5,8,4,10,9] # inefficent algorithm o(n2)
for i in range(len(arr)):
    is_max = True
    for j in range(len(arr)):
        if arr[j] > arr [i]:
            is_max = False
            break
    if is_max:
        print("Maximun: ", arr[i])

arr = [5,8,4,10,9] # efficent algorithm o(n)
maximum = arr[0]
for num in arr:
    if num > maximum:
        maximum = num
print("Maximum: ", maximum)


