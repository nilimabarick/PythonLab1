# Implement linear search

def linear_search(arr, target):
    for i in range(len(arr)):
        return i
    return -1

numbers = [10,25,30,35,40]
target = 30

result = linear_search(numbers,target)

if result != -1:
  print(f"Elemnet found at index{result}")
else:
   print("Element not found")


# Implement binary search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


numbers = [10, 20, 30, 40, 50, 60]
target = 40

result = binary_search(numbers, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")


# compare limear search and binary search

# search in rotated sorted array
arr = [ 3,6,7,2,4,1]
target = int(input("enter the search element: "))

low = 0
high = len(arr) -1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("element found: ", mid)
        break
    if arr[low] <= arr[mid]:
        if arr[low] <= target < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    else:
        if arr[mid] < target <= arr[high]:
            low = mid +1
        else:
            high = mid -1
else:
    print("element not found")


# find first and last occurance of an element
arr = [ 1,2,3,3,4,5]
key = int(input("enter element: "))

first = -1
last = -1

for i in range (len(arr)):
    if arr[i] == key:
        if first == -1:
            first = i
        last = i
print(" First Occurance: ",first)
print(" Last Occurance: ", last)
